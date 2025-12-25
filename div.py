import tkinter as tk
import tkinter.messagebox as messagebox
import random
import time

class DivmodGameGUI:
    def __init__(self, master, lives=5):
        self.master = master
        self.lives = lives
        self.score = 0
        self.round_num = 0
        self.start_time = time.time()
        self.a = None
        self.b = None
        self.correct_quot = None
        self.correct_rem = None

        master.title("Divmod Game")
        master.configure(bg="#23272f")
        self.frame = tk.Frame(master, bg="#23272f", bd=0, highlightthickness=0)
        self.frame.pack(padx=64, pady=64)  # More padding for spaciousness

        self.info_label = tk.Label(
            self.frame,
            text="🧮 Divmod Game",
            bg="#23272f",
            fg="#f8f8f2",
            font=("Segoe UI", 36, "bold"),
            justify="center",
            bd=0,
            highlightthickness=0
        )
        self.info_label.pack(pady=(0, 16))

        self.desc_label = tk.Label(
            self.frame,
            text="Find the quotient and remainder for two-digit numbers.",
            bg="#23272f",
            fg="#8be9fd",
            font=("Segoe UI", 22, "italic"),
            justify="center",
            bd=0,
            highlightthickness=0
        )
        self.desc_label.pack(pady=(0, 32))

        stats_frame = tk.Frame(self.frame, bg="#23272f")
        stats_frame.pack(pady=(0, 24))

        self.lives_label = tk.Label(stats_frame, text="", bg="#23272f", fg="#ff5555", font=("Segoe UI", 22, "bold"), bd=0, highlightthickness=0)
        self.lives_label.grid(row=0, column=0, padx=24)

        self.round_label = tk.Label(stats_frame, text="", bg="#23272f", fg="#8be9fd", font=("Segoe UI", 22, "bold"), bd=0, highlightthickness=0)
        self.round_label.grid(row=0, column=1, padx=24)

        self.time_stats_label = tk.Label(
            stats_frame,
            text="Total time: 0.00s | Avg per question: 0.00s",
            bg="#23272f",
            fg="#50fa7b",
            font=("Segoe UI", 20, "italic"),
            bd=0,
            highlightthickness=0
        )
        self.time_stats_label.grid(row=0, column=2, padx=24)

        self.question_label = tk.Label(self.frame, text="", bg="#23272f", fg="#f1fa8c", font=("Segoe UI", 28, "bold"), bd=0, highlightthickness=0)
        self.question_label.pack(pady=(0, 32))

        entry_style = {
            "bg": "#282a36",
            "fg": "#f8f8f2",
            "insertbackground": "#f8f8f2",
            "font": ("Segoe UI", 24),
            "width": 16,
            "justify": "center",
            "relief": "flat",
            "highlightthickness": 0,
            "bd": 0
        }

        input_frame = tk.Frame(self.frame, bg="#23272f")
        input_frame.pack(pady=(0, 24))

        self.quot_label = tk.Label(input_frame, text="Quotient:", bg="#23272f", fg="#bd93f9", font=("Segoe UI", 22, "bold"), bd=0, highlightthickness=0)
        self.quot_label.grid(row=0, column=0, padx=(0, 16))
        self.quot_entry = tk.Entry(input_frame, **entry_style)
        self.quot_entry.grid(row=0, column=1, padx=(0, 32))

        self.rem_label = tk.Label(input_frame, text="Remainder:", bg="#23272f", fg="#bd93f9", font=("Segoe UI", 22, "bold"), bd=0, highlightthickness=0)
        self.rem_label.grid(row=0, column=2, padx=(0, 16))
        self.rem_entry = tk.Entry(input_frame, **entry_style)
        self.rem_entry.grid(row=0, column=3)

        btn_style = {
            "bg": "#44475a",
            "fg": "#f8f8f2",
            "activebackground": "#6272a4",
            "activeforeground": "#f8f8f2",
            "font": ("Segoe UI", 18, "bold"),
            "width": 20,
            "height": 2,
            "relief": "flat",
            "bd": 0,
            "highlightthickness": 0
        }

        btn_frame = tk.Frame(self.frame, bg="#23272f")
        btn_frame.pack(pady=(0, 24))

        self.submit_btn = tk.Button(
            btn_frame, text="Submit", command=self.check_answer, **btn_style
        )
        self.submit_btn.grid(row=0, column=0, padx=16)

        self.next_btn = tk.Button(
            btn_frame, text="Next Round", command=self.next_round, state=tk.DISABLED, **btn_style
        )
        self.next_btn.grid(row=0, column=1, padx=16)

        self.quit_btn = tk.Button(
            btn_frame, text="Quit", command=self.quit_game, **btn_style
        )
        self.quit_btn.grid(row=0, column=2, padx=16)

        self.feedback_label = tk.Label(self.frame, text="", bg="#23272f", fg="#ffb86c", font=("Segoe UI", 22, "italic"), bd=0, highlightthickness=0)
        self.feedback_label.pack(pady=(24, 0))

        self.start_round()

    def start_round(self):
        self.a = random.randint(10, 99)
        self.b = random.randint(2, 10)
        self.correct_quot, self.correct_rem = divmod(self.a, self.b)
        self.round_label.config(text=f"Round {self.round_num + 1}")
        self.lives_label.config(text=f"Lives: {self.lives}")
        self.question_label.config(text=f"What is div({self.a}, {self.b})?")
        self.feedback_label.config(text="")
        self.quot_entry.delete(0, tk.END)
        self.rem_entry.delete(0, tk.END)
        self.submit_btn.config(state=tk.NORMAL)
        self.next_btn.config(state=tk.DISABLED)
        self.quot_entry.config(state=tk.NORMAL)
        self.rem_entry.config(state=tk.NORMAL)
        self.quot_entry.focus_set()
        self.update_time_stats()

    def check_answer(self):
        quot_text = self.quot_entry.get().strip()
        rem_text = self.rem_entry.get().strip()
        if not quot_text or not rem_text:
            self.feedback_label.config(text="Please enter both quotient and remainder.")
            return
        try:
            user_quot = int(quot_text)
            user_rem = int(rem_text)
            if user_quot < 0 or user_rem < 0:
                self.feedback_label.config(text="Please enter non-negative numbers.")
                return
        except ValueError:
            self.feedback_label.config(text="Invalid input! Enter integers only.")
            return

        if user_quot == self.correct_quot and user_rem == self.correct_rem:
            self.feedback_label.config(text="✅ Correct!")
            self.score += 1
            if not hasattr(self, 'score_window') or not self.score_window.winfo_exists():
                self.score_window = tk.Toplevel(self.master)
                self.score_window.title("Score")
                self.score_window.configure(bg="#091836")
                self.score_label = tk.Label(
                    self.score_window,
                    text=f"Score: {self.score}",
                    bg="#23272f",
                    fg="#50fa7b",
                    font=("Segoe UI", 32, "bold"),
                    bd=0,
                    highlightthickness=0
                )
                self.score_label.pack(padx=48, pady=48)
                self.score_window.resizable(False, False)
            else:
                self.score_label.config(text=f"Score: {self.score}")
            self.submit_btn.config(state=tk.DISABLED)
            self.next_btn.config(state=tk.NORMAL)
            self.quot_entry.config(state=tk.DISABLED)
            self.rem_entry.config(state=tk.DISABLED)
        else:
            self.lives -= 1
            self.lives_label.config(text=f"Lives: {self.lives}")
            if self.lives > 0:
                self.feedback_label.config(text=f"❌ Wrong! Try again. Lives left: {self.lives}")
                self.submit_btn.config(state=tk.NORMAL)
                self.next_btn.config(state=tk.DISABLED)
                self.quot_entry.config(state=tk.NORMAL)
                self.rem_entry.config(state=tk.NORMAL)
            else:
                self.feedback_label.config(
                    text=f"No more lives! The correct answer was ({self.correct_quot}, {self.correct_rem})."
                )
                self.submit_btn.config(state=tk.DISABLED)
                self.next_btn.config(state=tk.DISABLED)
                self.quot_entry.config(state=tk.DISABLED)
                self.rem_entry.config(state=tk.DISABLED)
                self.end_game()
        self.update_time_stats()

    def next_round(self):
        self.quot_entry.delete(0, tk.END)
        self.rem_entry.delete(0, tk.END)
        self.quot_entry.config(state=tk.NORMAL)
        self.rem_entry.config(state=tk.NORMAL)
        self.quot_entry.focus_set()
        self.round_num += 1
        self.start_round()

    def quit_game(self):
        self.submit_btn.config(state=tk.DISABLED)
        self.next_btn.config(state=tk.DISABLED)
        self.quot_entry.config(state=tk.DISABLED)
        self.rem_entry.config(state=tk.DISABLED)
        self.end_game()

    def end_game(self):
        elapsed = time.time() - self.start_time
        avg_time = elapsed / max(1, self.round_num)
        messagebox.showinfo(
            "Game Over",
            f"🎉 Well played!\n"
            f"Score: {self.score} rounds correct\n"
            f"Total time taken: {elapsed:.2f} seconds\n"
            f"Average time per question: {avg_time:.2f} seconds"
        )
        self.master.destroy()

    def update_time_stats(self):
        elapsed = time.time() - self.start_time
        avg_time = elapsed / max(1, self.round_num + 1)
        self.time_stats_label.config(
            text=f"Total time: {elapsed:.2f}s | Avg per question: {avg_time:.2f}s"
        )

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = DivmodGameGUI(root)
    root.mainloop()