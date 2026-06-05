# Tic-Tac-Toe Minimax AI

A robust, terminal-based Tic-Tac-Toe game featuring an intelligent AI powered by the **Minimax algorithm**. This project demonstrates core concepts in game theory, decision-making agents, and recursive state-space searching.

## 🎮 Features
* **Human vs. AI Mode:** Challenge an optimal AI that never makes a mistake.
* **AI vs. AI Mode:** Watch two optimal agents compete against each other to force a draw.
* **Minimax Implementation:** Uses recursive evaluation to calculate the "perfect" move for any given board state.
* **State Simulation:** Uses deep-copying techniques (`[r[:] for r in board]`) to explore future game states without corrupting the current board.

## 🧠 How It Works
The core of this project is the **Minimax algorithm**, a decision-making strategy for two-player, zero-sum games. 
* The **Maximizer ('X')** attempts to achieve the highest possible utility.
* The **Minimizer ('O')** attempts to achieve the lowest possible utility.
* The algorithm traverses the game tree recursively to the terminal nodes (win/loss/draw), then propagates these values back up to determine the most optimal move.

## 🚀 How to Run
1. **Clone the repository:**
Bash
```
   git clone https://github.com/TheNormalCoderr/tic-tac-toe-minimax.git
```
2. **Navigate to the directory:**
Bash
```
   cd tic-tac-toe-minimax
```
4. **Execute the game:**
Bash
```
   python tic_tac_toe.py
```

## 🛠️ Project Structure
* **tic_tac_toe.py:** Contains the game logic, Minimax functions, and board management.
* **Utility():** Evaluates the current board state and returns the score (+1 for win, -1 for loss).
* **Max_value() / Min_value():** Recursive functions that implement the Minimax strategy.
* **Terminal():** Determines if the game has reached a win, loss, or draw condition.
* **Actions():** To return a list of all the possible moves at current state
* **Result():** To perform an action to the state  

## 📈 Future Improvements
* **Depth Limiting:** Add a difficulty setting by restricting how many turns the AI can look ahead.
* **GUI Integration:** Replace the terminal interface with a graphical board using pygame or tkinter.

Created by Amiteshwar Singh
