from tkinter import *
import customtkinter
from PIL import Image,ImageTk
import time
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")
root=customtkinter.CTk()
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)


def fun():
    z2.tkraise()
def non():
    z1.tkraise()

def clock():
    hour=time.strftime("%H")
    minute=time.strftime("%M")
    second=time.strftime("%S")
    c23.configure(text=hour+":"+minute+":"+second)
    c23.after(1000,clock)

z1=customtkinter.CTkFrame(root,fg_color=("black", "teal"))
z1.grid(row=0,column=0,sticky="nsew")
z2=customtkinter.CTkFrame(root,fg_color=("black", "teal"))
z2.grid(row=0,column=0,sticky="nsew")



my_image1=customtkinter.CTkImage(light_image=Image.open("C:/Users/Dell/Downloads/22.jpeg"),size=(40,30))
my_image2=customtkinter.CTkImage(light_image=Image.open("C:/Users/Dell/Downloads/33.jpeg"),size=(2000,1100))

l2d=customtkinter.CTkLabel(z1,image=my_image2)
l2d.place(x=0,y=0)

l23=customtkinter.CTkLabel(z1,text="TIMETABLE FRAMER",font=("areail",80,'bold'),fg_color=("black", "teal"),text_color=("black","black"))
l23.pack()
m23=customtkinter.CTkLabel(z1,text="menu",fg_color=("black", "teal"),text_color=("black","black"),font=("areail",60,"bold"))
m23.pack(pady=30)

g23=customtkinter.CTkButton(z1,text="create timetable",font=("areail",50,"bold"))
g23.pack(pady=40)
g13=customtkinter.CTkButton(z1,text="about us",image=my_image1,font=("areail",50,"bold"),command=fun)
g13.pack()
c23=customtkinter.CTkLabel(z1,text="",font=("areail",40,'bold'),fg_color=("black", "teal"),text_color=("black","black"))
c23.pack(padx=200,pady=150)

l33=customtkinter.CTkLabel(z2,text="ABOUT US",font=("areail",80,'bold'),text_color=("black","black"))
l33.pack()
l43=customtkinter.CTkLabel(z2,text='''Hone your creativity with the power of timetable maker.
Explore professionally designed templates to get your wheels
spinning or create your own timetable from scratch.
Establish a theme for your designs using photos, icons, logos, 
personalized fonts, and other customizable elements to make them 
feel entirely authentic. Duplicate designs and resize them to 
create consistency across multiple types of assets. With timetable maker, 
it's free and easy to make, save, and share your designs within minutes.''',font=("areail",40,'bold'),text_color=("black","black"))
l43.pack()
g13=customtkinter.CTkButton(z2,text="back",font=("areail",40,"bold"),command=non)
g13.pack(pady=40)

clock()
z1.tkraise()
root.mainloop()
