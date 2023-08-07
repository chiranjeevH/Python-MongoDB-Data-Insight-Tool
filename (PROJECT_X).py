# %%
from os import read
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import *
from tkinter import Tk
from tkinter import *
import csv
import pymongo
import pandas as pd
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile, asksaveasfilename


# ---------------------------------------------------------------------------------------------------
# query  by mobile number
output = ""


def mobileinput():
    global mobileEntryTabOne
    string = mobileEntryTabOne.get()

    client = pymongo.MongoClient("mongodb://192.168.1.174:27017/")

    # Database Name
    db = client["truecallerDB"]
    # Num=input
    dbName = str(int(mobileEntryTabOne.get()))[:6]
    # Collection Name
    col = db[dbName]
    myquery = {"Number": mobileEntryTabOne.get()}
    mydoc = col.find(myquery)
    mydoc = list(mydoc)[0]
    mobilecsvtable(mydoc)



def mobilecsvtable(mydoc):
    # design the layout
    TableMargin = Frame(screen, width=10)
    TableMargin.pack(side=RIGHT, padx=100, pady=30)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=(['Number', 'Carrier', 'Name', 'Gender', 'Image', 'Address', 'JobTitle', 'CompanyName', 'Email', 'Website', 'Facebook',
                        'Twitter', 'Tags', 'Badges', 'Score', 'SpamCount']), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Number', text="Number", anchor=W)
    tree.heading('Carrier', text="Carrier", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Image', text="Image", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    tree.heading('JobTitle', text="JobTitle", anchor=W)
    tree.heading('CompanyName', text="CompanyName", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Website', text="Website", anchor=W)
    tree.heading('Facebook', text="Facebook", anchor=W)
    tree.heading('Twitter', text="Twitter", anchor=W)
    tree.heading('Tags', text="Tags", anchor=W)
    tree.heading('Badges', text="Badges", anchor=W)
    tree.heading('Score', text="Score", anchor=W)
    tree.heading('SpamCount', text="SpamCount", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=90)
    tree.column('#2', stretch=NO, minwidth=0, width=90)
    tree.column('#3', stretch=NO, minwidth=0, width=90)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=90)
    tree.column('#6', stretch=NO, minwidth=0, width=90)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.column('#8', stretch=NO, minwidth=0, width=90)
    tree.column('#9', stretch=NO, minwidth=0, width=90)
    tree.column('#10', stretch=NO, minwidth=0, width=90)
    tree.column('#11', stretch=NO, minwidth=0, width=90)
    tree.column('#12', stretch=NO, minwidth=0, width=9)
    tree.column('#13', stretch=NO, minwidth=0, width=90)
    tree.column('#14', stretch=NO, minwidth=0, width=90)
    tree.column('#15', stretch=NO, minwidth=0, width=110)
    tree.pack()

    tree.insert("", 0, values=(mydoc["Number"], mydoc["Carrier"], mydoc["Name"], mydoc["Gender"], mydoc["Image"], mydoc["Address"], mydoc["JobTitle"],
                               mydoc["CompanyName"], mydoc["Email"], mydoc["Website"], mydoc["Facebook"], mydoc["Twitter"], mydoc["Tags"], mydoc["Badges"], mydoc["Score"], mydoc["SpamCount"]))

    # tree.insert("", 0, values=("3453455343", "Airtel","Someone","M","None", "INdore", "Engineer",
    #                     "", "Abx@abc.com", "", "", "", "", "", "", ""))

# clear table from mobile input
    def deleteItems():
        TableMargin.destroy()
        close_button.destroy()

    close_button = tk.Button(tab1, text="clear table ", font=("Open Sans", 10, "bold"),
                             background="#e8e8e8", foreground="black", borderwidth=2, command=deleteItems)
    close_button.grid(row=2, column=2, padx=15, pady=15)
    # close_button.pack()


# -------------------------------------------------------------------------------------------------------------
# query by name
output2 = ""


def nameinput():
    global firstEntryTabOne
    string = firstEntryTabOne.get()

    client = pymongo.MongoClient("mongodb://192.168.1.174:27017/")

    # Database Name
    db = client["truecallerDB"]

    collections = db.list_collection_names()
    name = firstEntryTabOne.get()
    names_list = []
    
    record = {
            'Name' :   firstEntryTabOne.get()
            }

    for i, collection in enumerate(collections):
        print(i)
        # Collection Name            
        col = db[collection]
        myquery = {"Name": name}
        mydoc = col.find(myquery)
        mydoc = list(mydoc)
        if mydoc != []:
            for i in mydoc:
                names_list.append(i)

            if len(names_list) == 5:
                break

        # print(names_list)
    nameinputtable(names_list)
 

# creating a function to display query in a table
def nameinputtable(names_list):
    # design the layout
    TableMargin = Frame(screen, width=10)
    TableMargin.pack(side=RIGHT, padx=100, pady=30)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=(['Number', 'Carrier', 'Name', 'Gender', 'Image', 'Address', 'JobTitle', 'CompanyName', 'Email', 'Website', 'Facebook',
                        'Twitter', 'Tags', 'Badges', 'Score', 'SpamCount']), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Number', text="Number", anchor=W)
    tree.heading('Carrier', text="Carrier", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Image', text="Image", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    tree.heading('JobTitle', text="JobTitle", anchor=W)
    tree.heading('CompanyName', text="CompanyName", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Website', text="Website", anchor=W)
    tree.heading('Facebook', text="Facebook", anchor=W)
    tree.heading('Twitter', text="Twitter", anchor=W)
    tree.heading('Tags', text="Tags", anchor=W)
    tree.heading('Badges', text="Badges", anchor=W)
    tree.heading('Score', text="Score", anchor=W)
    tree.heading('SpamCount', text="SpamCount", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=90)
    tree.column('#2', stretch=NO, minwidth=0, width=90)
    tree.column('#3', stretch=NO, minwidth=0, width=90)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=90)
    tree.column('#6', stretch=NO, minwidth=0, width=90)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.column('#8', stretch=NO, minwidth=0, width=90)
    tree.column('#9', stretch=NO, minwidth=0, width=90)
    tree.column('#10', stretch=NO, minwidth=0, width=90)
    tree.column('#11', stretch=NO, minwidth=0, width=90)
    tree.column('#12', stretch=NO, minwidth=0, width=9)
    tree.column('#13', stretch=NO, minwidth=0, width=90)
    tree.column('#14', stretch=NO, minwidth=0, width=90)
    tree.column('#15', stretch=NO, minwidth=0, width=110)
    tree.pack()
    
    for mydoc in names_list:
        tree.insert("", 0, values=(mydoc["Number"], mydoc["Carrier"], mydoc["Name"], mydoc["Gender"], mydoc["Image"], mydoc["Address"], mydoc["JobTitle"],
                               mydoc["CompanyName"], mydoc["Email"], mydoc["Website"], mydoc["Facebook"], mydoc["Twitter"], mydoc["Tags"], mydoc["Badges"], mydoc["Score"], mydoc["SpamCount"]))
    
# clear table from name input

    def deleteItems():
        TableMargin.destroy()
        close_button.destroy()

    close_button = tk.Button(tab1, text="clear table ", font=("Open Sans", 10, "bold"),
                             background="#e8e8e8", foreground="black", borderwidth=2, command=deleteItems)
    close_button.grid(row=2, column=2, padx=15, pady=15)
    # close_button.pack()
# -------------------------------------------------------------------------------------------------------------


# Creates a Sample CSV for bulk input
file = ""


def samplecsv():
    try:
        data = [("csv file(*.csv)", "*.csv")]
        global file
        file = asksaveasfilename(filetypes=data, defaultextension=data)

        with open(file, "w") as csv_file:

            fieldnames = ['Number', 'Carrier', 'Name', 'Gender', 'Image', 'Address', 'JobTitle',
                          'CompanyName', 'Email', 'Website', 'Facebook', 'Twitter', 'Tags', 'Badges', 'Score', 'SpamCount']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'Number': '', 'Carrier': '', 'Name': '', 'Gender': '', 'Image': '', 'Address': '', 'JobTitle': '', 'CompanyName': '',
                            'Email': '', 'Website': '', 'Facebook': '', 'Twitter': '', 'Tags': '', 'Badges': ' ', 'Score': '', 'SpamCount': ''})
            print("CSV Created")
    except:
        print("An exception occured while creating sample csv")


