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
- **Cross-platform Compatibility**: Works on Windows (primary platform for window management).

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
    git clone https://github.com/your-username/AutoTravel.git
    cd AutoTravel
   
    poetry install
    poetry run
   ```

