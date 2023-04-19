from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox
import subprocess
from PyQt5.QtGui import QPixmap
import winsound
import os
import threading

class CPEitGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("CPEit")
        self.setGeometry(100, 100, 2000, 800)

        # Create central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create horizontal layout for central widget
        hbox = QHBoxLayout(central_widget)

        # Create left panel
        left_panel = QWidget(self)
        left_panel.setMaximumWidth(250)
        vbox_left = QVBoxLayout(left_panel)

        # Create button "Build Inventory"
        build_button = QPushButton("Build Inventory", left_panel)
        build_button.clicked.connect(self.build_inventory)
        vbox_left.addWidget(build_button)

        # Create button "Build NVD Inventory"
        export_button = QPushButton("Build NVD Inventory", left_panel)
        export_button.clicked.connect(self.build_nvd_inventory)
        vbox_left.addWidget(export_button)

        # Create button "Display NVD Inventory"
        display_button = QPushButton("Display NVD Inventory", left_panel)
        display_button.clicked.connect(self.display_nvd)
        vbox_left.addWidget(display_button)

        # Create image above the buttons
        image_label = QLabel(left_panel)
        pixmap = QPixmap("image.gif")
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        vbox_left.addWidget(image_label)

        # Add left panel to horizontal layout
        hbox.addWidget(left_panel)

        # Create web view for displaying HTML content
        self.web_view = QWebEngineView(self)
        self.web_view.setUrl(QUrl("https://www.github.com/raxx00n/cpeit#readme"))

        # Add web view to horizontal layout
        hbox.addWidget(self.web_view)


    def build_inventory(self):
    
        # Run subprocess
        subprocess.run(['python', 'BUILD_INVENTORY.py'])
    
        # Display HTML content
        html_path = 'Software-Inventory.html'
        with open(html_path, 'r') as f:
            html_content = f.read()
        self.web_view.setHtml(html_content)


    def build_nvd_inventory(self):
        try:
            if not os.path.exists('Got-Combined.json'):
                raise FileNotFoundError
            message = "Building the NVD inventory can take a long time, as the NVD API is rate limited. You can monitor the console behind this window for error messages, or just go grab a book and cup of coffee. Do you want to continue?"
            reply = QMessageBox.question(self, 'Build NVD Inventory', message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                subprocess.run(['python', 'BUILD_NVD_INVENTORY.py'])
                html_path = 'NVD-Inventory.html'
                with open(html_path, 'r') as f:
                    html_content = f.read()
                self.web_view.setHtml(html_content)
        except FileNotFoundError:
            QMessageBox.warning(self, 'Error', 'Please build the inventory before building the NVD inventory.')

    def display_nvd(self):
        html_path = 'NVD-Inventory.html'
        if not os.path.exists(html_path):
            QMessageBox.warning(self, 'Error', 'The file NVD-Inventory.html was not found. Please build the NVD inventory first.')
            return
        with open(html_path, 'r') as f:
            html_content = f.read()
        self.web_view.setHtml(html_content)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    gui = CPEitGUI()
    gui.show()

    sys.exit(app.exec_())
