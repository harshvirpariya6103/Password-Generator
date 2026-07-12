# Secure Password Generator 🔐

A modern, secure, and customizable desktop password generator application built with Python and `customtkinter`. This project was developed as **Project 4** for the DevStack Technologies Python Application Development Internship.

## 🚀 Features

* **Cryptographically Secure:** Uses Python's `secrets` module for true randomization to ensure maximum security.
* **Customizable Parameters:** 
  * Set password length (between 6 and 24 characters).
  * Toggle inclusion of Uppercase letters, Lowercase letters, Numbers, and Symbols.
* **Advanced Security Rules:** Automatically prevents consecutive identical characters and limits the overall repetition of any single character to create stronger keys.
* **Password History:** Keeps track of your last 10 generated passwords for easy retrieval during your current session.
* **One-Click Copy:** Seamlessly copy generated passwords directly to your clipboard using the `pyperclip` module.
* **Modern UI:** A sleek, responsive dark-mode interface built with CustomTkinter.

## 🛠️ Prerequisites

Make sure you have Python 3.x installed on your machine. You will also need to install the following Python libraries to run the application:

```bash
pip install customtkinter pyperclip Pillow
```

## 📥 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/password-generator.git
   cd password-generator
   ```

2. **Check Assets:** 
   Ensure that the `image.png` file (the lock graphic used in the UI) is located in the same directory as the Python script.

3. **Run the application:**
   ```bash
   python password_generator.py
   ```

## 📂 Project Structure

```text
├── password_generator.py   # Main Python application script
├── image.png               # Graphical asset for the user interface
└── README.md               # Project documentation
```

## 📜 Acknowledgments
* Developed for the **DevStack Technologies** Python Application Development Internship (Project 4).