# library_manager
A Python-based Library Inventory Management System built using Object-Oriented Programming, JSON file persistence, and a menu-driven CLI interface.
# 📚 Library Inventory Manager  
### Mini Project — Python OOP | JSON Based Storage | CLI Menu  
---

This project is a command-line based **Library Management System** that allows users to:

✔ Add Books  
✔ Issue Books  
✔ Return Books  
✔ Search Books  
✔ Display Complete Inventory  
✔ Data is stored permanently using JSON  

It is built using **Object-Oriented Programming concepts**, proper package structuring, file handling, exception control and logging — exactly as required in *Assignment 03*.

---

## 🔥 Features

| Feature | Description |
|-------|-------------|
| Book Class | Stores title, author, ISBN, status |
| Issue / Return System | Update book status instantly |
| JSON Storage | Data remains safe even after closing program |
| CLI Menu | Very simple to navigate |
| Search System | Search books by title / ISBN |
| Logging + Exception Handling | Error-free & trackable execution |

---

## 🧠 Learning Outcomes

By completing this project we implemented:

- Python **Classes & Objects**
- Encapsulation and Methods (`issue(), return_book(), is_available()`)
- JSON File Persistence (`save_data()`, `load_data()`)
- Error control using **try-except**
- Project packaging with `__init__.py`
- Modular coding + Menu-Driven Interface





    ├── book.py
    └── inventory.py
