import openai
from telegramde  l'importation de télégrammes  
du  télégramme . ext  import  ApplicationBuilder , CommandHandler , ContextTypes

# identifiants de l'API OpenAI
openai . api_key = "ICI-VOTRE-OPEN-API-TOKEN"
# Informations d'identification de l'API Telegram Bot
token  =  "ICI-VOTRE-TELEGRAM-API-KEY"

async  def  hello ( update : Update , context : ContextTypes . DEFAULT_TYPE ) ->  None :
    attendre la  mise à jour . message . texte_réponse ( f'Bonjour { mise à jour . utilisateur_effectif . prénom } ' )
async def ask(update, context):
    # Get the user's message
    message = update.message.text.split(" ", 1)[1]
    print(message)
    # Use OpenAI to generate a response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{message}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    await update.message.reply_text(f'Response {response}')

app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("ask", ask))
app.run_polling()
