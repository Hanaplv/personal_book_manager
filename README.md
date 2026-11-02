# Personal Book Manager
A simple book manager built with python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

## Features
- add multiple books
- display books
- save books
- load saved books
- admin mode

## Requirements
- Python
- Python-dotenv

## Installation
Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Envoirment setup
create a `.env` file in the project folder

use `.env.example` as a template

Add your admin password

```env
admin_pass=your_password_here
```

replace `your_password_here` with your own admin password

## run the program
run the main file:
```bash
pyhthon main.py

```

## Screenshots
![personal-task-manager-screenshot](images/screenshot.png)

## Demo
![personal-task-manager-demo](images/Animation.gif)

## Project Structure

- `main.py` - Main program.
- `books.py` - Book functions.
- `.gitignore` - Ignores unnecessary files.
- `.env.example` - Example of environment variables.
- `requirements.txt` - Required packages.
- `image/` - Stores screenshots and GIF files.
- `books.json` - Stores books.

## How It Works

1. The program gets the user's name.
2. It loads saved books.
3. The user adds new books.
4. The program displays all books.
5. The books are saved in `books.json`.
6. Admin Mode checks the password.

## Troubleshooting

### 1. FileNotFoundError
- **Meaning:** The file does not exist.
- **Reason:** `books.json` may not have been created yet.
- **Check:** Check the project folder.

### 2. JSONDecodeError
- **Meaning:** The JSON file has invalid data.
- **Reason:** The file may be empty or damaged.
- **Check:** Check the content of `books.json`.

### 3. ModuleNotFoundError
- **Meaning:** Python cannot find a module.
- **Reason:** `python-dotenv` may not be installed.
- **Check:** Install packages using:

```bash
python -m pip install -r requirements.txt
```