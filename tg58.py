from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
TOKEN = '8305366564:AAF1oivHY03uzdxDMf5gvv_GgbNpiDIA0sQ'

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