# Trial Tests Workspace

## Overview

This workspace contains several small experimental projects for learning web development, Python programming, and Tkinter GUI development.

Projects are grouped by folder:

- `3n_plus_one/` — JavaScript implementation of the Collatz (3n + 1) sequence.
- `chapter_one/` — Python console and GUI apps, plus a browser-based tip calculator.
- `Tkinter_touchy/chapter_one/` — Tkinter practice examples building simple interactive windows.

---

## 1. 3n_plus_one

### Files
- `3n_plus_one/solution1.js`

### Description
A JavaScript script that computes and prints the Collatz sequence for a given starting number. It displays each value and the total iteration count until the sequence reaches `1`.

### Run
Requires Node.js.

```bash
node 3n_plus_one/solution1.js
```

---

## 2. chapter_one

### Files
- `chapter_one/tipCalculator.py` — console tip calculator.
- `chapter_one/tipCalc.html` — browser-based tip calculator UI.
- `chapter_one/style.css` — styles for the HTML tip calculator.
- `chapter_one/tkinter_demo.py` — simple Tkinter button click demo.
- `chapter_one/tipCalculatorGUI.py` — Tkinter tip calculator GUI.

### Descriptions
- `tipCalculator.py`: text-based application that prompts for bill amount and tip percentage, calculates tip and total, and repeats until the user chooses to exit.
- `tipCalc.html` + `style.css`: a browser UI for calculating tips with form input and dynamic JavaScript result rendering.
- `tkinter_demo.py`: a minimal Tkinter window that updates a label when a button is clicked.
- `tipCalculatorGUI.py`: a graphical tip calculator implemented with Python Tkinter.

### Run
Requires Python 3.

```bash
python chapter_one/tipCalculator.py
python chapter_one/tkinter_demo.py
python chapter_one/tipCalculatorGUI.py
```

To use the browser app, open `chapter_one/tipCalc.html` in a web browser.

---

## 3. Tkinter_touchy/chapter_one

### Files
- `Tkinter_touchy/chapter_one/hello_world.py`
- `Tkinter_touchy/chapter_one/hello_tkinter.py`
- `Tkinter_touchy/chapter_one/fix_hello.py`

### Descriptions
- `hello_world.py`: a simple Tkinter app with buttons for greeting and closing the window.
- `hello_tkinter.py`: an early version of the hello GUI that demonstrates button callbacks.
- `fix_hello.py`: an improved Tkinter example using `tk.StringVar()` to manage label state more reliably.

### Run
Requires Python 3.

```bash
python Tkinter_touchy/chapter_one/hello_world.py
python Tkinter_touchy/chapter_one/hello_tkinter.py
python Tkinter_touchy/chapter_one/fix_hello.py
```

---

## Notes

- The projects are ideal for learning: console programs, front-end web UI, and desktop GUIs.
- Most Python projects use only the standard library.
- Keep experimenting by modifying values, labels, and layout logic.

---

## Contribution

Feel free to add new examples in dedicated folders and update this README as the workspace grows.