import email
from config import ENABLE_YARA, ENABLE_EMAILREP
from email_client import connect_imap, fetch_unread_emails
from attachment_handler import save_zip_attachment, extract_zip
from yara_scanner import scan_file_with_yara
from utils import ensure_dirs
from reputation import check_email_reputation

def process_email(mail, e_id):
    _, data = mail.fetch(e_id, '(RFC822)')
    raw = data[0][1]
    msg = email.message_from_bytes(raw)

    from_addr = email.utils.parseaddr(msg["From"])[1]
    subject = msg["Subject"]
    print(f"\n--- Email from {from_addr} | Subject: {subject} ---")

    if ENABLE_EMAILREP:
        check_email_reputation(from_addr)

    suspicious = False

    for part in msg.walk():
        if "attachment" in str(part.get("Content-Disposition", "")):
            filename = part.get_filename()
            if filename and filename.lower().endswith(".zip"):
                zip_path = save_zip_attachment(part, filename)
                files = extract_zip(zip_path)
                if ENABLE_YARA:
                    for f in files:
                        if scan_file_with_yara(f):
                            suspicious = True

    folder = "ToBeInspected" if suspicious else "Clean"
    mail.create(folder)
    mail.copy(e_id, folder)
    mail.store(e_id, '+FLAGS', '\\Deleted')

def main():
    mail = connect_imap()
    unread_ids = fetch_unread_emails(mail)
    print(f"📩 {len(unread_ids)} unread emails found.")
    for eid in unread_ids:
        process_email(mail, eid)
    mail.expunge()
    mail.logout()
    print("✅ Done.")

if __name__ == "__main__":
    main()
