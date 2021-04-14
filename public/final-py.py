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

def insertLink(): #insert data into customer table
    hID = l_hID.get()
    hashtag = l_hashtag.get()

    if (hID=="" or hashtag==""): #needs these parameters to execute
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
        cursor = con.cursor()
        cursor.execute("INSERT INTO Link VALUES('"+hID+"','"+hashtag+"')")
        cursor.execute("commit")

        l_hID.delete(0, 'end')
        l_hashtag.delete(0, 'end')
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

def deleteLink(): #deletes customer table
    answer = askyesno(title='Confirmation', message='Delete this position?')
    if answer:

        if(l_hID.get() == ''): #if parameter delete the id and inofmation belonging to it
            MessageBox.showinfo("Delete status","Deleted")
        else:
            con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
            cursor = con.cursor()
            cursor.execute("DELETE FROM Link WHERE hID='"+l_hID.get()+"'")
            cursor.execute("commit")

            l_hID.delete(0, 'end')
            l_hashtag.delete(0, 'end')
            MessageBox.showinfo("Delete Status", "Deleted Successfully")
            con.close()
    else:
        MessageBox.showinfo("Delete status","Failed")

def updateLink(): #updates customer table
    hID = l_hID.get()
    hashtag = l_hashtag.get()

    if (hID=="" or hashtag==""): #needs all parameters to update even if all of them are not changed does NOT updates id
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
        cursor = con.cursor()
        cursor.execute("UPDATE Link SET hashtag='"+hashtag+"' WHERE hID='"+hID+"'")
        cursor.execute("commit")

        l_hID.delete(0, 'end')
        l_hashtag.delete(0, 'end')
        MessageBox.showinfo("Update Status", "Update Successfully")
        con.close()

def getLink(): #gets the data fror company table
    if (l_hID.get() == ""): #needs id to retrieve data, makes it easy to use the other features just by saving time with typing
        MessageBox.showinfo("Fetch Status", "ID field required")
    else:
        con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Link WHERE hID='"+l_hID.get()+"'")
        rows = cursor.fetchall()

        for row in rows: #inserts each parameter into each text input box
            l_hashtag.insert(0, row[1])

        con.close()

def insertStore(): #insert data into customer table
    cID = s_cID.get()
    hID = s_hID.get()
    item = s_item.get()
    category = s_category.get()

    if (cID=="" or hID=="" or item=="" or category==""): #needs these parameters to execute
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
        cursor = con.cursor()
        cursor.execute("INSERT INTO Store VALUES('"+cID+"','"+hID+"','"+item+"','"+category+"')")
        cursor.execute("commit")

        s_cID.delete(0, 'end')
        s_hID.delete(0, 'end')
        s_item.delete(0, 'end')
        s_category.delete(0, 'end')
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

def deleteStore(): #deletes customer table
    answer = askyesno(title='Confirmation', message='Delete this position?')
    if answer:

        if(s_cID.get() == '' and s_hID.get() == ''): #if parameter delete the id and inofmation belonging to it
            MessageBox.showinfo("Delete status","Deleted")
        else:
            con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
            cursor = con.cursor()
            cursor.execute("DELETE FROM Store WHERE cID='"+s_cID.get()+"' and hID='"+s_hID.get()+"'")
            cursor.execute("commit")

            s_cID.delete(0, 'end')
            s_hID.delete(0, 'end')
            s_item.delete(0, 'end')
            s_category.delete(0, 'end')
            MessageBox.showinfo("Delete Status", "Deleted Successfully")
            con.close()
    else:
        MessageBox.showinfo("Delete status","Failed")

def updateStore(): #updates customer table
    cID = s_cID.get()
    hID = s_hID.get()
    item = s_item.get()
    category = s_category.get()

    if (cID=="" or hID=="" or item=="" or category==""): #needs all parameters to update even if all of them are not changed does NOT updates id
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
        cursor = con.cursor()
        cursor.execute("UPDATE Store SET item='"+item+"',category='"+category+"' WHERE cID='"+cID+"' and hID='"+hID+"'")
        cursor.execute("commit")

        l_hID.delete(0, 'end')
        l_hashtag.delete(0, 'end')
        MessageBox.showinfo("Update Status", "Update Successfully")
        con.close()

