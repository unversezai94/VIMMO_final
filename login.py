from tkinter import *
from PIL import ImageTk


class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("VIMMO")
        self.root.geometry('1024x540+0+0')

        self.bg = ImageTk.PhotoImage(file='images/background.jpg')
        self.user_ic = ImageTk.PhotoImage(file='images/user_icon.png')
        self.user_pass = ImageTk.PhotoImage(file='images/password.png')

        bg_lbl = Label(self.root,image=self.bg).pack()
        title = Label(self.root,text='L o g i n',font=('Biryani Light',15),bg='#E8E2E0',fg='#706B6A')
        title.place(x=0,y=100,relwidth=1)

        lbl_user = Label(self.root,text=" I D",image=self.user_ic,compound=LEFT,font=('Biryani Light',9),bg='#E8E2E0',fg='#706B6A')
        lbl_user.place(x=0,y=200,relwidth=1)

        lbl_pass = Label(self.root,text=" P I N",image=self.user_pass,compound=LEFT,font=('Biryani Light',9),bg='#E8E2E0',fg='#706B6A')
        lbl_pass.place(x=0,y=250,relwidth=1)
root = Tk()
obj = Login(root)
root.mainloop()