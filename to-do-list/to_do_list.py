from tkinter import*
from PIL import ImageTk,Image
window = Tk()
window.title("To-do-list")
label = Label(window,text="Welcome to my to-do-list app",font=("Arial Bold",50)).pack(ipadx=50)
img=Image.open("to-do-list.jpg")
img_resize=img.resize((100,60))
img1=ImageTk.PhotoImage(img_resize)
img_label=Label(image=img1)
img_label.pack(ipadx=300)
label1=Label(window,text="Task:").pack(ipadx=50)
task=Entry(window,width=50)
# task.insert(0,"Enter the task")
task.pack()
label2=Label(window,text="Time:").pack(ipadx=50)
time=Entry(window,width=50)
time.pack()
label3=Label(window,text="Priority Number:").pack(ipadx=50)
priority=Entry(window,width=50)
priority.pack()

def clicked():
    listbox_widget=Listbox(window,height = 10, 
                  width = 15, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")
    task_list=task.get()+" "+time.get()
    listbox_widget.insert(0,task_list)
    listbox_widget.pack()

    # if priority.get()=='1':
    #     p_message="Priority and Important"
    # elif priority.get()=='2':
    #     p_message="Priority and  Not Important"
    # elif priority.get()=='3':
    #     p_message="Not a Priority but Important"
    # else:
    #     p_message="Not a Priority Not Important"
    # task_list=LabelFrame(window,text=task.get()+" "+time.get()+" "+p_message)
    # task_list.pack()
    
bt = Button(window,text="Add",bg="red",fg="white",font=("Arial Bold",20),command=clicked).pack()
#bt.grid(column=1,row=0)
#window.geometry('600x400')
window.mainloop()