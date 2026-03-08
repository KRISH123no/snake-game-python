# Advanced Snake Game

A production-quality Snake game written in Python using pygame, featuring clean OOP design and SOLID principles.

## Features

- **Smooth real-time movement** with configurable game speed
- **Collision detection** with walls and self-collision
- **Score tracking** with persistent high score (saved to highscore.txt)
- **Multiple difficulty levels**: Easy, Medium, Hard (affects snake speed)
- **Pause/Resume** functionality (press P)
- **AI Mode** (press A) - Snake automatically navigates to food using BFS pathfinding
- **Clean grid-based movement** with proper game loop

## Controls

| Key | Action |
|-----|--------|
| Arrow Keys / WASD | Move snake |
| P | Pause/Resume game |
| R | Restart game (after game over) |
| Q | Quit game (after game over) |
| A | Toggle AI mode |
| 1 | Easy difficulty |
| 2 | Medium difficulty |
| 3 | Hard difficulty |

## Project Structure

```
snake_game/
├── main.py           # Entry point
├── game.py           # Main game logic and rendering
├── snake.py          # Snake class with AI pathfinding
├── food.py           # Food class
├── score_manager.py  # Score and highscore management
└── settings.py       # Constants and configuration
```

## Requirements

- Python 3.x
- pygame

## Running the Game

```bash
cd snake_game
python3 main.py
```

## Technical Details

- **Game Loop**: Uses pygame's clock for frame-rate controlled movement
- **AI Algorithm**: Breadth-First Search (BFS) for finding optimal path to food
- **Persistence**: High scores saved to `highscore.txt` in the snake_game directory
- **OOP Design**: Separate classes for Snake, Food, ScoreManager, and Game