def getStore(): #gets the data fror company table
    if (s_cID.get() == "" and s_hID.get() == ""): #needs id to retrieve data, makes it easy to use the other features just by saving time with typing
        MessageBox.showinfo("Fetch Status", "ID field required")
    else:
        con = mysql.connect(host="localhost", user="ms_user_two", password="manageuser", database="CustomerDb")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Store WHERE cID='"+s_cID.get()+"' and hID='"+s_hID.get()+"'")
        rows = cursor.fetchall()

        for row in rows: #inserts each parameter into each text input box
            s_item.insert(0, row[2])
            s_category.insert(0, row[3])

        con.close()

root = Tk()
root.geometry("2000x1100")
root.title("Store")

insert = Button(root, text="Insert", font=('italic',10), bg="white", command=insert)
insert.place(x=350, y=10)

update = Button(root, text="Update", font=('italic',10), bg="white", command=update)
update.place(x=350, y=40)

delete = Button(root, text="Delete", font=('italic',10), bg="white", command=delete)
delete.place(x=350, y=70)

get = Button(root, text="Get", font=('italic',10), bg="white", command=get)
get.place(x=350, y=100)

cID = Label(root, text="Customer ID:", font=('bold',14))
cID.place(x=20, y=10)

name = Label(root, text="Name:", font=('bold',14))
name.place(x=20, y=30)

#entry and placement for employee ID variable in database
c_cID = Entry(root)
c_cID.place(x=120, y=10)

c_name = Entry(root)
c_name.place(x=120, y=40)

insertLink = Button(root, text="Insert", font=('italic',10), bg="white", command=insertLink)
insertLink.place(x=350, y=200)

updateLink = Button(root, text="Update", font=('italic',10), bg="white", command=updateLink)
updateLink.place(x=350, y=230)

deleteLink = Button(root, text="Delete", font=('italic',10), bg="white", command=deleteLink)
deleteLink.place(x=350, y=260)

getLink = Button(root, text="Get", font=('italic',10), bg="white", command=getLink)
getLink.place(x=350, y=290)

hID = Label(root, text="Hashtag ID:", font=('bold',14))
hID.place(x=20, y=200)

hashtag = Label(root, text="Hashtag:", font=('bold',14))
hashtag.place(x=20, y=230)

#entry and placement for employee ID variable in database
l_hID = Entry(root)
l_hID.place(x=120, y=200)

l_hashtag = Entry(root)
l_hashtag.place(x=120, y=230)

insertStore = Button(root, text="Insert", font=('italic',10), bg="white", command=insertStore)
insertStore.place(x=350, y=360)

updateStore = Button(root, text="Update", font=('italic',10), bg="white", command=updateStore)
updateStore.place(x=350, y=390)

deleteStore = Button(root, text="Delete", font=('italic',10), bg="white", command=deleteStore)
deleteStore.place(x=350, y=420)

getStore = Button(root, text="Get", font=('italic',10), bg="white", command=getStore)
getStore.place(x=350, y=450)

cIDTwo = Label(root, text="Customer ID:", font=('bold',14))
cIDTwo.place(x=20, y=360)

hIDTwo = Label(root, text="Hashtag ID:", font=('bold',14))
hIDTwo.place(x=20, y=390) 

item = Label(root, text="Item:", font=('bold',14))
item.place(x=20, y=420) 

category = Label(root, text="Category:", font=('bold',14))
category.place(x=20, y=450) 

s_cID = Entry(root)
s_cID.place(x=120, y=360)

s_hID = Entry(root)
s_hID.place(x=120, y=390)

s_item = Entry(root)
s_item.place(x=120, y=420)

s_category = Entry(root)
s_category.place(x=120, y=450)

root.mainloop()