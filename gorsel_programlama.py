import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# Stil Sabitleri
APP_STYLE = """
    QMainWindow {
        background-color: #FFC0CB;  /* Pembe arka plan */
    }
    QLabel {
        color: #8B0000;  /* Koyu kırmızı metin */
        font-size: 16px;
        font-weight: bold;
    }
    QLineEdit {
        background-color: #FFFFFF;  /* Beyaz arka plan */
        border: 2px solid #8B0000;  /* Koyu kırmızı kenarlık */
        border-radius: 10px;
        padding: 5px;
        font-size: 14px;
        color: #8B0000;  /* Koyu kırmızı metin */
    }
    QPushButton {
        background-color: #FF69B4;  /* Canlı pembe */
        border: 2px solid #8B0000;  /* Koyu kırmızı kenarlık */
        border-radius: 10px;
        padding: 10px;
        font-size: 14px;
        font-weight: bold;
        color: #FFFFFF;  /* Beyaz metin */
    }
    QPushButton:hover {
        background-color: #FF1493;  /* Daha koyu pembe (hover efekti) */
    }
    QTableWidget {
        background-color: #FFFFFF;  /* Beyaz arka plan */
        border: 2px solid #8B0000;  /* Koyu kırmızı kenarlık */
        border-radius: 10px;
    }
    QHeaderView::section {
        background-color: #FF69B4;  /* Canlı pembe başlık */
        color: #FFFFFF;  /* Beyaz metin */
        font-weight: bold;
        padding: 5px;
    }
"""

# Verileri Bellekte Tutmak için Liste
faturalar = []

# Giriş Sayfası
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş Sayfası")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(APP_STYLE)

        login_page = QWidget()
        layout = QVBoxLayout()

        # Başlık
        self.title_label = QLabel("Fatura Takip Sistemi")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 20, QFont.Bold))
        layout.addWidget(self.title_label)

        # Kullanıcı Adı
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Kullanıcı Adı")
        layout.addWidget(self.username_input)

        # Şifre
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Giriş Butonu
        self.login_button = QPushButton("Giriş Yap")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        login_page.setLayout(layout)
        self.setCentralWidget(login_page)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "user" and password == "1234":  # Basit bir kullanıcı doğrulama
            QMessageBox.information(self, "Başarılı", "Giriş başarılı!")
            self.main_menu_window = MainMenuWindow()
            self.main_menu_window.show()
            self.hide()  # Giriş penceresini gizle, kapatma
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")

# Ana Menü Sayfası
class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ana Menü")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(APP_STYLE)

        main_menu_page = QWidget()
        layout = QVBoxLayout()

        self.fatura_ekle_button = QPushButton("Fatura Ekle")
        self.fatura_ekle_button.clicked.connect(self.open_fatura_ekle)
        layout.addWidget(self.fatura_ekle_button)

        self.faturalarim_button = QPushButton("Faturalarım")
        self.faturalarim_button.clicked.connect(self.open_faturalarim)
        layout.addWidget(self.faturalarim_button)

        self.fatura_ode_button = QPushButton("Fatura Öde")
        self.fatura_ode_button.clicked.connect(self.open_fatura_ode)
        layout.addWidget(self.fatura_ode_button)

        self.ayarlar_button = QPushButton("Ayarlar")
        self.ayarlar_button.clicked.connect(self.open_ayarlar)
        layout.addWidget(self.ayarlar_button)

        main_menu_page.setLayout(layout)
        self.setCentralWidget(main_menu_page)

    def open_fatura_ekle(self):
        self.fatura_ekle_window = FaturaEkleWindow()
        self.fatura_ekle_window.show()

    def open_faturalarim(self):
        self.faturalarim_window = FaturalarimWindow()
        self.faturalarim_window.show()

    def open_fatura_ode(self):
        self.fatura_ode_window = FaturaOdeWindow()
        self.fatura_ode_window.show()

    def open_ayarlar(self):
        self.ayarlar_window = AyarlarWindow()
        self.ayarlar_window.show()

