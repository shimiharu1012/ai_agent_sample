## CLI AI Agent (Python & Gemini)

https://ai.google.dev/gemini-api/docs?hl=ja

![動画](https://github.com/shimiharu1012/ai_agent_sample/edit/main/chat-demo.mov)

## やりたいこと
- 残りtokenを表示する機能
- コンテキストキャッシュで色々遊ぶ
- chat.pyの中に
    - 画像認識
    - 画像生成
- tavily（LLM向け検索用API）で高度なWEB検索
    - なんちゃってDeepリサーチ
    - 検索モードの場合，間にプロンプトを挟んでLLMによる検索キーワード抽出
    - 検索キーワードでtavily検索→Chat回答に仕様



## やったこと
- 会話履歴の保存
    - コンテキスト管理
    - コンテキストの永続化
        - 暗黙的な永続化:chatが生きている間は自動で
        - 明示的な永続化：chat離脱後もSQLiteでコンテキストを保持
            



## response.json
```
{
    "candidates": [
        {
            "content": {
                "parts": [
                    {
                        "text": "AI learns patterns from data to perform tasks and make decisions intelligently."
                    }
                ],
                "role": "model"
            },
            "finishReason": "STOP",
            "index": 0
        }
    ],
    "usageMetadata": {
        "promptTokenCount": 8,
        "candidatesTokenCount": 13,
        "totalTokenCount": 742,
        "promptTokensDetails": [
            {
                "modality": "TEXT",
                "tokenCount": 8
            }
        ],
        "thoughtsTokenCount": 721
    },
    "modelVersion": "gemini-2.5-flash",
    "responseId": "xxxxxx"
}
```

## 参考
- https://fly.io/blog/everyone-write-an-agent/
- https://github.com/google-gemini/cookbook
- [APIの料金](https://ai.google.dev/gemini-api/docs/pricing?hl=ja&_gl=1*19lnu2m*_up*MQ..*_ga*MTY4MzY3MTI4NC4xNzYyNzAyNjE4*_ga_P1DBVKWT6V*czE3NjI3MDI2MTckbzEkZzAkdDE3NjI3MDI2MTckajYwJGwwJGgxNzQyMjY4NzA.)
- https://googleapis.github.io/python-genai/
