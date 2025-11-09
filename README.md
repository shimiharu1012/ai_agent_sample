GEMINI APIで遊ぶよう

https://ai.google.dev/gemini-api/docs?hl=ja

## やりたいこと
- AI Agent作ってみる
    - 残りtokenを表示する機能
    - 画像用とか音楽用とか色々試す
    - 会話履歴を保存する
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