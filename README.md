# Prodigy Python Projects  

This repository contains five cybersecurity-related Python projects, covering encryption, security analysis, and ethical hacking techniques.  

## Projects Overview  

### 1️⃣ Caesar Cipher  
A simple encryption method that shifts letters in the alphabet by a given amount.  
- **Encryption & Decryption**
- **Supports uppercase & lowercase letters**
- **Retains non-alphabet characters**

📌 **Usage:**  
```python
caesar_cipher("Hello, World!", 3, mode="encrypt")  # Encrypt text  
caesar_cipher("Khoor, Zruog!", 3, mode="decrypt")  # Decrypt text  
2️⃣ Pixel Manipulation for Image Encryption
Encrypts images using bitwise XOR operations.

Works with any image format
Uses a numeric key for encryption & decryption
📌 Usage:

python
Copy
Edit
pixel_encrypt("image.png", 123)  # Encrypt an image  
pixel_decrypt("encrypted_image.png", 123)  # Decrypt the image  
3️⃣ Password Complexity Checker
Evaluates the strength of a password based on various criteria.

Checks length, uppercase, lowercase, digits, special characters
Returns a strength rating from "Very Weak" to "Very Strong"
📌 Usage:

python
Copy
Edit
password_strength("SecurePass123!")  # Output: "Very Strong"  
4️⃣ Simple Keylogger
Logs keystrokes and saves them to a file (keylog.txt).

Captures all keyboard input
Runs in the background
📌 Usage:

python
Copy
Edit
keylogger()  # Starts logging keystrokes  
5️⃣ Network Packet Analyzer
Sniffs network packets to analyze MAC addresses and protocols.

Captures raw network traffic
Displays source & destination MAC addresses
📌 Usage:

python
Copy
Edit
packet_sniffer()  # Starts capturing packets  
📌 Setup & Installation
Clone the repository:
sh
Copy
Edit
git clone https://github.com/Yahiyakhan00/my-new-repository.git
cd my-new-repository
Install dependencies:
sh
Copy
Edit
pip install -r requirements.txt
Run any project as needed! 🚀
⚠️ Disclaimer
This repository is intended for educational purposes only. Any misuse of these tools is strictly prohibited.

📩 Connect with me: GitHub
