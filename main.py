
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram_bot import Bot


# Bot variables
BOT = Bot()


def add_handlers(bot):
    # commands
    bot.add_handler(CommandHandler('start', BOT.start_command))
    bot.add_handler(CommandHandler('help', BOT.help_command))
    bot.add_handler(CommandHandler('status', BOT.status_command))
    bot.add_handler(CommandHandler('id', BOT.id_command))
    # Messages
    bot.add_handler(MessageHandler(filters.TEXT, BOT.handle_message))
    # Errors
    bot.add_error_handler(BOT.error)


def main():
    print("Starting bot...\n")
    interval_time = BOT.interval * 60

    app = Application.builder().token(BOT.TOKEN).build()

    add_handlers(app)

    # messaggio ricorrente ogni 5min
    app.job_queue.run_repeating(BOT.send_status, interval=interval_time, first=120)

    # controllo emergenze ogni 2min
    app.job_queue.run_repeating(BOT.check_emergency, interval=120, first=60)

    print("Polling...")
    app.run_polling()


