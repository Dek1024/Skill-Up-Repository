from tkinter import *

def collect(x):
    global content
    content = content + str(x)
    Text.set(content)

def clear():
    global content
    Text.set("")
    content = ""

def equals():
    global content
    Text.set(eval(content))
    
mcalc=Tk()
mcalc.title("Calculator")
Text = StringVar()
content = ""

#Display
display = Entry(mcalc, insertwidth = 4 , bd = 20 ,bg = "blue", fg = "white", font = ("Ariel",16,"bold"),
      textvariable = Text, justify = "right").grid(columnspan = 6)

#Buttons

#Row1
but1 = Button(mcalc, bd =  8, text = "1",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(1)).grid(row = 1, column =0,sticky = W)

but2 = Button(mcalc, bd = 8, text = "2",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(2)).grid(row = 1, column =1, sticky = W)

but3 = Button(mcalc, bd = 8, text = "3",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(3)).grid(row = 1, column =2, sticky = W)

butadd = Button(mcalc, bd = 8, text = "+",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect("+")).grid(row = 1, column =4, sticky = W)

#Row2
but4 = Button(mcalc, bd =  8, text = "4",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(4)).grid(row = 2, column =0,sticky = W)

but5 = Button(mcalc, bd = 8, text = "5",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(5)).grid(row = 2, column =1, sticky = W)

but6 = Button(mcalc, bd = 8, text = "6",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(6)).grid(row = 2, column =2, sticky = W)

butsub = Button(mcalc, bd = 8, text = "-",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect("-")).grid(row = 2, column =4, sticky = W)

#Row3
but7 = Button(mcalc, bd =  8, text = "7",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(7)).grid(row = 3, column =0,sticky = W)

but8 = Button(mcalc, bd = 8, text = "8",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(8)).grid(row = 3, column =1, sticky = W)

but9 = Button(mcalc, bd = 8, text = "9",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(9)).grid(row = 3, column =2, sticky = W)

butmul = Button(mcalc, bd = 8, text = "*",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect("*")).grid(row = 3, column =4, sticky = W)

#Row4
butdot = Button(mcalc, bd =  8, text = ".",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect(".")).grid(row = 4, column =0,sticky = W)

butclear = Button(mcalc, bd = 8, text = "C",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:clear()).grid(row = 4, column =1, sticky = W)

butequals = Button(mcalc, bd = 8, text = "=",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda: equals()).grid(row = 4, column =2, sticky = W)

butdiv = Button(mcalc, bd = 8, text = "/",padx = 16 , pady = 16,
       fg = "black", font = ("ariel",16,"bold"), command = lambda:collect("/")).grid(row = 4, column =4, sticky = W)

