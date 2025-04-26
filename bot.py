from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

#início
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salve furioso!  Manda a boa! 🔥')
    
#repetir msg
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"Msg: {user_message}")

#main
def main():
    TOKEN = "8173060128:AAFBsQFo013x-AfwpMAulIubLWCRHBJitTo"
    
    application = Application.builder().token(TOKEN).build
    
    application.add_handler(CommandHandler("start", start)) # chama a função start 
    application.add_handler(MessageHandler(Filters.text & ~Filters.command, echo)) 
    
    application.run_polling()
    
    if __name__ == '__main__':
        main()