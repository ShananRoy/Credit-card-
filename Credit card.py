from tkinter import *
root=Tk()
root.title("data-types error")
root.geometry("300x300")
root.configure(background="yellow")

inputbox=Entry(root)
inputbox.place(relx=0.5,rely=0.5,anchor=CENTER)

def check_credit_card():
    
    try:
        getinput=int(inputbox.get())
        messagebox.showinfo("message","credit card accepted")   
    except(ValueError):
                     messagebox.showinfo("Alert","Credit card is not accepted please enter a valid pin code.")
                     
add_btn=Button(root, text = "Check credit card", command=check_credit_card)
add_btn.pack()


 
root.mainloop()