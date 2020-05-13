from tkinter import *
from re import *

class Setup:
    def __init__(self, root):
        self.f = Frame(root, height=550, width=550)
        self.f.propagate(0)
        self.f.pack()

        self.lbl_heading = Label(self.f, text='Welcome to Password Cracker', height=2, font=('Courier', -30, 'bold underline'), bg='yellow', fg='black')
        self.lbl_heading.pack()
        self.lbl_creadit = Label(self.f, text='Developer: Mayank Tiwari',font=('Courier', -10, 'bold italic'), bg='yellow', fg='black')
        self.lbl_creadit.place(x=300, y=76, height=20, width=200)

        self.dataFrame = Frame(self.f)
        self.dataFrame.propagate(0)
        self.dataFrame.place(y=100,x=0, height=300, width=500)

        self.lbl_firstname = Label(self.dataFrame, text='First Name', font=('Georgia', -20, 'bold'), fg='black', bg='yellow').grid(row=0, column=0)
        self.lbl_lastname = Label(self.dataFrame, text='Last Name', font=('Georgia', -20, 'bold'), fg='black', bg='yellow').grid(row=1, column=0)
        self.lbl_dob = Label(self.dataFrame, text='Date of birth', font=('Georgia', -20, 'bold'), fg='black', bg='yellow').grid(row=2, column=0)
        self.lbl_emailid = Label(self.dataFrame, text='Email-Id', font=('Georgia', -20, 'bold'), fg='black', bg='yellow').grid(row=3, column=0)
        self.lbl_username = Label(self.dataFrame, text='User Name', font=('Georgia', -20, 'bold'), fg='black', bg='yellow').grid(row=4, column=0)
        self.lbl_phonenumber = Label(self.dataFrame, text='Phone Number', font=('Georgia', -20, 'bold'), fg='black', bg='yellow').grid(row=5, column=0)
        self.lbl_gender = Label(self.dataFrame, text='Gender', font=('Gerogia', -20, 'bold'), fg='black', bg='yellow').grid(row=6, column=0)
        

        self.var_firstname = StringVar()
        self.entry_firstname = Entry(self.dataFrame, fg='blue', bg='yellow', font=('Arial', 14), textvariable=self.var_firstname).grid(row=0, column=1)

        self.var_lastname = StringVar()
        self.entry_lastname = Entry(self.dataFrame, fg='blue', bg='yellow', font=('Arial', 14), textvariable=self.var_lastname).grid(row=1, column=1)
        
        self.var_dateofdob = IntVar()
        self.spinbox_dateofdob = Spinbox(self.dataFrame, fg='blue', bg='yellow', font=('Arial', 14), width=3, from_=1, to=31, textvariable=self.var_dateofdob).place(x=175, y=55)
        
        self.var_monthofdob = StringVar()
        self.list_monthname = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agusut', 'September', 'October', 'November', 'December')
        self.spinbox_monthofdob = Spinbox(self.dataFrame, fg='blue', bg='yellow', width=7, values=self.list_monthname, textvariable=self.var_monthofdob, font=('Arial', 14)).place(x=225, y=55)
        
        self.var_yearofdob = IntVar()
        self.spinbox_yearofdob = Spinbox(self.dataFrame, fg='blue', bg='yellow', width=5, from_=1950, to=2020, textvariable=self.var_yearofdob, font=('Arial', 14)).place(x=310, y=55)

        self.var_emailid = StringVar()
        self.entry_emailid = Entry(self.dataFrame, fg='blue', bg='yellow', font=('Arial', 14), textvariable=self.var_emailid).grid(row=3, column=1)

        self.var_username = StringVar()
        self.entry_username = Entry(self.dataFrame, fg='blue', bg='yellow', font=('Arial', 14), textvariable=self.var_username).grid(row=4, column=1)

        self.var_phonenumber = IntVar()
        self.entry_phonenumber = Entry(self.dataFrame, fg='blue', bg='yellow', font=('Arial', 14), textvariable=self.var_phonenumber).grid(row=5, column=1)

        self.var_gender = IntVar()
        self.radio_male = Radiobutton(self.dataFrame, text='Male', fg='blue', bg='yellow', variable=self.var_gender, value=1, font=('Arial', 14)).place(x=175, y=170)
        self.radio_female = Radiobutton(self.dataFrame, text='Female', fg='blue', bg='yellow', variable=self.var_gender, value=2, font=('Arial', 14)).place(x=285, y=170)


        self.frame_status = Frame(self.f, height=200, width=530)
        self.frame_status.propagate(0)
        self.frame_status.pack(side=BOTTOM)
        self.frame_status['bg'] = 'yellow'

        self.label_status_heading = Label(self.frame_status, fg='black', bg='yellow', font=('Gerogia', 20, 'bold underline'), text='STATUS').pack()
        


    def getFirstname(self):
        firstname = self.var_firstname.get()
        return firstname

    def getLastname(self):
        lastname = self.var_lastname.get()
        return lastname

    def getDateofdob(self):
        dateofdob = self.var_dateofdob.get()
        return dateofdob

    def getMonthofdob(self):
        monthofdob = self.var_monthofdob.get()
        return monthofdob

    def getYearofdob(self):
        yearofdob = self.var_yearofdob.get()
        return yearofdob

    def getEmailid(self):
        emailid = self.var_emailid.get()
        return emailid

    def getUsername(self):
        username = self.var_username.get()
        return username

    def getPhonenumber(self):
        phonenumber = int(self.var_phonenumber.get())
        return phonenumber

    def getGender(self):
        if self.var_gender.get() == 1:
            return 'Male'
        if self.var_gender.get() == 2:
            return 'Female'
        else:
            return False

    def getMonthName(self):
        return self.list_monthname

    def getDataFrame(self):
        return self.dataFrame

    def getFrameStatus(self):
        return self.frame_status

        
                   
