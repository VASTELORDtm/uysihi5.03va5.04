import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QScrollArea, QPushButton


class BottomNavigationBarItem(QWidget):
    def __init__(self, photo: str):
        super().__init__()
        icon = QPixmap(photo)
        label = QLabel()
        label.setPixmap(icon.scaled(icon.width(), icon.height(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio))
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)


class BottomNavigationBar(QWidget):
    def __init__(self):
        super().__init__()
        item1 = BottomNavigationBarItem("assets2/home.svg")
        item2 = BottomNavigationBarItem("assets2/chat.svg")
        item3 = BottomNavigationBarItem("assets2/categories.svg")
        item4 = BottomNavigationBarItem("assets2/profile.svg")

        self.setStyleSheet("padding: 0;")
        layout = QHBoxLayout()
        layout.addWidget(item1)
        layout.addWidget(item2)
        layout.addWidget(item3)
        layout.addWidget(item4)

        self.setLayout(layout)
        self.setStyleSheet("background-color: #FD5D69; border-radius: 30px;")


class TopBar(QWidget):
    back_signal = pyqtSignal()  # Define the back signal

    def __init__(self, title: str):
        super().__init__()
        top_bar_layout = QHBoxLayout()
        top_bar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        top_right_layout = QHBoxLayout()

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.on_back_button_clicked)

        menu_title = QLabel(title)
        menu_title.setStyleSheet("color: #FD5D69; font-weight: bold; font-size: 24px;")

        notifications_button = QLabel()
        notifications_button.setPixmap(QPixmap('assets2/notification-button.svg'))

        search_button = QLabel()
        search_button.setPixmap(QPixmap('assets2/search-button.svg'))

        top_right_layout.addWidget(notifications_button)
        top_right_layout.addWidget(search_button)

        top_bar_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        top_bar_layout.addWidget(menu_title, alignment=Qt.AlignmentFlag.AlignCenter)
        top_bar_layout.addWidget(QWidget().setLayout(top_right_layout), alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(top_bar_layout)

    def on_back_button_clicked(self):
        self.back_signal.emit()  # Emit the back signal


class SecondMenu(QWidget):
    def __init__(self, go_back_callback):
        super().__init__()
        self.go_back_callback = go_back_callback

        layout = QVBoxLayout()
        layout.addWidget(TopBar("Second Menu"))

        # Replicate the main menu's layout here
        seafood_label = QLabel("Seafood")
        seafood_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        seafood_label.setStyleSheet("color: gray; font-size: 24px;")

        seafood_pixmap = QPixmap('assets2/seafood.png').scaled(800, 400, Qt.AspectRatioMode.KeepAspectRatio)
        image_label = QLabel()
        image_label.setPixmap(seafood_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        images_layout = QHBoxLayout()

        self.createImageButton(images_layout, 'assets2/lunch.png', "Lunch")
        self.createImageButton(images_layout, 'assets2/breakfast.png', "Breakfast")

        additional_images_layout = QHBoxLayout()
        self.createImageButton(additional_images_layout, 'assets2/dinner.png', "Dinner")
        self.createImageButton(additional_images_layout, 'assets2/vegan.png', "Vegan")

        drinks_layout = QHBoxLayout()
        self.createImageButton(drinks_layout, 'assets2/dessert.png', "Dessert")
        self.createImageButton(drinks_layout, 'assets2/drinks.png', "Drinks")

        layout.addWidget(seafood_label)
        layout.addWidget(image_label)
        layout.addLayout(images_layout)
        layout.addLayout(additional_images_layout)
        layout.addLayout(drinks_layout)

        layout.addStretch()
        self.setLayout(layout)

    def createImageButton(self, layout, image_path, label_text):
        pixmap = QPixmap(image_path).scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel(label_text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: gray; font-size: 20px")

        button = QWidget()
        button_layout = QVBoxLayout(button)
        button_layout.addWidget(image_label)
        button_layout.addWidget(label)

        layout.addWidget(button)

        # Connect the button click to navigate to the second menu
        button.mousePressEvent = lambda event: self.go_back_callback()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1000, 800)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.addWidget(TopBar("Main Menu"))

        # Set up the main content
        self.setupMainContent()

        self.scroll_area.setWidget(self.main_widget)

        self.setStyleSheet("padding: 20px")
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)

        bottom_nav_bar = BottomNavigationBar()
        layout.addWidget(bottom_nav_bar, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setWindowTitle('My Figma Project')

    def setupMainContent(self):
        seafood_label = QLabel("Seafood")
        seafood_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        seafood_label.setStyleSheet("color: gray; font-size: 24px;")

        seafood_pixmap = QPixmap('assets2/seafood.png').scaled(800, 400, Qt.AspectRatioMode.KeepAspectRatio)
        image_label = QLabel()
        image_label.setPixmap(seafood_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        images_layout = QHBoxLayout()

        self.createImageButton(images_layout, 'assets2/lunch.png', "Lunch")
        self.createImageButton(images_layout, 'assets2/breakfast.png', "Breakfast")

        additional_images_layout = QHBoxLayout()
        self.createImageButton(additional_images_layout, 'assets2/dinner.png', "Dinner")
        self.createImageButton(additional_images_layout, 'assets2/vegan.png', "Vegan")

        drinks_layout = QHBoxLayout()
        self.createImageButton(drinks_layout, 'assets2/dessert.png', "Dessert")
        self.createImageButton(drinks_layout, 'assets2/drinks.png', "Drinks")

        self.main_layout.addWidget(seafood_label)
        self.main_layout.addWidget(image_label)
        self.main_layout.addLayout(images_layout)
        self.main_layout.addLayout(additional_images_layout)
        self.main_layout.addLayout(drinks_layout)

        self.main_layout.addStretch()

    def createImageButton(self, layout, image_path, label_text):
        pixmap = QPixmap(image_path).scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio)
        image_label = QLabel()
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel(label_text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: gray; font-size: 20px")

        button = QWidget()
        button_layout = QVBoxLayout(button)
        button_layout.addWidget(image_label)
        button_layout.addWidget(label)

        layout.addWidget(button)

        # Connect the button click to navigate to the second menu
        button.mousePressEvent = lambda event: self.showSecondMenu()

    def showSecondMenu(self):
        self.second_menu = SecondMenu(self.showMainMenu)
        self.scroll_area.setWidget(self.second_menu)

        # Ensure the TopBar is instantiated properly
        top_bar = self.second_menu.findChild(TopBar)
        if top_bar:
            top_bar.back_signal.connect(self.showMainMenu)

        self.second_menu.findChild(TopBar).back_signal.connect(self.showMainMenu)

    def showMainMenu(self):
        self.scroll_area.setWidget(self.main_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
