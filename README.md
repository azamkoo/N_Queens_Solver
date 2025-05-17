# N_Queens_Solver

## Project Overview
The N-Queens problem is a classic puzzle in artificial intelligence and algorithms, where the goal is to place N queens on an N×N chessboard so that no two queens threaten each other.  
This project provides two algorithms to solve the N-Queens problem:  
- Exact **Backtracking** algorithm to find all possible solutions  
- Approximate **Genetic Algorithm**  

Additionally, a graphical user interface (GUI) built with `Tkinter` allows users to visualize solutions interactively.

## Features
- Solve the N-Queens problem for any N between 1 and 20  
- Choose between Backtracking or Genetic Algorithm through the GUI  
- Graphical display of solutions showing queen placements on the chessboard  
- Navigate through multiple solutions using "Previous Solution" and "Next Solution" buttons 

## Limitations

- Backtracking may become very slow for N > 15 due to exponential complexity.  
- Genetic algorithm does not guarantee finding all solutions, and quality depends on parameters like population size and generations.

---

## Requirements
- Python 3.6 or higher  
- Tkinter library (usually included by default with Python)  

## How to Run

1. Install Python 3.6 or above.  
2. Run the GUI application with:  
   `python main_gui.py`  
3. Enter the size of the board (N), select the algorithm, and click Solve.  
4. Use navigation buttons to explore multiple solutions.

---