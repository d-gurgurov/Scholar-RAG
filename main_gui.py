from scholar_scraper import get_scholar_recommendations
from rag_implementation import setup_rag, get_paper_description

from tqdm import tqdm
from datetime import datetime
import warnings
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
import sys

# Silence specific deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="langchain")
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers")

import json

# Function to load cookies from a JSON file
def load_cookies(file_path):
    with open(file_path, 'r') as f:
        cookies = json.load(f)
    return cookies

# GUI class for viewing papers
class PaperViewer(QWidget):
    def __init__(self, papers):
        super().__init__()
        self.papers = papers
        self.current_index = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Paper Viewer")
        self.setGeometry(100, 100, 600, 400)

        # Set up the layout
        self.layout = QVBoxLayout()

        # Title label
        self.title_label = QLabel(self)
        self.title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")

        # Description label
        self.description_label = QLabel(self)
        self.description_label.setWordWrap(True)
        self.description_label.setStyleSheet("font-size: 14px; margin: 20px;")

        # Add widgets to layout
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.description_label)

        # Button to navigate right
        self.next_button = QPushButton('Next', self)
        self.next_button.clicked.connect(self.show_next_paper)
        self.layout.addWidget(self.next_button)

        # Button to navigate left
        self.prev_button = QPushButton('Previous', self)
        self.prev_button.clicked.connect(self.show_previous_paper)
        self.layout.addWidget(self.prev_button)

        self.setLayout(self.layout)

        self.update_paper_view()

    def update_paper_view(self):
        """Update the displayed paper title and description."""
        if self.papers:
            current_paper = self.papers[self.current_index]
            self.title_label.setText(current_paper['title'])
            self.description_label.setText(current_paper['description'])

    def show_next_paper(self):
        """Display the next paper."""
        if self.current_index < len(self.papers) - 1:
            self.current_index += 1
            self.update_paper_view()

    def show_previous_paper(self):
        """Display the previous paper."""
        if self.current_index > 0:
            self.current_index -= 1
            self.update_paper_view()

# Main logic for fetching papers and setting up RAG
def main():
    print(f"\nScholar Update Run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # Get Google Scholar cookies
    cookies = load_cookies('/Users/daniilgurgurov/Desktop/projects/cookies.json')

    print("Fetching and analyzing recent papers from Google Scholar...")
    print("=" * 80)

    # Fetch recent papers
    papers = get_scholar_recommendations(cookies)

    # Setup RAG
    db, chain = setup_rag(papers)

    # Generate descriptions for the papers
    for paper in tqdm(papers, desc="Processing Papers", unit="paper"):
        description = get_paper_description(db, chain, paper)
        paper['description'] = description

    # Launch the PyQt5 GUI to display the papers
    run_gui(papers)

# Function to run the PyQt5 application
def run_gui(papers):
    app = QApplication(sys.argv)
    viewer = PaperViewer(papers)
    viewer.show()
    app.exec()

if __name__ == "__main__":
    main()
