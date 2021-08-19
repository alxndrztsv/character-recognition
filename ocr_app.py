import easyocr
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, \
    QPushButton, QFileDialog, QPlainTextEdit, \
    QLabel, QWidget, QVBoxLayout, QHBoxLayout


class FileDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FileDialogDemo, self).__init__(parent)

        self.image_path = ''

        # create 3 buttons;
        btn_select_file = QPushButton('Select Image')
        btn_select_file.resize(50, 50)
        btn_transform = QPushButton('Transform')
        btn_transform.resize(50, 50)

        # add buttons to a horizontal layout;
        h_layout = QHBoxLayout()
        h_layout.addWidget(btn_select_file)
        h_layout.addStretch()
        h_layout.addWidget(btn_transform)

        # create space for image;
        self.label = QLabel()

        # create text area;
        self.txt_output = QPlainTextEdit()

        # add everything to a vertical layout;
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.label, alignment=Qt.AlignCenter)
        v_layout.addWidget(self.txt_output)

        self.setLayout(v_layout)

        # functionality for the buttons;
        btn_select_file.clicked.connect(self.select_file)
        btn_transform.clicked.connect(self.recognize_text)

    def select_file(self):
        """ Function to select file. """
        file_name = QFileDialog.getOpenFileName(self, 'Open file',
                                                'D:/')
        self.image_path = file_name[0]
        # show the resized image instead of the label;
        self.label.setPixmap(QPixmap(self.image_path)
                             .scaled(500, 500, Qt.KeepAspectRatio, Qt.FastTransformation))

    def recognize_text(self):
        """ Function to recognize the text. """
        reader = easyocr.Reader(['en'], gpu=False)
        # save the result of processed image;
        result = reader.readtext(self.image_path)
        text = []
        # loop through the detected values;
        for detection in result:
            # each word append to text list;
            word = detection[1]
            text.append(word)
        # clear if there is text from before;
        self.txt_output.clear()
        # join all the words together;
        self.txt_output.insertPlainText(' '.join(text).strip())


def main():
    app = QApplication(sys.argv)
    window = FileDialogDemo()
    # show the window;
    window.show()
    # start the event loop;
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
