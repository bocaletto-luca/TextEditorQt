#!/usr/bin/env python3
# Author: Bocaletto Luca
# Programming Language: Python
# Interface Language: English
# License: GPLv3

# Import the sys module to handle command line arguments
import sys

# Import the necessary PyQt5 classes and modules for creating the user interface
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

# Definition of the main text editor class
class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize the user interface
        self.init_ui()

    def init_ui(self):
        # Create the main text area
        self.text_area = QPlainTextEdit(self)
        self.setCentralWidget(self.text_area)

        # Create the menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        edit_menu = menubar.addMenu('Edit')
        format_menu = menubar.addMenu('Format')
        tools_menu = menubar.addMenu('Tools')

        # Create actions for the "File" menu
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # Create actions for the "Edit" menu
        cut_action = QAction('Cut', self)
        cut_action.setShortcut('Ctrl+X')
        cut_action.triggered.connect(self.text_area.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction('Copy', self)
        copy_action.setShortcut('Ctrl+C')
        copy_action.triggered.connect(self.text_area.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction('Paste', self)
        paste_action.setShortcut('Ctrl+V')
        paste_action.triggered.connect(self.text_area.paste)
        edit_menu.addAction(paste_action)

        undo_action = QAction('Undo', self)
        undo_action.setShortcut('Ctrl+Z')
        undo_action.triggered.connect(self.text_area.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction('Redo', self)
        redo_action.setShortcut('Ctrl+Y')
        redo_action.triggered.connect(self.text_area.redo)
        edit_menu.addAction(redo_action)

        # Create actions for the "Format" menu
        bold_action = QAction('Bold', self)
        bold_action.setCheckable(True)
        bold_action.triggered.connect(self.toggle_bold)
        format_menu.addAction(bold_action)

        italic_action = QAction('Italic', self)
        italic_action.setCheckable(True)
        italic_action.triggered.connect(self.toggle_italic)
        format_menu.addAction(italic_action)

        underline_action = QAction('Underline', self)
        underline_action.setCheckable(True)
        underline_action.triggered.connect(self.toggle_underline)
        format_menu.addAction(underline_action)

        font_action = QAction('Change Font', self)
        font_action.triggered.connect(self.change_font)
        format_menu.addAction(font_action)

        text_color_action = QAction('Text Color', self)
        text_color_action.triggered.connect(self.change_text_color)
        format_menu.addAction(text_color_action)

        # Create actions for the "Tools" menu
        find_replace_action = QAction('Find and Replace', self)
        find_replace_action.setShortcut('Ctrl+F')
        find_replace_action.triggered.connect(self.show_find_replace_dialog)
        tools_menu.addAction(find_replace_action)

        word_count_action = QAction('Word Count', self)
        word_count_action.triggered.connect(self.count_words)
        tools_menu.addAction(word_count_action)

        # Create a "Save" button
        save_button = QPushButton('Save', self)
        save_button.clicked.connect(self.save_file)

        # Create a layout for the interface
        layout = QVBoxLayout()
        layout.addWidget(self.text_area)
        layout.addWidget(save_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Set the dimensions and the title of the main window
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Text Editor')
        self.show()

    # Method to open a file
    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if file_name:
            with open(file_name, 'r') as file:
                self.text_area.setPlainText(file.read())

    # Method to save a file
    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.text_area.toPlainText())

    # Method to toggle bold formatting
    def toggle_bold(self):
        cursor = self.text_area.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Bold if cursor.charFormat().fontWeight() == QFont.Normal else QFont.Normal)
        cursor.mergeCharFormat(fmt)
        self.text_area.mergeCurrentCharFormat(fmt)

    # Method to toggle italic formatting
    def toggle_italic(self):
        cursor = self.text_area.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontItalic(not cursor.charFormat().fontItalic())
        cursor.mergeCharFormat(fmt)
        self.text_area.mergeCurrentCharFormat(fmt)

    # Method to toggle underline formatting
    def toggle_underline(self):
        cursor = self.text_area.textCursor()
        fmt = QTextCharFormat()
        fmt.setFontUnderline(not cursor.charFormat().fontUnderline())
        cursor.mergeCharFormat(fmt)
        self.text_area.mergeCurrentCharFormat(fmt)

    # Method to change the font
    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            cursor = self.text_area.textCursor()
            fmt = QTextCharFormat()
            fmt.setFont(font)
            cursor.mergeCharFormat(fmt)
            self.text_area.mergeCurrentCharFormat(fmt)

    # Method to change the text color
    def change_text_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            cursor = self.text_area.textCursor()
            fmt = QTextCharFormat()
            fmt.setForeground(color)
            cursor.mergeCharFormat(fmt)
            self.text_area.mergeCurrentCharFormat(fmt)

    # Method to show the "Find and Replace" dialog
    def show_find_replace_dialog(self):
        find_text, ok = QInputDialog.getText(self, 'Find', 'Find:')
        if ok:
            cursor = self.text_area.document().find(find_text)
            if cursor.isNull():
                QMessageBox.information(self, 'Find', 'Text not found.')
            else:
                self.text_area.setTextCursor(cursor)
                self.text_area.setFocus()

    # Method to count the words in the text
    def count_words(self):
        text = self.text_area.toPlainText()
        words = text.split()
        word_count = len(words)
        QMessageBox.information(self, 'Word Count', f'The document contains {word_count} words.')

# Entry point of the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = TextEditor()
    sys.exit(app.exec_())
