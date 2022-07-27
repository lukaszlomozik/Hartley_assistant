from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog


def error_dialog(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setInformativeText(text)
    msg.setWindowTitle("Błąd")
    msg.exec_()


def message_dialog(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setInformativeText(text)
    msg.setWindowTitle("Info")
    msg.exec_()


def question_dialog(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle("Uwaga")
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return_value = msg.exec()
    if return_value == QMessageBox.Ok:
        return True
    else:
        return False


def file_dialog():
    path = QFileDialog.getOpenFileName(None, "Wczytywanie pliku", "C://", "XLSX files(*.xlsx)")
    path = str(path[0])
    return path
