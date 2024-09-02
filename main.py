import random
import string
import tkinter as tk
from time import time
import statistics

# Функция для генерации пароля
def generate_password(length, alphabet):
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

# Функция для измерения времени ввода пароля
def measure_typing_time():
    typing_times = []  # Список для хранения времени ввода

    for _ in range(5):  # Ввод пароля n раз
        password = generate_password(password_length, alphabet)
        password_label.config(text="Сгенерированный пароль: " + password)

        start_time = time()

        # Блокируем кнопку для избежания повторного измерения
        start_button.config(state=tk.DISABLED)

        def check_password(event):
            user_input = input_entry.get()
            nonlocal start_time
            if user_input == password:
                end_time = time()
                typing_time = end_time - start_time
                typing_times.append(typing_time)
                result_label.config(text=f"Время ввода пароля: {typing_time:.2f} секунд")
                # Сбрасываем поле ввода
                input_entry.delete(0, tk.END)
                input_entry.focus()
                start_time = time()

            if len(typing_times) == 5:  # После n попыток расчет матожидания и дисперсии
                # Рассчитываем математическое ожидание и дисперсию
                mean_time = statistics.mean(typing_times)
                variance_time = statistics.variance(typing_times)
                mean_var_label.config(
                    text=f"Математическое ожидание: {mean_time:.2f} секунд\nДисперсия: {variance_time:.2f}")
                # Разблокируем кнопку
                start_button.config(state=tk.NORMAL)

        input_label.config(text="Введите пароль:")
        input_entry.config(state=tk.NORMAL)
        input_entry.delete(0, tk.END)
        input_entry.bind("<Return>", check_password)
        input_entry.focus()



# Интерфейс
root = tk.Tk()
root.geometry('400x300+500+200')
root.title("Генератор паролей и измерение времени ввода")

password_length = 8  # Длина пароля
alphabet = string.ascii_letters + string.digits

password_label = tk.Label(root, text="")
password_label.pack()

input_label = tk.Label(root, text="")
input_label.pack()

input_entry = tk.Entry(root, state=tk.DISABLED)
input_entry.pack()

start_button = tk.Button(root, text="Сгенерировать пароль и измерить время ввода", command=measure_typing_time)
start_button.pack()

typing_times = []  # Список для хранения времени ввода

result_label = tk.Label(root, text="")
result_label.pack()

mean_var_label = tk.Label(root, text="")
mean_var_label.pack()

root.mainloop()
