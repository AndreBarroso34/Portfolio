from tkinter import messagebox, Toplevel
from sys import exit
from my_classes import new_user_from, users_list_form

#mensagem a perguntar se quero sair da aplicação
def exit_app(win):
    answer = messagebox.askquestion('Exit Applicaction',' Are you sure tou want to exit the applicaction')
    if answer == 'yes':
        exit()
    else:
        messagebox.CANCEL

#Abrir uma nova janela
def new_user_window():
    window = new_user_from()
    center(window)
    window.mainloop()


def users_list_window():
    window = users_list_form()
    center(window)
    window.mainloop()
    
def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()