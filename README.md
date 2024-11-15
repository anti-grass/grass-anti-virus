# Grass Anti Virus

Grass Anti Virus scans any folders for grass within every single file in that directory.

## Features

- **Scan for Grass**: The core functionality scans your computer's files for the string 'grass''.
- **Reports**: After scanning, it generates a report listing all grass strings found on your system.
  
## Requirements

- Python 3.12+ (if self-compiling)

## Installation

Follow these steps to get Grass Anti Virus running on your local machine.

### Option 1: Pre-Compiled Executables (For Windows Users)

1. Head over to [the releases page](https://github.com/anti-grass/grass-anti-virus/releases)
2. Find the latest release (sadly, you can only install the pre-compiled executable for windows at the current moment)
3. Run the file

### Option 2: Self-Compiling (For Non Windows Users, Or Advanced Users)

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/anti-grass/grass-anti-virus.git
   ```
2. Navigate to the project directory:
    ```bash
    cd grass-anti-virus
    ```
3. Running the program:
    ```python
    python main.py
    ```