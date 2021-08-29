from pydantic import BaseSettings


class DBSettings(BaseSettings):
    db_url = "sqlite:///db/database.db"

    class Config:
        env_file = "env/db.env"


db_settings = DBSettings()
