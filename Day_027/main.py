import tkinter

window = tkinter.Tk()
window.title("Hello World!")
window.minsize(width=500, height=500)

label = tkinter.Label(text="Hello", font=("Arial", 24))
label.pack()

input = tkinter.Entry(width=20)
input.pack()


def com():
    label.config(text=input.get())


def chg_bg():
    label.config(background="red")


# WORKS
# def big_wdw():
#     window.minsize(width=1000, height=1000)


button = tkinter.Button(text="Hello again!", command=com)
button.pack()

button2 = tkinter.Button(text="Change Coloooor!", command=chg_bg)
button2.pack()


window.mainloop()
