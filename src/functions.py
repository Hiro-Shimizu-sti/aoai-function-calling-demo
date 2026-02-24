from datetime import datetime


def current_time(location: str):
    # 簡易的に現在時刻を送信
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "current_time": current_time,
        "location": location,
    }


def current_weather(location: str):
    # ダミーの天気データを返す
    return {
        "location": location,
        "temperature": 15,
        "description": "晴れ",
    }
