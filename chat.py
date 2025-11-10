import os
import dotenv
import google.genai as genai
from halo import Halo
import sqlite3
from InquirerPy import inquirer

# .envファイルから環境変数を読み込む
dotenv.load_dotenv()
DB_DIR_PATH=os.getenv("DB_DIR_PATH")

def open_database(filename):
    if filename=="new":
        filename=input("Enter the room name: ")
        connection = sqlite3.connect(f'{DB_DIR_PATH}/{filename}.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE history(id INTEGER PRIMARY KEY AUTOINCREMENT, role STRING, text STRING, created_at DATETIME)')  # tableを作成する指示
        connection.commit()
        cursor.close()
        return connection
    else:
        dbname = f'{DB_DIR_PATH}/{filename}'

    connection=sqlite3.connect(dbname)

    return connection

def configure_api():
    # 環境変数からGoogle APIキーを取得
    api_key = os.getenv("GEMINI_API_KEY")
    # APIキーが設定されていない場合はエラーを発生
    if not api_key:
        raise ValueError("Google API key is missing")
    # APIキーを用いてGoogle AIクライアントを初期化
    return genai.Client(api_key=api_key)


def add_to_history(response,connection,cursor):
    role=response.candidates[0].content.role
    text=response.candidates[0].content.parts[0].text

    cursor.execute("INSERT INTO history (role, text) VALUES (?, ?)", (role, text))
    connection.commit()

def format_history(rows):
    formatted_history=[]
    for row in rows:
        formatted_history.append({
            "role": row[1],
            "parts":[{"text":row[2]}]
        })
    return formatted_history


def main():
    db_files=os.listdir(DB_DIR_PATH)
    db_choices=[
        {"name": db_file.rstrip(".db"), "value": db_file} for db_file in db_files
    ]
    db_choices.append({"name": "Create new database", "value": "new"})

    filename=inquirer.select(
        message="Select the room:",
        choices=db_choices,
        default=db_choices[0],
        pointer="➤"
    ).execute()

    # SQLiteのDBへ接続
    connection=open_database(filename)
    cursor=connection.cursor()
    
    rows=cursor.execute("SELECT * FROM history").fetchall()
    history=format_history(rows)
    
    client = configure_api()
    spinner = Halo(text='Thinking...', spinner='dots')
    
    chat = client.chats.create(model="gemini-2.0-flash", history=history)

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            spinner.start()
            response = chat.send_message(user_input)
            spinner.stop()
            print("Gemini: ", response.text)
            add_to_history(response,connection,cursor)
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            break
    
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
    