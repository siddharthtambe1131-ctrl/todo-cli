# todo-cli

A simple, dependency-free command-line to-do manager written in Python.
Tasks are saved in a JSON file in your home folder (`~/.todo_cli.json`).

## Features
- Add, list, complete, and delete tasks
- Clear all completed tasks at once
- Persistent storage (JSON)
- Unit tests with pytest

## Requirements
- Python 3.8+

## Usage

```bash
python -m todo add "Buy groceries"
python -m todo add "Finish assignment"
python -m todo list
python -m todo done 1
python -m todo delete 2
python -m todo clear
```

Example output:

```
[x] #1  Buy groceries  (2026-11-21 10:30)
[ ] #2  Finish assignment  (2026-11-21 10:31)
```

## Run the tests

```bash
pip install -r requirements.txt
pytest
```

## Project structure

```
todo-cli/
├── todo/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py        # argument parsing & output
│   ├── core.py       # task logic
│   └── storage.py    # JSON load/save
├── tests/
│   └── test_core.py
├── requirements.txt
├── LICENSE
└── README.md
```

## License
MIT
