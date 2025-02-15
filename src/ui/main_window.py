from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QTabWidget, 
                            QLabel, QPushButton, QMessageBox, QDialog)
from PyQt5.QtCore import Qt
from .map_widget import MapWidget
from .business_tab import BusinessTab
from .customer_tab import CustomerTab
from .analytics_tab import AnalyticsTab
from ..utils.config import Config
from ..utils.subscription import PlanType, SubscriptionPlans
from .payment_dialog import PaymentDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.current_plan = PlanType.FREE  # Varsayılan olarak ücretsiz plan
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("İşletme ve Müşteri Yönetim Sistemi")
        self.setGeometry(100, 100, 1200, 800)
        
        # Stil dosyasını yükle
        try:
            with open("src/assets/styles/main.qss", "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            pass  # Stil dosyası bulunamazsa devam et
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        tabs = QTabWidget()
        tabs.addTab(MapWidget(self.config.get("google_maps_api_key", "API")), "Harita")
        tabs.addTab(BusinessTab(), "İşletmeler")
        tabs.addTab(CustomerTab(), "Müşteriler")
        tabs.addTab(AnalyticsTab(), "Analiz")
        
        layout.addWidget(tabs)
        
        # Üyelik durumu göstergesi
        self.setup_subscription_status()
        
        # Pro özellikleri için menü
        self.setup_pro_features_menu()
    
    def setup_subscription_status(self):
        status_bar = self.statusBar()
        self.plan_label = QLabel()
        self.update_plan_status()
        status_bar.addPermanentWidget(self.plan_label)
        
        upgrade_button = QPushButton("Pro'ya Yükselt")
        upgrade_button.clicked.connect(self.show_upgrade_dialog)
        status_bar.addPermanentWidget(upgrade_button)
    
    def update_plan_status(self):
        plan_name = "PRO" if self.current_plan == PlanType.PRO else "ÜCRETSİZ"
        self.plan_label.setText(f"Plan: {plan_name}")
    
    def show_upgrade_dialog(self):
        if self.current_plan == PlanType.PRO:
            QMessageBox.information(self, "Bilgi", "Zaten Pro üyeliğiniz bulunmakta!")
            return
            
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Pro Özellikleri")
        msg.setInformativeText(
            "✓ Sınırsız işletme ve müşteri kaydı\n"
            "✓ Gelişmiş analitik araçları\n"
            "✓ Veri dışa aktarma\n"
            "✓ API erişimi\n"
            "✓ Özel raporlar\n"
            "✓ Öncelikli destek\n\n"
            f"Aylık sadece {SubscriptionPlans.get_plan_price(PlanType.PRO)}₺"
        )
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        
        if msg.exec_() == QMessageBox.Ok:
            self.process_upgrade()
    
    def process_upgrade(self):
        # Ödeme işlemi burada gerçekleştirilecek
        payment_dialog = PaymentDialog(self)
        if payment_dialog.exec_() == QDialog.Accepted:
            self.current_plan = PlanType.PRO
            self.update_plan_status()
            QMessageBox.information(self, "Başarılı", "Pro üyeliğiniz aktif edildi!")
    
    def setup_pro_features_menu(self):
        pass  # Pro özellikler menüsü daha sonra eklenecek 