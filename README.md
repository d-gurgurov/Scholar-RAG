# Scholar Paper RAG

**Scholar Paper Fetcher** is a simple application that retrieves recent research papers from Google Scholar, generates their descriptions using a locally running LLM, and displays them either in the terminal or in a minimalistic GUI interface. The app runs automatically every time you unlock your computer, utilizing Hammerspoon and a Lua script.

## Features
- **Paper Retrieval**: Fetches recent papers from Google Scholar.
- **Viewing Modes**:
  - **Terminal-based version**: Displays paper titles and descriptions directly in the terminal.
  - **GUI-based version**: A user-friendly PyQt6 GUI with buttons to navigate between papers.
- **Retrieval-Augmented Generation (RAG)**: Enhances the descriptions of the papers using a RAG system.
- **Automatic Fetching**: Automatically retrieves and displays papers upon unlocking the computer via Hammerspoon.

## Setup and Installation

### 1. Prerequisites
- **Python 3.x**
- Install the required Python packages:

    ```bash
    pip3 install tqdm requests beautifulsoup4 PyQt6 langchain FAISS transformers
    ```

### 2. Getting Google Scholar Cookies
1. Open Google Chrome and navigate to Google Scholar.
2. Right-click anywhere on the page and select "Inspect."
3. Go to the "Application" tab, then find "Cookies" under the "Storage" section.
4. Copy the cookie data and save it in a JSON file (e.g., `cookies.json`) on your local machine. The file should look like this:

    ```json
    {
        "GSP": "",
        "NID": "",
        "HSID": "",
        "SSID": "",
        "APISID": "",
        "SAPISID": "",
        "SID": ""
    }
    ```

### 3. Installing Ollama for Running LLMs Locally
1. Download Ollama either using the command line or manually from the [website](https://ollama.com/download):

    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```

2. Pull a Large Language Model (the available models are listed [here](https://ollama.com/library)):

    ```bash
    ollama pull llama3.2
    ```

### 4. Building the Terminal-Based Version
The terminal-based version fetches papers and displays their titles and descriptions directly in the terminal.

1. Use a Python script to handle fetching papers, generating descriptions, and displaying them in the terminal:

    ```bash
    python3 main.py
    ```

### 5. Building the GUI Version
The GUI version uses PyQt6 to provide a more user-friendly interface where users can swipe between paper descriptions.

1. Use a Python script to fetch papers, generate descriptions, and display them in a PyQt6 window with "Next" and "Previous" buttons:

    ```bash
    python3 main_gui.py
    ```

### 6. Automating Paper Fetching with Hammerspoon
You can configure the app to run automatically whenever you unlock your computer using Hammerspoon, a macOS automation tool.

1. Install Hammerspoon from its [official website](https://www.hammerspoon.org/).
2. Create a Lua script to trigger the app whenever the screen is unlocked. An example is provided in `./lua/init.lua`.
3. Place the script in the following directory: `~/.hammerspoon/init.lua`.
4. Save and reload the Hammerspoon configuration.

---

With this setup, every time you unlock your computer, the script will automatically run and fetch the latest papers from Google Scholar.
