import os
import dotenv
import google.genai as genai
from halo import Halo
from tinydb import TinyDB
from InquirerPy import inquirer

# .envファイルから環境変数を読み込む
dotenv.load_dotenv()
DB_DIR_PATH=os.getenv("DB_DIR_PATH")

def open_database(filename):
    if filename=="new":
        filename=input("Enter the room name: ")+".json"
        
    return TinyDB(f'{DB_DIR_PATH}/{filename}')

def configure_api():
    # 環境変数からGoogle APIキーを取得
    api_key = os.getenv("GEMINI_API_KEY")
    # APIキーが設定されていない場合はエラーを発生
    if not api_key:
        raise ValueError("Google API key is missing")
    # APIキーを用いてGoogle AIクライアントを初期化
    return genai.Client(api_key=api_key)

def add_to_history(response,db):
    content={
        "role":response.candidates[0].content.role,
        "parts":[{"text":response.candidates[0].content.parts[0].text}]
    }
    db.table('history').insert(content)


def format_history(rows):
    formatted_history=[]
    for row in rows:
        formatted_history.append({
            "role": row[1],
            "parts":[{"text":row[2]}]
        })
    return formatted_history


def main():
    while True:
        db_files=os.listdir(DB_DIR_PATH)
    
        db_choices=[
            {"name": db_file.rstrip(".json"), "value": db_file} for db_file in db_files
        ]
        db_choices.append({"name": "Create new database", "value": "new"})
        
        filename=inquirer.select(
            message="Select the room:",
            choices=db_choices,
            default=db_choices[0],
            pointer="➤"
        ).execute()

        # TinyDBの接続
        db=open_database(filename)
        history=db.table('history').all()
        
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
                add_to_history(response,db)
            except Exception as e:
                print(f"エラーが発生しました: {e}")
                break
        
        db.close()

if __name__ == "__main__":
    main()
    