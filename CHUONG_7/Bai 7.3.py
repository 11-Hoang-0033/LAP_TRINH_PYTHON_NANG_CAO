from tkinter import *

def change_font():
    current_weight = lbl.cget("font")[-1]
    
    new_weight = "bold" if current_weight != "bold" else "normal"

    lbl.configure(font=("Arial", 50, new_weight))

window = Tk()
window.title("KHUD UNETI")

lbl = Label(window, text="Chào bạn", font=("Arial", 50, "bold"))
lbl.grid(column=0, row=0)

btn_change_font = Button(window, text="Đổi font", command=change_font)
btn_change_font.grid(column=0, row=1)

window.geometry('280x120')
window.mainloop()
