#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.

This program is dedicated to the public domain under the CC0 license.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from pricebot.handlers import price, cap, error, download_api_coinslists_handler, download_api_global_handler
from pricebot.config import TOKEN_BOT, TIME_INTERVAL

from pricebot.parse_apis import module_logger

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

def about(bot, update):
    """Send a message containing resource information."""
    update.message.reply_text('Website: hspace.app                                                                                   Trello: https://trello.com/b/nrzksknR/hyperspace-feature-roadmap                                                                        Discord: https://discordapp.com/invite/bsffQ76                                                                                     Reddit: https://www.reddit.com/r/HyperSpace/                                                                                            Twitter: https://twitter.com/HyperspaceCloud                                                                                                      Facebook: https://www.facebook.com/HyperspaceApp/                                                                                Github: https://github.com/HyperspaceApp')
	
def coin(bot, update):
    """Send a message containing coin information."""
    update.message.reply_text('- Coin Information -                                                                                                                                       CoinGecko https://www.coingecko.com/en/coins/hyperspace                                                                                                                         Mining Calculator https://www.coincalculators.io/coin.aspx?crypto=hyperspace-mining-calculator')

def exchange(bot, update):
    """Send a message detailing exchange information."""
    update.message.reply_text('- Exchange Information -                                                                                                   C-Patex https://c-patex.com/markets/xscbtc                                                                                                       BiteBTC https://bitebtc.com/trade/xsc_btc                                                                                                        Safe.Trade https://safe.trade/trading/xscbtc                                                                           WKJ (玩客家) http://www.wkj.link/trade/index/market/xsc_cny/')

def rules(bot, update):
    """Send a message regarding the chat rules when invoked."""
    update.message.reply_text('- Hyperspace Telegram Chat Rules -                                                                                            1.) Respect and be nice to each other                                                                                                                        2.) No spamming. This includes active advertising (pump and dump groups, ICOs, products, services, and other coins) and links to other Discords                                                                                                               3.) Nicknames cannot be advertisements or offensive to coins or other users.')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    """Start the bot."""

    # Create the EventHandler and pass it your bot's token.
    updater = Updater("TOKEN GOES HERE")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
	
    # Add pricebot handlers
    price_handler = CommandHandler('price', price, pass_args=True)
    dp.add_handler(price_handler)

    cap_handler = CommandHandler('cap', cap)
    dp.add_handler(cap_handler)

    # pricebot job queue
    job_queue = updater.job_queue
    job_queue.run_repeating(download_api_coinslists_handler, TIME_INTERVAL, 10, context='coinmarketcap')
    job_queue.run_repeating(download_api_global_handler, TIME_INTERVAL, 5)

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("coin", coin))
    dp.add_handler(CommandHandler("exchange", exchange))
    dp.add_handler(CommandHandler("rules", rules))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