root = Tk()
ss = Setup(root)


dataframe = ss.getDataFrame()
statusframe = ss.getFrameStatus()
dict_error_message = {}

class Create_Error_Message:
    def __init__(self, message, dataframe):
        self.label_error_message = Label(statusframe, text=message, bg='yellow', fg='black', font=('Helvetica', 14, 'italic'))

    def getLabelErrorMessage(self):
        return self.label_error_message
    

def validate_Input():

    for k, v in dict_error_message.items():
        v.destroy()



    count = 0
    firstname = ss.getFirstname()
    lastname = ss.getLastname()
    dateofdob = ss.getDateofdob()
    monthofdob = ss.getMonthofdob()
    yearofdob = ss.getYearofdob()
    emailid = ss.getEmailid()
    username = ss.getUsername()
    phonenumber = str(ss.getPhonenumber())
    gender = ss.getGender()

    
    def check_firstname(firstname):
        if findall(r'\W', firstname):
            k = 'firstnameError'
            message = 'You cannot use special charcter in first name try again....'
            obj_error_message = Create_Error_Message(message, statusframe)
            v = obj_error_message.getLabelErrorMessage()
            v.pack(side=TOP, pady=4)
            dict_error_message.update({k:v})
            return True
        return False

    def check_lastname(lastname):
        if findall(r'\W', lastname):
            k = 'lastnameError'
            message = 'You cannot use special charcter in last name try again....'
            obj_error_message = Create_Error_Message(message, statusframe)
            v = obj_error_message.getLabelErrorMessage()
            v.pack(side=TOP, pady=3)
            dict_error_message.update({k:v})
            return True
        return False
    
    def check_dateofdob(dateofdob):
        if dateofdob > 31:
            k = 'dateofdobError'
            message = 'Date cannot exceeds more than 31 try again....'
            obj_error_message = Create_Error_Message(message, statusframe)
            v = obj_error_message.getLabelErrorMessage()
            v.pack(side=TOP, pady=3)
            dict_error_message.update({k:v})
            return True
        return False


    def check_monthofdob(monthofdob):
        if monthofdob != None:
            count = 0
            list_month = ss.getMonthName()
            for month in list_month:
                if month != monthofdob:
                    count += 1
                    if count == 12:
                        k = 'monthofdobError'
                        message = 'Month is unknow try again....'
                        obj_error_message = Create_Error_Message(message, statusframe)
                        v = obj_error_message.getLabelErrorMessage()
                        v.pack(side=TOP, pady=3)
                        dict_error_message.update({k:v})
                        return True
        return False
                

    def check_emailid(emailid):
        if not findall(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', emailid):
            k = 'emailidError'
            message = 'Invalid email address try again....'
            obj_error_message = Create_Error_Message(message, statusframe)
            v = obj_error_message.getLabelErrorMessage()
            v.pack(side=TOP, pady=3)
            dict_error_message.update({k:v})
            return True
        return False

    def check_phonenumber(phonenumber):
        if len(phonenumber) != 10:
            k = 'phonenumberError'
            message = 'Phone number must contain ten digit try again....'
            obj_error_message = Create_Error_Message(message, statusframe)
            v = obj_error_message.getLabelErrorMessage()
            v.pack(side=TOP, pady=3)
            dict_error_message.update({k:v})
            return True
        return False


    def check_gender(gender):
        if gender == False:
            k = 'genderError'
            message = 'please select atleast one option from gender try again....'
            obj_error_message = Create_Error_Message(message, statusframe)
            v = obj_error_message.getLabelErrorMessage()
            v.pack(side=TOP, pady=3)
            dict_error_message.update({k:v})
            return True
        return False
        
        
    if not check_firstname(firstname):
        if not check_lastname(lastname):
            if not check_dateofdob(dateofdob):
                if not check_monthofdob(monthofdob):
                    if not check_emailid(emailid):
                        if not check_phonenumber(phonenumber):
                            if not check_gender(gender):
                                k = 'successMessage'
                                message = firstname + lastname + 'You are Welcome!!!!'
                                obj_error_message = Create_Error_Message(message, statusframe)
                                v = obj_error_message.getLabelErrorMessage()
                                v.pack(side=TOP, pady=3)
                                dict_error_message.update({k:v})
    


button_submit = Button(dataframe, text='SUBMIT', command=validate_Input).pack(side=BOTTOM, pady=50)

root.mainloop()
