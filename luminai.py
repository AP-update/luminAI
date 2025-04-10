import requests
import json
import time
import sys

chat_history = []

def kirim_ke_luminai(pesan):
    url = 'https://luminai.my.id/'
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }

    chat_history.append(f"Kamu: {pesan}")
    history_text = "\n".join(chat_history)

    data = {
        'content': history_text
    }

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers, timeout=15)
        if response.status_code == 200:
            hasil = response.json()
            balasan = hasil.get("result", "[Key 'result' tidak ditemukan]\nRaw: " + str(hasil))
            chat_history.append(f"LuminAI {balasan}")
            return balasan
        else:
            return f"[Gagal] Status code: {response.status_code}\n{response.text}"
    except requests.exceptions.RequestException as e:
        return f"[Gagal menghubungi LuminAI] {e}"

def efek_ketik(teks, delay=0.02):
    for char in teks:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # baris baru

def mulai_chat():
    print("\033[93m" + "=" * 60)
    print("Selamat datang di obrolan bersama LuminAI!")
    print("Script by AP | Didukung oleh API LuminAI milik siputz")
    print("Ketik 'keluar' untuk mengakhiri obrolan.")
    print("=" * 60 + "\033[0m")

    idle_start = time.time()

    while True:
        if time.time() - idle_start > 30:
            print("\033[94m\n[LuminAI]: Masih di sana? Yuk lanjut ngobrol!\033[0m")
            idle_start = time.time()

        try:
            user_input = input("\n\033[96mKamu:\033[0m ").strip()
        except KeyboardInterrupt:
            print("\n\033[92mLuminAI: Sampai jumpa, tetap semangat ya!\033[0m")
            break

        if user_input.lower() in ["keluar", "exit", "quit"]:
            print("\033[92mLuminAI: Sampai jumpa, tetap semangat ya!\033[0m")
            break

        idle_start = time.time()

        print("\033[90mLuminAI sedang mengetik...\033[0m", end="\r")
        time.sleep(1.2)  # Delay buat efek ngetik

        balasan = kirim_ke_luminai(user_input)

        print(" " * 50, end="\r")  # Clear typing indicator
        print("\033[92mLuminAI:\033[0m ", end="")
        efek_ketik(balasan)
        print("\033[90m" + "-" * 60 + "\033[0m")

if __name__ == "__main__":
    mulai_chat()