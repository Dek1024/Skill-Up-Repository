from tkinter import *

def collect():
    expCollect = expEntry.get()
    ans = eval(expCollect)
    expInput.set(ans)

scalc = Tk()
scalc.title("Expression_Evaluator")
scalc.configure(background = "gray")
expInput = StringVar()

#Heading
Label(scalc, padx = 16, pady = 16, font = ("ariel",16,"bold"),
      bg = "gray", fg = "white", text = "Enter the expression for evaluation.").grid(row = 0, column = 0, sticky = W)

#EntryBox
expEntry = Entry(scalc, font = ("ariel",16,"bold"),
                 bg = "gray", fg = "white", textvariable = expInput,bd = 30,insertwidth = 60, justify = 'right')
expEntry.grid(row = 1, column = 0, sticky = E)

#Button
Button(scalc, text = "Go",padx = 24 , pady = 24, command = collect,
       bg = "black",fg = "white", font = ("ariel",16,"bold")).grid(row = 1, column =0,sticky= W)

scalc.mainloop()
 
