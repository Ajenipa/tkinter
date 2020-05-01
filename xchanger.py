from tkinter import *
ex=Tk()
ex.title("currency converter by jamiu@ajenipa.com")
ex.geometry("500x500")
heading=Label(ex,text="Currency Converter",fg="powder blue", font=("arial",20,"bold"))
heading.pack()
enter_box=Label(ex, text="Enter Amount To Convert:", fg="red", font=("arial",23,"bold"))
enter_box.pack()
amount=IntVar()
screen=Entry(ex, font=("arial",20,"bold"),fg="black",bg="powder blue", bd=16,textvariable=amount)
screen.pack()
def dconverter():
    here=amount.get()
    final=here*387
    lab1=Label(ex, bg="green", fg="white", text=("₦/$ " +str(final)), font=("arial",20,"bold"))
    lab1.place(x=90, y=340)
def econverter():
    here=amount.get()
    final=here*425
    lab2=Label(ex, bg="blue", fg="white", text=("₦/€"+ str(final)), font=("arial",20,"bold"))
    lab2.place(x=360, y=340)
def pconverter():
    here=amount.get()
    final=here*485
    lab3=Label(ex, bg="red", fg="white", text=("₦/£"+str(final)), font=("arial",20,"bold"))
    lab3.place(x=90, y=390)
def yconverter():
    here=amount.get()
    final=here*3983736
    lab4=Label(ex, bg="green", fg="white", text=("₦/฿"+str(final)), font=("arial",20,"bold"))
    lab4.place(x=360, y=390)
btn1=Button(ex, bg="green", fg="white", font=("arial",20,"bold"), width=8, height=2, bd=10, text="$", command=dconverter)
btn1.place(x=90,y=140)
btn2=Button(ex, bg="brown", fg="white", font=("arial",20,"bold"),width=8, height=2, bd=10, text="€", command=econverter)
btn2.place(x=250,y=140)
btn3=Button(ex, bg="blue", fg="white", font=("arial",20,"bold"),width=8, height=2, bd=10, text="£",command=pconverter)
btn3.place(x=90,y=230)
btn4=Button(ex, bg="green", fg="white" ,font=("arial",20,"bold"),width=8, height=2, bd=10, text="฿", command=yconverter)
btn4.place(x=250,y=230)


ex.mainloop()