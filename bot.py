from telegram import (
    Update,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")  # GitHub Actions подставит сюда секрет

if not TOKEN:
    raise ValueError("Токен не найден! Проверь Secrets в GitHub.")
WEB_APP_URL = "https://sc0ppp.github.io/ilusha/"  # URL вашего Mini App

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    # Создаем большую кнопку
    keyboard = [
        [KeyboardButton(
            text="🌟 ОТКРЫТЬ MINI APP 🌟", 
            web_app={"url": WEB_APP_URL}
        )]
    ]
    
    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        text="Добро пожаловать! Нажмите кнопку ниже, чтобы открыть приложение:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,    # Кнопка подстраивается под ширину экрана
            one_time_keyboard=True,  # Скрыть клавиатуру после нажатия
            input_field_placeholder="Нажмите кнопку 'ОТКРЫТЬ'"
        )
    )

def main() -> None:
    """Запуск бота"""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start_command))
    
    # Запускаем бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":

    main()

