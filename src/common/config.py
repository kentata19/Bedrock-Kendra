from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str
    BASE_DIR: str

    # AWSの設定
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_DEFAULT_REGION: str = "ap-northeast-1"

    class Config:
        case_sensitive = True
