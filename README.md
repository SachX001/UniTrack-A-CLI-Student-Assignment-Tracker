# UniTrack: Student Assignment Manager

## Project Description
UniTrack is a CLI (Command Line Interface) based tool designed to help students track their academic assignments and project deadlines. As a freshman, keeping track of multiple submission dates across different courses can be difficult. This tool solves that problem by allowing users to add assignments, view them in a readable format, and save the data permanently to a text file.

## Theme
Productivity & Automation

## Course
CSE1003 - Introduction to Problem Solving & Programming

## Features
* **Add Assignments:** Input a project description and a due date.
* **View List:** Displays all current tasks in a clean, readable format.
* **Data Persistence:** Uses File I/O to save data to `vit_projects.txt`, so assignments aren't lost when the program closes.
* **Modular Design:** The code is split into three separate files for better organization and readability.

## Project Structure
The project is divided into three Python modules:

1.  **`main.py`**:
    * The entry point of the application.
    * Contains the main `while` loop and the menu interface.
    * Connects the logic module with the storage module.

2.  **`storing_data.py`**:
    * Handles all File I/O operations.
    * `save_data()`: Writes the list of projects to a text file using a `|` separator.
    * `load_data()`: Reads the text file and reconstructs the list of dictionaries.

3.  **`Dictionaries.py`**:
    * Handles data formatting.
    * `create_dictionary()`: Bundles inputs into a structured dictionary object.
    * `get_readable_dictionary()`: returns a formatted string for display.

## How to Run
1.  Ensure you have Python installed.
2.  Download the repository.
3.  Open the terminal in the project folder.
4.  Run the following command:
    ```bash
    python main.py
    ```
5.  Follow the on-screen menu prompts.

## Future Scope
In the future, I plan to add:
* Sorting assignments by date.
* A feature to delete completed tasks.
* Color-coded output for urgent deadlines.

## Screenshots
Screenshots of the working application can be found in the `/screenshots` folder.

## Recordings
As of now, there are no recordings available for the project, they will be added once the project ticks all the goals
