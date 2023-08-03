# Bot Notifikasi Adzan di Telegram

Bot ini akan memberikan notifikasi jadwal adzan di wilayah Indonesia kepada pengguna yang berlangganan. Bot ini menggunakan Python dan pustaka python-telegram-bot serta BeautifulSoup untuk mengambil data waktu adzan.

## Instalasi

1. Pastikan Anda memiliki Python terinstal di komputer Anda. Anda bisa mendownloadnya di [python.org](https://www.python.org/downloads/).

2. Clone repository ini atau unduh kode sumbernya.

    ```
    git clone https://github.com/namareg/bot-notifikasi-adzan.git
    ```

3. Buka terminal dan navigasi ke direktori repository.

    ```
    cd bot-notifikasi-adzan
    ```

4. Buat dan aktifkan lingkungan virtual (opsional, tapi direkomendasikan).

    ```
    python -m venv venv
    source venv/bin/activate
    ```

5. Instal pustaka yang diperlukan menggunakan `pip`.

    ```
    pip install -r requirements.txt
    ```

6. Ganti nilai `BOT_TOKEN` dengan token bot Telegram Anda pada file `bot_adzan.py`.

## Menjalankan Bot

1. Pastikan Anda masih berada di lingkungan virtual yang aktif (jika menggunakan).

2. Jalankan bot dengan menjalankan file `bot_adzan.py`.

    ```
    python bot_adzan.py
    ```

3. Buka Telegram dan cari nama bot Anda. Mulai obrolan dengan bot dan gunakan perintah `/start` untuk berlangganan notifikasi adzan atau `/stop` untuk berhenti berlangganan.

Bot akan mengirim notifikasi jadwal adzan setiap hari sesuai dengan waktu yang Anda tentukan.

---

Jika Anda memiliki pertanyaan atau masalah, jangan ragu untuk menghubungi saya melalui [email](mailto:domaswp@gmail.com).

