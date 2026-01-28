# Mastermind (Python) — Codebreakers & Codemakers

A small Python project around the Mastermind game:
- multiple **codebreaker** strategies (solvers)
- multiple **codemaker** strategies (secret generators)
- optional plots to compare performance

## Project structure

- `play.py` — run games / simulations
- `plot.py` — generate plots (matplotlib)
- `common.py` — shared utilities
- `codebreakers/` — solver strategies
- `codemakers/` — secret generation strategies

## Requirements

- Python 3.10+ recommended
- Works on macOS / Linux / Windows (with a standard Python install)

## Quick start

### 1) Clone

```bash
git clone https://github.com/NathanSV1/mastermind.git
cd mastermind
```

### 2) Create & Activate a virtual environment

- macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Windows (PowerShell) :

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4) Run & Have Fun !

```bash
python play.py
```

### 5) Optional (Plots)

```bash
python plot.py
```

## Notes

- If imports fail, make sure you are running from the project root and using the virtual environment `(.venv)`.
- Strategy files are located in `codebreakers/` and `codemakers/`.
