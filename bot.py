import requests
from telegram import Update
from telegram.ext import Application,ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes



#início
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salve furioso! Manda a boa!🔥🔥')
    
#repetir msg
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"Msg: {user_message}")

#lista comandos
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Comandos disponíveis:\n/start - Iniciar\n/jogos - Ver os próximos jogos e os anteriores\n/stats - Ver estatísticas')

#mostrar jogos hltv
async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Confira os jogos no site da HLTV: (https://www.hltv.org/team/8297/furia#tab-matchesBox)",
        parse_mode="Markdown")

async def proximos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://hltv-api.vercel.app/api/team?id=8297"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        partidas = dados["team"].get("upcomingMatches", [])

        if partidas:
            mensagem = "🎯 Próximos jogos da FURIA:\n\n"
            for jogo in partidas:
                mensagem += f"- Furia x **{jogo['opponent']}** no evento **{jogo['event']}** dia **{jogo['date']}**\n"
            await update.message.reply_text(mensagem, parse_mode="Markdown")
        else:
            await update.message.reply_text("Nenhum jogo marcado no momento. 😢")
    else:
        await update.message.reply_text("Erro ao buscar os próximos jogos! 😔")

#noticias
async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://hltv-api.vercel.app/api/news.json"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        mensagem = "📰 Últimas notícias de CS/FURIA:\n\n"
        
        # Vamos pegar só as 3 primeiras notícias
        for noticia in dados:
            count = 0
            if "furia" in noticia['title'].lower() and count < 3 :
                mensagem += f"- [{noticia['title']}]({noticia['link']})\n"
                count+=1
        
        await update.message.reply_text(mensagem, parse_mode="Markdown")
    else:
        await update.message.reply_text("Erro ao buscar notícias. 😢")

#respostas automatizadas
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()
    if "furia" in texto:
        await update.message.reply_text("🔥 Você também é furioso!")
    elif "kscerato" in texto:
        await update.message.reply_text("🎯 kscerato joga mtooo!")
    else:
        await update.message.reply_text("Não entendi o que falou!")




#main
def main():
    TOKEN = "8173060128:AAFBsQFo013x-AfwpMAulIubLWCRHBJitTo"
    
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start)) # chama a função start
    application.add_handler(CommandHandler("jogos", jogos))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("proximos", proximos))
    application.add_handler(CommandHandler("noticias", noticias))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder)) 
    
    application.run_polling()
    
if __name__ == '__main__':
    main()