# ---------------------------------------------------------------------------------------------------
# Defines a browse function to load a CSV for bulk input
def browse():
    global file
    filename = askopenfilename(filetypes=[('CSV File', '*.csv')])
    ent1.insert(END, filename)
    if file == "":
        file = filename
# ---------------------------------------------------------------------------------------------------


# "Bulk Input" Connection with MDB Database, read data("Numbers") from Sample CSV and query in the database, stores the query data by writing  in the Sample CSV
csvtodownload = {}
NumberList, Carrier, Name, Gender, ImageList, Address, JobTitle, CompanyName, Email, Website, Facebook, Twitter, Tags, Badges, Score, SpamCount = [
], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []


def bulkinput():
    global file
    client = pymongo.MongoClient("mongodb://192.168.1.174:27017/")

    # Database Name
    db = client["truecallerDB"]

    def read_csv_data():
        reader = pd.read_csv(ent1.get())
        # Returning the list of number in csv
        return reader["Number"]
    if __name__ == "__main__":

        # read_csv_data()
        for idx, rows in enumerate(read_csv_data()):
            try:
                rows = str(int(rows))
                dbName = str(int(rows))[:6]
                # Collection Name
                col = db[dbName]
                myquery = {"Number": rows}
                mydoc = col.find(myquery)
                mydoc = list(mydoc)[0]
                NumberList.append(mydoc["Number"])
                Carrier.append(mydoc["Carrier"])
                Name.append(mydoc["Name"])
                Gender.append(mydoc["Gender"])
                ImageList.append(mydoc["Image"])
                Address.append(mydoc["Address"])
                JobTitle.append(mydoc["JobTitle"])
                CompanyName.append(mydoc["CompanyName"])
                Email.append(mydoc["Email"])
                Website.append(mydoc["Website"])
                Facebook.append(mydoc["Facebook"])
                Twitter.append(mydoc["Twitter"])
                Tags.append(mydoc["Tags"])
                Badges.append(mydoc["Badges"])
                Score.append(mydoc["Score"])
                SpamCount.append(mydoc["SpamCount"])
            except Exception as e:
                print("An exception occured: ", e)
        global MyDataFrame
        MyDataFrame = pd.DataFrame(
            {
                "Number": NumberList,
                "Carrier": Carrier,
                "Name": Name,
                "Gender": Gender,
                "Image": ImageList,
                "Address": Address,
                "JobTitle": JobTitle,
                "CompanyName": CompanyName,
                "Email": Email,
                "Website": Website,
                "Facebook": Facebook,
                "Twitter": Twitter,
                "Tags": Tags,
                "Badges": Badges,
                "Score": Score,
                "SpamCount": SpamCount
            }
        )
        global csvtodownload  
        csvtodownload = MyDataFrame
        MyDataFrame.to_csv(file, index=False)
