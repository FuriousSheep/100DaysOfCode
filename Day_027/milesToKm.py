from tkinter import (Tk, Entry, Label, Button)

MTK_COEFFICIENT = 1.609344
FONT = ("Arial", 12)


window = Tk()
window.minsize(height=90, width=280)
window.title("Miles to kilometers")


def mtk(miles):
    return round(miles * MTK_COEFFICIENT, 3)


# what do we want:
#               [       ]   Miles
# is equal to   [       ]   Kilometers
#               (Calculate)

def convert():
    km = round(int(milesEntry.get()) * MTK_COEFFICIENT, 2)
    resultLabel.config(text=str(km))


calcButton = Button(text="Calculate", command=convert)
isEqualLabel = Label(text="is equal to", font=FONT)
kmLabel = Label(text="Kilometers", font=FONT)
milesEntry = Entry(width=10)
milesLabel = Label(text="Miles", font=FONT)
resultLabel = Label(text="0", font=FONT)


calcButton.grid(column=1, row=2)
isEqualLabel.grid(column=0, row=1)
kmLabel.grid(column=2, row=1)
milesEntry.grid(row=0, column=1)
milesLabel.grid(column=2, row=0)
resultLabel.grid(column=1, row=1)


window.mainloop()
