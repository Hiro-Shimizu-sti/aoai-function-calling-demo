import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv
from schemas import FunctionSchemaManager, TimeArgs, WeatherArgs
from functions import current_time, current_weather


# .envファイルから環境変数を読み込み
load_dotenv()

api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Azure OpenAIクライアントの作成
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

tools = FunctionSchemaManager.get_all_tools()

messages = [
    {
        "role": "system",
        "content": "あなたは優秀なアシスタントAIです。",
    },
    {"role": "user", "content": "八王子の時刻を教えてください。"},
]

# １回目のFunctionCallingリクエスト
response = client.chat.completions.create(
    messages=messages,
    max_tokens=1000,
    temperature=0.7,
    model=deployment,
    tools=tools,
    tool_choice="auto",
)

response_message = response.choices[0].message
messages.append(response_message)

print("レスポンス：")
print(response_message)

# 関数実行
if response_message.tool_calls:
    for tool_call in response_message.tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        print(f"関数呼び出し: {function_name}")
        print(f"引数: {function_args}")

        if function_name == "current_weather":
            args = WeatherArgs.model_validate(function_args)  # 引数チェック
            tool_response = current_weather(location=args.location)
        elif function_name == "current_time":
            args = TimeArgs.model_validate(function_args)  # 引数チェック
            tool_response = current_time(location=args.location)
        else:
            tool_response = {"error": "不明な関数"}

        messages.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": json.dumps(tool_response, ensure_ascii=False),
            }
        )
else:
    print("関数呼び出しはありませんでした。")

final_response = client.chat.completions.create(
    messages=messages,
    max_tokens=1000,
    temperature=0.7,
    model=deployment,
)

print("最終レスポンス：")
print(final_response.choices[0].message.content)
