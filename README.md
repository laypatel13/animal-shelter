# 🐾 Animal Shelter - CLI

A simple command-line Animal Shelter Manager built using Python.
This project helps you manage shelter animals, track adoption status, and view animals by type with a colorful and neatly formatted interface.

---

## ✨ Features

- Add animals (Dog, Cat, Parrot) with name, age, and breed
- View all animals in a formatted table
- Filter animals by type
- Mark animals as adopted by ID
- Save data in a JSON file (`animals.json`)
- Colorful CLI output for better readability

---

## 📦 Install via pip

```bash
pip install laypatel13-animal-shelter
```

Then run it from anywhere in your terminal:

```bash
animal-shelter
```

---

## 🛠️ Install from source

```bash
git clone https://github.com/laypatel13/animal-shelter.git
cd animal-shelter
pip install -r requirements.txt
pip install -e .
```

Then run:

```bash
animal-shelter
```

---

## 📂 Project Structure

```text
animal-shelter/
├── animal_shelter/
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 🧰 Built With

- Used [Colorama](https://pypi.org/project/colorama/) for colored terminal output.
- Used [Tabulate](https://pypi.org/project/tabulate/) for formatted table display.