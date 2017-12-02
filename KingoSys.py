from PyQt5.QtWidgets import QApplication
import sys
from tray_icon import TrayIcon

if __name__ == "__main__":

    app = QApplication(sys.argv)

    tray_icon = TrayIcon('crown.png')
    tray_icon.show()

    sys.exit(app.exec())