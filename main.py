import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task[0])
    else:
        selected_task = completed_listBox.curselection()
        if selected_task:
            completed_listBox.delete(selected_task[0])

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task = task_listBox.get(selected_task)
        task_listBox.delete(selected_task)
        completed_listBox.insert(tk.END, task)

root = tk.Tk()
root.title("Task list")
root.configure(background="chocolate1")
root.geometry("600x600")

# Заголовок поля ввода задачи
text1 = tk.Label(root, text="Введите вашу задачу:", bg="chocolate1")
text1.pack(pady=5)

# Ввод задачи
task_entry = tk.Entry(root, width=80, bg="LightPink1")
task_entry.pack(pady=10)

# Фрейм для кнопок
button_frame = tk.Frame(root, bg="chocolate1")
button_frame.pack(pady=5)

# Кнопка "Добавить задачу"
add_task_button = tk.Button(button_frame, text="Добавить задачу", command=add_task)
add_task_button.pack(side=tk.LEFT, padx=5)

# Кнопка удаления задачи
delete_button = tk.Button(button_frame, text="Удалить задачу", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

# Кнопка выполненной задачи
mark_button = tk.Button(button_frame, text="Выполнено", command=mark_task)
mark_button.pack(side=tk.LEFT, padx=5)

# Заголовок списка актуальных задач
text2 = tk.Label(root, text="Актуальные задачи", bg="chocolate1")
text2.pack(pady=5)

# Список добавленных задач
task_listBox = tk.Listbox(root, height=10, width=80, bg="LightPink1")
task_listBox.pack(pady=10)

# Заголовок списка выполненных задач
text3 = tk.Label(root, text="Выполненные задачи", bg="chocolate1")
text3.pack(pady=5)

# Список выполненных задач
completed_listBox = tk.Listbox(root, height=10, width=80, bg="LightPink1")
completed_listBox.pack(pady=10)

root.mainloop()
