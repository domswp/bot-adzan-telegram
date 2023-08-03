import requests
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import JobQueue
from bs4 import BeautifulSoup

# Ganti dengan token bot Anda
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Inisialisasi bot
bot = Bot(token=BOT_TOKEN)

# Daftar pengguna yang berlangganan
subscribers = set()

def start(update, context):
    user_id = update.message.chat_id
    subscribers.add(user_id)
    update.message.reply_text("Anda telah berlangganan notifikasi adzan.")

def stop(update, context):
    user_id = update.message.chat_id
    subscribers.discard(user_id)
    update.message.reply_text("Anda telah berhenti berlangganan notifikasi adzan.")

def get_adzan_times():
    # API untuk mendapatkan waktu adzan di wilayah Indonesia
    url = "https://api.pray.zone/v2/times/today.json?city=29"
    response = requests.get(url)
    data = response.json()

    adzan_times = {
        "Fajr": data["results"]["datetime"][0]["times"]["Fajr"],
        "Dhuhr": data["results"]["datetime"][0]["times"]["Dhuhr"],
        "Asr": data["results"]["datetime"][0]["times"]["Asr"],
        "Maghrib": data["results"]["datetime"][0]["times"]["Maghrib"],
        "Isha": data["results"]["datetime"][0]["times"]["Isha"]
    }

    return adzan_times

def send_adzan_notification(context: CallbackContext):
    adzan_times = get_adzan_times()
    
    for user_id in subscribers:
        message = "🕌 Jadwal Adzan Hari Ini:\n\n"
        for adzan, time in adzan_times.items():
            message += f"{adzan}: {time}\n"
        bot.send_message(chat_id=user_id, text=message)

def main():
    updater = Updater(bot=bot, use_context=True)
    dispatcher = updater.dispatcher
    jq: JobQueue = updater.job_queue

    # Menambahkan handler perintah
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    stop_handler = CommandHandler('stop', stop)
    dispatcher.add_handler(stop_handler)

    # Memulai mengirim notifikasi adzan setiap hari
    jq.run_repeating(send_adzan_notification, interval=86400, first=0)  # Setiap 24 jam

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
