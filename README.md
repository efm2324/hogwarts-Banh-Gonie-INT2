# Python-Project-Hogwart-INT2

## 1. Project Description
This is a text-based adventure game that follows a student's journey through Hogwarts. The project is divided into five chapters, covering the Sorting Hat ceremony, academic classes, a Quidditch tournament, and a final confrontation in the Chamber of Secrets. 

The goal of this project is to demonstrate Python programming skills, specifically modular code organization, data structure management, and interactive user logic.

## 2. Technical Requirements Met
Following the project guidelines (specifically Section 3.6.2), this game implements:
* **Modular Programming:** Each chapter is stored in a separate file within the `chapters/` folder.
* **External Data Handling:** Quidditch team rosters are loaded from an external `teams_quidditch.json` file.
* **Nested Dictionaries:** Complex data (like team roles and house points) are managed using nested dictionary structures.
* **Global State Management:** The `houses` dictionary tracks points across all chapters, consolidating the player's progress.

## 3. Installation and Usage
1.  **Extract** all project files into a single directory.
2.  **Open** your terminal or command prompt.
3.  **Navigate** to the project folder.
4.  **Run** the game using the following command:
    ```bash
    python main.py
    ```

## 4. File Structure
* `main.py`: The starting point that launches the game.
* `menu.py`: Controls the flow between chapters and manages house points.
* `data/`: Contains `teams_quidditch.json`.
* `utils/`: Contains `input_utils.py` for input handling and file loading.
* `chapters/`: 
    * `chapter_1.py` to `chapter_3.py`: Early adventure and classes.
    * `chapter_4.py`: The Quidditch Match simulation.
    * `chapter_5_extension.py`: The final Basilisk duel.

## 5. Credits
Developed for the "Art of Coding" Python Course. 
Inspired by the Wizarding World of Harry Potter.
