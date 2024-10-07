#!/bin/bash

# Open a new Terminal window and run the command
osascript <<EOF
tell application "Terminal"
    do script "python3 /Users/daniilgurgurov/Desktop/projects/scholar_rag/main.py; exit"
end tell
EOF