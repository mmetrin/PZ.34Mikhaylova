from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.font
import pickle

root = Tk ()
root['bg']='#fbf9f4'
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 4.5
root.wm_geometry("+%d+%d" % (x, y))
root.geometry("300x600")
root.title("Войти в систему")

# обеспечение написания подсказки для entry (placeholder)
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder=None):
        super().__init__(master)
        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = 'grey'
            self.default_fg_color = self['fg']
            self.bind("<FocusIn>", self.focus_in)
            self.bind("<FocusOut>", self.focus_out)
            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    # Если был вставлен какой-то символ в начало, удаляем не весь текст, а только placeholder:
    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()

# функция для регистрации
def registrarion():
    
    def click_name(event):
        registr_name.delete(0, END)
    def click_surname(event):
        registr_surname.delete(0, END)
    def click_login(event):
        registr_login.delete(0, END)
    def click_pass1(event):
        registr_password1.delete(0, END)
    def click_pass2(event):
        registr_password2.delete(0, END)
    
    FontOfEntryList=tkinter.font.Font(family="Calibri",size=14)
    
    registr_name = Entry(root, bd=2,fg='grey',relief='groove', width=22, font = FontOfEntryList,justify="center", background='lavender')
    registr_name.insert(0,"имя")    
    registr_name.bind('<Button-1>', click_name)
    # registr_surname = EntryWithPlaceholder(root, "фамилия")  
    registr_surname = Entry(root, bd=2,fg='grey',relief='groove', width=22, font = FontOfEntryList,justify="center", background='lavender')
    registr_surname.insert(0,"фамилия")    
    registr_surname.bind('<Button-1>', click_surname)
    
    registr_login = Entry(root, bd=2,fg='grey',relief='groove', width=22, font = FontOfEntryList,justify="center", background='lavender')
    registr_login.insert(0,"логин")    
    registr_login.bind('<Button-1>', click_login)
    
    registr_password1 = Entry(root, bd=2,fg='grey',relief='groove', width=22, font = FontOfEntryList,justify="center", background='lavender')
    registr_password1.insert(0,"пароль")    
    registr_password1.bind('<Button-1>', click_pass1)
    
    registr_password2 = Entry(root, bd=2,fg='grey',relief='groove', width=22, font = FontOfEntryList,justify="center", background='lavender')
    registr_password2.insert(0,"повтор пароля")    
    registr_password2.bind('<Button-1>', click_pass2)
        
    # анонимно вызовет функцию пароля эквивалентности паролей при регистрации
    button_registr = Button(text="регистрация", bd=2, fg='#525056', relief='groove', font = FontOfEntryList, background='#ccbce0', activebackground='#ac9dbf',  command=lambda:data_check())
    
    # выводим данные на рабочую область
    registr_name.place(relx=.5, rely=.2, anchor="c", height=30, width=230)
    registr_surname.place(relx=.5, rely=.29, anchor="c", height=30, width=230)    
    registr_login.place(relx=.5, rely=.38, anchor="c", height=30, width=230)
    registr_password1.place(relx=.5, rely=.47, anchor="c", height=30, width=230)
    registr_password2.place(relx=.5, rely=.56, anchor="c", height=30, width=230)
    button_registr.place(relx=.5, rely=.7, anchor="c", height=30, width=230)    

    # валидация
    def data_check():
        # проверка на длину пароля
        if (len(registr_password1.get())>5) and (len(registr_password1.get())<21):
            # проверка на корректность введенного имени
            if ((registr_name.get().istitle() == True) and (registr_name.get().isalpha() == True)):
                # проверка на корректность введенной фамилии
                if ((registr_surname.get().istitle() == True) and (registr_surname.get().isalpha() == True)):
                    # проверка на эквивалентность паролей
                    if registr_password1.get()==registr_password2.get():
                    # вызов функции сохранения данных
                        save()
                    else:
                        messagebox.showerror("Ошибка!","Пароли не совпадают! Повторите ввод и попробуйте еще раз!")
                else:
                    messagebox.showerror("Ошибка!","Введите корректую фамилию")
            else:
                messagebox.showerror("Ошибка!","Введите корректое имя")
        else:
            messagebox.showerror("Ошибка!","Пароль должен содержать от 6 до 20 символов")
        
    
    # функция для сохранения введенных данных
    def save():
        # словарь, ассоциативный массив
        login_pass_save = {} 
        login_pass_save[registr_login.get()]=registr_password1.get()
        
        # создание и запись в файл для сохранения
        doc = open("login.txt", "wb")
        pickle.dump(login_pass_save, doc)
        doc.close()
        
        # скрытие ненужных полей с экрана при переходе на регистрацию        
        registr_name.destroy()
        registr_surname.destroy()
        registr_login.destroy()
        registr_password1.destroy()
        registr_password2.destroy()
        button_registr.destroy()
        login()
  
