import sqlite3
from sqlite3 import Error
import tkinter as tk
import random

global connection


def login(eun,epw,root):
  #if user does not exist, it fails. if it does, then it loads the gui
  cur = connection.cursor()
  cur.execute("SELECT * FROM users")
  if not cur.fetchone():  # An empty result evaluates to False.
    print("Login failed")
  else:
    print("Welcome")
    interface(root)




def create_acc(efn,eln,eun,epw):
  #creates random key and then adds first name, last name, username, password, and key to the database
  rand = random.randrange(0, 100, 3)
  connection.execute("INSERT INTO users VALUES (%d, '%s', '%s', '%s', '%s')" % (rand,str(efn.get()),str(eln.get()),str(eun.get()),str(epw.get())))
  print("succesfully inputted")
  cursor = connection.execute("SELECT * from users ")

  connection.commit()
   
  # display all data from users table
  for row in cursor:
    print(row)

def create_account(root1):
  root1.destroy()
  
  root = tk.Tk()
  root.geometry("300x200")
  # Create Account page
  label_fn = tk.Label(root, text="First Name")
  label_fn.pack()
  e1 = tk.StringVar()
  efn = tk.Entry(root, textvariable = e1)
  efn.pack()
  
  label_ln = tk.Label(root, text="Last Name")
  label_ln.pack()
  e2 = tk.StringVar()
  eln = tk.Entry(root, textvariable = e2)
  eln.pack()
  
  label_username = tk.Label(root, text="Username")
  label_username.pack()
  e3 = tk.StringVar()
  eun = tk.Entry(root, textvariable = e3)
  eun.pack()
  
  label_password = tk.Label(root, text="Password")
  label_password.pack()
  e4 = tk.StringVar()
  epw = tk.Entry(root, show="*", textvariable = e4)
  epw.pack()
  
  bca = tk.Button(root, text="Create Account", command=lambda:[create_acc(efn,eln,eun,epw), mainRoot(root), root.destroy()])
  bca.pack()
  root.mainloop()


  username = str(input('Enter username: '))
  password = str(input('Enter password: '))
  print("Username and Password have been created.")
  print("Username: " + username + "; Password: " + password)







def interface(root1):
  root1.destroy()
  
  root = tk.Tk()
  root.geometry("300x200")

  cur = connection.cursor()
  cur.execute("SELECT FNAME FROM users")
  fn = cur.fetchone()

  root.title("Welcome %s" % fn)
   
  root.grid_rowconfigure(0, weight=1)
  root.grid_rowconfigure(1, weight=1)
  root.grid_columnconfigure(0, weight=1)
  root.grid_columnconfigure(1, weight=1)

  # Create four frames for quadrants
  frame1 = tk.Frame(root)
  frame2 = tk.Frame(root)
  frame3 = tk.Frame(root)
  frame4 = tk.Frame(root)

  # Place the frames in the window using grid
  frame1.grid(row=0, column=0, sticky="nsew")
  frame2.grid(row=0, column=1, sticky="nsew")
  frame3.grid(row=1, column=0, sticky="nsew")
  frame4.grid(row=1, column=1, sticky="nsew")

  cam = tk.Label(frame1, text="Video Feed").pack()
  api = tk.Label(frame2, text="API").pack()
  blank = tk.Label(frame3, text="Blank Space").pack()
  loglabel = tk.Label(frame4, text="Log").pack()
  log = tk.Text(frame4, width = 20, height = 10).pack()
  
















# create connection by using object
connection = sqlite3.connect('users.db')
 
# query to create a table
connection.execute(''' CREATE TABLE IF NOT EXISTS users
         (FIND INT PRIMARY KEY     NOT NULL,
         FNAME           TEXT    NOT NULL,
         LNAME           TEXT    NOT NULL,
         USER           TEXT    NOT NULL,
         PASS           TEXT    NOT NULL);
         ''')

 
print("All data in food table\n")
 
# create a cousor object for select query
cursor = connection.execute("SELECT * from users ")
 
# display all data from users table
for row in cursor:
    print(row)








def mainRoot(root1):
  root1.destroy()
  
  root = tk.Tk()
  root.geometry("300x200")
  # Login page
  label_username = tk.Label(root, text="Username")
  label_username.pack()
  eun = tk.Entry(root)
  eun.pack()
  label_password = tk.Label(root, text="Password")
  label_password.pack()
  epw = tk.Entry(root, show="*")
  epw.pack()
  button_login = tk.Button(root, text="Login", command=lambda:login(eun,epw,root))
  button_login.pack()
  button_create_account = tk.Button(root, text="Create Account", command=lambda:create_account(root))
  button_create_account.pack()
  root.mainloop()


root = tk.Tk()
mainRoot(root)