from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from Controls.cpu import Cpu
from Controls.ram import Ram
from Controls.disks import Disk
from Controls.network import Network
from Controls.general_info import General_info

# Objects
CPU = Cpu()
RAM = Ram()
DISK = Disk()
NETWORK = Network()
GENERAL_INFO = General_info()


class Bot:
    def __init__(self, chat_id="", interval=5):
        self.__USERNAME = "@SysScanner_bot"
        self.TOKEN = "7717659591:AAHLYDAqpO1MZoDmQKnf_KD7H2KSpuAh4ZI"
        self.chat_id = chat_id
        self.interval = interval


    def set_interval(self, value):
        self.interval = value

    def update_id_list(self, id_list):
        self.chat_id = id_list


    def __get_server_status(self):
        return (
            "<b>Server Health Check 🔍</b>\n\n"
            f"CPU usage: {CPU.set_percentage()}% {CPU.get_priority()}\n"
            f"CPU frequency: {CPU.set_frequency()} Hz\n\n"
            f"RAM available: {RAM.set_available()} GB\n"
            f"RAM available percentage: {RAM.set_percentage()}% {RAM.get_priority()}\n"
            f"RAM in use: {RAM.set_active()} GB\n"
            f"RAM not in use: {RAM.set_inactive()} GB\n\n"
            f"Disk total space: {DISK.set_total()} GB\n"
            f"Disk used space: {DISK.set_used()} GB {DISK.get_priority()}\n"
            f"Disk used space in percentage: {DISK.set_percent()}%\n\n"
            f"Download speed: {NETWORK.download_speed()} Kb/s\n"
            f"Upload speed: {NETWORK.upload_speed()} Kb/s\n\n"
            f"Temperature: {GENERAL_INFO.temperature()} {GENERAL_INFO.get_priority()}\n"
            f"Uptime: {GENERAL_INFO.uptime()}\n"
        )


    async def send_status(self, context: CallbackContext) -> None:
        for uid in self.chat_id:
            await context.bot.send_message(chat_id=uid, text=self.__get_server_status(), parse_mode="HTML")


    async def check_emergency(self, context: CallbackContext) -> None:
        if (CPU.get_priority() != "" or
            RAM.get_priority() != "" or
            DISK.get_priority() != "" or
            GENERAL_INFO.get_priority() != ""
        ):
            for uid in self.chat_id:
                await context.bot.send_message(chat_id=uid, text=self.__get_server_status(), parse_mode="HTML")


    # Commands
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        username = update.message.chat.first_name

        # messaggio diverso per gruppo e chat privata
        if update.message.chat.type == "private":
            await update.message.reply_text(f"Hello {username}! 👋🏻 \n\nThanks for choosing our service 👨🏻‍💻\n\nHere you will receive recurring notification about the status of you machine every 5min. 🔔\n\nWrite /help to see the list of all available commands.")
        else:
            await update.message.reply_text(
                f"Hello {username}! 👋🏻 \n\nThanks for choosing our service 👨🏻‍💻\n\n"
                "Don't forget to make me admin of the group, or I won't be able to reply to the commands"
            )


    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        help_message = ("<b>List of available commands: </b>\n\n"
                        "/status - get info about the current status of the server\n"
                        "/help - get the list of all the commands\n"
                        "/id - get your chatID"
                        )
        await update.message.reply_text(help_message, parse_mode="HTML")


    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.message.chat.id
        if f"{chat_id}" in self.chat_id:
            await update.message.reply_text(self.__get_server_status(), parse_mode="HTML")
        else:
            await update.message.reply_text("Not Available")


    async def id_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.message.chat.id
        chat_type = update.message.chat.type
        await update.message.reply_text(f"Your {chat_type} chatID is:\n {user_id}")


    # Responses
    def __handle_response(self, text):
        if "/" not in text:
            return "To see the list of all the commands write /help"
        else:
            return "Command not found. \nTo se the list of all the commands write /help"


    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text

        if self.__USERNAME in text:
            new_text = text.replace(self.__USERNAME, "").strip()
            response = self.__handle_response(new_text)
        else:
            response = self.__handle_response(text)

        await update.message.reply_text(response)


    # Errors
    async def error(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f'Update {update} caused error {context.error}')

