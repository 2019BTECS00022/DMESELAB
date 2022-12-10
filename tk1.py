from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import ttk

Assign1_root =  Tk()

#width x height
Assign1_root.geometry("980x1020")
Assign1_root.minsize(650,720)
Assign1_root['bg'] = 'cyan'
photo = PhotoImage(file ="wce1.png ")
p_label = Label(image= photo)
p_label.pack()
S1 = Label(text ="This is Assignment 5 and I am PRN 2019BTECS00022 ")
S1.pack()


menubar= Menu(Assign1_root)
menu_f= Menu(menubar,tearoff=0)
menu_ct= Menu(menubar,tearoff=0)
menu_disp= Menu(menubar,tearoff=0)
menu_display= Menu(menubar,tearoff=0)


menubar.add_cascade(label='Upload file',menu=menu_f)
trv=ttk.Treeview(Assign1_root,selectmode= 'browse')
trv = ttk.Treeview(Assign1_root, columns=10, show='headings', height=15)
#trv.grid(row=1,column=2,columnspan=3,padx=50,pady=50)
trv['show'] = 'tree'
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
menu_f.add_command(label='new',command=lambda:upload_file())



frame = Frame(Assign1_root, borderwidth=6, bg="blue", relief = SUNKEN)
frame.pack(side= LEFT, anchor= "nw")

b1 = Button(frame, fg= "Black", text="Insert dataset")
b1.pack(side=LEFT)
b2 = Button(frame, fg= "Black", text="KNN")
b2.pack(side=LEFT)
b3 = Button(frame, fg= "Black", text="K-mean")
b3.pack(side=LEFT)
b4 = Button(frame, fg= "Black", text="ANN")
b4.pack(side=LEFT)


Assign1_root.mainloop()