# ---------------------------------------------------------------------------------------------------
# download function for bulk input


def downloadCsv():
    savepath = asksaveasfile(defaultextension="*.csv")
    print("File", savepath)
    MyDataFrame.to_csv(savepath, index=False)
# ---------------------------------------------------------------------------------------------------
# CSV table for bulk input


def csvtable():
    global file
    # design the layout
    TableMargin = Frame(screen, width=10)
    TableMargin.pack(side=RIGHT, padx=100, pady=30)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=(['Number', 'Carrier', 'Name', 'Gender', 'Image', 'Address', 'JobTitle', 'CompanyName', 'Email', 'Website', 'Facebook',
                        'Twitter', 'Tags', 'Badges', 'Score', 'SpamCount']), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Number', text="Number", anchor=W)
    tree.heading('Carrier', text="Carrier", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('Image', text="Image", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    tree.heading('JobTitle', text="JobTitle", anchor=W)
    tree.heading('CompanyName', text="CompanyName", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Website', text="Website", anchor=W)
    tree.heading('Facebook', text="Facebook", anchor=W)
    tree.heading('Twitter', text="Twitter", anchor=W)
    tree.heading('Tags', text="Tags", anchor=W)
    tree.heading('Badges', text="Badges", anchor=W)
    tree.heading('Score', text="Score", anchor=W)
    tree.heading('SpamCount', text="SpamCount", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=90)
    tree.column('#2', stretch=NO, minwidth=0, width=90)
    tree.column('#3', stretch=NO, minwidth=0, width=90)
    tree.column('#4', stretch=NO, minwidth=0, width=90)
    tree.column('#5', stretch=NO, minwidth=0, width=90)
    tree.column('#6', stretch=NO, minwidth=0, width=90)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.column('#8', stretch=NO, minwidth=0, width=90)
    tree.column('#9', stretch=NO, minwidth=0, width=90)
    tree.column('#10', stretch=NO, minwidth=0, width=90)
    tree.column('#11', stretch=NO, minwidth=0, width=90)
    tree.column('#12', stretch=NO, minwidth=0, width=9)
    tree.column('#13', stretch=NO, minwidth=0, width=90)
    tree.column('#14', stretch=NO, minwidth=0, width=90)
    tree.column('#15', stretch=NO, minwidth=0, width=110)
    tree.pack()

    # creating main function
    with open(file) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            Number = row['Number']
            Carrier = row['Carrier']
            Name = row['Name']
            Gender = row['Gender']
            Image = row['Image']
            Address = row['Address']
            JobTitle = row['JobTitle']
            CompanyName = row['CompanyName']
            Email = row['Email']
            Website = row['Website']
            Facebook = row['Facebook']
            Twitter = row['Twitter']
            Tags = row['Tags']
            Badges = row['Badges']
            Score = row['Score']
            SpamCount = row['SpamCount']

            tree.insert("", 0, values=(Number, Carrier, Name, Gender, Image, Address, JobTitle,
                        CompanyName, Email, Website, Facebook, Twitter, Tags, Badges, Score, SpamCount))
# clear table from bulk input

    def deleteItems():
        TableMargin.destroy()
        close_button.destroy()

    close_button = tk.Button(tab2, text="clear table ", font=("Open Sans", 10, "bold"),
                             background="#e8e8e8", foreground="black", borderwidth=2, command=deleteItems)
    close_button.grid(row=2, column=2, padx=15, pady=15)
    # close_button.pack()




screen = tk.Tk()
screen.title("Profile X")
screen.geometry("1000x700")
screen.configure(bg='#f7f7f7')


tab_parent = ttk.Notebook(screen)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text="                                                          Individual Search                                                                                                                                            ")
tab_parent.add(tab2, text="                                                         Bulk Search                                                                                                                                                          ")

TrueUI_label = Label(screen, text="Profile X", bg='#f7f7f7',
                     borderwidth=9, foreground='Black', font=("Courier", 20, "bold"))
TrueUI_label.pack()
TrueUI_label.place(x=410, y=0)
# === WIDGETS FOR TAB ONE
EnterName = tk.Label(tab1, text="Enter Name:", font=(
    "Open Sans", 10, "bold"), foreground="black", borderwidth=2)
EnterMobile = tk.Label(tab1, text="Enter Mobile:", font=(
    "Open Sans", 10, "bold"), foreground="black", borderwidth=2)
EnterMobile.place(x=20)


Search1 = tk.Button(tab1, text="Search", font=("Open Sans", 9, "bold"), background="#e8e8e8",
                    foreground="black", borderwidth=2, command=nameinput)  # ,command=lambda:[mongotocsv(),csvtable()]
label4 = tk.Label(screen, text=lambda: [
                  output(), output2()], font=('helvetica', 10, 'bold'))
Search2 = tk.Button(tab1, text="Search", font=("Open Sans", 9, "bold"),
                    background="#e8e8e8", foreground="black", borderwidth=2, command=mobileinput)

firstEntryTabOne = tk.Entry(tab1)
mobileEntryTabOne = tk.Entry(tab1)

# === ADD WIDGETS TO GRID ON TAB ONE
EnterName.grid(row=0, column=0, padx=15, pady=15)
firstEntryTabOne.grid(row=0, column=1, padx=15, pady=15)

EnterMobile.grid(row=1, column=0, padx=15, pady=15)
EnterMobile.focus_set()

mobileEntryTabOne.grid(row=1, column=1, padx=15, pady=15)

Search1.grid(row=0, column=2, padx=15, pady=15)
Search2.grid(row=1, column=2, padx=15, pady=15)


# === WIDGETS FOR TAB TWO

ent1 = tk.Entry(tab2, width=62, font=0, borderwidth=1)
SampleCSV = tk.Button(tab2, text="Sample CSV", font=("Open Sans", 10, "bold"),
                      background="#e8e8e8", foreground="black", borderwidth=2, command=samplecsv)
Browsebutton = tk.Button(tab2, text="  Browse  ", font=(
    "Open Sans", 10, "bold"), background="#e8e8e8", foreground="black", borderwidth=2, command=browse)
Download = tk.Button(tab2, text="Download", font=("Open Sans", 10, "bold"),
                     background="#e8e8e8", foreground="black", borderwidth=2, command=downloadCsv)
Findbutton = tk.Button(tab2, text="    Find    ", font=("Open Sans", 10, "bold"), background="#e8e8e8",
                       foreground="black", borderwidth=2, command=lambda: [bulkinput(), csvtable()])

# === ADD WIDGETS TO GRID ON TAB TWO
ent1.grid(row=4, column=1, padx=0, pady=15)
SampleCSV.grid(row=0, column=0, padx=15, pady=15)
Browsebutton.grid(row=4, column=2, padx=5, pady=15)
# button should be showed only when CSV table is called 🌟
Download.grid(row=5, column=2, padx=15, pady=15)
Findbutton.grid(row=5, column=1, padx=15, pady=15)


tab_parent.pack(expand=1, fill='both', pady=55)

screen.minsize(1000, 700)
screen.maxsize(1000, 700)
screen.mainloop()
# %%
