from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text") #event.widget gives the button which is clicked
    #cget() this cget function is used to get text from the widget
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = 'error'


        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()



root = Tk()
root.title("CALCULATOR")
height = 600
width = 1000
root.geometry(f"{height}x{width}")
root.config(bg="black")
root.wm_iconbitmap("Iconsmind-Outline-Calculator-2.ico")



scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f = Frame(root,bg="black")

b = Button(f,text="9",font="lucida 35 bold",padx=28,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="8",font="lucida 35 bold",padx=28,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="7",font="lucida 35 bold",padx=28,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="black")

b = Button(f,text="6",font="lucida 35 bold",padx=28,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="5",font="lucida 35 bold",padx=28,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="4",font="lucida 35 bold",padx=28,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="black")
b = Button(f,text="3",font="lucida 35 bold",padx=28,pady=15)

b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="2",font="lucida 35 bold",padx=28,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="1",font="lucida 35 bold",padx=28,pady=15)

b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="black")

b = Button(f,text="0",font="lucida 35 bold",padx=31,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="-",font="lucida 35 bold",padx=31,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="+",font="lucida 35 bold",padx=31,pady=15)
b.pack(side=LEFT,padx=20,pady=5)
b.bind("<Button-1>",click)
f.pack()


f = Frame(root,bg="black")


b = Button(f,text="*",font="lucida 35 bold",padx=31,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="/",font="lucida 35 bold",padx=31,pady=15)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

b = Button(f,text="=",font="lucida 35 bold",padx=31,pady=15)
b.pack(side=LEFT,padx=20,pady=5)
b.bind("<Button-1>",click)
f.pack()


f = Frame(root,bg="black")


b = Button(f,text="/",font="lucida 35 bold",padx=31,pady=15)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="%",font="lucida 35 bold",padx=25,pady=15)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)

b = Button(f,text="C",font="lucida 35 bold",padx=25,pady=15)
b.pack(side=LEFT,padx=18,pady=12)
b.bind("<Button-1>",click)
f.pack()


f = Frame(root,bg="black")


f.pack()

root.mainloop()