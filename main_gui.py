import tkinter as tk
from tkinter import messagebox
from backtracking import solve_n_queens
from genetic import solve_n_queens_genetic

CELL_SIZE = 50  # اندازه هر خانه

class NQueensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("N-Queens Solver")

        # انتخاب الگوریتم
        self.algo_var = tk.StringVar(value="backtracking")
        tk.Label(root, text="Select Algorithm:").pack()

        tk.Radiobutton(root, text="Backtracking", variable=self.algo_var, value="backtracking").pack()
        tk.Radiobutton(root, text="Genetic Algorithm", variable=self.algo_var, value="genetic").pack()

        self.n_label = tk.Label(root, text="Enter N:")
        self.n_label.pack()

        self.n_entry = tk.Entry(root)
        self.n_entry.pack()

        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.pack()

        self.prev_button = tk.Button(root, text="Previous Solution", command=self.prev_solution, state=tk.DISABLED)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.next_button = tk.Button(root, text="Next Solution", command=self.next_solution, state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.solutions = []
        self.current_index = 0

    def solve(self):
        try:
            n = int(self.n_entry.get())
            if n < 1 or n > 20:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 20.")
            return

        self.canvas.delete("all")

        # انتخاب الگوریتم بر اساس ورودی کاربر
        if self.algo_var.get() == "backtracking":
            self.solutions = solve_n_queens(n)
        else:
            self.solutions = solve_n_queens_genetic(n)

        if not self.solutions:
            messagebox.showinfo("No Solution", f"No solutions found for N = {n}")
            self.prev_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)
            return

        self.current_index = 0
        self.draw_board(self.solutions[self.current_index])
        self.update_buttons()
        
    def draw_board(self, solution):
        n = len(solution)
        cell_size = CELL_SIZE
        self.canvas.config(width=n * cell_size, height=n * cell_size)

        for i in range(n):
            for j in range(n):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                fill_color = "white" if (i + j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

                if solution[i][j] == "Q":
                    self.canvas.create_text(
                        x1 + cell_size / 2,
                        y1 + cell_size / 2,
                        text="♛",
                        font=("Arial", int(cell_size / 2)),
                        fill="red"
                    )
    
    def update_buttons(self):
        if len(self.solutions) <= 1:
            self.prev_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)
        else:
            self.prev_button.config(state=tk.NORMAL if self.current_index > 0 else tk.DISABLED)
            self.next_button.config(state=tk.NORMAL if self.current_index < len(self.solutions) - 1 else tk.DISABLED)
    
    def prev_solution(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.draw_board(self.solutions[self.current_index])
            self.update_buttons()
    
    def next_solution(self):
        if self.current_index < len(self.solutions) - 1:
            self.current_index += 1
            self.draw_board(self.solutions[self.current_index])
            self.update_buttons()

if __name__ == "__main__":
    root = tk.Tk()
    app = NQueensGUI(root)
    root.mainloop()
