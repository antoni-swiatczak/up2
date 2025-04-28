from PyQt5.QtWidgets import QApplication, QTableView, QMessageBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QAbstractTableModel, Qt, QSortFilterProxyModel
from PyQt5.QtGui import QIcon, QColor
from datetime import datetime, timedelta
import sys

# Klasa reprezentująca książki
class Ksiazka:
    def __init__(self, tytul, autor, gatunek, status="Dostępna", osoba=None, data_wypozyczenia=None):
        self.tytul = tytul
        self.autor = autor
        self.gatunek = gatunek
        self.status = status
        self.osoba = osoba
        self.data_wypozyczenia = data_wypozyczenia

# Model danych
class BibliotekaModel(QAbstractTableModel):
    def __init__(self, ksiazki):
        super().__init__()
        self.ksiazki = ksiazki

    def rowCount(self, index):
        return len(self.ksiazki)

    def columnCount(self, index):
        return 6  # Tytuł, Autor, Gatunek, Status, Osoba, Data wypożyczenia

    def data(self, index, role):
        if not index.isValid():
            return None

        ksiazka = self.ksiazki[index.row()]
        kolumna = index.column()

        if role == Qt.DisplayRole:
            return [
                ksiazka.tytul,
                ksiazka.autor,
                ksiazka.gatunek,
                ksiazka.status,
                ksiazka.osoba or "",
                ksiazka.data_wypozyczenia.strftime("%Y-%m-%d") if ksiazka.data_wypozyczenia else ""
            ][kolumna]

        if role == Qt.DecorationRole and kolumna == 3:  # Ikony dla statusu
            if ksiazka.status == "Dostępna":
                return QIcon("ikona_dostepna.png")
            elif ksiazka.status == "Wypożyczona":
                return QIcon("ikona_wypozyczona.png")

        if role == Qt.BackgroundRole and sprawdz_przedawnione(ksiazka):
            return QColor("red")  # Podświetlenie przedawnionych książek

        return None

    def sort(self, column, order):
        if column == 0:  # Sortowanie po tytule
            self.ksiazki.sort(key=lambda x: x.tytul, reverse=order == Qt.DescendingOrder)
        elif column == 1:  # Sortowanie po autorze
            self.ksiazki.sort(key=lambda x: x.autor, reverse=order == Qt.DescendingOrder)
        elif column == 5:  # Sortowanie po dacie wypożyczenia
            self.ksiazki.sort(key=lambda x: x.data_wypozyczenia or datetime.min, reverse=order == Qt.DescendingOrder)
        self.layoutChanged.emit()

# Funkcja sprawdzająca przedawnione książki
def sprawdz_przedawnione(ksiazka):
    if ksiazka.status == "Wypożyczona" and ksiazka.data_wypozyczenia:
        termin = ksiazka.data_wypozyczenia + timedelta(days=14)
        if datetime.now() > termin:
            return True
    return False

# Główna aplikacja
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Lista książek
    ksiazki = [
        Ksiazka("Pan Tadeusz", "Adam Mickiewicz", "Epika"),
        Ksiazka("Lalka", "Bolesław Prus", "Powieść"),
        Ksiazka("Krzyżacy", "Henryk Sienkiewicz", "Historyczna", "Wypożyczona", "Jan Kowalski", datetime(2025, 4, 10)),  # Po terminie
        Ksiazka("Zbrodnia i Kara", "Fiodor Dostojewski", "Dramat"),
        Ksiazka("W pustyni i w puszczy", "Henryk Sienkiewicz", "Przygodowa", "Wypożyczona", "Anna Nowak", datetime(2025, 4, 20)),  # Nie po terminie
        Ksiazka("Hobbit", "J.R.R. Tolkien", "Fantasy", "Wypożyczona", "Piotr Zieliński", datetime(2025, 4, 22)),  # Nie po terminie
        Ksiazka("Potop", "Henryk Sienkiewicz", "Historyczna", "Wypożyczona", "Magdalena Kowalska", datetime(2025, 4, 18)),  # Nie po terminie
    ]

    # Model danych i widok
    model = BibliotekaModel(ksiazki)
    proxy_model = QSortFilterProxyModel()
    proxy_model.setSourceModel(model)

    view = QTableView()
    view.setModel(proxy_model)
    view.setSortingEnabled(True)
    view.setWindowTitle("Biblioteka")
    view.resize(800, 400)

    # Funkcja filtracji
    def filtruj(status=None):
        if status:
            proxy_model.setFilterRegExp(status)
        else:
            proxy_model.setFilterRegExp("")  # Pokaż wszystkie książki
        proxy_model.setFilterKeyColumn(3)  # Kolumna statusu

    # Przyciski do filtracji
    okno = QWidget()
    layout = QVBoxLayout()

    btn_dostepne = QPushButton("Filtruj: Dostępne")
    btn_dostepne.clicked.connect(lambda: filtruj("Dostępna"))

    btn_wypozyczone = QPushButton("Filtruj: Wypożyczone")
    btn_wypozyczone.clicked.connect(lambda: filtruj("Wypożyczona"))

    btn_wszystkie = QPushButton("Pokaż wszystkie")
    btn_wszystkie.clicked.connect(lambda: filtruj(None))

    # Dodanie przycisków do interfejsu
    layout.addWidget(view)
    layout.addWidget(btn_dostepne)
    layout.addWidget(btn_wypozyczone)
    layout.addWidget(btn_wszystkie)
    okno.setLayout(layout)
    okno.setWindowTitle("Biblioteka - Filtracja")
    okno.resize(850, 500)
    okno.show()

    # Sprawdź książki przedawnione
    przedawnione = [k for k in ksiazki if sprawdz_przedawnione(k)]
    if przedawnione:
        komunikat = QMessageBox()
        komunikat.setText("Są przedawnione książki!")
        komunikat.setInformativeText("\n".join(k.tytul for k in przedawnione))
        komunikat.exec_()

    sys.exit(app.exec_())
