# Import libraries 
import tkinter as tk   #tkinter for gui 
import os
import csv


to_do_list=[]
# to add title 
app = tk.Tk()
app.title("To-Do List Application")

# Create a frame to hold the to-do list items
frame = tk.Frame(app)
frame.pack()

# to add label
label=tk.Label(app, text=("to do list"))
label.pack() 


#add function
def add():
    #to create task id and and assign all things together
    task_id = len(to_do_list) + 1
    task = {"id": task_id, "title": textbox_dis.get("1.0","end-1c"), "description": textbox_task.get("1.0","end-1c"), "completed": False}
    
    # to show the task in task list
    to_do_task.insert(tk.END, str(task_id) + ": " + textbox_dis.get("1.0","end-1c") + " - " + textbox_task.get("1.0","end-1c"))
    
# save the task to txt file
def save():
    task_id = len(to_do_list) + 1
    task = {"id": task_id, 'title': textbox_dis.get("1.0","end-1c"), 'description': textbox_task.get("1.0","end-1c"), 'completed': False}
    to_do_list.append(task)
    file=("task.txt")
    with open((file), "w") as f:
       for task in to_do_list:
        f.write(f"{task['id']},{task['title']},{task['description']},{task['completed']}\n")
    
    # to clear the text box
    textbox_dis.delete("1.0", tk.END)
    textbox_task.delete("1.0", tk.END)

# to delete the task 
def delete():
    # Get the selected task index
    selected_task_index = to_do_task.curselection()[0]

    # Delete the task from the to-do list
    to_do_task.delete(selected_task_index)

def complete():
    # Get the selected task index
    selected_task_index = to_do_task.curselection()[0]

    # Get the task title
    textbox_task = to_do_task.get(selected_task_index)

    # Mark the task as complete
    to_do_task.delete(selected_task_index)
    to_do_task.insert(tk.END, textbox_task + " (Completed)")

# Define the edit function
def edit():
  # Get the selected task index
  selected_task_index = to_do_task.curselection()[0]
  # Get the task object
  task = to_do_list[selected_task_index]
  # Set the text of the textboxes to the task title and description
  textbox_dis.delete("1.0", tk.END)
  textbox_dis.insert("1.0", task["title"])
  textbox_task.delete("1.0", tk.END)
  textbox_task.insert("1.0", task["description"])
  # Delete the task from the to-do list
  to_do_list.delete(selected_task_index)
  # Insert a new task into the to-do list with the edited title and description
  to_do_list.insert(selected_task_index, {"id": task["id"], "title": textbox_dis.get("1.0", tk.END), "description": textbox_task.get("1.0", tk.END), "completed": task["completed"]})
  # Refresh the to-do list
  to_do_list.delete(0, tk.END)
  for task in to_do_list:
    to_do_list.insert(tk.END, str(task["id"]) + " : " + task["title"] + " - " + task["description"])
  
# to add discription of the task
l=tk.Label(text="Enter your task discription here:")
l.pack()
textbox_dis=tk.Text(app, height=3, font=("Areal, 16"))
textbox_dis.pack(padx=20,pady=20)
#to add task
l1=tk.Label(text="Enter your task here:")
l1.pack()
textbox_task=tk.Text(app, height=8, font=("Areal, 16"))
textbox_task.pack(padx=20,pady=20)

#to display the task
to_do_task = tk.Listbox(frame,width=150)
to_do_task.pack()

#button for add delete and save
button_frame=tk.Frame(app)
button_frame.columnconfigure(0,weight=1)
button_frame.columnconfigure(1,weight=1)
button_frame.columnconfigure(2,weight=1)
button_frame.columnconfigure(3,weight=1)
button_frame.columnconfigure(4,weight=1)

#add button
add_button=tk.Button(button_frame, bd=30, bg="green", text="Add  ", font=('Areal',18),command=add)
add_button.grid(row=0,column=0,sticky=tk.W+tk.E)

#delete button
delete_button=tk.Button(button_frame, bd=30, bg="red", text="delete", font=('Areal',18),command=delete)
delete_button.grid(row=0,column=1,sticky=tk.W+tk.E)
#edit button
edit_button = tk.Button(button_frame, bd=30, bg="orange", text="Edit", font=('Areal',18), command=edit)
edit_button.grid(row=0, column=4, sticky=tk.W+tk.E)

#complete button
complete_button=tk.Button(button_frame, bd=30, bg="gray", text="complete",font=('Areal',18),command=complete)
complete_button.grid(row=0,column=2,sticky=tk.W+tk.E) 

#save button
save_button=tk.Button(button_frame, bd=30, bg="blue", text="save",font=('Areal',18),command=save)
save_button.grid(row=0,column=3,sticky=tk.W+tk.E)

button_frame.pack()
app.mainloop()