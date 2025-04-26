from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#início
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salve furioso! Manda a boa!🔥🔥')
    
#repetir msg
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"Msg: {user_message}")

#lista comandos
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Comandos disponíveis:\n/start - Iniciar\n/jogos - Ver os próximos jogos e os anteriores\n/stats - Ver estatísticas')

#mostrar jogos hltv
async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Confira os jogos no site da HLTV: (https://www.hltv.org/team/8297/furia#tab-matchesBox)",
        parse_mode="Markdown")

#main
def main():
    TOKEN = "8173060128:AAFBsQFo013x-AfwpMAulIubLWCRHBJitTo"
    
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start)) # chama a função start
    application.add_handler(CommandHandler("jogos", jogos))
    application.add_handler(CommandHandler("help_command", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo)) 
    
    application.run_polling()
    
if __name__ == '__main__':
    main()