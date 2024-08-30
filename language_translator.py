from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googletrans import Translator 

# Initialize the translator
translator = Translator()

# Define command handlers
def start(update, context):
    update.message.reply_text('Hello! Send me a message, and I will translate it for you.')

def translate_message(update, context):
    original_text = update.message.text
    
    translated_text = translator.translate(original_text, dest='de').text
    update.message.reply_text(translated_text)

def main():
    # Telegram Bot Token
    TOKEN = 'Bot-Token'   
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    # Commands
    dp.add_handler(CommandHandler("start", start))
    # Messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))
    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
