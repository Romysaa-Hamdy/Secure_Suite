import customtkinter as ctk
import tool
import result_module as rm
import tkinter.simpledialog as sd
import tkinter.filedialog as fd

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SecurityApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("450x650")
        self.title("Secure Suite")
        self.resizable(False, False)

        frame = ctk.CTkFrame(self, corner_radius=20, fg_color="#1f1f1f")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        title = ctk.CTkLabel(
            frame, 
            text="🔐 Secure Suite",
            font=("Century Gothic", 38, "bold"),
            text_color="#00aaff"
        )
        title.pack(pady=25)

        # Buttons
        self.create_button(frame, "🔑 Generate Strong Password", self.generate_pwd)
        self.create_button(frame, "💪 Check Password Strength", self.check_pwd)
        self.create_button(frame, "📁 Encrypt File (Caesar)", self.encrypt_file)
        self.create_button(frame, "📂 Decrypt File (Caesar)", self.decrypt_file)
        self.create_button(frame, "🧮 Calculate File MD5", self.calc_md5)

        # Output Box
        self.output = ctk.CTkTextbox(frame, width=360, height=150, corner_radius=15 )
        self.output.pack(pady=20)

    def create_button(self, frame, text, command):
        btn = ctk.CTkButton(frame, text=text, height=50, width=300,
                            corner_radius=15, font=("Century Gothic", 16, "bold"),
                            command=command)
        btn.pack(pady=10)

    # =============================
    # Instead of putting output here,
    # send to result_module, THEN load result
    # =============================

    def update_output(self):
        self.output.delete("1.0", "end")
        self.output.insert("end", rm.get_result())

    def generate_pwd(self):
        pwd = tool.generate_password()
        rm.set_result(f"Generated Password:\n{pwd}")
        self.update_output()

    def check_pwd(self):
        pwd = sd.askstring("Password Check", "Enter password:")
        if pwd:
            result = tool.evaluate_password(pwd)
            rm.set_result(result)
            self.update_output()

    def encrypt_file(self):
        file = fd.askopenfilename()
        if file:
            shift = 3
            text = open(file, "r", encoding="utf-8").read()
            encrypted = tool.caesar_cipher(text, shift)
            open("encrypted.txt", "w", encoding="utf-8").write(encrypted)

            rm.set_result("Encrypted → saved as encrypted.txt")
            self.update_output()

    def decrypt_file(self):
        file = fd.askopenfilename()
        if file:
            shift = 3
            text = open(file, "r", encoding="utf-8").read()
            decrypted = tool.caesar_decipher(text, shift)
            open("decrypted.txt", "w", encoding="utf-8").write(decrypted)

            rm.set_result("Decrypted → saved as decrypted.txt")
            self.update_output()

    def calc_md5(self):
        file = fd.askopenfilename()
        if file:
            md5 = tool.calculate_md5(file)
            rm.set_result(f"MD5 Hash:\n{md5}")
            self.update_output()


app = SecurityApp()
app.mainloop()
