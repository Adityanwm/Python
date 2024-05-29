import tkinter as tk
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess The Number")
        self.master.geometry("300x150")

        self.secret_number = random.randint(1, 100)
        self.remaining_attempts = 5

        self.label = tk.Label(master, text="Guess the number (1-100):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.remaining_attempts_label = tk.Label(master, text=f"Attempts remaining: {self.remaining_attempts}")
        self.remaining_attempts_label.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        if guess == self.secret_number:
            self.result_label.config(text="Congratulations! You guessed the number!")
            self.guess_button.config(state=tk.DISABLED)
        else:
            self.remaining_attempts -= 1
            self.remaining_attempts_label.config(text=f"Attempts remaining: {self.remaining_attempts}")
            if self.remaining_attempts == 0:
                self.result_label.config(text=f"Sorry, you're out of attempts. The number was {self.secret_number}.")
                self.guess_button.config(state=tk.DISABLED)
            elif guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            else:
                self.result_label.config(text="Too high! Try again.")

def main():
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
