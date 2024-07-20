import tkinter as tk
from tkinter import filedialog, messagebox
import os

class TextSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Sorter")

        self.label = tk.Label(root, text="Выберите текстовый файл для сортировки строк по символу окончания")
        self.label.pack(pady=10)

        self.load_button = tk.Button(root, text="Загрузить файл", command=self.load_file)
        self.load_button.pack(pady=5)

        self.sort_button = tk.Button(root, text="Сохранить отсортированный файл", command=self.sort_and_save_file, state=tk.DISABLED)
        self.sort_button.pack(pady=5)

        self.text_data = None
        self.file_path = None

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.text_data = file.readlines()
            messagebox.showinfo("Файл загружен", "Файл успешно загружен!")
            self.sort_button.config(state=tk.NORMAL)

    def sort_lines(self, lines):
        space_lines = [line for line in lines if line.rstrip().endswith(' ')]
        period_lines = [line for line in lines if line.rstrip().endswith('.')]
        exclam_lines = [line for line in lines if line.rstrip().endswith('!')]
        question_lines = [line for line in lines if line.rstrip().endswith('?')]
        other_lines = [line for line in lines if not (line.rstrip().endswith((' ', '.', '!', '?')))]

        return space_lines + period_lines + exclam_lines + question_lines + other_lines

    def sort_and_save_file(self):
        if self.text_data:
            sorted_text = self.sort_lines(self.text_data)
            directory = os.path.dirname(self.file_path)
            save_path = os.path.join(directory, "sorted_text.txt")
            with open(save_path, 'w', encoding='utf-8') as file:
                file.writelines(sorted_text)
            messagebox.showinfo("Файл сохранен", f"Отсортированный файл сохранен как {save_path}")
        else:
            messagebox.showwarning("Ошибка", "Сначала загрузите файл!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextSorterApp(root)
    root.mainloop()
