from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from ui.dialog.ui_Widget_WebControl import Ui_Form

class WebControl(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.resize(800, 600)
        self.setWindowTitle("Web Control")
        
        # Create layout
        self.layout = QVBoxLayout(self)
        
        # Create address bar
        self.address_layout = QHBoxLayout()
        self.address_bar = QLineEdit()
        self.address_bar.setPlaceholderText("Enter URL...")
        self.address_bar.returnPressed.connect(self.navigate_to_url)
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.navigate_to_url)
        self.back_button = QPushButton("Back")
        self.forward_button = QPushButton("Forward")
        self.refresh_button = QPushButton("Refresh")
        
        # Add widgets to address layout
        self.address_layout.addWidget(self.back_button)
        self.address_layout.addWidget(self.forward_button)
        self.address_layout.addWidget(self.refresh_button)
        self.address_layout.addWidget(self.address_bar)
        self.address_layout.addWidget(self.go_button)
        
        # Create web view
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl("https://www.google.com"))
        self.address_bar.setText("https://www.google.com")
        
        # Connect signals
        self.back_button.clicked.connect(self.web_view.back)
        self.forward_button.clicked.connect(self.web_view.forward)
        self.refresh_button.clicked.connect(self.web_view.reload)
        self.web_view.urlChanged.connect(self.update_address_bar)
        
        # Add layouts and widgets to main layout
        self.layout.addLayout(self.address_layout)
        self.layout.addWidget(self.web_view)
        
        # Set layout
        self.setLayout(self.layout)
    
    def navigate_to_url(self):
        url = self.address_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.web_view.load(QUrl(url))
    
    def update_address_bar(self, url):
        self.address_bar.setText(url.toString())