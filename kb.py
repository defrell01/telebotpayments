from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# currencyRub = KeyboardButton('RUB 🇷🇺')
# currencyUsd = KeyboardButton('USD 🇺🇸')

# currencyKb = ReplyKeyboardMarkup(resize_keyboard=True)
# currencyKb.add(currencyRub)
# currencyKb.add(currencyUsd)


# buySubRu = KeyboardButton('/buy')

# userKbRu = ReplyKeyboardMarkup(resize_keyboard=True)
# userKbRu.add(buySubRu)


# buySubUs = KeyboardButton('Buy subscription')

# userKbUs = ReplyKeyboardMarkup(resize_keyboard=True)
# userKbUs.add(buySubUs)


mainKb = ReplyKeyboardMarkup(resize_keyboard=True)

buyUsd = KeyboardButton('Buy subscription USD 🇺🇸')
buyRub = KeyboardButton('Купить подписку Руб. 🇷🇺')

mainKb.add(buyRub).add(buyUsd)