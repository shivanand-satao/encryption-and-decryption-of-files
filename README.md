# 🔐 String Encryption and Decryption Portal

> A secure desktop application built with Python and Tkinter that allows users to encrypt and decrypt text messages with AES encryption. The application includes recipient-specific encryption and a two-factor authentication system for decryption.


## ✨ Features

- ✅ **AES Encryption**: Implements secure AES encryption for text messages
- 🎨 **User-Friendly Interface**: Clean and intuitive GUI with separate encryption and decryption panels
- 👥 **Recipient Management**: Predefined recipient list with masked details for secure message targeting
- 🔒 **Two-Factor Authentication**: Requires both password and recipient-specific details for decryption
- 🔄 **Animated Interface**: Features an animated lock icon for visual feedback
- ↩️ **Reset Functionality**: Allows users to clear input fields and start over

## 📸 Screenshots

### 1. Main Interface
![Main Interface]![Screenshot 2024-12-21 175528](https://github.com/user-attachments/assets/d87213ae-3a42-43ff-be53-2b5dbfd61ae7)
*The main application window showing encryption (left) and decryption (right) panels with the central lock icon.*


### 2. Encryption Process
![Encryption Process]![Screenshot 2024-12-21 175603](https://github.com/user-attachments/assets/df2e7d90-0bfe-4093-8201-4370d246cad2)
*Text encryption interface with recipient selection dropdown.*

### 3. Recipient Selection
![Reciepient Selection]![Screenshot 2024-12-21 175648](https://github.com/user-attachments/assets/22589be9-40e2-4398-b589-5dbf5fb0851d)
*Selecting a recipient for message encryption with predefined user list.*

### 4. Decryption Validation
![Decryption Validation]![Screenshot 2024-12-21 175654](https://github.com/user-attachments/assets/455b5d02-1e46-4d3d-a6e9-4a7048478fc6)

*Two-factor authentication popup for message decryption.*

## 📋 Prerequisites

- **Python 3.x**
- **Required Python packages:**
  ```bash
  pip install pillow pycryptodome
  ```

## 📁 Project Structure

```plaintext
string-encryption-portal/
│
├── main.py                  # Main application file with encryption/decryption logic
│
├── assets/                  # Directory for application assets
│   └── encrypt.gif         # Animated lock icon
│
├── screenshots/             # Application screenshots for documentation
│   ├── main_interface.png  # Main application window
│   ├── encryption_process.png    # Encryption interface
│   ├── recipient_selection.png   # Recipient selection popup
│   └── decryption_validation.png # Validation popup
│
│
└── README.md               # Project documentation
```


## 📖 Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **To encrypt a message:**
   - Enter the secret key (password)
   - Type your message in the left (red) panel
   - Click "Encrypt"
   - Select the intended recipient
   - Copy the generated encrypted text

3. **To decrypt a message:**
   - Enter the secret key (password)
   - Paste the encrypted text in the right (green) panel
   - Click "Decrypt"
   - Enter the recipient's masked name and birth date
   - View the decrypted message


# 🔒 Security Features

## 🔄 Bit Shifting
Implements additional security through bit shifting operations. Each character in sensitive data undergoes a bit-level transformation, adding an extra layer of security beyond standard encryption.

## 🎭 Masked Recipients
Uses masked names and birth dates for recipient verification. Recipients' identities are protected through a masking system that reveals only necessary partial information for verification purposes.

## 🗝️ Secure Key Storage
Employs AES key for encryption/decryption operations. Utilizes military-grade AES encryption algorithm with a 256-bit key length for maximum security of stored and transmitted data.

## ✅ Two-Step Verification
Requires both password and recipient details for successful decryption. This dual-layer authentication system ensures that only intended recipients with proper credentials can access the encrypted messages.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request



## 🙏 Acknowledgments

- Built using **Python's Tkinter** library for GUI
- Uses **PyCryptodome** for AES encryption
- Implements custom bit shifting algorithms for additional security

## ⚠️ Important Notes

1. **Security**: 
   > Remember to never share your encryption key or recipient details

2. **Password**: 
   > The default password for testing is `1234567890`


