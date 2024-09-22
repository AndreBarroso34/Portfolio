from tkinter import *
from my_functions import center, exit_app, new_user_window, users_list_window

window = Tk()
window.geometry('600x400')
window.title("Menu Princial")
center(window)

#Botões
btn_new_user = Button(window, text="New User", width=35, pady=25, font=("Consolas",16), command=new_user_window)
btn_new_user.pack(expand=True)

btn_users_list = Button(window, text="View Users", width=35, pady=25, font=("Consolas",16), command=users_list_window)
btn_users_list.pack(expand=True)

btn_exit = Button(window, text="Exit Applicaction", width=35, pady=25, font=("Consolas",16), command=lambda:exit_app('window'))
btn_exit.pack(expand=True)

window.mainloop()


