from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Crypto.Cipher import AES

# AES encryption key
aes_key = b'W4d#2Rf0Zc8y6S*7@9jK^1Lm5p$3XqYh'

# Predefined recipients with masked details
recipients = {
    "shivanand": {"password": "1234567890", "masked_name": "shiv", "birth_date": "2108"},
    "sharvari": {"password": "1234567890", "masked_name": "shar", "birth_date": "1111"},
    "shreya": {"password": "1234567890", "masked_name": "shre", "birth_date": "1111"},
    "omkar": {"password": "1234567890", "masked_name": "omka", "birth_date": "1111"}
}

def bit_shift_right(text):
    """Right shift each character by 1 bit"""
    return ''.join(chr((ord(char) >> 1) & 0xFF) for char in text)

def bit_shift_left(text):
    """Left shift each character by 1 bit"""
    return ''.join(chr((ord(char) << 1) & 0xFF) for char in text)

def reset():
    code.set('')
    decrypt_textbox.delete("1.0", END)

def show_recipient_popup(encrypted_text_root, text_to_encrypt):
    popup = Toplevel(screen)
    popup.geometry("300x200")
    popup.title("Select Recipient")

    Label(popup, text="Select the recipient:").pack(pady=10)

    recipient_var = StringVar()
    recipient_var.set("Select Recipient")

    recipient_dropdown = OptionMenu(popup, recipient_var, *recipients.keys())
    recipient_dropdown.pack(pady=10)

    def on_recipient_selected():
        recipient = recipient_var.get()
        if recipient in recipients:
            masked_name = recipients[recipient]["masked_name"]
            birth_date = recipients[recipient]["birth_date"]
            
            # Right shift the masked_name and birth_date before encryption
            shifted_name = bit_shift_right(masked_name)
            shifted_birth = bit_shift_right(birth_date)
            
            encrypted_text = encrypt_text_with_recipient(text_to_encrypt, shifted_name, shifted_birth)

            encrypted_textbox = Text(encrypted_text_root, font=("Arial", 12), height=10, width=40)
            encrypted_textbox.pack(padx=20, pady=20)
            encrypted_textbox.insert(END, encrypted_text)

            popup.destroy()
        else:
            messagebox.showerror("Recipient Error", "Please select a valid recipient.")

    Button(popup, text="Submit", command=on_recipient_selected).pack(pady=20)

def encrypt_text_with_recipient(text_to_encrypt, shifted_name, shifted_birth):
    cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text_to_encrypt.encode('utf-8'))
    nonce = cipher.nonce
    encrypted_text = ciphertext.hex() + ":" + nonce.hex() + f":{shifted_name}:{shifted_birth}"
    return encrypted_text

def decrypt():
    password = code.get()
    print("Decrypt function called. Password entered:", password)

    if password == "1234567890":
        encrypted_text = decrypt_textbox.get("1.0", END).strip()

        try:
            ciphertext_hex, nonce_hex, shifted_name, shifted_birth = encrypted_text.split(":")
            ciphertext = bytes.fromhex(ciphertext_hex)
            nonce = bytes.fromhex(nonce_hex)
            cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
            decrypted_text = cipher.decrypt(ciphertext).decode('utf-8')

            show_validation_popup(shifted_name, shifted_birth, decrypted_text)

        except ValueError as e:
            messagebox.showerror("Decryption Error", f"Failed to decrypt text: {e}")
    else:
        messagebox.showerror("Password Error", "Invalid password.")

def show_validation_popup(shifted_name, shifted_birth, decrypted_text):
    popup = Toplevel(screen)
    popup.geometry("300x200")
    popup.title("Validate Recipient")

    Label(popup, text="Enter masked name:").pack(pady=5)
    masked_name_entry = Entry(popup)
    masked_name_entry.pack(pady=5)

    Label(popup, text="Enter birth date (DD-MM):").pack(pady=5)
    birth_date_entry = Entry(popup)
    birth_date_entry.pack(pady=5)

    def validate():
        # Right shift the entered values for comparison
        entered_name_shifted = bit_shift_right(masked_name_entry.get())
        entered_birth_shifted = bit_shift_right(birth_date_entry.get())
        
        if entered_name_shifted == shifted_name and entered_birth_shifted == shifted_birth:
            show_decrypted_text(decrypted_text)
            popup.destroy()
        else:
            messagebox.showerror("Validation Error", "Masked name or birth date is incorrect.")

    Button(popup, text="Validate", command=validate).pack(pady=20)

