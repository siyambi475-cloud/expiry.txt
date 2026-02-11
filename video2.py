import os
import requests
import datetime

# আপনার GitHub-এর Raw লিঙ্কগুলো
EXPIRY_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/expiry.txt"
COMMAND_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/cmd2.txt"

# আপনার টেলিগ্রাম লিঙ্ক
TELEGRAM_LINK = "https://t.me/rifat_developer" 

def get_data(url):
    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            return r.text.strip()
        return None
    except:
        return None

def start():
    print("\n[+] চেকিং এক্সেস (Tool 2)...")
    
    # ১. একটাই expiry.txt থেকে মেয়াদ চেক করা
    expiry_data = get_data(EXPIRY_URL)
    if not expiry_data:
        print("[-] সার্ভার কানেকশন এরর!")
        return

    try:
        expiry_date = datetime.datetime.strptime(expiry_data, '%Y-%m-%d').date()
    except:
        print("[-] তারিখের ফরম্যাটে ভুল!")
        return

    if datetime.date.today() > expiry_date:
        print("\n🚫 TIME EXPIRED! মেয়াদ শেষ। আপনাকে টেলিগ্রামে পাঠানো হচ্ছে...")
        os.system(f"termux-open-url {TELEGRAM_LINK}")
        return

    # ২. নতুন কমান্ড (cmd2.txt) লোড করা
    print("[+] এক্সেস অনুমোদিত! Tool 2 এর কমান্ড লোড হচ্ছে...")
    raw_command = get_data(COMMAND_URL)
    
    if not raw_command:
        print("[-] cmd2.txt ফাইল পাওয়া যায়নি!")
        return

    # ৩. ভিডিও চেক করা
    if not os.path.exists('_outputDone'): os.makedirs('_outputDone')
    if not os.path.exists('_output'):
        print("[-] '_output' ফোল্ডারটি পাওয়া যায়নি! আগে প্রথম টুলটি রান করুন।")
        return

    # আপনার লুপ কমান্ডটি সরাসরি রান করা
    print("[🚀] মাল্টি-ভিডিও প্রসেসিং শুরু হচ্ছে...")
    
    # কমান্ডের ভেতর {input} এর জায়গায় '_output/*' বসিয়ে দেওয়া হচ্ছে
    final_cmd = raw_command.replace("{input}", "_output/*").replace("{output}", "")
    
    os.system(final_cmd)

    print("\n[✅] অভিনন্দন! Tool 2 এর সব কাজ শেষ।")
    print("[💾] ভিডিওগুলো '_outputDone' ফোল্ডারে সেভ হয়েছে।")

if __name__ == "__main__":
    start()
