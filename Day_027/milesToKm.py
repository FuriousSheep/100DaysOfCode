import tkinter as tk

MTK_COEFFICIENT = 1.609344

window = tk.Tk()
window.title("Miles to Kilometers")
window.minsize(height=500, width=500)


# CONVERTER FUNCTIONS
def mtk(miles):
    return round(miles * MTK_COEFFICIENT, 3)


def ktm(km):
    return round(km / MTK_COEFFICIENT, 3)


input = tk.Entry(width=20)
output = tk.Label(text="", font=("Arial", 24))
# TODO: Both com functions


def mtk_com():
    miles = int(input.get())
    km = mtk(miles)
    output.config(text=str(km) + " kilometers")


def ktm_com():
    km = int(input.get())
    miles = ktm(km)
    output.config(text=str(miles) + " miles")


# what do we want?
#   label "Type a number"
label = tk.Label(text="Convert this number:", font=("Arial", 24))
label.pack()
#   input
input.pack()
#   button "Miles to Kilometers"
mtk_button = tk.Button(text="From Miles to Kilometers", command=mtk_com)
mtk_button.pack()
#   button "Kilometers to Miles"
ktm_button = tk.Button(text="From Kilometers to Miles", command=ktm_com)
ktm_button.pack()
#   Empty label to display result and unit
output.pack()

window.mainloop()
