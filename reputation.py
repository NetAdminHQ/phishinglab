import requests

def check_email_reputation(email_addr):
    if not email_addr or "@" not in email_addr:
        return
    try:
        r = requests.get(f"https://emailrep.io/{email_addr}")
        if r.status_code == 200:
            data = r.json()
            print(f"📧 Email reputation: {data['reputation']}, Suspicious: {data['suspicious']}")
    except Exception as e:
        print(f"⚠️ Error checking sender: {e}")
