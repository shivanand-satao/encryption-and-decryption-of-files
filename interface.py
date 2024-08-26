from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


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
    
    if password == "shiv":
        # Create a new Toplevel window
        encrypted_text_root = Toplevel(screen)
        
        current_x = screen.winfo_x()
        current_y = screen.winfo_y()
        
        
        new_x = current_x + 185  
        new_y = current_y + 250
        
        
        encrypted_text_root.geometry(f"400x300+{new_x}+{new_y}")
        encrypted_text_root.title("Encrypted the message ")
        encrypted_text_root.configure(bg="#ed3833")
        
        # Optionally, add widgets to the new window here
        Label(encrypted_text_root, text="Encrypted Text", font=("Arial", 12),bg="#ed3833",fg="white").pack(pady=10)
        Text(encrypted_text_root, font=("Arial", 12), height=45, width=45).pack(padx=20, pady=20)
        
        encrypted_text_root.mainloop()
        
    else:
        messagebox.showerror("Password Error", "Invalid password.")
        
        
        
        
def decrypt():
    password=code.get()
    print("Encrypt function called. Password entered:", password)
    
    if password=="shiv":
       # Create a new Toplevel window
       decrypted_text_root=Toplevel(screen)
       
       current_x = screen.winfo_x()
       current_y = screen.winfo_y()
        
        # Calculate the new window's position (e.g., place it 50 pixels left of the current window)
       new_x = current_x + 950  # Adjust 400 to the width of the new window if needed
       new_y = current_y + 250
        
       decrypted_text_root.geometry(f"400x300+{new_x}+{new_y}")
       decrypted_text_root.title("Decrypted your cipher text ")  
       decrypted_text_root.configure(bg="#00bd56")
       
       # Optionally, add widgets to the new window here
       Label(decrypted_text_root,text="Decrypted Text",font=("Arial",12),bg="#00bd65",fg="white").pack(pady=10)
       Text(decrypted_text_root, font=("Arial", 12), height=45, width=45).pack(padx=20, pady=20)
       
       decrypted_text_root.mainloop()
       
    else:
        messagebox.showerror("Password Error", "Invalid password.")

    
    
    


def main_screen():
    global screen
    global code
    global encrypt_textbox
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
    
    # Encryption block
    encrypt_frame = Frame(screen, bg="#ed3833", bd=2, relief=RIDGE)
    encrypt_frame.place(x=50, y=50, width=screen.winfo_screenwidth()/3 - 70, height=screen.winfo_screenheight() - 150)
    
    Label(encrypt_frame, text="Enter the text to Encrypt", font="arial 15", fg="white", bg="#ed3833").pack(pady=10)
    encrypt_textbox = Text(encrypt_frame, font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD, bd=2)
    encrypt_textbox.pack(pady=10, padx=10, expand=True, fill=BOTH)

    Button(encrypt_frame, text="Encrypt", height="2", width=15, bg="white", fg="#ed3833", bd=2, command=encrypt).pack(pady=20)

    # Decryption block
    decrypt_frame = Frame(screen, bg="#00bd56", bd=2, relief=RIDGE)
    decrypt_frame.place(x=screen.winfo_screenwidth()/3 + 530, y=50, width=screen.winfo_screenwidth()/3 - 70, height=screen.winfo_screenheight() - 150)
    
    Label(decrypt_frame, text="Enter the text to Decrypt", font="arial 15", fg="white", bg="#00bd56").pack(pady=10)
    decrypt_textbox = Text(decrypt_frame, font="Roboto 14", bg="white", relief=GROOVE, wrap=WORD, bd=2)
    decrypt_textbox.pack(pady=10, padx=10, expand=True, fill=BOTH)
    
    Button(decrypt_frame, text="Decrypt", height="2", width=15, bg="white", fg="#00bd56", bd=2, command=decrypt).pack(pady=20)
    
    
    
    
    
    
    
    # Center section for GIF, password, and reset button
    center_frame = Frame(screen)
    center_frame.place(relx=0.5, rely=0.75, anchor=CENTER)
    
    #making it enter using the center_frame
    Label(center_frame, text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).pack(pady=10)
    
    #making it enter using the center_frame
    code = StringVar()
    Entry(center_frame, textvariable=code, width=19, bd=0, font=("arial", 25), show='*').pack(pady=10)
    
    
    #Reset button #making it enter using the center_frame
    Button(center_frame, text="RESET", height="2", width=30, bg="#1089ff", fg="white", bd=0, command=lambda: [code.set(""), encrypt_textbox.delete(1.0, END), decrypt_textbox.delete(1.0, END)]).pack(pady=20)
    
    
    
    
    
    
    
    
    
    
    
    screen.mainloop()

main_screen()
