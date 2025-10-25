import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

# List of sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a useful skill for programmers and writers.",
    "Artificial intelligence continues to evolve rapidly.",
    "Machine learning helps computers identify patterns in data.",
    "Consistency is key when improving typing speed."
]

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        self.time_limit = 60  # seconds for the countdown
        self.time_left = self.time_limit
        self.running = False
        self.start_time = None
        
        self.setup_ui()

    def setup_ui(self):
        self.label_title = tk.Label(self.root, text="Typing Speed Test", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=10)

        self.text_display = tk.Text(self.root, height=5, width=60, wrap="word", font=("Consolas", 12))
        self.text_display.pack(pady=10)
        self.text_display.config(state="disabled")  # Make non-editable

        self.entry = tk.Text(self.root, height=5, width=60, wrap="word", font=("Consolas", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_typing)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=500, mode="determinate", maximum=self.time_limit)
        self.progress.pack(pady=10)
        self.progress["value"] = 0

        self.timer_label = tk.Label(self.root, text=f"Time Left: {self.time_limit}s", font=("Arial", 14))
        self.timer_label.pack()

        self.start_button = tk.Button(self.root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def start_test(self):
        self.running = True
        self.time_left = self.time_limit
        self.progress["value"] = 0
        self.result_label.config(text="")
        self.start_button.config(state="disabled")
        self.start_time = None

        # Choose random sentence
        self.test_text = random.choice(sentences)
        self.text_display.config(state="normal")
        self.text_display.delete("1.0", tk.END)
        self.text_display.insert(tk.END, self.test_text)
        self.text_display.config(state="disabled")

        self.entry.delete("1.0", tk.END)
        self.entry.focus_set()

        self.update_timer()

    def start_typing(self, event):
        if self.running and self.start_time is None:
            self.start_time = time.time()

    def update_timer(self):
        if self.time_left > 0 and self.running:
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.progress["value"] = self.time_limit - self.time_left
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.running:
            self.finish_test()

    def finish_test(self):
        self.running = False
        typed_text = self.entry.get("1.0", tk.END).strip()
        self.start_button.config(state="normal")

        if self.start_time:
            elapsed_time = min(time.time() - self.start_time, self.time_limit)
        else:
            elapsed_time = self.time_limit

        words = len(typed_text.split())
        wpm = words / (elapsed_time / 60) if elapsed_time > 0 else 0

        correct_chars = sum(1 for a, b in zip(self.test_text, typed_text) if a == b)
        accuracy = (correct_chars / len(self.test_text)) * 100 if self.test_text else 0

        self.result_label.config(
            text=f"Speed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%"
        )
        messagebox.showinfo(
            "Test Over",
            f"Time’s up!\nYour speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
