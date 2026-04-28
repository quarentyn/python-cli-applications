# python-cli-applications
A collection of secure CLI Applications including an encrypted password manager, a CRUD task manager, and a dynamic QR Code Generator

 These projects focus on secure data handling, core CRUD operations, and defensive programming principles.

## 1. Secure Password Verifier (Hashlib)
A terminal-based authentication script demonstrating one-way cryptographic hashing and secure user input.

* **Core Technologies:** Python, `hashlib`, `getpass`
* **Key Features:**
  * Utilizes SHA-256 hashing to securely verify user credentials without ever storing or exposing plain-text passwords.
  * Implements the `getpass` module for invisible terminal input, protecting against shoulder-surfing during password entry.
  * Features an interactive state loop for seamless account creation and login validation.

## 2. Dynamic To-Do Task Manager
A robust task management application executing core CRUD (Create, Read, Update, Delete) operations entirely within the terminal.

* **Core Technologies:** Python, Data Structures (Lists & Dictionaries)
* **Key Features:**
  * Maintains an interactive, continuous loop for managing and tracking task states in real-time.
  * Engineered with defensive programming protocols (`try/except` blocks) to sanitize unpredictable user input and prevent fatal runtime crashes.
  * Utilizes dynamic zero-indexed logic to safely mark specific tasks as complete or remove them from memory.

---
*Developed by Eben | Spring 2026*
