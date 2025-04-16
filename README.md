# CodeAlpha Data Redundancy System

A simple Python-based CLI tool that prevents duplicate data entries using SHA-256 hashing and an SQLite database. Built for learning and data integrity, this system ensures that only unique entries are stored.

---

## 🚀 Features

- Detects duplicate entries using secure SHA-256 hashes
- Stores data in a lightweight SQLite database
- Command-line interface with real-time feedback
- Modular code with clear separation of concerns

---

## 🧱 Project Structure

CodeAlpha_DataRedundancySystem/
├── app.py           # Main script that runs the program and handles user input
├── database.py      # Sets up the SQLite database and table
├── utils.py         # Contains the hashing function
├── README.md        # Project overview and instructions (you’re reading it!)
├── .gitignore       # (Optional) Tells Git which files to ignore, like __pycache__
└── data.db          # SQLite database (auto-generated after first run)

