from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Crypto.Cipher import AES

# AES encryption key
aes_key = b'W4d#2Rf0Zc8y6S*7@9jK^1Lm5p$3XqYh'

# Predefined recipients with masked details (first 4 chars of name, birthdate)
recipients = {
    "Alice": {"password": "1234", "masked_name": "Alic****", "birth_date": "05-07"},
    "Bob": {"password": "1234", "masked_name": "Bob****", "birth_date": "12-11"},
    "Charlie": {"password": "1234", "masked_name": "Char****", "birth_date": "23-04"}
}

def show_recipient_popup(encrypted_text_root, text_to_encrypt):
    # Create a new popup window for selecting recipient
    popup = Toplevel(screen)
    popup.geometry("300x200")
    popup.title("Select Recipient")

    Label(popup, text="Select the recipient:").pack(pady=10)

    recipient_var = StringVar()
    recipient_var.set("Select Recipient")

    # Dropdown menu to select recipient
    recipient_dropdown = OptionMenu(popup, recipient_var, *recipients.keys())
    recipient_dropdown.pack(pady=10)

    def on_recipient_selected():
        recipient = recipient_var.get()
        if recipient in recipients:
            # Fetch masked name and birthdate for the selected recipient
            masked_name = recipients[recipient]["masked_name"]
            birth_date = recipients[recipient]["birth_date"]

            # Encrypt the text and append recipient details
            encrypted_text = encrypt_text_with_recipient(text_to_encrypt, masked_name, birth_date)

            # Display the encrypted text in the original window
            encrypted_textbox = Text(encrypted_text_root, font=("Arial", 12), height=10, width=40)
            encrypted_textbox.pack(padx=20, pady=20)
            encrypted_textbox.insert(END, encrypted_text)

            popup.destroy()  # Close the popup after selection
        else:
            messagebox.showerror("Recipient Error", "Please select a valid recipient.")

    # Button to submit recipient selection
    Button(popup, text="Submit", command=on_recipient_selected).pack(pady=20)

def encrypt_text_with_recipient(text_to_encrypt, masked_name, birth_date):
    # Encrypt the text using AES
    cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text_to_encrypt.encode('utf-8'))
    nonce = cipher.nonce

    # Store both ciphertext and nonce as hex strings for easy transfer
    encrypted_text = ciphertext.hex() + ":" + nonce.hex() + f":{masked_name}:{birth_date}"

    return encrypted_text

def update_gif(frame_number):
    global gif_frames
    global gif_label
    gif_label.config(image=gif_frames[frame_number])
    frame_number += 1
    if frame_number >= len(gif_frames):
        frame_number = 0
    screen.after(100, update_gif, frame_number)

def encrypt():
    password = code.get()
    print("Encrypt function called. Password entered:", password)

    if password == "1234":
        # Create a new Toplevel window
        encrypted_text_root = Toplevel(screen)

        current_x = screen.winfo_x()
        current_y = screen.winfo_y()

        new_x = current_x + 185
        new_y = current_y + 250

        encrypted_text_root.geometry(f"400x300+{new_x}+{new_y}")
        encrypted_text_root.title("Encrypted Message")
        encrypted_text_root.configure(bg="#ed3833")

        Label(encrypted_text_root, text="Enter the text to Encrypt", font=("Arial", 12), bg="#ed3833", fg="white").pack(pady=10)

        # Create a textbox to enter the text to encrypt
        encrypt_textbox = Text(encrypted_text_root, font=("Arial", 12), height=5, width=40)
        encrypt_textbox.pack(padx=20, pady=20)

        # Button to proceed to recipient selection
        Button(encrypted_text_root, text="Next", command=lambda: show_recipient_popup(encrypted_text_root, encrypt_textbox.get("1.0", END).strip())).pack(pady=20)

    else:
        messagebox.showerror("Password Error", "Invalid password.")

