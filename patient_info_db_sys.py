from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root

        self.root.title("Patient Information Database System")
        self.root.geometry('1030x650')
        self.root.resizable(False, False)

        self.name = StringVar()
        self.ref = StringVar()
        self.age = StringVar()
        self.gender = StringVar()
        self.illness = StringVar()
        self.medication = StringVar()
        self.date = StringVar()

        lbl_title = Label(self.root,text = "Patient Deatils Form", font = ("times new roman", 25), border=5,relief=RIDGE)
        lbl_title.pack(side=TOP,fill=X)

    # ================== Data Frame ======================
        dataframe = Frame(self.root, border=5,relief=RIDGE)
        dataframe.place(x=0,y=50,width=1030,height=300)

        dataframe_left = LabelFrame(dataframe, bd=5, relief=RIDGE,padx=5, text="Patient Info", font = ("times new roman", 15, "bold"))
        dataframe_left.place(x=5,y=5,width=500,height=270)

        dataframe_right = LabelFrame(dataframe, bd=5, relief=RIDGE,padx=5, text="Prescription details", font = ("times new roman", 15, "bold"))
        dataframe_right.place(x=510,y=5,width=505,height=270)
    
    # ================== Data Frame Left ==================
        lbl_pname = Label(dataframe_left, text="Name", font = ("times new roman", 15, "bold"), padx=5, pady=5)
        lbl_pname.grid(row=0,column=0, sticky = W)
        en_pname = Entry(dataframe_left, textvariable=self.name, font = ("times new roman", 12, "bold"), width=40)
        en_pname.grid(row=0, column=1, padx=30,pady=5)

        lbl_ref = Label(dataframe_left, text="Reference", font = ("times new roman", 15, "bold"), padx=5, pady=5)
        lbl_ref.grid(row=1,column=0, sticky = W)
        en_ref = Entry(dataframe_left, textvariable=self.ref, font = ("times new roman", 12, "bold"), width=40)
        en_ref.grid(row=1, column=1, padx=30,pady=5)

        lbl_gender = Label(dataframe_left, text="Gender", font = ("times new roman", 15, "bold"), padx=5, pady=5)
        lbl_gender.grid(row=2,column=0, sticky = W)
        cmb_gender = ttk.Combobox(dataframe_left, textvariable=self.gender, state="readonly", font = ("times new roman", 12, "bold"), width=10)
        cmb_gender["values"] = ("Male", "Female", "Others")
        cmb_gender.grid(row=2,column=1, sticky=W, padx=30,pady=5)

        lbl_age = Label(dataframe_left, text="Age", font = ("times new roman", 15, "bold"), padx=5, pady=5)
        lbl_age.place(x=280, y=72)
        en_age = Entry(dataframe_left, textvariable=self.age, font = ("times new roman", 12, "bold"), width=10)
        en_age.place(x=340, y=80)

        lbl_ill = Label(dataframe_left, text="Illness", font = ("times new roman", 15, "bold"), padx=5, pady=5)
        lbl_ill.grid(row=3,column=0, sticky = W)
        en_ill = Entry(dataframe_left, textvariable=self.illness, font = ("times new roman", 12, "bold"), width=40)
        en_ill.grid(row=3, column=1, padx=30,pady=5)

        lbl_med = Label(dataframe_left, text="Medication", font = ("times new roman", 15, "bold"), padx=5, pady=5)
        lbl_med.grid(row=4,column=0, sticky = W)
        en_med = Entry(dataframe_left, textvariable=self.medication, font = ("times new roman", 12, "bold"), width=40)
        en_med.grid(row=4, column=1, padx=30,pady=5)

        lbl_date = Label(dataframe_left, text="Date", font = ("times new roman", 15, "bold"), padx=5, pady=5)
        lbl_date.grid(row=5,column=0, sticky = W)
        en_date = Entry(dataframe_left, textvariable=self.date, font = ("times new roman", 12, "bold"), width=40)
        en_date.grid(row=5, column=1, padx=30,pady=5)

    # ================== Data frame right ==================
        self.txt_pres = Text(dataframe_right, font = ("times new roman", 15, "bold"), width=47, height=9)
        self.txt_pres.grid(row=0,column=0, padx=5, pady=5)

    # ================== Buttons Frame ==================
        buttonframe = Frame(self.root, border=5,relief=RIDGE)
        buttonframe.place(x=0,y=350,width=1030,height=60)

        btn_pres = Button(buttonframe, text="Show Prescription", command= self.Pres, font = ("times new roman", 12, "bold"), width=20, background="light grey")
        btn_pres.grid(row=0,column=0, padx=8, pady=8)

        btn_pr_data = Button(buttonframe, text="Add Prescription Data", command= self.Pres_data, font = ("times new roman", 12, "bold"), width=20, background="light grey")
        btn_pr_data.grid(row=0,column=1, padx=8, pady=8)


        btn_del = Button(buttonframe, text="Delete", command= self.Delete, font = ("times new roman", 12, "bold"), width=20, background="light grey")
        btn_del.grid(row=0,column=2, padx=8, pady=8)

        btn_rst = Button(buttonframe, text="Reset", command= self.Reset, font = ("times new roman", 12, "bold"), width=20, background="light grey")
        btn_rst.grid(row=0,column=3, padx=8, pady=8)

        btn_exit = Button(buttonframe, text="Exit", command= self.Exit,font = ("times new roman", 12, "bold"), width=19, background="light grey")
        btn_exit.grid(row=0,column=4, padx=8, pady=8)

    # ================== Details Frame ==================
        detailsframe = Frame(self.root, border=5,relief=RIDGE)
        detailsframe.place(x=0,y=410,width=1030,height=235)
        
        self.hosp_table = ttk.Treeview(detailsframe, columns=("Name","Reference","Age","Gender","Illness","Medication","Date"))

        scroll_x = ttk.Scrollbar(command=self.hosp_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hosp_table.yview)

        self.hosp_table.heading("Name", text="Name")
        self.hosp_table.heading("Reference", text="Reference")
        self.hosp_table.heading("Age", text="Age")
        self.hosp_table.heading("Gender", text="Gender")
        self.hosp_table.heading("Illness", text="Illness")
        self.hosp_table.heading("Medication", text="Medication")
        self.hosp_table.heading("Date", text="Date")

        self.hosp_table["show"] = "headings"
        self.hosp_table.pack(fill=BOTH, expand=1)

        self.hosp_table.column("Name", width=100)
        self.hosp_table.column("Reference", width=100)
        self.hosp_table.column("Age", width=50)
        self.hosp_table.column("Gender", width=50)
        self.hosp_table.column("Illness", width=100)
        self.hosp_table.column("Medication", width=100)
        self.hosp_table.column("Date", width=100)

        self.hosp_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    # ======================= Functions =======================
    
    def Pres_data(self):
        if self.name.get()=="" or self.ref.get()=="" or self.age.get()=="" or self.gender.get()=="" or self.illness.get()=="" or self.medication.get()=="" or self.date.get()=="":
            messagebox.showerror("Empty fields!")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database="patient_db")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into patient_info values(%s,%s,%s,%s,%s,%s,%s)", (self.name.get(),self.ref.get(),self.gender.get(),self.age.get(),self.illness.get(),self.medication.get(),self.date.get()))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record successfully inserted")


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="patient_db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from patient_info")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hosp_table.delete(*self.hosp_table.get_children())
            for i in rows:
                self.hosp_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self, event=""):
        cursor_row = self.hosp_table.focus()
        content = self.hosp_table.item(cursor_row)
        row = content['values']
        self.name.set(row[0])
        self.ref.set(row[1])
        self.gender.set(row[2])
        self.age.set(row[3])
        self.illness.set(row[4])
        self.medication.set(row[5])
        self.date.set(row[6])
    
    def Pres(self):
        self.txt_pres.delete("1.0","end")
        self.txt_pres.insert(END, "Name:\t\t\t" + self.name.get() + "\n")
        self.txt_pres.insert(END, "Reference:\t\t\t" + self.ref.get() + "\n")
        self.txt_pres.insert(END, "Gender:\t\t\t" + self.gender.get() + "\n")
        self.txt_pres.insert(END, "Age:\t\t\t" + self.age.get() + "\n")
        self.txt_pres.insert(END, "Illness:\t\t\t" + self.illness.get() + "\n")
        self.txt_pres.insert(END, "Medication:\t\t\t" + self.medication.get() + "\n")
        self.txt_pres.insert(END, "Date:\t\t\t" + self.date.get() + "\n")
    

    def Delete(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="patient_db")
        my_cursor = conn.cursor()
        my_cursor.execute("delete from patient_info where Reference=%s", (self.ref.get(),))

        
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Record has been deleted")


    def Reset(self):
        self.name.set("")
        self.ref.set("")
        self.age.set("")
        self.gender.set("")
        self.illness.set("")
        self.medication.set("")
        self.date.set("")
        self.txt_pres.delete("1.0","end")


    def Exit(self):
        Exit = messagebox.askyesno("Exit","Do you want to Exit")
        if Exit > 0:
            root.destroy()
            return


root = Tk()
ob = Hospital(root)
root.mainloop()
