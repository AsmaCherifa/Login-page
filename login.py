from tkinter import *
from tkinter import messagebox

loginPage=Tk()
loginPage.title('Login Page')
loginPage.geometry("800x500")
loginPage.configure(bg="#fff")
loginPage.resizable(False,False)

def signUp():
    username = userEntry.get()
    pwd = pwdEntry.get()
    if username == 'admin' and pwd =='123':
        screen = Toplevel(loginPage)
        screen.title('App Page')
        screen.geometry("800x500")
        screen.configure(bg="#fff")
        screen.resizable(False,False)
        Label(screen,text="hello everyone!!")
        screen.mainloop()
    else:
        messagebox.showerror("invalid","invalid username!")
        
img= PhotoImage(file='login.png')
Label(loginPage,image=img,bg='white').place(x=50,y=50)

frame = Frame (loginPage, width=350,height=350,bg="white")
frame.place(x=400,y=70)
heading = Label(frame,text="Sign In",fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',33,'bold'))
heading.place(x=60,y=5)

userLabel = Label(frame,text="username",bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
userLabel.place(x=30,y=110)

userEntry = Entry(frame,width=25,fg='black',border=2)
userEntry.place(x=120,y=110)



pwdLabel = Label(frame,text="Password",bg='white',font=('Microsoft YaHei UI Light',12,'bold'))
pwdLabel.place(x=30,y=170)

pwdEntry = Entry(frame,width=25,fg='black',border=2)
pwdEntry.place(x=120,y=170)

Button(frame,width=35,pady=5,text='sign in',bg='#57a1f8',fg='white',border=0,command=signUp).place(x=35,y=230)

signupLabel = Label(frame,text="Don't have an account?",bg='white',font=('Microsoft YaHei UI Light',9,'bold'))
signupLabel.place(x=70,y=270)

Button(frame,width=6,text='sign in',bg='white',fg='#57a1f8',cursor='hand2',border=0).place(x=240,y=270)


loginPage.mainloop()
