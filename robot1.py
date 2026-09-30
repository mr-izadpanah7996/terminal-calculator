import telebot
import sys

bot = telebot.TeleBot("8236846459:AAHRqxxVm-Dp6oYViMpMxOEkqcb16B10HHQ")
CHANNEL_ID = "@chehraye_no77"

def create_main_markup():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_site = telebot.types.KeyboardButton("سایت خبری موسسه")
    btn_aparat = telebot.types.KeyboardButton("آپارات")
    btn_stop = telebot.types.KeyboardButton("توقف ربات")
    markup.add(btn_site, btn_aparat)
    markup.add(btn_stop)
    return markup

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "سلام. پنل مدیریت ربات فعال شد. لطفا گزینه مورد نظر را انتخاب کنید:", reply_markup=create_main_markup())

@bot.message_handler(func=lambda message: message.text == "سایت خبری موسسه")
def send_site_news_to_channel(message):
    photo_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
    caption_text = "این خبر جدید سایت است که توسط ربات در کانال منتشر شد."
    try:
        bot.send_photo(CHANNEL_ID, photo_url, caption=caption_text)       
        bot.send_message(message.chat.id, "✅ خبر سایت با موفقیت در کانال درج شد.")
    except:
        bot.send_message(message.chat.id, "❌ خطا: لطفا چک کنید ربات در کانال ادمین باشد و آیدی کانال درست وارد شده باشد.")

@bot.message_handler(func=lambda message: message.text == "آپارات")
def send_aparat_video_to_channel(message):
    video_url = "http://techslides.com/demos/sample-videos/small.mp4"
    caption_text = "این ویدیوی جدید آپارات است که در کانال منتشر شد."
    try:
        bot.send_video(CHANNEL_ID, video_url, caption=caption_text)
        bot.send_message(message.chat.id, "✅ ویدیوی آپارات با موفقیت در کانال درج شد.")
    except:
        bot.send_message(message.chat.id, "❌ خطا: در ارسال ویدیو به کانال مشکلی پیش آمد.")

@bot.message_handler(func=lambda message: message.text == "توقف ربات")
def stop_bot(message):
    remove_keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "ربات با موفقیت خاموش شد.", reply_markup=remove_keyboard)
    raise SystemExit

@bot.message_handler(content_types=['text'])
def handle_unknown_text(message):
    bot.send_message(message.chat.id, "دستور نامعتبر است. لطفا از منو استفاده کنید:", reply_markup=create_main_markup())

bot.infinity_polling()