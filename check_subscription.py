import logging
from datetime import datetime, timedelta

from config import DATABASE_URL
from database.requests import DatabaseManager

logger = logging.getLogger(__name__)
dsn = DATABASE_URL
db_manager = DatabaseManager(dsn=dsn)


async def check_status(id_user: int, date):
    now = datetime.now().replace(second=0, microsecond=0)
    user = await db_manager.get_user(user_id=id_user)
    date_user = user.subscription_end_date
    days = date_user - now
    if days.days == 3:
        print(3)
    elif 0 < days.days < 3:
        print(False)
    elif days.days < 0:
        print('kick')