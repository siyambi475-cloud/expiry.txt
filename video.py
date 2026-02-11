import os
import requests
import datetime
import webbrowser

# আপনার GitHub-এর সঠিক Raw লিঙ্কগুলো
EXPIRY_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/expiry.txt"
COMMAND_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/cmd.txt"

# আপনার টেলিগ্রাম লিঙ্ক (এখানে আপনার ইউজারনেম দিন)
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
    print("\n[+] চেকিং এক্সেস ও সার্ভার স্ট্যাটাস...")
    
    expiry_data = get_data(EXPIRY_URL)
    if not expiry_data:
        print("[-] সার্ভার কানেকশন এরর!")
        return

    try:
        expiry_date = datetime.datetime.strptime(expiry_data, '%Y-%m-%d').date()
    except:
        print("[-] তারিখের ফরম্যাটে ভুল!")
        return

    # মেয়াদ চেক করা
    if datetime.date.today() > expiry_date:
        print("\n" + "="*45)
        print("🚫 TIME EXPIRED! আপনার মেয়াদ শেষ।")
        print("🔗 আপনাকে সরাসরি এডমিনের টেলিগ্রামে নিয়ে যাওয়া হচ্ছে...")
        print("="*45 + "\n")
        
        # সরাসরি ব্রাউজারে টেলিগ্রাম ওপেন করার কমান্ড
        os.system(f"termux-open-url {TELEGRAM_LINK}")
        return

    print("[+] এক্সেস অনুমোদিত! ভিডিও প্রসেসিং কমান্ড লোড হচ্ছে...")
    raw_command = get_data(COMMAND_URL)
    
    if not raw_command:
        print("[-] কমান্ড ফাইল পাওয়া যায়নি!")
        return

    if not os.path.exists('_output'): os.makedirs('_output')
    if not os.path.exists('_input'):
        os.makedirs('_input')
        print("[!] '_input' ফোল্ডার তৈরি করা হয়েছে।")
        return

    input_files = [f for f in os.listdir('_input') if f.endswith(('.mp4', '.mkv', '.mov'))]
    
    if not input_files:
        print("[-] '_input' ফোল্ডারে কোনো ভিডিও নেই!")
        return

    for file in input_files:
        print(f"\n[🚀] এডিট হচ্ছে: {file}")
        input_path = f"_input/{file}"
        output_path = f"_output/{file}"
        final_cmd = raw_command.replace("{input}", input_path).replace("{output}", output_path)
        os.system(final_cmd)

    print("\n[✅] কাজ শেষ!")

if __name__ == "__main__":
    start()
