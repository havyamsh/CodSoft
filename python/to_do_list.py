import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
import os
import json
import threading
import time
try:
    from playsound import playsound
except ImportError:
    playsound = None
    
tasks=[]
TASK_FILE = "tasks.json"
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,'r')as f:
            data = json.load(f)
            tasks.extend(data)
            refresh_list()
            
            
            

def save_tasks():
    with open(TASK_FILE,'w') as f:
        json.dump(tasks, f)
        
def refresh_list():
    listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        reminder = f" [remind at{task['reminder']}]" if task["reminder"] else ""
        listbox.insert(tk.END, f"{idx+1},{task['text']}{status}{reminder}")
        
def add_task():
    task_text = entry.get()
    if task_text:
        reminder = simpledialog.askstring("Reminder (optional)", "Enter time(HH:MM 24hr format):", parent=root)
        task = {"text": task_text,"done":False,"reminder": reminder}
        tasks.append(task)
        refresh_list()
        entry.delete(0,tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error","Enter a task.")
        
def delete_task():
    selection = listbox.curselection()
    if selection:
        tasks.pop(selection[0])
        refresh_list()
        save_tasks()
    else:
        messagebox.showwarning("Selection Error", "Select a task to delete.")
        
        
def update_task():
    selection=listbox.curselection()
    if selection:
        idx=selection[0]
        new_text=simpledialog.askstring("Update Task","Enter a new task text :")
        if new_text:
            tasks[idx]["text"]=new_text
            refresh_list()
            save_tasks()
            
            
def toggle_status():
    selection = listbox.curselection()
    if selection:
        idx=selection[0]
        tasks[idx]["done"]=not tasks[idx]["done"]
        refresh_list()
        save_tasks()
        
        
def check_reminders():
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for task in tasks:
            if task["reminder"] == now:
                root.after(0,lambda t=task: show_reminder(t["task"]))
                task["reminder"]=None
                save_tasks()
            time.sleep(60)
            
            
def show_reminder(task_text):
    messagebox.showinfo("Reminder",f"Reminder for task:{task_text}")
    if playsound:
        try:
            playsound("alarm.wav")
        except:
            pass
        
#GUI setup
root=tk.Tk()
root.title("To-Do List")
root.geometry("500x500")

entry = tk.Entry(root,width=40,font=("Arial",12))
entry.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Add Task",width=12,command=add_task).grid(row=0,column=0)
tk.Button(frame, text="Delete Task",width=12,command=delete_task).grid(row=0,column=1)
tk.Button(frame, text="Update Task",width=12,command=update_task).grid(row=0,column=2)
tk.Button(frame, text="Mark Task",width=12,command=toggle_status).grid(row=0,column=3)

listbox = tk.Listbox(root, width=70,height=15,font=("courier New",11))
listbox.pack(pady=10)

load_tasks()
threading.Thread(target=check_reminders,daemon=True).start()

root.mainloop()