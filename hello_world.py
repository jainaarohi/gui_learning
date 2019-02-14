import tkinter

root = tkinter.Tk()
root.title("Hello World!!!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="white", bg="cadet blue", font=("nunito", "50", "italic"))
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text="Hello there!", fg="light blue", bg="white", font=("Stencil", "50"), padx="20")
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(text="Hello you!", fg="light pink", bg="orange", font=("Times", "50", "bold"), pady="30")
my_label3.grid()

root.mainloop()
