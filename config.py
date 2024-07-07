from dataclasses import dataclass
import environs


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = environs.Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))


def admins_ids(path: str | None = None) -> list:
    env = environs.Env()
    env.read_env(path)
    ids = env('admins_id').split(',')
    return ids


DATABASE_URL = 'postgresql+asyncpg://postgres:FunkoPop@localhost/travels_db'
