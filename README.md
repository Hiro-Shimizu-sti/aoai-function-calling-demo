Azure OpenAIを使用したFunctionCallingのデモ実装プロジェクトです。
こちらのリポジトリをクローンしていただき以下の手順に従うことで、実際に実行することが可能です。

## 前提条件
- pythonがインストールされている
- AOAIモデルをデプロイしている(デプロイしていない場合は、[こちら](https://tech-lab.sios.jp/archives/50667)のデプロイメント方法をまとめたブログが参考になるかもしれません。)

## 実行手順
1. 以下の内容で.envファイルを作成する。
```text
AZURE_OPENAI_API_KEY=<モデルのAPIキー>
AZURE_OPENAI_ENDPOINT=<モデルのエンドポイント>
AZURE_OPENAI_API_VERSION=<モデルのAPIバージョン>
AZURE_OPENAI_DEPLOYMENT_NAME=<デプロイメントしたモデルの名前>
```
2.  仮想環境を作成する。
```text
python3 -m venv .venv
```
3. 仮想環境を有効化する。
```text
source .venv/bin/activate
```
4. 依存関係をインストールする。
```text
pip install -r requirements.txt
```
5.  実行する。
```text
python3 src/main.py
```

実行結果からfunctioncallingされていることを確認できます。
また、main.pyのmessagesを自由に書き換えることで別の指示を与えることが可能です。以下は該当箇所です。
```text
messages = [
    {
        "role": "system",
        "content": "あなたは優秀なアシスタントAIです。",
    },
    {"role": "user", "content": "八王子の時刻を教えてください。"},
]
```
