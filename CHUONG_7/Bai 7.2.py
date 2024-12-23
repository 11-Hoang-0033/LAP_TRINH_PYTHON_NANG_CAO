from tkinter import * 

window = Tk() 
window.title("UNETI") 

lbl = Label(window, text="Chào bạn", font=("Arial Bold", 50))

window.geometry('280x80') 

lbl.grid(column=0, row=0) 
window.mainloop()
