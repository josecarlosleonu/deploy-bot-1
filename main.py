from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello world!")

async def echo (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

application = ApplicationBuilder().token("7117914726:AAEnZUGRMQGwLVlZEUnUD8MhrWRsoKdmaQg").build()
application.add_handler(CommandHandler("start",say_hello))
application.add_handler(CommandHandler("echo", echo))
application.run_polling(allowed_updates=Update.ALL_TYPES)