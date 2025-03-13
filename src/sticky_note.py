from PyQt5.QtWidgets import QWidget, QPlainTextEdit
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QBrush, QColor, QPalette, QFont, QFontDatabase
from PyQt5.QtCore import QSettings
import os

class StickyNoteWidget(QWidget):
    settings = QSettings("StickyNotesSettings")
    
    def __init__(self):
        super().__init__()
        
        last_position = self.settings.value("position", QPoint())
        
        self.old_position = last_position
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(240, 240)
        self.move(last_position)
        
        self._renderTextEdit()
    
    def _renderTextEdit(self):
        # Font
        font_path = os.path.abspath('assets/fonts/Inter.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = "Arial" if font_id == -1 else QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font = QFont(font_family, 16)
        
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setGeometry(20, 20, self.width() - 40, self.height() - 40)
        self.text_edit.setWordWrapMode(True)
        self.text_edit.setFrameStyle(QPlainTextEdit.NoFrame)
        self.text_edit.setFont(font)
        
        # Palette
        palette = self.text_edit.palette()
        palette.setColor(QPalette.Base, QColor(255, 255, 255, 0)) # Transparent background
        palette.setColor(QPalette.Text, QColor(0, 0, 0, 200))  # Light text color
        
        self.text_edit.setPalette(palette)
        
        self._load_text()
        self.text_edit.textChanged.connect(self._save_text)
    
    def _save_text(self):
        self.settings.setValue("text_edit_content", self.text_edit.toPlainText())

    def _load_text(self):
        loaded_text = self.settings.value("text_edit_content", "")
        self.text_edit.setPlainText(loaded_text)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = event.globalPos() - self.old_position
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_position = event.globalPos()
            self.settings.setValue("position", self.pos())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(255, 226, 153, 255)))  # Sticky Note background color
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())
