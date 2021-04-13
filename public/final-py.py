import tkinter
from tkinter import *
from tkinter import ttk

import tkinter.messagebox as MessageBox
from tkinter.messagebox import askyesno

import mysql.connector as mysql
from mysql.connector import errorcode

con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
cursor = con.cursor()

def insert(): #insert data into customer table
    cID = c_cID.get()
    name = c_name.get()

    if (cID=="" or name==""): #needs these parameters to execute
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
        cursor = con.cursor()
        cursor.execute("INSERT INTO Customer VALUES('"+cID+"','"+name+"')")
        cursor.execute("commit")

        c_cID.delete(0, 'end')
        c_name.delete(0, 'end')
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

def delete(): #deletes customer table
    answer = askyesno(title='Confirmation', message='Delete this position?')
    if answer:

        if(c_cID.get() == ''): #if parameter delete the id and inofmation belonging to it
            MessageBox.showinfo("Delete status","Deleted")
        else:
            con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
            cursor = con.cursor()
            cursor.execute("DELETE FROM Customer WHERE cID='"+c_cID.get()+"'")
            cursor.execute("commit")

            c_cID.delete(0, 'end')
            c_name.delete(0, 'end')
            MessageBox.showinfo("Delete Status", "Deleted Successfully")
            con.close()
    else:
        MessageBox.showinfo("Delete status","Failed")

def update(): #updates customer table
    cID = c_cID.get()
    name = c_name.get()

    if (cID=="" or name==""): #needs all parameters to update even if all of them are not changed does NOT updates id
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
        cursor = con.cursor()
        cursor.execute("UPDATE Customer SET name='"+name+"' WHERE cID='"+cID+"'")
        cursor.execute("commit")

        c_cID.delete(0, 'end')
        c_name.delete(0, 'end')
        MessageBox.showinfo("Update Status", "Update Successfully")
        con.close()

def get(): #gets the data fror company table
    if (c_cID.get() == ""): #needs id to retrieve data, makes it easy to use the other features just by saving time with typing
        MessageBox.showinfo("Fetch Status", "ID field required")
    else:
        con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Customer WHERE cID='"+c_cID.get()+"'")
        rows = cursor.fetchall()

        for row in rows: #inserts each parameter into each text input box
            c_name.insert(0, row[1])

        con.close()

root = Tk()
root.geometry("2000x1100")
root.title("Store")

cID = Label(root, text="Customer ID:", font=('bold',14))
cID.place(x=20, y=10)

name = Label(root, text="Name:", font=('bold',14))
name.place(x=20, y=50)

#entry and placement for employee ID variable in database
c_cID = Entry(root)
c_cID.place(x=120, y=10)

c_name = Entry(root)
c_name.place(x=120, y=50)

insert = Button(root, text="Insert", font=('italic',10), bg="white", command=insert)
insert.place(x=350, y=30)

update = Button(root, text="Update", font=('italic',10), bg="white", command=update)
update.place(x=350, y=60)

delete = Button(root, text="Delete", font=('italic',10), bg="white", command=delete)
delete.place(x=350, y=90)

get = Button(root, text="Get", font=('italic',10), bg="white", command=get)
get.place(x=350, y=120)

cIDTwo = Label(root, text="Customer ID:", font=('bold',14))
cIDTwo.place(x=20, y=100)

s_cID = Entry(root)
s_cID.place(x=120, y=100)


root.mainloop()