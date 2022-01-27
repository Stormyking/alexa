import tkinter


window = tkinter.Tk()
greetings = tkinter.Label(text = "hello, Tkinter", fg = "white", bg = "black", width = 10, height = 10)
click = tkinter.Button(text = "Click me!", width = 25, height = 5, bg = "blue", fg = "yellow")
entry = tkinter.Entry(fg = "red", bg = "blue", width = 50)
entry.pack()

click.pack()
greetings.pack()
window.mainloop()
window.close()



space = tkinter.Tkinter()
label = tkinter.Label( text = "Name")
userEntry = tkinter.Entry()
label.pack()
window.close()

