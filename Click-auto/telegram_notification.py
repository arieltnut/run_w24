from telegram import Bot

# Hàm gửi tin nhắn đến bot Telegram
def send_telegram_message(bot_token, chat_id, message):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# Thông tin của bot và chat_id
bot_token = "7016202931:AAG-BRNvn3TbWW6DKz17R7xdq_pf0pd_cNg"
chat_id = "6604544426"

# Tin nhắn bạn muốn gửi
message = "Hello from Python!"

# Gửi tin nhắn
send_telegram_message(bot_token, chat_id, message)
