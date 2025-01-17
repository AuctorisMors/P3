The program is a terminal-based game application written in Python. It includes several modules and classes to handle different aspects of the game, such as settings, text display, language support, and game logic. The project has been completely rebuilt a few times as I learn more about types of patterns and pythonic guidelines.

The current state of the program in Jan 2025 requires me to do a larger rewrite as it has become obvious there is an inherent issue with how the code is all organized. My plan is to rewrite it to be more straight forward and pythonic.[[Jan-Flow-Revision.canvas|Jan-Flow-Revision]] features the current structural idea for the refactoring.

In the new refactor we import everything into support then pass the settings, funds, text objects as needed


AI note:
Your idea of structuring the project by having support modules and a settings module that get imported into the main program is a good approach. Here are some guidelines to ensure that the structure is modular, maintainable, and allows easy access to shared functionalities like the text functions:

1. **Main Program (`program.py`)**:
    
    - This should be the entry point of your application.
    - Import necessary modules (e.g., `settings`, `text`, `game_list`).
    - Create and configure the settings object.
    - Pass the settings object and other shared objects (like `Text`) to functions and classes that need them.
2. **Settings Module (`settings.py`)**:
    
    - Manage global settings, including loading and saving settings.
    - Provide methods for language selection and initialization of game funds.
    - This module should not directly handle text display; instead, it should provide data to be used by the `Text` module.
3. **Text Module (`text.py`)**:
    
    - Manage text display and formatting.
    - Provide utility functions for printing text, handling user prompts, and setting/getting the language.
    - This module should be imported and used by the main program and passed to other modules/functions as needed.
4. **Language Module (`language.py`)**:
    
    - Define language classes with dictionaries for different text strings used in the game.
    - This module should be imported by the settings module to set the appropriate language.
5. **Game List Module (`game_list.py`)**:
    
    - Import specific game classes (e.g., `Slots`, `Numbers`, `Guess`).
    - This module should be used by the main program to access and run different games.
6. **Game Modules (e.g., `slots.py`, `numbers.py`, `guess.py`)**:
    
    - Define the logic for individual games.
    - These modules should accept the settings object and the `Text` class or instance as parameters to access shared functionalities.
7. **Support Modules (e.g., `funds.py`)**:
    
    - Provide additional functionalities needed by the games (e.g., managing funds).
    - These modules should accept the settings object and the `Text` class or instance as parameters to access shared functionalities.

### Example Structure:

- `program.py`: Main entry point, imports and initializes settings, text, and game modules.
- `support/`
    - `settings.py`: Manages global settings.
    - `text.py`: Manages text display and formatting.
    - `language.py`: Defines language classes.
    - `funds.py`: Manages player funds.
    - `game_list.py`: Imports specific game classes.
- `games/`
    - `slots.py`: Defines the Slots game.
    - `numbers.py`: Defines the Numbers game.
    - `guess.py`: Defines the Guess game.

### Example Flow:

1. **Main Program**:
    
    - Import `Settings`, `Text`, and `game_list`.
    - Create and configure the settings object.
    - Pass the settings object and `Text` class to the main menu and game functions.
2. **Main Menu**:
    
    - Display the main menu using the `Text` class.
    - Handle user input and navigate to the selected game.
3. **Game Functions**:
    
    - Accept the settings object and `Text` class as parameters.
    - Use the settings object to access game-specific settings (e.g., language, funds).
    - Use the `Text` class to display text and handle user input.

By following this structure, you ensure that the project is modular, maintainable, and allows easy access to shared functionalities like the text functions. Each module has a clear responsibility, and dependencies are managed through parameter passing rather than direct imports, promoting loose coupling and better code organization.