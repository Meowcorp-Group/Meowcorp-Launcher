# GNU GEMERAL PUBLIC LICENSE Version 3, 29 June 2007
#!/usr/bin/env python3

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

# Main Window
class LMainWindow(QMainWindow):
	# main function (basically)
	def __init__(self):
		# initialize main window ui
		super().__init__()
		loadUi("LMainWindow.ui", self)

if __name__ == "__main__":
	app = QApplication([])
	window = LMainWindow()
	window.show()
	app.exec()