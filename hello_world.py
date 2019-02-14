import tkinter
root = tkinter.Tk()

root.title("Hello World!!!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="green")
my_label.grid()

my_label2 = tkinter.Label(root)
my_label2.config(text="Hello there!", fg="blue")
my_label2.grid()

my_label3 = tkinter.Label(root)
my_label3.config(text="Hello you!", fg="pink")
my_label3.grid()

root.mainloop()
