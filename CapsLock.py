from tkinter import*
import string
from typing import List
from tkinter import messagebox

win=Tk()
win.title("Caps Lock")
win.geometry("630x350+200+150")

var=IntVar()



def fonk():
    a=0
    b=""
    met=metin.get("1.0",END)
    metin.delete("1.0",END)
    
    if met != "" and met!="\n" and met!=" ":
        met=met[:-1]
        if var.get()==1:
            par=met.split(" ")
            for f in par:
                metin.insert("1."+str(a),b+f.capitalize())
                b=" "
                a=a+len(f)+1
        elif var.get()==2:
            metin.insert("1.0",met.upper())
        elif var.get()==3:
            metin.insert("1.0",met.lower())
        elif var.get()==4:      

            par2=met.split(". ")
            for f in par2:
                
                metin.insert("1."+str(a),b+f.capitalize())
                b=". "
                a=a+len(f)+2
            
        else:
            messagebox.showerror("Hata","Lütfen dönüştürme yöntemini seçin.")
    else:
        messagebox.showerror("Hata","Lütfen dönüştürmek için metin giriniz.")


metin=Text(win,width=45, height=12, bg="grey")
radio1=Radiobutton(win,text="Baş harfleri büyült.",variable=var,value=1,command=fonk)
radio2=Radiobutton(win,text="Bütün harfleri büyült.",variable=var,value=2,command=fonk)
radio3=Radiobutton(win,text="Bütün harfleri küçült.",variable=var,value=3,command=fonk)
radio4=Radiobutton(win,text="Sadece noktadan sonraki harfleri büyült.",variable=var,value=4,command=fonk)

metin.place(x=10,y=10)
radio1.place(x=375,y=10)
radio2.place(x=375,y=30)
radio3.place(x=375,y=50)
radio4.place(x=375,y=70)

win.mainloop()