# Simple Tkinter To-Do App

A desktop To-Do List application built with **Python** and **CustomTkinter**. It uses **SQLite** to store tasks locally.

## Features

- Add tasks with a title and status
- View saved tasks, with the newest tasks displayed first
- Edit an existing task
- Delete a task with a confirmation prompt
- Store tasks in a local SQLite database
- Simple dark-themed graphical interface

## Built With

- Python
- CustomTkinter
- CTkMessagebox
- SQLite3 (Python standard library)

## Project Files

```text
Simple-Tkinter-To-Do-App/
├── to_do_list.py
├── add_task.py
├── edit_task.py
├── dbconnect.py
└── README.md
```

- `to_do_list.py` — main application window; displays tasks and provides edit/delete actions.
- `add_task.py` — window for creating a task.
- `edit_task.py` — window for updating a task.
- `dbconnect.py` — creates the SQLite database table if it does not already exist.

The SQLite database file (`to_do_list.db`) is created locally when the application runs. It is not included in this repository.

## Requirements

- Python 3
- CustomTkinter
- CTkMessagebox

Install the required packages:

```bash
python -m pip install customtkinter CTkMessagebox
```

## Run the Application

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the required packages.
4. Run the main file:

```bash
python to_do_list.py
```

Keep the supporting Python files in the same folder because the application opens them when you add or edit tasks.

## Database

The application uses SQLite and stores tasks in `to_do_list.db` in the working directory. The database table contains:

| Column | Purpose |
| --- | --- |
| `id` | Unique task identifier |
| `task` | Task title |
| `status` | Task status (Pending or Done) |

Your tasks are stored locally on your computer.

## Author

**Anji Sean**

---

This project was built as a Python GUI practice project to apply CustomTkinter, SQLite, and basic CRUD operations.