def show_decrypted_text(decrypted_text):
    decrypted_text_root = Toplevel(screen)
    current_x = screen.winfo_x()
    current_y = screen.winfo_y()
    new_x = current_x + 950
    new_y = current_y + 250

    decrypted_text_root.geometry(f"400x300+{new_x}+{new_y}")
    decrypted_text_root.title("Decrypted Message")
    decrypted_text_root.configure(bg="#00bd56")

    Label(decrypted_text_root, text="Decrypted Text", font=("Arial", 12), bg="#00bd56", fg="white").pack(pady=10)
    decrypted_textbox = Text(decrypted_text_root, font=("Arial", 12), height=10, width=40)
    decrypted_textbox.pack(padx=20, pady=20)
    decrypted_textbox.insert(END, decrypted_text)

def update_gif(frame_number):
    global gif_frames
    gif_label.config(image=gif_frames[frame_number])
    frame_number += 1
    if frame_number >= len(gif_frames):
        frame_number = 0
    screen.after(100, update_gif, frame_number)

def encrypt():
    password = code.get()
    print("Encrypt function called. Password entered:", password)
()
    if password == "1234567890":
        encrypted_text_root = Toplevel(screen)
        current_x = screen.winfo_x()
        current_y = screen.winfo_y()
        new_x = current_x + 185
        new_y = current_y + 250

        encrypted_text_root.geometry(f"400x300+{new_x}+{new_y}")
        encrypted_text_root.title("Encrypted Message")
        encrypted_text_root.configure(bg="#ed3833")

        Label(encrypted_text_root, text="Enter the text to Encrypt", font=("Arial", 12), bg="#ed3833", fg="white").pack(pady=10)
        encrypt_textbox = Text(encrypted_text_root, font=("Arial", 12), height=5, width=40)
        encrypt_textbox.pack(padx=20, pady=20)

        Button(encrypted_text_root, text="Next", command=lambda: show_recipient_popup(encrypted_text_root, encrypt_textbox.get("1.0", END).strip())).pack(pady=20)
    else:
        messagebox.showerror("Password Error", "Invalid password.")

def main_screen():
    global screen
    global code
    global decrypt_textbox
    global gif_frames
    global gif_label

    screen = Tk()

    screen.geometry("1600x900")
    screen.title("String Encryption and Decryption Portal")

    gif_image = Image.open("encrypt.gif")
    gif_frames = []
    for i in range(gif_image.n_frames):
        gif_image.seek(i)
        frame = ImageTk.PhotoImage(gif_image.copy())
        gif_frames.append(frame)

    gif_label = Label(screen)
    gif_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    update_gif(0)

    decrypt_frame = Frame(screen, bg="#00bd56", bd=2, relief=RIDGE)
    decrypt_frame.place(x=screen.winfo_screenwidth()/3 + 530, y=50, width=screen.winfo_screenwidth()/3 - 70, height=screen.winfo_screenheight() - 150)

    Label(decrypt_frame, text="Enter the encrypted text to Decrypt", font="arial 15", fg="white", bg="#00bd56").pack(pady=10)
    decrypt_textbox = Text(decrypt_frame, font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD, bd=2)
    decrypt_textbox.pack(padx=5, pady=10)

    Button(decrypt_frame, text="Decrypt", font="arial 15", bg="white", fg="#00bd56", command=decrypt).pack(pady=5)

    encrypt_frame = Frame(screen, bg="#ed3833", bd=2, relief=RIDGE)
    encrypt_frame.place(x=screen.winfo_screenwidth()/9 - 70, y=50, width=screen.winfo_screenwidth()/3 - 70, height=screen.winfo_screenheight() - 150)

    Label(encrypt_frame, text="Enter the text to encrypt", font="arial 15", fg="white", bg="#ed3833").pack(pady=10)

    encrypt_textbox = Text(encrypt_frame, font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD, bd=2)
    encrypt_textbox.pack(padx=5, pady=10)
    
    Button(encrypt_frame, text="Encrypt", font="arial 15", bg="white", fg="#ed3833", command=encrypt).pack(pady=5)

    center_frame = Frame(screen)
    center_frame.place(relx=0.5, rely=0.75, anchor=CENTER)

    Label(center_frame, text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).pack(pady=10)

    code = StringVar()
    Entry(center_frame, textvariable=code, width=19, bd=0, font=("arial", 25), show='*').pack(pady=5)

    Button(center_frame, text="Reset", command=reset, width=5, font=("arial", 14)).pack(pady=10)

    screen.mainloop()

if __name__ == "__main__":
    main_screen()