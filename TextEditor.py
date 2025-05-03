# Importa il modulo `sys` per la gestione degli argomenti della riga di comando
import sys

# Importa le classi e i moduli necessari da PyQt5 per la creazione dell'interfaccia utente
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QAction,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QFileDialog,
    QFontDialog,
    QColorDialog,
    QInputDialog,
    QMessageBox,
    QPlainTextEdit,
)
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QTextBlockFormat, QTextFormat
from PyQt5.QtCore import Qt

# Definizione della classe principale dell'editor di testo
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Inizializza l'interfaccia utente
        self.init_ui()

    def init_ui(self):
        # Crea un'area di testo principale
        self.text_edit = QPlainTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Crea la barra del menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Modifica')
        format_menu = menubar.addMenu('Formato')
        tools_menu = menubar.addMenu('Strumenti')

        # Crea le azioni per il menu "File"
        open_action = QAction('Apri', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction('Salva', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # Crea le azioni per il menu "Modifica"
        cut_action = QAction('Taglia', self)
        cut_action.setShortcut('Ctrl+X')
        cut_action.triggered.connect(self.text_edit.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction('Copia', self)
        copy_action.setShortcut('Ctrl+C')
        copy_action.triggered.connect(self.text_edit.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction('Incolla', self)
        paste_action.setShortcut('Ctrl+V')
        paste_action.triggered.connect(self.text_edit.paste)
        edit_menu.addAction(paste_action)

        undo_action = QAction('Annulla', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.text_edit.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction('Ripeti', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_action)

        # Crea le azioni per il menu "Formato"
        bold_action = QAction('Grassetto', self)
        bold_action.setCheckable(True)
        bold_action.triggered.connect(self.toggle_bold)
        format_menu.addAction(bold_action)

        italic_action = QAction('Corsivo', self)
        italic_action.setCheckable(True)
        italic_action.triggered.connect(self.toggle_italic)
        format_menu.addAction(italic_action)

        underline_action = QAction('Sottolineato', self)
        underline_action.setCheckable(True)
        underline_action.triggered.connect(self.toggle_underline)
        format_menu.addAction(underline_action)

        font_action = QAction('Cambia Carattere', self)
        font_action.triggered.connect(self.change_font)
        format_menu.addAction(font_action)

        text_color_action = QAction('Colore del Testo', self)
        text_color_action.triggered.connect(self.change_text_color)
        format_menu.addAction(text_color_action)

        # Crea le azioni per il menu "Strumenti"
        find_replace_action = QAction('Trova e Sostituisci', self)
        find_replace_action.setShortcut('Ctrl+F')
        find_replace_action.triggered.connect(self.show_find_replace_dialog)
        tools_menu.addAction(find_replace_action)

        word_count_action = QAction('Conta Parole', self)
        word_count_action.triggered.connect(self.count_words)
        tools_menu.addAction(word_count_action)

        # Crea un pulsante "Salva"
        save_button = QPushButton('Salva', self)
        save_button.clicked.connect(self.save_file)

        # Crea un layout per l'interfaccia
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(save_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Imposta le dimensioni e il titolo della finestra principale
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Editor di Testo')
        self.show()

    # Metodo per aprire un file
    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Apri File', '', 'File di Testo (*.txt);;Tutti i File (*)', options=options)

        if file_name:
            with open(file_name, 'r') as file:
                self.text_edit.setPlainText(file.read())

    # Metodo per salvare un file
    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Salva File', '', 'File di Testo (*.txt);;Tutti i File (*)', options=options)

        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_edit.toPlainText())

    # Metodo per attivare/disattivare il grassetto
    def toggle_bold(self):
        cursor = self.text_edit.textCursor()
        format = QTextCharFormat()
        format.setFontWeight(QFont.Bold if cursor.charFormat().fontWeight() == QFont.Normal else QFont.Normal)
        cursor.mergeCharFormat(format)
        self.text_edit.mergeCurrentCharFormat(format)

    # Metodo per attivare/disattivare il corsivo
    def toggle_italic(self):
        cursor = self.text_edit.textCursor()
        format = QTextCharFormat()
        format.setFontItalic(not cursor.charFormat().fontItalic())
        cursor.mergeCharFormat(format)
        self.text_edit.mergeCurrentCharFormat(format)

    # Metodo per attivare/disattivare il sottolineato
    def toggle_underline(self):
        cursor = self.text_edit.textCursor()
        format = QTextCharFormat()
        format.setFontUnderline(not cursor.charFormat().fontUnderline())
        cursor.mergeCharFormat(format)
        self.text_edit.mergeCurrentCharFormat(format)

    # Metodo per cambiare il tipo di carattere
    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            cursor = self.text_edit.textCursor()
            format = QTextCharFormat()
            format.setFont(font)
            cursor.mergeCharFormat(format)
            self.text_edit.mergeCurrentCharFormat(format)

    # Metodo per cambiare il colore del testo
    def change_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            cursor = self.text_edit.textCursor()
            format = QTextCharFormat()
            format.setForeground(color)
            cursor.mergeCharFormat(format)
            self.text_edit.mergeCurrentCharFormat(format)

    # Metodo per mostrare la finestra di "Trova e Sostituisci"
    def show_find_replace_dialog(self):
        find_text, ok = QInputDialog.getText(self, 'Trova', 'Trova:')
        if ok:
            cursor = self.text_edit.document().find(find_text)
            if cursor.isNull():
                QMessageBox.information(self, 'Trova', 'Testo non trovato.')
            else:
                self.text_edit.setTextCursor(cursor)
                self.text_edit.setFocus()

    # Metodo per contare le parole nel testo
    def count_words(self):
        text = self.text_edit.toPlainText()
        words = text.split()
        word_count = len(words)
        QMessageBox.information(self, 'Conteggio Parole', f'Il documento contiene {word_count} parole.')

# Punto di ingresso del programma
if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())
