import requests
import json
import time
import sys
import base64

chat_history = []

def get_url():
    encoded = "aHR0cHM6Ly9sdW1pbmFpLm15LmlkLw=="
    return base64.b64decode(encoded).decode('utf-8')

def kirim_ke_luminai(pesan):
    url = get_url()
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
    print()

def mulai_chat():
    encoded_text = (
        "PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQ0KU2VsYW1hdCBkYXRhbmcgZGkgb2Jyb2xhbiBiZXJzYW1hIEx1bWluQUkhDQpTY3JpcHQgYnkgQVAgfCBEaWR1a3VuZ2kgb2xlaCBBUEkgTHVtaW5BSSBtaWxpayBzaXB1dHpNCktldGlrICdrZWx1YXInIHVudHVrIG1lbmdha2hpcmkgb2Jyb2xhbi4NCj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQ=="
    )
    decoded_text = base64.b64decode(encoded_text).decode("utf-8")
    print("\033[93m" + decoded_text + "\033[0m")

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
        time.sleep(1.2)

        balasan = kirim_ke_luminai(user_input)

        print(" " * 50, end="\r")
        print("\033[92mLuminAI:\033[0m ", end="")
        efek_ketik(balasan)
        print("\033[90m" + "-" * 60 + "\033[0m")

if __name__ == "__main__":
    mulai_chat()
