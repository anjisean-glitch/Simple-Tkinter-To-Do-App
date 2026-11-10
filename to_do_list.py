import customtkinter as ctk
import subprocess
import sqlite3
from CTkMessagebox import CTkMessagebox
import dbconnect

tasks = [{}]

class ToDo_List():
  def __init__(self):
    self.root = ctk.CTk()
    self.root.title("My To-Do List App")
    self.root.geometry("400x500")
    self.root.configure(fg_color="black")

    

    ## title label
    self.title = ctk.CTkLabel(self.root, text="My To do list", font=("Arial", 30, "bold"), text_color="White")
    self.title.pack(padx=20, pady=(10,30))

    ## tasks label
    self.tasks_title = ctk.CTkLabel(self.root, text="My tasks:", font=("Arial", 25), text_color="White")
    self.tasks_title.pack(padx=20, pady=(10,5))

    self.tasks_frame = ctk.CTkScrollableFrame(
    self.root,
    width=350,
    height=180,
    fg_color="black"
    )
    self.tasks_frame.pack(padx=10, pady=10, fill="both", expand=True)


    con = sqlite3.connect('to_do_list.db')
    cur = con.cursor()
    tasks_extract = cur.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()

    tasks = tasks_extract
    con.commit()
    print (tasks)
    if tasks:
      for task in tasks:
        id = task[0]
        title = task[1]
        status = task[2]

        ctk.CTkLabel(self.tasks_frame, text=f"Title: {title}\nStatus: {status}", font=("Arial", 20), text_color="white", fg_color="black").pack(padx=10, pady=(20, 5))
        self.function_frm = ctk.CTkFrame(self.tasks_frame, fg_color="black")
        ctk.CTkButton(self.function_frm, text="Edit", font=("Arial", 17), text_color="white", fg_color="grey", hover_color="green", command=lambda task_id=id: self.edit(task_id)).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(self.function_frm, text="delete", font=("Arial", 17), text_color="white", fg_color="grey", hover_color="green", command=lambda task_id=id: self.delete(task_id)).grid(row=0, column=1, padx=10, pady=10)
        self.function_frm.pack(padx=10, pady=(0, 10))

    else:
      ctk.CTkLabel(self.tasks_frame, text="No tasks have been added yet...", font=("Arial", 20), text_color="white", fg_color="black").pack(padx=10, pady=(10, 30))

    self.add_btn = ctk.CTkButton(self.tasks_frame, text="Add Task", font=("Arial", 20), text_color="white", fg_color="grey", hover_color="green", command=self.add)
    self.add_btn.pack(padx=10, pady=10)

    
    ## credit
    self.credit = ctk.CTkLabel(self.tasks_frame, text="MADE BY ANJI", fg_color="black", text_color="white", font=("Arial", 15))
    self.credit.pack(padx=10, pady=50)





    self.root.mainloop()

  def add(self):
    subprocess.Popen(["python","add_task.py"])
    self.root.destroy()

  def edit(self, id):
    try:
      con = sqlite3.connect('to_do_list.db')
      cur = con.cursor()


      result = cur.execute("SELECT * FROM tasks WHERE id = ?",(id,)).fetchone()
      gotten_id = result[0]
      con.commit()
      con.close()
      print(f"Gotten ID: {gotten_id}")
      print(f"Task: {result[1]}")
      
      

      subprocess.Popen([
      "python",
      "edit_task.py",
      str(result[0]),
      str(result[1]),
      str(result[2]),
      ])

      self.root.destroy()

    except Exception as e:
      CTkMessagebox(title="Error", message=str(e))

  def delete(self, id):
    try:
      msg = CTkMessagebox(
        title="Confirm Delete",
        message="Are you sure you want to delete this task?",
        icon="question",
        option_1="Cancel",
        option_2="Yes"
    )

      response = msg.get()

      if response == "Yes":
          print("User wants to delete the task...")

          con = sqlite3.connect('to_do_list.db')
          cur = con.cursor()

          cur.execute(''' delete from tasks where id=? ''',(id,))
          con.commit()

          subprocess.Popen(["python","to_do_list.py"])
          self.root.destroy()
          print("Successfully deleted")
          


      else:
          print("Deletion cancelled")
          return
      
    except Exception as e:
      CTkMessagebox(title="Error", message=str(e))

      con.close()





ToDo_List()