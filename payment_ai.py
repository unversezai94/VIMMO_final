from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import numpy as np



class PaymentAI:
    def __init__(self,root):
        self.root = root
        # res
        self.root.geometry('1200x530+100+100')

        # title
        self.root.title('VIMMO A.I')
        self.root.config(bg='#E5E7DB')
        self.root.focus_force()
        model = self.train()
        self.model = model

        self.var_grade = DoubleVar(value="")
        self.var_softwarexp = IntVar(value="")
        self.var_elcxp = IntVar(value="")
        self.var_mechxp = IntVar(value="")
        self.var_mng_xp = IntVar(value="")
        self.var_projects = IntVar(value="")
        self.var_langs = IntVar(value="")
        self.var_master = StringVar()
        self.var_payment = IntVar(value="")

        # 1
        label_grade = Label(self.root,text='GANO',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=50,y=130)
        label_software = Label(self.root,text='Yazılım',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=250,y=130)
        label_elect = Label(self.root,text='Elektronik',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=450,y=130)
        label_mech = Label(self.root,text='Makine',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=650,y=130)

        txt_grade = Entry(self.root,textvariable=self.var_grade,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=139,y=130,width=100)
        txt_software = Entry(self.root,textvariable=self.var_softwarexp,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=335,y=130,width=100)
        txt_elect = Entry(self.root,textvariable=self.var_elcxp,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=540,y=130,width=100)
        txt_mech = Entry(self.root,textvariable=self.var_mechxp,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=740,y=130,width=100)

        label_mng = Label(self.root,text='Yönetim',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=50,y=160)
        label_project = Label(self.root,text='Proje sayısı',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=250,y=160)
        label_langs = Label(self.root,text='Yabancı Dil',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=450,y=160)

        txt_mng = Entry(self.root,textvariable=self.var_mng_xp,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=138,y=160,width=100)
        txt_project = Entry(self.root,textvariable=self.var_projects,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=335,y=160,width=100)
        txt_langs = Entry(self.root,textvariable=self.var_langs,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=540,y=160,width=100)

        label_master = Label(self.root,text='Yüksek Lisans',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=50,y=190)
        label_payment = Label(self.root,text='Maaş',font=('Biryani Light',10),bg='#E5E7DB',fg='#0F0A0A').place(x=250,y=190)

        cmb_master = ttk.Combobox(self.root,textvariable=self.var_master,values=('Seçiniz','Var','Yok'),state='readonly',justify=CENTER,font=('Biryani Light',10),background='#DBE4E4',name="lütfen seçiniz")
        cmb_master.place(x=138,y=190,width=100)
        cmb_master.current(0)
        txt_payment = Entry(self.root,textvariable=self.var_payment,font=('Biryani Light',10),bg='#B3CCA2',fg='#0F0A0A').place(x=335,y=190,width=100)

        
        btn_predict = Button(self.root,text='Predict',command=self.prediction_payment,font=('Biryani Light',8,'bold'),bg='#5DA36A',fg='#0F0A0A').place(x=538,y=260,width=100,height=20)


        
    def train(self):
        payment_data = pd.read_csv('datasets/payments_son.csv')


        x_train, x_test, y_train, y_test = train_test_split(payment_data[['GradeAvg','SoftwareXP',
                                                                        'ElectronicsXP','MechanicalXP',
                                                                        'ManagementXP','Projects',
                                                                        'Languages','Master']],
                                                            payment_data['Payment'], test_size=0.1)


        model = LinearRegression()
        model.fit(x_train, y_train)
        return model    


    def prediction_payment(self):
        grade_avg = self.var_grade.get()
        software_xp = self.var_softwarexp.get()
        electronics_xp = self.var_elcxp.get()
        mechanical_xp = self.var_mechxp.get()
        management_xp = self.var_mng_xp.get()
        projects = self.var_projects.get()
        languages = self.var_langs.get()
        master = self.var_master.get()
        if master == 'Var':
            master = 1
        if master == 'Yok':
            master = 0
        if master == 'Seçiniz':
            messagebox.showerror('Hata!','Lütfen seçim yapınız.',parent=self.root)
        infos = [grade_avg,software_xp,electronics_xp, mechanical_xp,management_xp,projects,languages,master]
        infos_df = pd.DataFrame(np.array([infos]), columns = ['GradeAvg','SoftwareXP', 'ElectronicsXP','MechanicalXP','ManagementXP','Projects','Languages','Master'])

        prediction = self.model.predict(infos_df)[0]
        self.var_payment.set(round(prediction))
    

if __name__ == '__main__':
    root = Tk()
    im = PaymentAI(root)
    root.mainloop()