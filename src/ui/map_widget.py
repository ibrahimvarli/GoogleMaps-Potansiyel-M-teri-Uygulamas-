from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import io

class MapWidget(QWidget):
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # Arama kontrollerini oluştur
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Konum ara...")
        self.search_button = QPushButton("Ara")
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        
        # Harita görünümü
        self.web_view = QWebEngineView()
        self.show_default_map()
        
        layout.addLayout(search_layout)
        layout.addWidget(self.web_view)
    
    def show_default_map(self):
        m = folium.Map(location=[41.0082, 28.9784], zoom_start=13)
        data = io.BytesIO()
        m.save(data, close_file=False)
        self.web_view.setHtml(data.getvalue().decode()) 