
from telegram_bot import send_status, check_emergency, TOKEN
import telegram_bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters


def add_handlers(bot):
    # commands
    bot.add_handler(CommandHandler('start', telegram_bot.start_command))
    bot.add_handler(CommandHandler('help', telegram_bot.help_command))
    bot.add_handler(CommandHandler('status', telegram_bot.status_command))
    bot.add_handler(CommandHandler('id', telegram_bot.id_command))
    # Messages
    bot.add_handler(MessageHandler(filters.TEXT, telegram_bot.handle_message))
    # Errors
    bot.add_error_handler(telegram_bot.error)


def main():
    print("Starting bot...\n")
    app = Application.builder().token(TOKEN).build()

    add_handlers(app)

    # messaggio ricorrente con lo stato del server (ogni 5min)
    app.job_queue.run_repeating(send_status, interval=300, first=120)

    # controllo emergenze ogni 2min
    app.job_queue.run_repeating(check_emergency, interval=120, first=60)

    print("Polling...")
    app.run_polling()


if __name__ == "__main__":
    main()

