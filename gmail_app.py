import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import smtplib


class container:
    def __init__(self, master):
        # =============== external variables =====================
        self.getting5 = None
        self.password = None
        self.server = None
        self.receiver = None
        self.Subject = None
        self.message = None
        self.getting4 = None
        self.sender = None
        self.getting1 = None
        self.getting2 = None
        self.getting3 = None
        self.master = master

        # ======Title=======
        self.Title = Label(self.master, text="Gmail APP", font=("Algeria 20"))
        self.Title.pack(expand=False, fill="both")

        # =======Labels======
        self.canvas = Canvas(self.master, bd=2, bg="black", height=800)
        self.canvas.pack(expand=False, fill=X)
        self.sender_lbl = Label(self.canvas, text="Sender :", font=("console 20 bold"), bg="#000", fg="#00ff00")
        self.sender_lbl.place(x=20, y=20)
        self.receiver_lbl = Label(self.canvas, text="Receiver :", font=("console 20 bold"), bg="#000", fg="#00ff00")
        self.receiver_lbl.place(x=20, y=75)
        self.subject_lbl = Label(self.canvas, text="Subject :", font=("console 20 bold"), bg="#000", fg="#00ff00")
        self.subject_lbl.place(x=20, y=130)
        self.message_lbl = Label(self.canvas, text="Message :", font=("console 20 bold"), bg="#000", fg="#00ff00")
        self.message_lbl.place(x=20, y=185)

        # ======entry=====
        self.entry1 = Entry(self.canvas, font="InkFree 20", bg="gray", fg="cyan")
        self.entry1.place(y=20, x=180, width=500)
        self.entry2 = Entry(self.canvas, font="InkFree 20", bg="gray", fg="cyan")
        self.entry2.place(y=75, x=180, width=500)
        self.entry3 = Entry(self.canvas, font="InkFree 20", bg="gray", fg="cyan")
        self.entry3.place(y=130, x=180, width=500)
        self.entry4 = Text(self.canvas, bg="white", fg="blue", width=62, height=10)
        self.entry4.place(x=180, y=185)

        # ======Buttons============
        self.button1 = Button(self.canvas, text="Send", command=self.send, font="Ebrima 30 bold")
        self.button1.place(x=360, y=390, width=100, height=40)

    def send(self):
        self.getting1 = self.entry1.get()
        self.getting1 = str(self.getting1)

        self.getting2 = self.entry2.get()
        self.getting2 = str(self.getting2)

        self.getting3 = self.entry3.get()
        self.getting3 = str(self.getting3)

        self.getting4 = self.entry4.get(1.0, END)
        self.getting4 = str(self.getting4)

        if self.getting1 == "" or self.getting2 == "" or self.getting3 == "":
            tkinter.messagebox.showerror("ERROR", "all Field are required")

            print("all Field are required")
        else:
            self.destroyer()

            self.canvas = Canvas(self.master, bd=2, bg="black", height=800)
            self.canvas.pack(expand=False, fill=X)
            self.sender_lbl = Label(self.canvas, text="Please Enter your Password :", font="console 20 bold",
                                    bg="#000", fg="#00ff00")
            self.sender_lbl.place(x=20, y=20)

            self.password = Entry(self.canvas, font="InkFree 20", bg="gray", show="*", fg="cyan")
            self.password.place(y=75, x=180, width=500)

            self.button1 = Button(self.canvas, text="Send", command=self.confirm, font="Ebrima 30 bold")
            self.button1.place(x=360, y=290, width=100, height=40)

            self.sender = self.getting1
            self.receiver = self.getting2
            self.Subject = self.getting3
            self.message = (f"""Sender: {self.sender}
receiver: {self.receiver}
subject: {self.Subject}\n
{self.getting4}""")

    def confirm(self):
        self.getting5 = self.password.get()
        self.getting5 = str(self.getting5)
        try:
            self.server = smtplib.SMTP("smtp.gmail.com", 587)
            self.server.starttls()
            self.server.login(self.getting1, self.getting5)
            print("Login Success Full")
            self.server.sendmail(self.getting1, self.getting2, self.message)
        except smtplib.SMTPAuthenticationError:
            tkinter.messagebox.showerror("sorry", "Logging in Failed")
            # print("logging in Failed")

    def destroyer(self):
        self.canvas.destroy()
        # self.sender_lbl.destroy()
        # self.receiver_lbl.destroy()
        # self.subject_lbl.destroy()
        # self.message_lbl.destroy()
        # self.entry2.destroy()
        # self.entry1.destroy()
        # self.entry3.destroy()
        # self.entry4.destroy()
        # self.button1.destroy()


window = Tk()
container(window)
window.geometry("800x600")
window.resizable(False, False)
window.mainloop()
