from tkinter import *
from verify import *
import mysql.connector
from main2 import *
import pygame
import math

class Menu():
    def __init__(self,fenetre):
        self.fenetre = fenetre
        
    def open(self):
        self.fenetre.mainloop()
    def close(self):
        self.fenetre.quit()
        self.fenetre.destroy()
    def open_register(self):
        
        def retour():
            registerfen.destroy()
            
        def register():
                name = str(entryPseudo.get())
                m = str(entryMail2.get())
                p = str(entryPassword2.get())
    
                mydb = mysql.connector.connect(
                  host="localhost",
                  user="root",
                  password="",
                  database = "jeu"
                )
                mycursor = mydb.cursor()
                
                if name != "" and m !="" and p != "":
                    if verify_mail(m) == False:
                        print("Vous avez été enregister bon jeu à vous.")
                        sql =( "INSERT INTO User VALUES (NULL,'{0}','{1}','{2}');").format(name,m,p)
                        mycursor.execute(sql)
                        registerfen.destroy()
                        menu.close()
                        lance()
                    else:
                        messagebox.showinfo("ERROR","Veuillez entrez une addresse mail valide !!!")
                        registerfen.destroy()
                else:
                    messagebox.showinfo("ERROR","Veuillez entrez toutes les informations demandé !!!")
                    registerfen.destroy()
                
        
    
                mydb.commit()
                mydb.close()
        
        
        registerfen = Tk()
        registerfen.title("Register")
        registerfen.config(background = "grey")
        registerfen.geometry("350x200")
    
        lblPseudo = Label(registerfen, text = "Entrer un pseudo")
        lblPseudo.place( x = 20 , y =25)
        entryPseudo = Entry(registerfen)
        entryPseudo.place(x = 175, y = 25)

        lblMail2 = Label(registerfen, text = "Entrer une addresse mail")
        lblMail2.place( x = 20 , y =75)
        entryMail2 = Entry(registerfen)
        entryMail2.place(x = 175, y = 75)

        lblPassword2 = Label(registerfen, text = "Entrer un mot de passe")
        lblPassword2.place( x = 20 , y = 125)
        entryPassword2 = Entry(registerfen,show= "*")
        entryPassword2.place(x = 175, y = 125)

        register= Button(registerfen,text= "Register",command = register)
        register.place( x = 275,y=170)
    
        back= Button(registerfen,text="Back",command = retour)
        back.place(x = 20,y = 170)
        
    def open_login(self):
        def retour():
            loginfen.destroy()
        def login():
            m = str(entryMail.get())
            p = str(entryPassword.get())  
        
            mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              password="",
              database = "jeu"
            )
            mycursor = mydb.cursor()
            sql =( "SELECT Email,Password FROM User WHERE Email = '{0}';").format(m)
            mycursor.execute(sql)
            resultat = mycursor.fetchall()
            for i in resultat:
                if i[0]== m and i[1] == p:
                    print("Vous etes connecté")
                    loginfen.destroy()
                    menu.close()
                    lance()
        
            if resultat == []:
                messagebox.showinfo("ERROR","""Votre addresse mail ou votre mot de passe est invalide \nSi le probleme persiste veuillez vous enregistrez""")
                loginfen.destroy()
            mydb.close()
    
        loginfen = Tk()
        loginfen.title("Login")
        loginfen.config(background = "grey")
        loginfen.geometry("350x200")
    
        lblMail = Label(loginfen, text = "Entrer votre mail")
        lblMail.place( x = 20 , y = 25)
        entryMail = Entry(loginfen)
        entryMail.place(x = 175, y = 25)

        lblPassword = Label(loginfen, text = "Entrer un mot de passe")
        lblPassword.place( x = 20 , y = 75)
        entryPassword = Entry(loginfen,show= "*")
        entryPassword.place(x = 175, y = 75)
    
        login2 =Button(loginfen,text ="Login", command = login)
        login2.place(x = 275,y = 150)
    
        back = Button(loginfen,text ="Back",command = retour)
        back.place(x=20,y = 150)
    
        loginfen.mainloop()


fen = Tk()
fen.title("Business Adventure")
fen.geometry("400x300")
fen.config(background = "grey")
frame =Frame(fen,width = 350,height = 150,bg = "black")
menu = Menu(fen)
login = Button(frame,text="Login",bg = "white",font =("Arial",20),width = 8,height = 3,command = menu.open_login)
login.grid(row = 0 ,column = 0)

register = Button(frame,text="Register",bg = "white",font =("Arial",20),width = 8,height = 3, command =menu.open_register)
register.grid(row = 0 ,column = 1)
frame.pack(expand= YES)
menu.open()











        
        



         
    



    


