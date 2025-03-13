from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from sticky_note import StickyNoteWidget
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Sticky Notes")
    app.setWindowIcon(QIcon("assets/icon.png"))

    sticky_note = StickyNoteWidget()
    sticky_note.show()
    
    sys.exit(app.exec_())
