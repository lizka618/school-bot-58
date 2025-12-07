from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"В этом боте вы сможете получить полезную информацию о расписании, звонках, коллегах и учителях")
    await update.message.reply_text(
        f'Выберите кто вы:')
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start',start))
    app.run_polling()
if __name__ == "__main__":

    main()
