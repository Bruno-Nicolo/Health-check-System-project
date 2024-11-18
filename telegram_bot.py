
from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from Controls import cpu, ram, disks, network, general_info
import thresholds


# Bot variables
BOT_USERNAME = "@SysScanner_bot"
TOKEN = "7717659591:AAHLYDAqpO1MZoDmQKnf_KD7H2KSpuAh4ZI"
chat_id = "725588367"


def get_server_status():
    return (
        "<b>Server Health Check 🔍</b>\n\n"
        f"CPU usage: {cpu.percentage()}% {cpu.get_priority()}\n"
        f"CPU frequency: {cpu.frequency()} Hz\n\n"
        f"RAM available: {ram.available()} GB\n"
        f"RAM available percentage: {ram.percentage()}% {ram.get_priority()}\n"
        f"RAM in use: {ram.active()} GB\n"
        f"RAM not in use: {ram.inactive()} GB\n\n"
        f"Disk total space: {disks.total()} GB\n"
        f"Disk used space: {disks.used()} GB {disks.get_priority()}\n"
        f"Disk used space in percentage: {disks.percent()}%\n\n"
        f"Download speed: {network.download_speed()} Kb/s\n"
        f"Upload speed: {network.upload_speed()} Kb/s\n\n"
        f"Temperature: {general_info.temperature()} {general_info.get_priority()}\n"
        f"Uptime: {general_info.uptime()}\n"
    )


async def send_status(context: CallbackContext) -> None:
    await context.bot.send_message(chat_id=chat_id, text=get_server_status(), parse_mode="HTML")


async def check_emergency(context: CallbackContext) -> None:
    if (cpu.percentage() >= thresholds.CPU or
        ram.percentage() <= thresholds.RAM or
        disks.total() - disks.used() <= thresholds.DISKS or
        general_info.get_priority() != ""
    ):
        await context.bot.send_message(chat_id=chat_id, text=get_server_status(), parse_mode="HTML")


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.chat.first_name

    # messaggio diverso per gruppo e chat privata
    if update.message.chat.type == "private":
        await update.message.reply_text(f"Hello {username}! 👋🏻 \n\nThanks for choosing our service 👨🏻‍💻")
    else:
        await update.message.reply_text(
            f"Hello {username}! 👋🏻 \n\nThanks for choosing our service 👨🏻‍💻\n\n"
            "Don't forget to make me admin of the group, or I won't be able to reply to the commands"
        )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = ("<b>List of available commands: </b>\n\n"
                    "/status - get info about the current status of the server\n"
                    "/help - get the list of all the commands\n"
                    "/id - get your chatID"
                    )
    await update.message.reply_text(help_message, parse_mode="HTML")


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_server_status(), parse_mode="HTML")


async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = update.message.chat.id
    chat_type = update.message.chat.type
    await update.message.reply_text(f"Your {chat_type} chatID is:\n {id}")


# Responses
def handle_response(text):
    if "/" not in text:
        return "To see the list of all the commands write /help"
    else:
        return "Command not found. \nTo se the list of all the commands write /help"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if BOT_USERNAME in text:
        new_text = text.replace(BOT_USERNAME, "").strip()
        response = handle_response(new_text)
    else:
        response = handle_response(text)

    await update.message.reply_text(response)


# Errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

