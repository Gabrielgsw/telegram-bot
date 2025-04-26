from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os


TOKEN = 'SEU_TOKEN_AQUI'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salve, fã da FURIA! 🔥 Me pergunte algo!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Comandos disponíveis:\n/start - Iniciar\n/quiz - Jogar quiz\n/stats - Ver estatísticas')

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Não entendi 😅. Tente outro comando!')


load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
app = ApplicationBuilder().token(TOKEN).build()

# Handlers (ações)
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.COMMAND, unknown))  # Para comandos desconhecidos

# Rodar
print("Bot rodando...")
app.run_polling()
