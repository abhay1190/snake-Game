# Food Game

A Python turtle graphics project featuring a Food class that creates randomly positioned food items.

## Description

This project contains a `Food` class that inherits from Python's `Turtle` class. The food appears as a blue circle that randomly repositions itself on the screen when refreshed.

## Features

- Food item represented as a blue circle
- Random positioning within screen boundaries (-280 to 280 pixels)
- Built using Python's turtle graphics library

## Requirements

- Python 3.x
- turtle module (included with Python standard library)

## Usage

```python
from food import Food

# Create a food instance
food = Food()

# Refresh food position
food.refresh()
```

## Project Structure

```
snake-game/
├── README.md              # Project documentation
├── main.py.py            # Main game entry point
├── snake.py              # Snake class implementation
├── food.py               # Food class implementation
├── score_card.py         # ScoreCard class for score management
├── data.txt              # High score data storage
```

### File Descriptions

- **`main.py.py`** - Main entry point to run the Snake game
- **`snake.py`** - Contains the Snake class that manages snake movement, growth, and collision detection
- **`food.py`** - Contains the Food class that creates randomly positioned food items
- **`score_card.py`** - Contains the ScoreCard class for displaying and managing scores
- **`data.txt`** - Stores the high score data persistently
- **`README.md`** - This documentation file
- **`.gitignore`** - Specifies files and folders to ignore in version control

## Installation and Setup

### Prerequisites
- Python 3.x installed on your system
- Git installed on your system

### Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Verify Python installation**
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

3. **Run the project**
   ```bash
   python main.py
   ```
   or
   ```bash
   python3 main.py
   ```

### Usage in Your Own Project

```python
from food import Food

# Create a food instance
food = Food()

# Refresh food position
food.refresh()
```

### Troubleshooting

- If you get a "python command not found" error, try using `python3` instead of `python`
- Make sure you're in the correct directory after cloning
- The turtle graphics window should open automatically when running the script

## How to Play

1. Run the main game file:
   ```bash
   python ch20p.py
   ```

2. Use arrow keys to control the snake:
   - **↑** - Move Up
   - **↓** - Move Down  
   - **←** - Move Left
   - **→** - Move Right

3. Eat the blue food circles to grow and increase your score
4. Avoid hitting the walls or your own tail
5. Try to beat your high score!

## Game Mechanics

- **Snake Movement**: The snake moves continuously in the current direction
- **Food Consumption**: When the snake's head touches food, it grows and score increases
- **Collision System**: 
  - Wall collision or self-collision resets the game
  - High score is saved if current score exceeds it
- **Speed**: Game runs at 0.1 second intervals for smooth gameplay

## Technical Implementation

### Object-Oriented Design
- **Snake Class**: Manages snake segments, movement, and growth
- **Food Class**: Inherits from Turtle, handles random positioning
- **ScoreCard Class**: Manages score display and file persistence

### Key Programming Concepts
- Class inheritance and super() usage
- File I/O for persistent data storage
- Event-driven programming with key bindings
- Game loop implementation
- Collision detection algorithms

## Future Improvements

### Gameplay Enhancements
- **Power-Up Food**: Add enlarged food circles that appear at regular intervals (every 30-60 seconds)
  - Worth more points (5x or 10x normal food)
  - Larger visual size to distinguish from regular food
  - Limited time availability (disappears after 10-15 seconds)
  - Different color (gold/yellow) to indicate special status

- **Speed Boost**: Temporary speed increase when eating power-up food
- **Bonus Levels**: Special challenge levels with obstacles or time limits
- **Multiple Food Types**: Different colored food with varying point values
- **Snake Customization**: Allow players to choose snake colors or patterns

### Technical Improvements
- **Sound Effects**: Add audio feedback for eating food, collisions, and achievements
- **Pause Functionality**: Allow players to pause and resume the game
- **Settings Menu**: Configurable game speed, difficulty levels, and controls
- **Leaderboard**: Track top 10 scores with player names and timestamps
- **Game Statistics**: Track total games played, average score, and play time

### Visual Enhancements
- **Animated Food**: Pulsing or rotating food items for better visibility
- **Snake Trail Effects**: Visual effects when snake moves or grows
- **Background Themes**: Multiple background options and color schemes
- **Score Animations**: Animated score increases and achievement notifications
- **Grid System**: Optional grid overlay for precise movement

### Advanced Features
- **Multiplayer Mode**: Two-player snake game on the same screen
- **AI Snake**: Computer-controlled snake for single-player challenges
- **Level Progression**: Increasing difficulty with obstacles and faster speeds
- **Achievement System**: Unlock rewards for reaching milestones
- **Mobile Controls**: Touch/swipe controls for mobile devices