def decrypt():
    password = code.get()
    print("Decrypt function called. Password entered:", password)

    if password == "1234":
        # Create a new Toplevel window for decrypted text
        
        show_validation_popup(None, masked_name, birth_date, decrypted_text)
        
        
        
        decrypted_text_root = Toplevel(screen)

        current_x = screen.winfo_x()
        current_y = screen.winfo_y()

        new_x = current_x + 950  # Adjust as needed
        new_y = current_y + 250

        decrypted_text_root.geometry(f"400x300+{new_x}+{new_y}")
        decrypted_text_root.title("Decrypted Message")
        decrypted_text_root.configure(bg="#00bd56")

        Label(decrypted_text_root, text="Decrypted Text", font=("Arial", 12), bg="#00bd56", fg="white").pack(pady=10)

        # Get the encrypted text from the decrypt textbox
        encrypted_text = decrypt_textbox.get("1.0", END).strip()

        try:
            # Split ciphertext, nonce, masked name, and birth date from the hex string
            ciphertext_hex, nonce_hex, masked_name, birth_date = encrypted_text.split(":")

            # Convert the encrypted text and nonce back to bytes
            ciphertext = bytes.fromhex(ciphertext_hex)
            nonce = bytes.fromhex(nonce_hex)

            # Create a new AES cipher object with the nonce
            cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
            
            # Decrypt the ciphertext (but don't show it yet)
            decrypted_text = cipher.decrypt(ciphertext).decode('utf-8')

            # Show validation popup first
            show_validation_popup(decrypted_text_root, masked_name, birth_date, decrypted_text)

        except ValueError as e:
            messagebox.showerror("Decryption Error", f"Failed to decrypt text: {e}")

    else:
        messagebox.showerror("Password Error", "Invalid password.")

def show_validation_popup(decrypted_text_root, masked_name, birth_date, decrypted_text):
    # Create a new popup for validating recipient details
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
        if masked_name_entry.get() == masked_name and birth_date_entry.get() == birth_date:
            # If validated, show the decrypted text
            decrypted_textbox = Text(decrypted_text_root, font=("Arial", 12), height=10, width=40)
            decrypted_textbox.pack(padx=20, pady=20)
            decrypted_textbox.insert(END, decrypted_text)
            popup.destroy()  # Close the validation popup
        else:
            messagebox.showerror("Validation Error", "Masked name or birth date is incorrect.")

    Button(popup, text="Validate", command=validate).pack(pady=20)


def main_screen():
    global screen
    global code
    global decrypt_textbox
    global gif_frames
    global gif_label

    screen = Tk()

    screen.geometry("1600x900")
    screen.title("String Encryption and Decryption Portal")

    # Load GIF image and create frames
    gif_image = Image.open("encrypt.gif")  # Replace with your GIF path
    gif_frames = []
    for i in range(gif_image.n_frames):
        gif_image.seek(i)
        frame = ImageTk.PhotoImage(gif_image.copy())
        gif_frames.append(frame)

    # Center GIF Image
    gif_label = Label(screen)
    gif_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    update_gif(0)  # Start animation

    # Decryption block
    decrypt_frame = Frame(screen, bg="#00bd56", bd=2, relief=RIDGE)
    decrypt_frame.place(x=screen.winfo_screenwidth()/3 + 530, y=50, width=screen.winfo_screenwidth()/3 - 70, height=screen.winfo_screenheight() - 150)

    Label(decrypt_frame, text="Enter the encrypted text to Decrypt", font="arial 15", fg="white", bg="#00bd56").pack(pady=10)
    decrypt_textbox = Text(decrypt_frame, font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD, bd=2)
    decrypt_textbox.pack(padx=5, pady=10)

    Button(decrypt_frame, text="Decrypt", font="arial 15", bg="white", fg="#00bd56", command=show_validation_popup).pack(pady=5)

    # Encryption block
    encrypt_frame = Frame(screen, bg="#ed3833", bd=2, relief=RIDGE)
    encrypt_frame.place(x=screen.winfo_screenwidth()/3 - 70, y=50, width=screen.winfo_screenwidth()/3 - 70, height=screen.winfo_screenheight() - 150)

    Label(encrypt_frame, text="Enter Password to Encrypt", font="arial 15", fg="white", bg="#ed3833").pack(pady=10)

    code = Entry(encrypt_frame, font="Roboto 14", bg="white", relief=GROOVE, bd=2)
    code.pack(padx=5, pady=10)

    Button(encrypt_frame, text="Encrypt", font="arial 15", bg="white", fg="#ed3833", command=encrypt).pack(pady=5)

    screen.mainloop()

main_screen()
