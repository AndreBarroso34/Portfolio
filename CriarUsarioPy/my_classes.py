from tkinter import Toplevel, Label, Entry, Button, ttk

class user():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

#função para quando clicar no botão cancelar, limpar as caixas
def clear_boxes(box1, box2, box3, *boxes):
    box1.delete(0,'end')
    for box in boxes:
        box.delete(0,'end')
    box2.delete(0,'end')
    box3.delete(0,'end')
    box1.focous_set()

def save_user(name,username,password):
    new_user = user(name, username, password)
    f = open(r'utilizadores.txt', "a")
    f.write("%,%,%\n" % (new_user.name.get(), new_user.username.get(), new_user.password.get()))
    f.close()
    clear_boxes(name,username,password)

class new_user_from(Toplevel):

    def __init__(self):
        super().__init__()
        
        self.geometry('400x300')
        self.title('New user')

        #Create control
        my_name_label = Label(self, text="Name", justify= "left")
        my_name_text = Entry(self, width=62)

        my_username_label = Label(self, text="Username",  justify= "left")
        my_username_text = Entry(self, width=62)

        my_password_label = Label(self, text="Password",  justify= "left")
        my_password_text = Entry(self, width=62, show="*")

        btn_insert = Button(self, text="Insert new user", width=21, pady=5, command=lambda:save_user(my_name_text, my_username_text,my_password_text))
        btn_cancel = Button(self, text="Cancel", width=21, pady=5, command=lambda:clear_boxes(my_name_text, my_username_text,my_password_text))

        #insert controls into the form
        my_name_label.grid(row=0, column=0, padx=(10,0), sticky="w")
        my_name_text.grid(row=1, column=0, columnspan=2, padx=(10,0), pady=(0,10))

        #insert controls into the form
        my_username_label.grid(row=3, column=0, padx=(10,0),sticky="w")
        my_username_text.grid(row=4, column=0, columnspan=2, padx=(10,0), pady=(0,10))
        
        #insert controls into the form
        my_password_label.grid(row=6, column=0, padx=(10,0),sticky="w")
        my_password_text.grid(row=7, column=0, columnspan=2, padx=(10,0), pady=(0,10))


        btn_insert.grid(row=9, column=0, padx=(10,0))
        btn_cancel.grid(row=9, column=1, padx=(10,0))

class users_list_form(Toplevel):
    def __init__(self):
        super().__init__()
        
        self.geometry('400x300')
        self.title('List of users')
        #Create controls
        title_lable = Label(self,text="List of users", width=40,pady=10)
        trv_list_users = ttk.Treeview(self,columns=("name","username"))
        btn_delete = Button(self, text="delete user ", width=30, pady=5)

        title_lable.pack(expand=True)
        trv_list_users.pack(expand=True)
        btn_delete.pack(expand=True)