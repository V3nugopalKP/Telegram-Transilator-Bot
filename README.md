
# Telegram Translator Bot

## Description
This is a simple Telegram bot that translates messages sent to it. It uses the Google Translate API to translate messages into the specified language. The bot provides a `/start` command to greet users and translate any text messages it receives.

## Features
- Responds to the `/start` command with a welcome message.
- Translates incoming text messages into the specified language.
- Uses the `python-telegram-bot` library for Telegram Bot API integration.
- Utilizes the `googletrans` library for translation services.

## Requirements
- Python 3.x
- `python-telegram-bot` library
- `googletrans` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/V3nugopalKP/telegram-translator-bot.git
   cd telegram-translator-bot
2. Install the required libraries:

   ```bash
   pip install python-telegram-bot googletrans
3. Replace the placeholder TOKEN in bot.py with your actual Telegram Bot API token.

## Configuration
1. To change the target language for translation:

 - Open `language_translator.py`.
2. Locate the line:

    ```bash
   translated_text = translator.translate(original_text, dest='de').text
    
3. Replace 'de' with the desired language code. Here are some common language codes:
   
 - English: en.
 - Spanish: es
 - French: fr
 - German: de
 - Italian: it
 - Portuguese: pt
 - Chinese: zh-CN
 - Japanese: ja
 - Korean: ko
 - Russian: ru
 
- For a full list of language codes supported by Google Translate, refer to Google's documentation.
## Usage
1. Run the bot:
   ```bash
   python language_translator.py
2. Interact with the bot on Telegram:

 - Start the bot by sending the /start command.
 - Send any text message, and the bot will reply with the translated message in the configured language.
   

## Contributing
Feel free to open issues or submit pull requests if you'd like to contribute improvements to the bot.
