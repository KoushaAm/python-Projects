#March 5th, 2021

import tkinter 
import tkinter.messagebox
import pickle 
root = tkinter.Tk()
root.title("To Do")

#label 
heading = tkinter.Label(root , text = "To Do List")
heading.config(font = ("Courier", 30))
heading.pack()


# frame 
frame_task = tkinter.Frame(root)
frame_task.pack()


# scroll bar
scrollbar = tkinter.Scrollbar(frame_task)
scrollbar.pack(side = tkinter.RIGHT,  fill = tkinter.Y)

#create list 
list_box = tkinter.Listbox(frame_task, height = 20, width = 50)
list_box.config(font=("courier", 15))
list_box.pack()

list_box.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = list_box.yview)


def add_task(): 
    task = task_input.get()
    if task != "":
        x = "◍  "  + task
        
        list_box.insert(tkinter.END, x)
        task_input.delete(0, tkinter.END)
    else: 
        tkinter.messagebox.showerror(title = "warning", message = "Empty task!")

def delete_task():
    try : 
        index = list_box.curselection()[0] # selection of the task selected * 0 means one item selected
        list_box.delete(index)
    except: 
        pass



def load_task():
    try : 
        tasks = pickle.load(open("tasks.dat", "rb")) 
        list_box.delete(0, tkinter.END)
        for task in tasks: 
            list_box.insert(tkinter.END, task)
    except: 
        pass

def save_task():
    tasks = list_box.get(0, list_box.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


#Entry Task
task_input = tkinter.Entry(root, width = 50)
task_input.pack()

# add button 
buttAdd = tkinter.Button(root, text = "+", width = 48, command = add_task)
buttAdd.pack()

buttDelete = tkinter.Button(root, text = "Delete task", width = 48, command = delete_task)
buttDelete.pack()

buttLoad = tkinter.Button(root, text = "Load Task", width = 48, command = load_task)
buttLoad.pack()

buttSave = tkinter.Button(root, text = "Save Task", width = 48, command = save_task)
buttSave.pack()


root.mainloop()


