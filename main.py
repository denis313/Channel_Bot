import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from check_subscription import check_status
from config import load_config
from handlers import start_handler, handler_buy, check_handler

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(level=logging.DEBUG,
                        filename="py_log.log",
                        filemode="w",
                        format='[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s')

    # Загружаем конфиг в переменную config
    config = load_config()
    # Инициализируем бот и диспетчер
    dp = Dispatcher()
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Регистриуем роутеры в диспетчере
    dp.include_routers(start_handler.router, handler_buy.router, check_handler.router)


    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # scheduler = AsyncIOScheduler()
    # scheduler.add_job(check_status, 'cron', day=1, hour=0, minute=0)  # Запуск каждый месяц в первый день в полночь
    # scheduler.start()
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("stopped")
