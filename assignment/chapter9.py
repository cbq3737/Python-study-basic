#############################################frame씌우는것#############
# from tkinter import *
# #라디오버튼에서  같은 변수로써 사용한건 value로 분류를 하고 하나가 선택되면 하나가 꺼지기위해서 하지만 체크버튼은 아예 변수를 두개 만드는방법을 써야할듯
# class Widget:
#     def __init__(self):
#         window = Tk()
#         window.title("frame")
#
#         frame1 = Frame(window)
#         frame1.pack()
#         self.v1 = IntVar()
#         checkbutton = Checkbutton(frame1,text="Bold",variable = self.v1,command =self.ProcessCheck)
#         checkbutton.grid(row = 0, column = 0)
#
#         self.v2 = IntVar()
#         radiobutton = Radiobutton(frame1,text="Red",variable = self.v2,value =1, bg="red",command =self.processRadio)
#         radiobutton.grid(row =0,column=1)
#
#         radiobutton2 = Radiobutton(frame1,text="Yellow",variable = self.v2,value =2,bg="yellow",command=self.processRadio)
#         radiobutton2.grid(row=0, column=2)
#
# #####################################################여기까지가 frame1##
#         frame2 = Frame(window)
#         frame2.pack()
#
#         label = Label(frame2,text="Enter Your name: ")
#         label.grid(row=1,column=0)
#
#         self.name = StringVar()
#         entry = Entry(frame2,textvariable = self.name)
#         entry.grid(row= 1, column=1)
#
#         btn = Button(frame2,text="Get Name",command =self.processButton)
#         btn.grid(row=1,column=2)
#
#         message = Message(frame2,text="It is a widgets demo")
#         message.grid(row=1,column=3)
#
#         text= Text(window)
#         text.pack()
#         text.insert(END,"Tip\nThe best way yo learn Tkinter is to read")
#         text.insert(END, "these carefully designed examples and use them ")
#         text.insert(END, "to create your applications")
#
#         window.mainloop()
#
#
#     def ProcessCheck(self):
#         print("check button is","checkd" if self.v1.get() ==1 else "unchecked")
#
#     def processRadio(self):
#         print("Red" if self.v2.get() ==1 else "Yellow","is selected")
#
#     def processButton(self):
#         print("Your name is",self.name.get())
#
# Widget()


###################################클래스를 통해서 불러올시#######
# from ProcessButton import *
#
# ProcessButtonEvent()
#########################################1번################################
#######################https://blog.naver.com/huntingbear21/221217087410 계산기#######
###########################################################################사전에 글 찾는것.
# from tkinter import *
#
# window = Tk()
# window.title("my glossary")
#
# def click():
#     entry1_text = entry1.get()
#     output.delete(0.0,END)
#     try:
#         definition = myglo[entry1_text]
#     except:
#         definition = "There is o entry for this word"
#     output.insert(END,definition)
#
# label1 = Label(window,text="Enter the word you want defining")
# label1.grid(row =0,column=0,sticky=W)
#
# entry1 = Entry(window,bg="lightgreen",width = 20)
# entry1.grid(row=1,column =0,sticky=W)
#
# button = Button(window,text="SUBMIT",command= click,width=5)
# button.grid(row =2 ,column=0,sticky=W)
#
# label2 = Label(window,text="\nDefinition")
# label2.grid(row =3,column=0,sticky=W)
#
# output = Text(window,bg="lightgreen",width=30,height= 5,wrap=WORD)
# output.grid(row=4,column=0,columnspan=2)
#
# myglo ={     #dict사전
#
#     '1':"One",
#     '2':"Two",
#     '3':"Three",
#     '4':"Four",
#     '5':"Five"
# }
#
# window.mainloop()
############################################################################메뉴만들기##
# from tkinter import *
# window1 = Tk()
# window1.title("Drop Down")
#
# def newFile():
#     print("This is new File")
# def openFile():
#     print("This is open File")
# def openModule():
#     print("This is open Module")
#
# mainMenu11 = Menu(window1)
# window1.configure(menu = mainMenu11)
#
# subMenu= Menu(mainMenu11)
# mainMenu11.add_cascade(label = "File",menu = subMenu)
#
# subMenu.add_command(label="New File", command=newFile)
# subMenu.add_command(label="open File", command=openFile)
# subMenu.add_separator()
#
# subMenu11 = Menu(subMenu)
# subMenu.add_cascade(label="another",menu =subMenu11)
# subMenu11.add_command(label="another one")
#
# subMenu.add_command(label="open Module", command=openModule)
#
#
# window1.mainloop()

########################################################################버튼눌렀을때 이벤트
# from tkinter import *
#
# class ProcessButtonEvent:
#     def __init__(self):
#         window = Tk()
#         btOk = Button(window,text="ok",fg="blue",command=self.processOK)  #command로 함수부를때 ()표시 x
#         btcancel = Button(window,text="Cancel",bg="yellow",command=self.processCancel)
#
#         btOk.pack()
#         btcancel.pack()
#
#         window.mainloop()
#
#     def processOK(self):
#         print("OK button is clicked")
#
#     def processCancel(self):
#         print("Cancel button is clicked")
#
# ProcessButtonEvent()
###################################################################
# from tkinter import *
#
# def processOK():
#     print("OK button is clicked")
#
# def processCancel():
#     print("Cancel button is clicked")
#
# window = Tk()
# btOk = Button(window,text="ok",fg="blue",command=processOK)  #command로 함수부를때 ()표시 x
# btcancel = Button(window,text="Cancel",bg="yellow",command=processCancel)
#
# btOk.pack()
# btcancel.pack()
#
# window.mainloop()
#########################################################
# from tkinter import *
# window = Tk()
#
# label = Label(window,text ="Welcome to Python")
# button = Button(window,text = "Click me")
# label.pack() #띄우겠다.
# button.pack()
#
# window.mainloop() #이벤트 루프를 생성
