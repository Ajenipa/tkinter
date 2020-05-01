from tkinter import *
root=Tk()
root.title("currency konverter")
root.geometry("400x400+250+250")
heading=Label(root, text="WELCOME TO AJENIPA'S CURRENCY CONVERTER", font=("arial",10,"bold"), fg="steel blue")
heading.pack()
enter_amount=Label(root, text="enter any amount in dollar",font=("arial",20,"bold"))
enter_amount.place(x=20,y=50)
my_num=IntVar()
enter_box=Entry(root, width=50, textvariable=my_num)
enter_box.place(x=40, y=90)
def converter():
    here=my_num.get()
    final=here*360
    lab=Label(root, text=("#" +str(final)), font=("arial",20,"bold"),fg="red")
    lab.place(x=280, y=220)
def reverse():
    here=my_num.get()
    final=here/360
    lab=Label(root, text=("$" +str(final)),font=("arial",20,"bold"), fg="green")
    lab.place(x=10,y=260)
btn1=Button(root, text="conversion", width=12, height=2, bg="light green", command=converter)
btn1.place(x=280,y=130)
btn2=Button(root, text="reverse", width=12, height=2, bg="light green", command=reverse)
btn2.place(x=10,y=130)

root.mainloop()