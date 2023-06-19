import config
import logging
import kb
from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types.message import ContentType, Message
from aiogram.types import ReplyKeyboardRemove

PRICERUB = types.LabeledPrice(
    label="Подписка на 1 месяц", amount=500*100)

PRICEUSD = types.LabeledPrice(
    label="1 month subssciption", amount=5*100)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('You can pay both USD and RUB \nВы можете использовать как USD так Руб.', reply_markup=kb.mainKb)

@dp.message_handler(lambda message: message.text and 'купить' in message.text.lower())
async def buy(message: types.Message):
    
    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=config.PAYMENT_TOKEN,
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICERUB],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")
    
@dp.message_handler(lambda message: message.text and 'buy' in message.text.lower())
async def buy(message: types.Message):
    
    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=config.PAYMENT_TOKEN_USD,
                           currency="USD",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICEUSD],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
