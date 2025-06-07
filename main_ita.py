#!/usr/bin/env python3
# Author: Bocaletto Luca
# Programming Language: Python
# Interface Language: English
# License: GPLv3
# Importa il modulo `sys` per la gestione degli argomenti della riga di comando
import sys

# Importa le classi e i moduli necessari da PyQt5 per la creazione dell'interfaccia utente
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPlainTextEdit,
    QAction,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QFileDialog,
    QFontDialog,
    QColorDialog,
    QInputDialog,
    QMessageBox,
)
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QFont
from PyQt5.QtCore import Qt

# Definizione della classe principale dell'editor di testo
class EditorDiTesto(QMainWindow):
    def __init__(self):
        super().__init__()
        # Inizializza l'interfaccia utente
        self.inizializza_ui()

    def inizializza_ui(self):
        # Crea l'area di testo principale
        self.area_testo = QPlainTextEdit(self)
        self.setCentralWidget(self.area_testo)

        # Crea la barra dei menu
        barra_menu = self.menuBar()
        menu_file = barra_menu.addMenu('File')
        menu_modifica = barra_menu.addMenu('Modifica')
        menu_formato = barra_menu.addMenu('Formato')
        menu_strumenti = barra_menu.addMenu('Strumenti')

        # Crea le azioni per il menu "File"
        azione_apri = QAction('Apri', self)
        azione_apri.setShortcut('Ctrl+O')
        azione_apri.triggered.connect(self.apri_file)
        menu_file.addAction(azione_apri)

        azione_salva = QAction('Salva', self)
        azione_salva.setShortcut('Ctrl+S')
        azione_salva.triggered.connect(self.salva_file)
        menu_file.addAction(azione_salva)

        # Crea le azioni per il menu "Modifica"
        azione_taglia = QAction('Taglia', self)
        azione_taglia.setShortcut('Ctrl+X')
        azione_taglia.triggered.connect(self.area_testo.cut)
        menu_modifica.addAction(azione_taglia)

        azione_copia = QAction('Copia', self)
        azione_copia.setShortcut('Ctrl+C')
        azione_copia.triggered.connect(self.area_testo.copy)
        menu_modifica.addAction(azione_copia)

        azione_incolla = QAction('Incolla', self)
        azione_incolla.setShortcut('Ctrl+V')
        azione_incolla.triggered.connect(self.area_testo.paste)
        menu_modifica.addAction(azione_incolla)

        azione_annulla = QAction('Annulla', self)
        azione_annulla.setShortcut('Ctrl+Z')
        azione_annulla.triggered.connect(self.area_testo.undo)
        menu_modifica.addAction(azione_annulla)

        azione_ripeti = QAction('Ripeti', self)
        azione_ripeti.setShortcut('Ctrl+Y')
        azione_ripeti.triggered.connect(self.area_testo.redo)
        menu_modifica.addAction(azione_ripeti)

        # Crea le azioni per il menu "Formato"
        azione_grassetto = QAction('Grassetto', self)
        azione_grassetto.setCheckable(True)
        azione_grassetto.triggered.connect(self.alterna_grassetto)
        menu_formato.addAction(azione_grassetto)

        azione_corsivo = QAction('Corsivo', self)
        azione_corsivo.setCheckable(True)
        azione_corsivo.triggered.connect(self.alterna_corsivo)
        menu_formato.addAction(azione_corsivo)

        azione_sottolineato = QAction('Sottolineato', self)
        azione_sottolineato.setCheckable(True)
        azione_sottolineato.triggered.connect(self.alterna_sottolineato)
        menu_formato.addAction(azione_sottolineato)

        azione_cambia_carattere = QAction('Cambia Carattere', self)
        azione_cambia_carattere.triggered.connect(self.cambia_carattere)
        menu_formato.addAction(azione_cambia_carattere)

        azione_colore_testo = QAction('Colore del Testo', self)
        azione_colore_testo.triggered.connect(self.cambia_colore_testo)
        menu_formato.addAction(azione_colore_testo)

        # Crea le azioni per il menu "Strumenti"
        azione_trova_sostituisci = QAction('Trova e Sostituisci', self)
        azione_trova_sostituisci.setShortcut('Ctrl+F')
        azione_trova_sostituisci.triggered.connect(self.mostra_dialogo_trova_sostituisci)
        menu_strumenti.addAction(azione_trova_sostituisci)

        azione_conta_parole = QAction('Conta Parole', self)
        azione_conta_parole.triggered.connect(self.conta_parole)
        menu_strumenti.addAction(azione_conta_parole)

        # Crea un pulsante "Salva"
        pulsante_salva = QPushButton('Salva', self)
        pulsante_salva.clicked.connect(self.salva_file)

        # Crea un layout per l'interfaccia
        layout = QVBoxLayout()
        layout.addWidget(self.area_testo)
        layout.addWidget(pulsante_salva)

        contenitore = QWidget()
        contenitore.setLayout(layout)

        self.setCentralWidget(contenitore)

        # Imposta le dimensioni e il titolo della finestra principale
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Editor di Testo')
        self.show()

    # Metodo per aprire un file
    def apri_file(self):
        opzioni = QFileDialog.Options()
        nome_file, _ = QFileDialog.getOpenFileName(self, 'Apri File', '', 'File di Testo (*.txt);;Tutti i File (*)', options=opzioni)
        if nome_file:
            with open(nome_file, 'r') as file:
                self.area_testo.setPlainText(file.read())

    # Metodo per salvare un file
    def salva_file(self):
        opzioni = QFileDialog.Options()
        nome_file, _ = QFileDialog.getSaveFileName(self, 'Salva File', '', 'File di Testo (*.txt);;Tutti i File (*)', options=opzioni)
        if nome_file:
            with open(nome_file, 'w') as file:
                file.write(self.area_testo.toPlainText())

    # Metodo per attivare/disattivare il grassetto
    def alterna_grassetto(self):
        cursore = self.area_testo.textCursor()
        formato = QTextCharFormat()
        formato.setFontWeight(QFont.Bold if cursore.charFormat().fontWeight() == QFont.Normal else QFont.Normal)
        cursore.mergeCharFormat(formato)
        self.area_testo.mergeCurrentCharFormat(formato)

    # Metodo per attivare/disattivare il corsivo
    def alterna_corsivo(self):
        cursore = self.area_testo.textCursor()
        formato = QTextCharFormat()
        formato.setFontItalic(not cursore.charFormat().fontItalic())
        cursore.mergeCharFormat(formato)
        self.area_testo.mergeCurrentCharFormat(formato)

    # Metodo per attivare/disattivare il sottolineato
    def alterna_sottolineato(self):
        cursore = self.area_testo.textCursor()
        formato = QTextCharFormat()
        formato.setFontUnderline(not cursore.charFormat().fontUnderline())
        cursore.mergeCharFormat(formato)
        self.area_testo.mergeCurrentCharFormat(formato)

    # Metodo per cambiare il tipo di carattere
    def cambia_carattere(self):
        font, ok = QFontDialog.getFont()
        if ok:
            cursore = self.area_testo.textCursor()
            formato = QTextCharFormat()
            formato.setFont(font)
            cursore.mergeCharFormat(formato)
            self.area_testo.mergeCurrentCharFormat(formato)

    # Metodo per cambiare il colore del testo
    def cambia_colore_testo(self):
        colore = QColorDialog.getColor()
        if colore.isValid():
            cursore = self.area_testo.textCursor()
            formato = QTextCharFormat()
            formato.setForeground(colore)
            cursore.mergeCharFormat(formato)
            self.area_testo.mergeCurrentCharFormat(formato)

    # Metodo per mostrare la finestra di "Trova e Sostituisci"
    def mostra_dialogo_trova_sostituisci(self):
        testo_da_trovare, ok = QInputDialog.getText(self, 'Trova', 'Trova:')
        if ok:
            cursore = self.area_testo.document().find(testo_da_trovare)
            if cursore.isNull():
                QMessageBox.information(self, 'Trova', 'Testo non trovato.')
            else:
                self.area_testo.setTextCursor(cursore)
                self.area_testo.setFocus()

    # Metodo per contare le parole nel testo
    def conta_parole(self):
        testo = self.area_testo.toPlainText()
        parole = testo.split()
        numero_parole = len(parole)
        QMessageBox.information(self, 'Conteggio Parole', f'Il documento contiene {numero_parole} parole.')

# Punto di ingresso del programma
if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = EditorDiTesto()
    sys.exit(app.exec_())
