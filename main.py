import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="slate blue")

root = tk.Tk()
root.title("Task list")
root.configure(background="HotPink")

# Заголовок поля ввода задачи
text1 = tk.Label(root, text="Введите вашу задачу:", bg="HotPink")
text1.pack(pady=5)

# Ввод задачи
task_entry = tk.Entry(root, width=30, bg="DeepPink1")
task_entry.pack(pady=10)

# Кнопка "Добавить задачу"
add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

# Кнопка удаления задачи
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

# Кнопка выполненной задачи
mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

# Заголовок списка задач
text2 = tk.Label(root, text="Список задач:", bg="HotPink")
text2.pack(pady=5)

# Список добавленных задач
task_listBox = tk.Listbox(root, height=10, width=50, bg="LightPink1")
task_listBox.pack(pady=10)

root.mainloop()
