Oops — you're totally right 😅  
Let me give you a clean and ready-to-copy version of the `README.md` with working markdown, code blocks, and clear formatting:

---

## ✅ `README.md`

```markdown
# 🧪 phishinglab

A modular Python-based email scanner that detects malicious attachments and suspicious links — without using paid APIs like VirusTotal.

---

## 🚀 Features

- 📬 Fetch unread emails via IMAP
- 📦 Extract `.zip` attachments from emails
- 🧪 Scan attachments using custom YARA rules
- 🌐 Analyze links in email body:
  - Detect phishing-related keywords in domains
  - Flag domains registered in the last 30 days
- 🔐 Fully offline link analysis (no paid APIs)
- 📁 Automatically sort emails into: `Clean`, `ToBeInspected`

---

## 📁 Project Structure

```
phishinglab/
├── main.py                   # Orchestrates the whole process
├── config.py                 # Sensitive settings (email credentials etc.)
├── email_client.py           # Connects to IMAP and fetches emails
├── attachment_handler.py     # Extracts ZIP attachments
├── yara_scanner.py           # Static malware scan using YARA
├── link_checker.py           # Suspicious link detection (domain analysis)
├── sandbox_runner.py         # Optional: run files in isolated environment
├── utils.py                  # Helpers (hashing, moving emails)
├── requirements.txt          # Python dependencies
└── rules/
    └── malware_rules.yar     # Your YARA rule definitions
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/NetAdminHQ/phishinglab.git
cd phishinglab
```

### 2. Create a Virtual Environment
```bash
python3 -m venv phishinglab
source phishinglab/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Copy and edit your configuration file:
```bash
cp config.py.template config.py
```

Fill in your email details in `config.py`:
```python
EMAIL = "your_email@example.com"
PASSWORD = "your_app_password"
IMAP_SERVER = "imap.example.com"

ATTACH_DIR = "attachments"
EXTRACTED_DIR = "extracted"
YARA_RULE_FILE = "rules/malware_rules.yar"
```

**⚠️ Never commit your `config.py` to GitHub. Use `.gitignore` to keep it private.**

---

## ▶️ Run the Scanner

```bash
python3 main.py
```

---

## 🛡️ Safe Usage Tips

- Use a **dedicated inbox** for testing (not your real one)
- Run in a **virtual machine** or isolated environment
- Inspect suspicious results before interacting with them
- Enable sandboxing **only** if properly isolated

---

## 🧪 Roadmap / Ideas

- DKIM/SPF checks
- PDF phishing detection
- Office macro analysis
- ELK integration (for alerting)
- Web interface (dashboard)

---

## 👨‍💻 Author

Made by [NetAdminHQ](https://github.com/NetAdminHQ) with ❤️  
Pull requests and suggestions welcome!

---

## 📄 License

MIT License — free to use, modify, and improve.
```

---

Let me know if you want me to:
- Save this to a file for you (and push it)
- Add a matching `config.py.template`
- Set up `.gitignore` if it's not already there

Ready when you are 💻🔥
