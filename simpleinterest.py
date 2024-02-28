from tkinter import *


window=Tk()
window.title('Simple Interest Calculator')
window.geometry("500x600")
def simpleInterest():
    pr=int(p.get())
    ti=int(t.get())
    ra=int(r.get())
    interest=(pr*ra*ti)/100
    i=Label(result_frame, text="Your interest is "+interest, fg = "black", font=("Calibri", 20),bd=5)
    i.place(x=100,y=500)
    i.pack()


principal=Label(window, text="Principal", fg = "black", font=("Calibri", 20),bd=5)
principal.place(x=100, y=100)
p=Entry(window, text="", bd=2, width=22)
p.place(x=220,y=115)

time=Label(window, text="Time", fg = "black", font=("Calibri", 20),bd=5)
time.place(x=100,y=200)
t=Entry(window, text="", bd=2, width=22)
t.place(x=220,y=215)

rate=Label(window, text="Rate", fg = "black", font=("Calibri", 20),bd=5)
rate.place(x=100,y=300)
r=Entry(window, text="", bd=2, width=22)
r.place(x=220,y=315)

calculate=Button(text="Calculate",fg="black",bg="blue",bd=4, command=simpleInterest)
calculate.place(x=400,y=200)




result_frame = LabelFrame(window,text="Result", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=100,y=500)

result_label=Label(result_frame,text=" ", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()


window.mainloop()