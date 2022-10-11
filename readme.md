<h1 align="center">
  <br>
 :robot: Image Text Extraction Telegram Bot by Boramorka :robot:
</h1>


<h2 align="center">
  Built with
  <br>
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" width="100">
    <img src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white" width="100">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" width="119">
    <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=green" width="100">
</h2>

<p align="center">
  <a href="#how-to-use">How To Use</a> •
  <a href="#how-to-run-locally">How To Run Locally</a> •
  <a href="#built-process">Built process</a> •
  <a href="#feedback">Feedback</a>
</p>

You may interested in this bot if you need to recognize some text from the image. It's free and quick.

Supported languages:
* English :us:
* Russian :ru:

The :old_key: key technology is we used is a Tesseract OCR by Google that has Python API.
![Tesseract](https://github.com/boramorka/usercontent/blob/main/gifs/Tesseract.gif?raw=true)

## How To Use
:robot: Bot link: https://t.me/boramorka_text_extraction_bot

![Usage](https://github.com/boramorka/usercontent/blob/main/gifs/tg%20bot%201.gif?raw=true)
* Send a photo of text. Type **/lang** to choose a language. :heavy_check_mark:
* Make sure that your document has a white background, readable black letters and picture is not rotated. :heavy_check_mark:
* If choosed EN+RU mode it recognises both languages at the same time. But more artifacts may arise. If your document is in one language, please select that language. :heavy_check_mark:

## How To Run Locally :desktop_computer:

  ``` bash
  # Clone this repository
  $ git clone https://github.com/boramorka/text-extraction-app.git

  # Go into the repository
  $ cd text-extraction-app

  # Install dependencies
  $ pip install requirements.txt

  # Run app
  $ python bot.py
  ```

## Built process :keyboard:

- First of all we creating an app.py file for the main app. It contains:
  ```python
  # Path to pytesseract
  pytesseract.pytesseract.tesseract_cmd

  # Code for text recognition
  def get_text():
  ...............
  ```
- Bot.py script starts the bot. It containts **AIOGram**. It's a pretty simple and fully asynchronous framework for [Telegram Bot API](https://core.telegram.org/bots/api) written in Python 3.7 with [asyncio](https://docs.python.org/3/library/asyncio.html) and [aiohttp](https://github.com/aio-libs/aiohttp). It helps you to make your bots faster and simpler.
  

  ```python
  # Bot class takes an API key to connect to the Telegram servers.
  bot = Bot(token=os.getenv("TEXT_EXTRACTOR_API_KEY")) #Note: API key is envioroment variable

  # Dispatcher will process incoming updates: messages, edited messages, channel posts, edited channel posts, inline queries, chosen inline results, callback queries, shipping queries, pre-checkout queries.
  dp = Dispatcher(bot) 

  # Decorator that takes a message and processes it.
  @dp.message_handler(text=message)
  ```

- Heroku deployment:
Important files:
  - :page_facing_up: bot.py: the bot application (refer to my Github for the source code) 
  - :page_facing_up: Aptfile : the third-party dependencies for Heroku to install (e.g: tesseract-ocr)
  - :page_facing_up: Procfile : a list of process types in an app (on Heroku)
  - :page_facing_up: requirements.txt : a list of dependencies to install
  - :page_facing_up: runtime.txt : version of Python to run on Heroku (optional)

  ```bash
  # HEROKU DEPLOYMENT PROCESS

  # Note:
  # Add this line to bot.py
  pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"
  # (refer to my Github for the source code)

  # Login to Heroku, and create a new app:
  $ heroku login
  $git init
  $heroku create boramorka-text-extraction-app
  $heroku git:remote -a boramorka-text-extraction-app

  # Add Buildpacks:
  $ heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt
  $ heroku buildpacks:add --index 2 heroku/python

  # Add Config Vars:
  $ heroku config:set TESSDATA_PREFIX=/app/.apt/usr/share/tesseract-ocr/4.00/tessdata

  # heroku stack (heroku-20) has bad compatibility with tesseract.
  # You may need to change heroku stack from 20 to 18 using command:
  $ heroku stack:set heroku-18

  # Deploy app on Heroku:
  $ git add .
  $ git commit -m "Initial commit to Heroku"
  $ heroku git:remote -a boramorka-text-extraction-app
  $ git push heroku master

  # Check worker status:
  $ heroku ps

  # Run worker
  $ heroku ps:scale worker=1
  ```

## Feedback
:person_in_tuxedo: Feel free to send me feedback on [Telegram](https://t.me/boramorka). Feature requests are always welcome. 

:abacus: [Check my other projects.](https://github.com/boramorka)


