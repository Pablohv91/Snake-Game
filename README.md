# Snake Game

## Project Overview

This repository contains a classic implementation of the **Snake Game** written in Python using the `turtle` graphics library. It features player‑controlled movement, food generation, collision detection, scoring, and game reset logic. This project highlights fundamental game logic, object‑oriented design, and real‑time user interaction.

## Features

- **Player Controlled Snake:** Move the snake using arrow keys.
- **Random Food Generation:** Food objects appear randomly on the screen.
- **Automatic Growth:** Snake grows in length when it eats food.
- **Score Tracking:** Tracks and displays the current and high score.
- **Collision Detection:** Detects collisions with borders and the snake’s own body.
- **Game Over and Restart:** Resets the game when the snake collides with itself or the boundary.

## Project Structure

- `main.py`: Entry point of the game that runs the game loop and handles game logic.  
- `snake.py`: Defines the `Snake` class, handling snake movement, growth, and collision detection.  
- `food.py`: Defines the `Food` class, responsible for food placement and random positioning on screen.  
- `scoreboard.py`: Defines the `Scoreboard` class, displays and updates the player score.

## Tools and Libraries

- Python 3.x  
- `turtle` — Python standard library for graphics and simple game development  
- Object‑oriented programming principles for modular design

## How to Run

1. Clone the repository.  
2. Open a terminal/command prompt in the project directory.  
3. Run the game:
   ```bash
   python main.py
