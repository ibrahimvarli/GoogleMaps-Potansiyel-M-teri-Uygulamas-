from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, 
                            QLineEdit, QPushButton, QLabel)

class PaymentDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("Ödeme Bilgileri")
        layout = QVBoxLayout(self)
        
        form = QFormLayout()
        
        self.card_number = QLineEdit()
        self.card_number.setPlaceholderText("1234 5678 9012 3456")
        form.addRow("Kart Numarası:", self.card_number)
        
        self.expiry = QLineEdit()
        self.expiry.setPlaceholderText("MM/YY")
        form.addRow("Son Kullanma:", self.expiry)
        
        self.cvv = QLineEdit()
        self.cvv.setPlaceholderText("123")
        self.cvv.setMaxLength(3)
        form.addRow("CVV:", self.cvv)
        
        layout.addLayout(form)
        
        pay_button = QPushButton("Ödemeyi Tamamla")
        pay_button.clicked.connect(self.accept)
        layout.addWidget(pay_button) 