from tkinter import*

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        window.title("test")

        btn1 = Button(window, text="OK", fg="red", command=self.Okbuton)
        btn1.pack()

        btn2 = Button(window, text="Cancel", fg="black", bg="yellow", command=self.Cancelbuton)
        btn2.pack()

        window.mainloop()

    def Okbuton(self):
        print("Ok button is clicked")

    def Cancelbuton(self):
        print("Cancel button is clicked")
