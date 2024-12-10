# AutoTravel

AutoTravel is a Python-based automation tool that monitors the clipboard for specific commands, such as `/travel`, and performs a series of actions in a targeted application window. 

It features a graphical user interface (GUI) for starting and stopping monitoring and viewing logs of detected actions.

---

## Features

- **Clipboard Monitoring**: Detects `/travel` commands copied to the clipboard.
- **Automated Actions**:
  - Activates a specific window whose title ends with `"- Release"`.
  - Pastes the clipboard content into the target window.
  - Performs additional keyboard actions, such as pressing `SPACE` and `ENTER`.
- **Graphical User Interface**:
  - Log viewer to display actions and events in real time.
  - Start and stop buttons for controlling monitoring.
---

## Installation

### Prerequisites
1. **Python**: Ensure you have Python 3.10+ installed. You can download it from [python.org](https://www.python.org/).
2. **Poetry**: Install Poetry for dependency management:
   ```bash
   pip install poetry
   ```
   
3. Clone the project and install dependencies
   ```bash
    git clone https://github.com/Ozerioss/DofusAutoTravel.git
    cd DofusAutoTravel
   ```
   
4. a) Installing dependencies through poetry
   ```bash
   poetry install
   ```
   
4. b) Installing through requirements.txt (recommended if you do not want to install poetry)
   ```bash
   pip install -r requirements.txt
   ```
   
4. Running the script
    ```bash
    poetry run python src/main.py
    or
    python src/main.py
    ```
5. Building an executable
```bash
poetry run pyinstaller --onefile --windowed --name=DofusAutoTravel main.py
```

### Contributing (WIP)
To update requirements.txt through poetry
    ```bash
        poetry export --without-hashes -f requirements.txt -o requirements.txt
    ```
