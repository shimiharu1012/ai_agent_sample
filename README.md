GEMINI APIで遊ぶよう

https://ai.google.dev/gemini-api/docs?hl=ja

## やりたいこと
- AI Agent作ってみる
    - 残りtokenを表示する機能
    - 会話履歴を保存する
        - コンテキスト管理
    - 会話履歴のファイルを複数持つ


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