# 🌳 treel

**treel** is a modern, colorful, and fully featured Python CLI tool to visualize directory structures — a smarter, customizable alternative to the classic Unix `tree` command.

It supports color-coded output, depth control, sorting, file sizes, hidden files, and exporting clean text reports — all in one neat command.

---

## 🚀 Features

✅ **Limit folder depth** — show only what you need  
✅ **Include or hide files**  
✅ **Show file sizes (KB)**  
✅ **Sort by name, size, or modified time**  
✅ **Export clean `.txt` output (no color codes)**  
✅ **Toggle colors** for terminal or automation scripts  
✅ **Cross-platform** — works on Windows, Linux, and macOS  
✅ **No dependencies except [`colorama`](https://pypi.org/project/colorama/)**  

---

## ⚙️ Installation

You can install `treel` directly from PyPI:

```bash
pip install treel
```

---

## 💻 Usage

Here are the most common ways to use it:

### Basic directory tree
```bash
treel .
```

### Limit tree depth to 2 levels
```bash
treel . -d 2
```

### Include files as well
```bash
treel . -f
```

### Show file sizes
```bash
treel . -f -s
```

### Show hidden files too
```bash
treel . -a
```

### Sort entries by size
```bash
treel . --sort size
```

### Export a clean text version
```bash
treel . -f -o structure.txt
```

### Disable colors (useful for CI/CD logs)
```bash
treel . --no-color
```

### Check version or help
```bash
treel --version
treel --help
```

---

## 🧠 Example Output

```
📁 C:\Projects\MyApp
├── backend
│   ├── app
│   ├── tests
│   ├── run.py
│   └── seed.py
├── frontend
│   ├── src
│   ├── public
│   ├── index.html
│   └── package.json
└── README.md
```

---

## 🧰 Command Reference

| Flag | Description | Example |
|------|--------------|----------|
| `-d`, `--depth` | Limit directory depth | `treel -d 2` |
| `-f`, `--files` | Include files in the tree | `treel -f` |
| `-a`, `--all` | Show hidden files/folders | `treel -a` |
| `-s`, `--size` | Show file sizes in KB | `treel -s` |
| `--sort` | Sort by `name`, `size`, or `time` | `treel --sort size` |
| `-o`, `--output` | Export to text file | `treel -f -o tree.txt` |
| `--no-color` | Disable color output | `treel --no-color` |
| `-v`, `--version` | Show version info | `treel --version` |
| `-h`, `--help` | Show help menu | `treel --help` |

---

## 🔧 Development

Clone the repository and install locally in editable mode:

```bash
git clone https://github.com/23f2005532/treel.git
cd treel
python -m venv .venv
.\.venv\Scripts\activate  # (on Windows)
pip install -e .
```

Run the tool directly:
```bash
treel . -f -d 2
```

---

## 🧩 Project Structure

```
treel/
├── treel/
│   ├── __init__.py
│   ├── treel.py
├── setup.py
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 🪴 Example Use Cases

- Quickly visualizing project folder structure for documentation  
- Generating clean, text-based directory trees for README files  
- Inspecting codebases in CI/CD pipelines without GUI tools  
- Lightweight alternative to the Linux `tree` command  

---

## 🧑‍💻 Author

**Ehtesham**  
📦 [PyPI: treel](https://pypi.org/project/treel/)  
🐙 [GitHub: 23f2005532](https://github.com/23f2005532)  
💬 Always open for collaboration & feedback!

---

## 📜 License

This project is licensed under the **MIT License** — you’re free to use, modify, and distribute it with attribution.

---

> 💡 *Treel is built with simplicity and practicality in mind — a small CLI that does one thing beautifully.*
