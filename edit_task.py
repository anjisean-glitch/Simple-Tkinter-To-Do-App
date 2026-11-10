import customtkinter as ctk
import subprocess
import sqlite3
from CTkMessagebox import CTkMessagebox
import dbconnect
import sys

id = sys.argv[1]
task = sys.argv[2]
status = sys.argv[3]


class ToDo_List():
  def __init__(self):
    self.root = ctk.CTk()
    self.root.title(f"Edit task Page/{task}/{id}")
    self.root.geometry("600x400")
    self.root.configure(fg_color="black")

    self.title = ctk.CTkLabel(self.root, text="Lets edit this task!!", font=("Arial", 30, "bold"), text_color="White")
    self.title.pack(padx=20, pady=(10,30))

    self.frm = ctk.CTkFrame(self.root, fg_color="black")

    self.title_lbl = ctk.CTkLabel(self.frm, text="Title:", font=("Arial", 25), fg_color="black", text_color="white")
    self.title_lbl.grid(row=0, column=0, padx=10, pady=10)

    self.title_ent = ctk.CTkEntry(self.frm, font=("Arial", 25), fg_color="white", text_color="black")
    self.title_ent.grid(row=0, column=1, padx=10, pady=10)
    self.title_ent.insert("end", task)


    self.status_lbl = ctk.CTkLabel(self.frm, text="Status:", font=("Arial", 25), fg_color="black", text_color="white")
    self.status_lbl.grid(row=1, column=0, padx=10, pady=10)
    


    self.status_ent = ctk.CTkComboBox(
                                    self.frm,
                                    values=["Pending", "Done"] 
        )
    self.status_ent.grid(row=1, column=1, padx=10, pady=10)
    

    self.frm.pack(padx=10, pady=20)

    self.edit_btn = ctk.CTkButton(self.root, text="Edit Task", font=("Arial", 20), text_color="white", fg_color="grey", hover_color="green", command=self.edit)
    self.edit_btn.pack(padx=10, pady=10)

    self.back_btn = ctk.CTkButton(self.root, text="Go Back", font=("Arial", 20), text_color="white", fg_color="grey", hover_color="green", command=self.back)
    self.back_btn.pack(padx=10, pady=(20,5))



    ## credit
    self.credit = ctk.CTkLabel(self.root, text="MADE BY ANJI", fg_color="black", text_color="white", font=("Arial", 15))
    self.credit.pack(padx=10, pady=20)

    self.root.mainloop()

  def edit(self):

    try:

      title = self.title_ent.get().strip()
      status = self.status_ent.get().strip()

      if not title or not status:
        CTkMessagebox(title="Error", message="Please fill all the space")
        return

      con = sqlite3.connect('to_do_list.db')
      cur = con.cursor()

      cur.execute("""UPDATE tasks SET task = ?, status =? WHERE id = ?
                  """,(title, status, id))  
      con.commit()

      msg = CTkMessagebox(title="Info", message=f"You have successfully edited the task\n - {title}\n - {status}", icon="info")
      msg.get()

      con.close()

      self.back()
    except Exception as e:
      CTkMessagebox(title="Error", message=str(e)) 
      

                  

  def back(self):
    subprocess.Popen(["python","to_do_list.py"])
    self.root.destroy()


ToDo_List()