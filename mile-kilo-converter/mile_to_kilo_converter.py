from tkinter import *

window = Tk()
window.title("Miles to kilometer Converter")
window.config(padx=20, pady=20)


def mileToKm():
    miles = float(input_bar.get())
    km = miles * 1.609
    kilo_result_label.config(text=f"{km}")

#label droit
right_label = Label(text="is equal to ")
right_label.grid(column=0, row=1)

#input user petites taille
input_bar = Entry(width=7)
input_bar.grid(column=2, row=0)

#label resultat de calcule
kilo_result_label = Label(text="0")
kilo_result_label.grid(column=2, row=1)

#label miles
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

#label km
km_label = Label(text="Km")
km_label.grid(column=3, row=1)

#bouton calculate
calculate_button = Button(text="Calculate", command=mileToKm)
calculate_button.grid(column=2, row=3)

window.mainloop()