# Fatura Ekle Sayfası
class FaturaEkleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fatura Ekle")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(APP_STYLE)

        fatura_ekle_page = QWidget()
        layout = QVBoxLayout()

        self.tur_input = QLineEdit()
        self.tur_input.setPlaceholderText("Fatura Türü (Gelir/Gider)")
        layout.addWidget(self.tur_input)

        self.miktar_input = QLineEdit()
        self.miktar_input.setPlaceholderText("Miktar")
        layout.addWidget(self.miktar_input)

        self.aciklama_input = QLineEdit()
        self.aciklama_input.setPlaceholderText("Açıklama")
        layout.addWidget(self.aciklama_input)

        self.kaydet_button = QPushButton("Kaydet")
        self.kaydet_button.clicked.connect(self.kaydet_fatura)
        layout.addWidget(self.kaydet_button)

        self.ana_menu_button = QPushButton("Ana Menüye Dön")
        self.ana_menu_button.clicked.connect(self.close)
        layout.addWidget(self.ana_menu_button)

        fatura_ekle_page.setLayout(layout)
        self.setCentralWidget(fatura_ekle_page)

    def kaydet_fatura(self):
        tur = self.tur_input.text()
        miktar = self.miktar_input.text()
        aciklama = self.aciklama_input.text()

        if not tur or not miktar or not aciklama:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun!")
            return

        try:
            miktar = float(miktar)  # Miktarın sayısal değer olduğunu kontrol et
        except ValueError:
            QMessageBox.warning(self, "Hata", "Miktar geçerli bir sayı olmalıdır!")
            return

        durum = "Bekliyor"  # Varsayılan durum

        # Faturayı listeye ekle
        fatura = {
            "id": len(faturalar) + 1,
            "tur": tur,
            "miktar": miktar,
            "aciklama": aciklama,
            "durum": durum
        }
        faturalar.append(fatura)

        QMessageBox.information(self, "Başarılı", "Fatura başarıyla eklendi!")
        self.tur_input.clear()
        self.miktar_input.clear()
        self.aciklama_input.clear()

# Faturalarım Sayfası
class FaturalarimWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Faturalarım")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet(APP_STYLE)

        faturalarim_page = QWidget()
        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Tür", "Miktar", "Açıklama", "Durum"])
        layout.addWidget(self.table)

        self.guncelle_button = QPushButton("Durumu Güncelle")
        self.guncelle_button.clicked.connect(self.durum_guncelle)
        layout.addWidget(self.guncelle_button)

        self.ana_menu_button = QPushButton("Ana Menüye Dön")
        self.ana_menu_button.clicked.connect(self.close)
        layout.addWidget(self.ana_menu_button)

        faturalarim_page.setLayout(layout)
        self.setCentralWidget(faturalarim_page)
        self.load_data()

    def load_data(self):
        self.table.setRowCount(len(faturalar))
        for i, fatura in enumerate(faturalar):
            self.table.setItem(i, 0, QTableWidgetItem(str(fatura["id"])))
            self.table.setItem(i, 1, QTableWidgetItem(fatura["tur"]))
            self.table.setItem(i, 2, QTableWidgetItem(str(fatura["miktar"])))
            self.table.setItem(i, 3, QTableWidgetItem(fatura["aciklama"]))
            self.table.setItem(i, 4, QTableWidgetItem(fatura["durum"]))

    def durum_guncelle(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Hata", "Lütfen bir fatura seçin!")
            return

        fatura_id = int(self.table.item(selected_row, 0).text())
        current_status = self.table.item(selected_row, 4).text()

        # Durumu tersine çevir (Ödendi <-> Bekliyor)
        new_status = "Ödendi" if current_status == "Bekliyor" else "Bekliyor"

        # Faturanın durumunu güncelle
        for fatura in faturalar:
            if fatura["id"] == fatura_id:
                fatura["durum"] = new_status
                break

        QMessageBox.information(self, "Başarılı", f"Fatura durumu {new_status} olarak güncellendi!")
        self.load_data()  # Tabloyu yeniden yükle

# Fatura Öde Sayfası
class FaturaOdeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fatura Öde")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(APP_STYLE)

        fatura_ode_page = QWidget()
        layout = QVBoxLayout()

        self.info_label = QLabel("Fatura ödeme işlemleri henüz geliştirilmedi.")
        layout.addWidget(self.info_label)

        self.ana_menu_button = QPushButton("Ana Menüye Dön")
        self.ana_menu_button.clicked.connect(self.close)
        layout.addWidget(self.ana_menu_button)

        fatura_ode_page.setLayout(layout)
        self.setCentralWidget(fatura_ode_page)

# Ayarlar Sayfası
class AyarlarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ayarlar")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet(APP_STYLE)

        ayarlar_page = QWidget()
        layout = QVBoxLayout()

        self.info_label = QLabel("Ayarlar menüsü henüz geliştirilmedi.")
        layout.addWidget(self.info_label)

        self.ana_menu_button = QPushButton("Ana Menüye Dön")
        self.ana_menu_button.clicked.connect(self.close)
        layout.addWidget(self.ana_menu_button)

        ayarlar_page.setLayout(layout)
        self.setCentralWidget(ayarlar_page)

# Uygulama Başlatma
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())