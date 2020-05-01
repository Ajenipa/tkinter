from tkinter import *
cal=Tk()
cal.title("30 calculater")
operator=""
def btnclick(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)
def btnclear(c):
    global operator
    operator=""
    text_input.set("")
def btnequal():
    global operator
    sumup=eval(str(operator))
    text_input.set(sumup)
text_input=StringVar()
screen=Entry(cal,font=("Arial",20,"bold"),bg="powder blue",justify="right",bd=20, textvariable=text_input)
screen.grid(columnspan=16)
btn7=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16, padx=6, pady=6, text="7", command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=-6,pady=6,text="8", command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=6,pady=6, text="9", command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
btnp=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=16,pady=6 ,text="+",command=lambda:btnclick("+"))
btnp.grid(row=1,column=3)
#..........................................................................
btn4=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16, padx=6, pady=6, text="4", command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=-6,pady=6,text="5", command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=6,pady=6, text="6", command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
btnm=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=16,pady=6 ,text="-", command=lambda:btnclick("-"))
btnm.grid(row=2,column=3)

#----------------------------------------------------------------------------
btn1=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16, padx=6, pady=6, text="1", command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=-6,pady=6,text="2", command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=6,pady=6, text="3", command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
btnd=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=16,pady=6 ,text="/",command=lambda:btnclick("/"))
btnd.grid(row=3,column=3)
#----------------------------------------------------------------------------
btnz=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16, padx=6, pady=6, text="0", command=lambda:btnclick(0))
btnz.grid(row=4,column=0)
btnc=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=-6,pady=6,text="c", command=lambda:btnclear("c"))
btnc.grid(row=4,column=1)
btnmu=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=6,pady=6, text="x",command=lambda:btnclick("*"))
btnmu.grid(row=4,column=2)
btne=Button(cal, font=("Arial",20,"bold"), bg="powder blue", bd=16,padx=16,pady=6 ,text="=", command=lambda:btnequal())
btne.grid(row=4,column=3)
cal.mainloop()