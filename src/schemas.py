from pydantic import BaseModel, Field
from typing import Dict, Any


class WeatherArgs(BaseModel):
    """get_current_weather関数の引数モデル"""

    location: str = Field(
        ...,
        description="天気情報を取得したい都市名(日本語)。例: '東京'",
    )


class TimeArgs(BaseModel):
    """get_current_time関数の引数モデル"""

    location: str = Field(
        ...,
        description="時刻を取得したい都市名(日本語)。例: '東京', 'ニューヨーク'",
    )


class FunctionSchemaManager:
    """複数の関数スキーマを管理するクラス"""

    @staticmethod
    def get_weather_tool() -> Dict[str, Any]:
        """天気取得ツールのスキーマ"""
        return {
            "type": "function",
            "function": {
                "name": "current_weather",
                "description": "指定された都市の現在の天気情報を取得します",
                "parameters": WeatherArgs.model_json_schema(),
            },
        }

    @staticmethod
    def get_time_tool() -> Dict[str, Any]:
        """時刻取得ツールのスキーマ"""
        return {
            "type": "function",
            "function": {
                "name": "current_time",
                "description": "指定された都市の現在時刻を取得します",
                "parameters": TimeArgs.model_json_schema(),
            },
        }

    @staticmethod
    def get_all_tools() -> list[Dict[str, Any]]:
        """利用可能な全てのツールを返す"""
        return [
            FunctionSchemaManager.get_weather_tool(),
            FunctionSchemaManager.get_time_tool(),
        ]
