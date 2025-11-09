import os
import dotenv
import google.genai as genai
from halo import Halo

# .envファイルから環境変数を読み込む
dotenv.load_dotenv()


def configure_api():
    # 環境変数からGoogle APIキーを取得
    api_key = os.getenv("GEMINI_API_KEY")
    # APIキーが設定されていない場合はエラーを発生
    if not api_key:
        raise ValueError("Google API key is missing")
    # APIキーを用いてGoogle AIクライアントを初期化
    return genai.Client(api_key=api_key)


def main():
    client = configure_api()
    spinner = Halo(text='Thinking...', spinner='dots')
    # AIモデルを指定
    history=[
        {
            "role":"user",
            "parts":[
                {
                    "text": "あなたの名前はAです"
                }
            ]
        },
        {
            "role":"model",
            "parts":[
                {
                    "text": "はい，私の名前はAです"
                }
            ]
        },
        {
            "role":"user",
            "parts":[
                {
                    "text": "私は来年の４月からWEBエンジニアとして働く予定です"
                }
            ]
        }
    ]
    chat = client.chats.create(model="gemini-2.0-flash", history=history)

    while True:
        try:
            user_input = input("あなたの質問: ")
            if user_input.lower() == "exit":
                break
            spinner.start()
            response = chat.send_message(user_input)
            spinner.stop()
            print("Gemini: ", response.text)
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            break


if __name__ == "__main__":
    main()