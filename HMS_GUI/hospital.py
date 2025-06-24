from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from config import creds

class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsinfMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        self.BloodPressure = StringVar()
        self.Medication = StringVar()
        self.NhsNumber = StringVar()
        self.PatientName = StringVar()





        lbltitle = Label(self.root,
                        bd=20,
                        relief=RIDGE,
                        text="HOSPITAL MANAGEMENT SYSTEM",
                        fg="red",
                        bg="white",
                        font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #================================Dataframe=======================================================
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft = LabelFrame(Dataframe,
                                    bd=10,
                                    relief=RIDGE,
                                    padx=10,
                                    font=("times new roman",12,"bold"),
                                    text="Patient information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        #================================BUTTON FRAME ==============================

        Buttonframe = Frame(self.root,bd=20,relief=RIDGE,bg="black")
        Buttonframe.place(x=0,y=520,height=70,width=1530)

        #================================ Details Frame ==============================

        Detailsframe = Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #================================== DataframeLeft =============================

        lblNameTablet = Label(DataframeLeft,text = "Name of Tablet:", font=("ariel",12, "bold"),padx = 2, pady=6)
        lblNameTablet.grid(row = 0, column = 0)

        comNametablet = ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("ariel", 12 , "bold") , width = 33, values = ("Nice" , "Corona Vacacine","Acetaminophen", "Adderall" , "Amlodipine","Ativan"))
        comNametablet.grid(row = 0, column= 1)

        lblref = Label(DataframeLeft, font =("ariel" , 12, "bold"), text = "Reference No:", padx = 2)
        lblref.grid(row = 1 , column =0 , sticky = W)
        txtref = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.ref, width = 35)
        txtref.grid(row = 1, column=1)

        lblDose =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Dose:",padx=2, pady = 6)
        lblDose.grid(row = 2 , column = 0 , sticky =  W)
        txtDose = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.dose, width = 35)
        txtDose.grid(row = 2, column=1)

        lblNooftablet =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="No of Tablet:",padx =2, pady = 6)
        lblNooftablet.grid(row = 3 , column = 0 , sticky =  W)
        txtNoOfTablet = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.NumberofTablets,width = 35)
        txtNoOfTablet.grid(row = 3, column=1)

        lbllot =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Lot:",padx=2, pady = 4)
        lbllot.grid(row = 4 , column = 0 , sticky =  W)
        txtlot = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.Lot, width = 35)
        txtlot.grid(row = 4, column=1)


        lblissueData =  Label(DataframeLeft, font =( "arial",12,"bold"),text =" issue Date",padx=2, pady = 6)
        lblissueData.grid(row = 5 , column = 0 , sticky =  W)
        txtissueData = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.Issuedate,width = 35)
        txtissueData.grid(row = 5, column=1)

        lblExpDate =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Exp Date",padx=2, pady = 4)
        lblExpDate.grid(row = 6 , column = 0 , sticky =  W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 13, "bold"),textvariable=self.ExpDate ,width = 35)
        txtExpDate.grid(row = 6, column=1)

        lblDailyDose =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Daily Dose:",padx=2, pady = 4)
        lblDailyDose.grid(row = 7 , column = 0 , sticky =  W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.DailyDose,width = 35)
        txtDailyDose.grid(row = 7, column=1)


        lblsideeffect =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Side Effect:",padx=2, pady = 4)
        lblsideeffect.grid(row = 8 , column = 0 , sticky =  W)
        txtsideeffect = Entry(DataframeLeft, font=("arial", 13, "bold"), textvariable=self.sideEffect ,width = 35)
        txtsideeffect.grid(row = 8, column=1)

        lblFurtherinfo =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Futher Information",padx=2)
        lblFurtherinfo.grid(row = 0 , column = 2 , sticky =  W)
        txtFuther_Information = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.FurtherInformation,width = 35)
        txtFuther_Information.grid(row = 0, column=3)

        lblBloodPressure =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Blood Pressure:",padx=2, pady = 6)
        lblBloodPressure.grid(row = 1 , column = 2 , sticky =  W)
        txtrefBloodPressur = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.BloodPressure,width = 35)
        txtrefBloodPressur.grid(row = 1, column=3)

        lblstorage =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="storage Advice:",padx=2, pady = 6)
        lblstorage.grid(row = 2 , column = 2 , sticky =  W)
        txtstorage = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.StorageAdvice,width = 35)
        txtstorage.grid(row = 2, column=3)

        lblMedicine =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Medication",padx=2, pady = 6)
        lblMedicine.grid(row = 3 , column = 2 , sticky =  W)
        txtMedicine = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.Medication,width = 35)
        txtMedicine.grid(row = 3, column=3)


        lblPatientId =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Patient Id",padx=2, pady = 6)
        lblPatientId.grid(row = 4 , column = 2 , sticky =  W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.PatientId, width = 35)
        txtPatientId.grid(row = 4, column=3)

        lblNhsNumber =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Nhs Number",padx=2, pady = 6)
        lblNhsNumber.grid(row = 5 , column = 2 , sticky =  W)
        txtNhsNumber  = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.NhsNumber,width = 35)
        txtNhsNumber.grid(row = 5, column=3)


        lblPatientName =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Patient Name",padx=2, pady = 6)
        lblPatientName.grid(row = 6 , column = 2 , sticky =  W)
        txtlblPatientName = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.PatientName ,width = 35)
        txtlblPatientName.grid(row = 6, column=3)

        lblDateOfBirth =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Date Of Birth:",padx=2, pady = 6)
        lblDateOfBirth.grid(row = 7 , column = 2 , sticky =  W)
        txtDateOfBirth = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.DateOfBirth,width = 35)
        txtDateOfBirth.grid(row = 7, column=3)

        lblPatientAddress =  Label(DataframeLeft, font =( "arial",12,"bold"),text ="Patient Address",padx=2, pady = 6)
        lblPatientAddress.grid(row = 8 , column = 2 , sticky =  W)
        txtlblPatientAddress = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.PatientAddress,width = 35)
        txtlblPatientAddress.grid(row = 8, column=3)




    #===================================DataframeRight 25mins       =========================================================

        DataframeRight = LabelFrame(Dataframe,
                                    bd=10,
                                    relief=RIDGE,
                                    padx=10,
                                    font=("times new roman",12,"bold"),
                                    text="Prescription")
        DataframeRight.place(x=981,y=5,width=500,height=350)

        self.txtPrescription=Text(DataframeRight,font=("arial", 12, "bold"),width=45, height=16,padx=2, pady=6)
        self.txtPrescription.grid(row = 0, column = 0)


    #====================================  Button ===================================================================

        pixel = PhotoImage(width=1, height=1)

        btnPrescription= Button(Buttonframe, command=self.iPrescription,text="Presciption", bg="blue", fg="white", font=("arial",12,"bold"),image=pixel, compound="c", width=239, height=40,padx=2, pady = 6)
        btnPrescription.image=pixel
        btnPrescription.grid(row=0 , column = 0)

        btnPrescriptiondata= Button(Buttonframe, command=self.iPrescriptionData, text="Presciption Data", bg="blue", fg="white", font=("arial",12,"bold"),image=pixel, compound="c", width=239, height=40,padx=2, pady = 6)
        btnPrescriptiondata.image=pixel
        btnPrescriptiondata.grid(row=0 , column = 1)

        btnUpdate= Button(Buttonframe, command=self.update,text="update", bg="blue", fg="white", font=("arial",12,"bold"),image=pixel, compound="c", width=239, height=40,padx=2, pady = 6)
        btnUpdate.image=pixel
        btnUpdate.grid(row=0 , column = 2)

        btnDelete= Button(Buttonframe, command=self.idelete, text="Delete", bg="blue", fg="white", font=("arial",12,"bold"),image=pixel, compound="c", width=239, height=40,padx=2, pady = 6)
        btnDelete.image=pixel
        btnDelete.grid(row=0 , column = 3)

        btnClear= Button(Buttonframe, command=self.clear ,  text="Clear", bg="blue", fg="white", font=("arial",12,"bold"),image=pixel, compound="c", width=239, height=40,padx=2, pady = 6)
        btnClear.image=pixel
        btnClear.grid(row=0 , column = 4)

        btnExit= Button(Buttonframe, command=self.iExit,  text="Exit", bg="blue", fg="white", font=("arial",12,"bold"),image=pixel, compound="c", width=239, height=40,padx=2, pady = 6)
        btnExit.image=pixel
        btnExit.grid(row=0 , column = 5)


        #====================================== TABLE ================================================================
        # ===================================== Scrollbar ============================================================

        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)

                
        scroll_x.pack=("side= BOTTOM, fill = X")
        scroll_Y.pack=("side= RIGHT, fill = Y")

        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=True,yscrollcommand=True)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_Y=ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("nameoftable", text="Name Of Table")
        self.hospital_table.heading("ref", text="Refernce No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Name Of Table")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="ADDRESS")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill= BOTH,expand=1)


        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill =  BOTH, expand = 1)
        self.hospital_table.bind("<ButtonRelease-1>" , self.get_cursor)


        self.fetch_data()


        #============================= Functionality Declartion ====================================================

    def iPrescriptionData(self):
        if self.Nameoftablets.get()== "" or self.ref.get()=="" or self.dose.get()=="" or self.NumberofTablets.get()=="" or self.Lot.get()=="" or self.Issuedate.get()=="" or self.ExpDate.get()=="" or self.DailyDose.get()=="" or self.StorageAdvice.get()=="" or self.NhsNumber.get()=="" or self.PatientName.get()=="" or self.DateOfBirth.get()=="" or self.PatientAddress.get()=="":
            messagebox.showerror("Error", "All fields are required")   
        else:
            conn=mysql.connector.connect(**creds)   
            my_cursor= conn.cursor()
            #create database table ================== 50 min=========

            my_cursor.execute("INSERT INTO hospital VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.Nameoftablets.get(),
                                                                                                self.ref.get(),
                                                                                                self.dose.get(),
                                                                                                self.NumberofTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.Issuedate.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.sideEffect.get(),
                                                                                                self.FurtherInformation.get(),
                                                                                                self.StorageAdvice.get(),
                                                                                                self.DrivingUsinfMachine.get(),
                                                                                                self.HowToUseMedication.get(),
                                                                                                self.PatientId.get(),
                                                                                                self.NhsNumber.get(),
                                                                                                self.PatientName.get(),
                                                                                                self.DateOfBirth.get(),
                                                                                                self.PatientAddress.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("success","Record has been inserted")


    def update(self):
        conn=mysql.connector.connect(**creds)   
        my_cursor= conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s , Dose=%s , NumberofTablets=%s , Lot=%s , Issuedate=%s ,ExpDate=%s ,  DailyDose=%s , StorageAdvice=%s , NhsNumber=%s , PatientName=%s , DateOfBirth=%s , PatientAddress=%s  where Ref=%s",(
                                                                                                self.Nameoftablets.get(),
                                                                                                self.dose.get(),
                                                                                                self.NumberofTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.Issuedate.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.StorageAdvice.get(),
                                                                                                self.NhsNumber.get(),
                                                                                                self.PatientName.get(),
                                                                                                self.DateOfBirth.get(),
                                                                                                self.PatientAddress.get(),
                                                                                                self.ref.get()))


    def fetch_data(self):
        conn=mysql.connector.connect(**creds) 
        my_cursor= conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END,values=i)
            conn.commit()
        conn.close()



    def get_cursor(self, event= ""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        if row:
            self.Nameoftablets.set(row[0])
            self.ref.set(row[1])
            self.dose.set(row[2])
            self.Nameoftablets.set(row[3])
            self.Lot.set(row[4])
            self.Issuedate.set(row[5])
            self.ExpDate.set(row[6])
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.NhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateOfBirth.set(row[11])
            self.PatientAddress.set(row[12])


    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END, "Refernce NO:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END, "name of Dose:\t\t\t"+self.dose.get()+"\n")
        self.txtPrescription.insert(END, "Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END, "Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END, "Isuue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END, "Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END, "daily dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END, "StorageAdvice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END, "DrivingusingMachine:\t\t\t"+self.DrivingUsinfMachine.get()+"\n")
        self.txtPrescription.insert(END, "PatientId:\t\t\t"+self.PatientAddress.get()+"\n")
        self.txtPrescription.insert(END, "NHSNumber:\t\t\t"+self.NhsNumber.get()+"\n")
        self.txtPrescription.insert(END, "PatientName:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END, "DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END, "PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")

    def idelete(self):
        conn=mysql.connector.connect(**creds)   
        my_cursor= conn.cursor()
        query="delete from hospital where Refernce_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient has been deleted successfully")


    def clear(self):
        self.Nameoftablets.set("")
        self.FurtherInformation.set("")
        self.ref.set("")
        self.BloodPressure.set("")
        self.dose.set("")
        self.StorageAdvice.set("")
        self.NumberofTablets.set("")
        self.Medication.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.NhsNumber.set("")
        self.ExpDate.set("")
        self.PatientName.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.DrivingUsinfMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")



    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system", "Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return










if __name__ == "__main__":
    root=Tk()
    application=Hospital(root)
    root.mainloop()