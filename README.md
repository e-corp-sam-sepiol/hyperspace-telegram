# hyperspace-telegram
Resources and python script for Hyperspace telegram bot

## Telegram Chat Commands
**[Admin Commands]**
* **!kick** - `Reply to a user to kick them from your chat.` They can come back later. `!skick` is the silent version.
* **!ban** - `Reply to a user to ban them from your chat.` They won't be able to join your chat again. 

>To issue a temporary ban, use: `!ban 30d` (30 days), `!ban 2w` (2 weeks), `!ban 10h` (10 hours), `!ban 2m` (2 minutes). 

You can also ban by user ID. In this case, the order of parameters does not matter, all of these are valid: 

`!ban 1234 5m`; `!ban 5m 1234`; `!ban 1234` (permanent).

>`!sban` is the silent version.

* **!unban** `Reply to a user to unban them.`

* **!mute** - `Reply to a user to mute them for 12 hours` (default). 

To issue a temporary mute, use: 

`!mute 30d (30 days), !mute 2w (2 weeks), !mute 10h (10 hours), !mute 2m (2 minutes).`

>!smute is the silent version.

* **!unmute** `Reply to a user to unmute them.`

* **!readonly**, **!channelmode**, **!ro** - `Enable read-only mode.` Only admins can send messages. Whitelisted people won't be able to send messages. Send the command again to disable the mode.

* **!warn** [amount=1] [reason] - `Reply to a user to warn them.` When number of warns reaches 3 (default), user is banned (default). You can change the defaults in moderation settings. You can omit "amount" parameter and just input your reason.

* **!unwarn**, **!acquit** [amount=1] [reason] - `Reply to a user to clear their warning history.`

* **!unrestrict**, **!un** - `Reply to a user to unmute them and remove all possible restrictions.`

* **!status** - `Reply to a user to request a status report.`

* **!purge** - `Reply to a message to delete any messages between that message and your message.` **Use with care.**

* **!d** - `Mark the message for deletion after some time.` 

>Usage: `!d 30d` (30 days), `!d 2w` (2 weeks), `!d 10h` (10 hours), `!d 2m` (2 minutes).

**[User commands]**
>These commands work for everybody.

* **!report** - `Reply to a message to report it to admins.` Report system must be enabled.

* **!cdoctor** - `Check the current status of Combot in your group.`

## Hyperspace Bot Commands
```
/about - Display Hyperspace links and resources
/coin - Display coin information links
/cap - Display global market cap information
/exchange - Display exchange information
/price - Display price of [ticker] (via CoinMarketCap)
/rules - Display the chat rules
```
**Examples:**  

__/about__  
```
Website: hspace.app                                                                                   
Trello: https://trello.com/b/nrzksknR/hyperspace-feature-roadmap
Discord: https://discordapp.com/invite/bsffQ76
Reddit: https://www.reddit.com/r/HyperSpace/
Twitter: https://twitter.com/HyperspaceCloud
Facebook: https://www.facebook.com/HyperspaceApp/
Github: https://github.com/HyperspaceApp
```

__/exchange__  
```
- Exchange Information -                                                                                                   
C-Patex https://c-patex.com/markets/xscbtc
BiteBTC https://bitebtc.com/trade/xsc_btc
Safe.Trade https://safe.trade/trading/xscbtc
WKJ (玩客家) http://www.wkj.link/trade/index/market/xsc_cny/
```

__/rules__
```
- Hyperspace Telegram Chat Rules -
1.) Respect and be nice to each other
2.) No spamming. This includes active advertising (pump and dump groups, ICOs, products, services, and other coins) and links to other Discords
3.) Nicknames cannot be advertisements or offensive to coins or other users.
```