# функция для авторизации  
def login():
    
    def click_login_a(event):
        enter_login.delete(0, END)
    def click_pass_a(event):
        enter_password.delete(0, END)
    FontOfEntryList=tkinter.font.Font(family="Calibri",size=14)
    
    enter_login = Entry(root, bd=2,fg='grey',relief='groove', width=22, font = FontOfEntryList,justify="center", background='lavender')
    enter_login.insert(0,"логин")    
    enter_login.bind('<Button-1>', click_login_a)
            
    enter_password = Entry(root, bd=2,fg='grey',relief='groove', width=22, font = FontOfEntryList,justify="center", background='lavender')
    enter_password.insert(0,"пароль")
    enter_password.bind('<Button-1>', click_pass_a)
    
    button_enter = Button(text="вход", bd=2, fg='#525056', relief='groove', font = FontOfEntryList, background='#ccbce0', activebackground='#ac9dbf' , command=lambda: log_pass())
    button_reg = Button(text="регистрация", background='#b7a1d3', activebackground='#9a81b9', bd=2, fg='white', relief='groove', font = FontOfEntryList, command=lambda: reg_open())
    c1 = Checkbutton(text="запомнить пароль", onvalue=1, offvalue=0, background='#fbf9f4', font = 'Calibri, 10', bd=1)
    forget_pass = Label(text="забыли пароль?", background='#fbf9f4', font = 'Calibri, 10')   
    
    # добавление полей на рабочую область 
    enter_login.place(relx=.5, rely=.3, anchor="c", height=30, width=230)
    enter_password.place(relx=.5, rely=.39, anchor="c", height=30, width=230)    
    button_enter.place(relx=.5, rely=.5, anchor="c", height=30, width=230)    
    button_reg.place(relx=.5, rely=.59, anchor="c", height=30, width=230)
    c1.place(relx=.6, rely=.67, anchor="e", height=30, width=130)
    forget_pass.place(relx=.5, rely=.72, anchor="w", height=30, width=130)
    # enter_password.pack(pady=10)
    # c1.pack()    
    # forget_pass.pack()
    # button_enter.pack()
    # button_reg.pack()
    
    def reg_open():
        # скрытие ненужных полей с экрана при переходе на регистрацию
        enter_login.destroy()
        enter_password.destroy()
        button_enter.destroy()
        button_reg.destroy()
        c1.destroy()
        forget_pass.destroy()  
        
        # вызов функции регистрации
        registrarion()
    
    def log_pass():
        doc= open("login.txt", "rb")
        list_login = pickle.load(doc)
        doc.close()
        # проверка на содержание введенного логина в сохраненных данных при регистрации
        if enter_login.get() in list_login:
            # проверка на корректность пароля по введенному логину
            if enter_password.get() ==list_login[enter_login.get()]:
                messagebox.showinfo("Вход выполнен","Привет! Вход успешно выполнен")
            else:
                messagebox.showerror("Ошибка", "Введен неверный пароль")
        else:
            messagebox.showerror("Ошибка!", "Неверный логин!")

# вызов функции авторизации при отладке
login()

root.mainloop()
