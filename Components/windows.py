import os, sys, json
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from .utils import login_user, validate_registration_input, logout_user, validate_dish_input
from .custom_components import CustomListItem
from .Dishes.Starter import Starter
from .Dishes.MainDish import MainDish
from .Dishes.Dessert import Dessert
from .Dishes.Dish import Dish
from connector import Connector

# Stałe które będą często wykorzystywane w programie
LIGHT_THEME = None
LANGUAGE = None
STYLE_SHEET = None

class MainWindow(QMainWindow):
    def __init__(self, title: str):     #, x: int, y: int, width: int, height: int):
        super().__init__()
        self.setWindowTitle(title)
        # self.setGeometry(x, y, width, height)
        self.get_style_sheets()
        self.get_settings()
        self.InitUI()

    def InitUI(self):
        if LIGHT_THEME:
            self.setStyleSheet(f"{STYLE_SHEET['light-theme']['background-color']} {STYLE_SHEET['light-theme']['text-color-1']} {STYLE_SHEET['light-theme']['borders']}")
        else:
            self.setStyleSheet(f"{STYLE_SHEET['dark-theme']['background-color']} {STYLE_SHEET['dark-theme']['text-color-1']} {STYLE_SHEET['dark-theme']['borders']}")

        login_page_btn = QPushButton('Login', self)
        login_page_btn.setGeometry(700, 100, 500, 60)
        login_page_btn.clicked.connect(self.LoginButton_onClick)
        
        options_page_btn = QPushButton("Options", self)
        options_page_btn.setGeometry(700, 200, 500, 60)
        options_page_btn.clicked.connect(self.OptionsButton_onClick)

        exit_btn = QPushButton('Exit', self)
        exit_btn.setGeometry(700, 300, 500, 60)
        exit_btn.clicked.connect(self.ExitButton_onClick)

        self.showMaximized()

    @pyqtSlot()
    def LoginButton_onClick(self):
        self.windows = LoginWindow()
        self.windows.showMaximized()
        self.close()

    @pyqtSlot()
    def OptionsButton_onClick(self):
        self.windows = OptionsWindow() 
        self.windows.showMaximized()
        self.close()

    @pyqtSlot()
    def ExitButton_onClick(self):
        self.close()
        exit(0)

    def get_style_sheets(self, filepath: str = os.getcwd().replace('\\', '/') + "/Data/style_sheets.json"):
        global STYLE_SHEET

        with open(filepath, 'r', encoding='utf8', errors="ignore") as in_file:
            STYLE_SHEET = json.load(in_file)
        

    def get_settings(self, filepath: str = os.getcwd().replace('\\', '/') + "/Data/settings.json"):
        global LIGHT_THEME, LANGUAGE

        with open(filepath, 'r', encoding='utf8', errors="ignore") as in_file:
            settings = json.load(in_file)

        LIGHT_THEME = settings["LIGHT_THEME"]
        LANGUAGE = settings["LANGUAGE"]

class LoginWindow(QDialog):
    def __init__(self, value = None, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Login')
        self.setMinimumSize(300,400)
        self.setMaximumSize(500,600)

        self.connector = Connector()

        if LIGHT_THEME:
            self.setStyleSheet(f"{STYLE_SHEET['light-theme']['background-color']} {STYLE_SHEET['light-theme']['text-color-1']} ")
        else:
            self.setStyleSheet(f"{STYLE_SHEET['dark-theme']['background-color']} {STYLE_SHEET['dark-theme']['text-color-1']} ")
        
        layoutV = QVBoxLayout()

        layoutV.setSpacing(10)
        layoutV.setContentsMargins(10,10,10,10)

        self.username_label = QLabel('Nazwa użytkownika:', self)
        self.username_label.setFont(QFont("Arial", 12))
        layoutV.addWidget(self.username_label)

        self.username_input = QLineEdit(self)
        self.username_input.setFont(QFont("Arial", 20))
        layoutV.addWidget(self.username_input)

        self.password_label = QLabel('Hasło:', self)
        self.password_label.setFont(QFont("Arial", 12))
        layoutV.addWidget(self.password_label)

        self.password_input = QLineEdit(self)
        self.password_input.setFont(QFont("Arial", 20))
        layoutV.addWidget(self.password_input)

        self.label = QLabel("Nie posiadasz konta?", self)
        self.label.setFont(QFont("Arial", 12))
        layoutV.addWidget(self.label)

        self.register_page_btn = QPushButton("Zarejestruj się", self)
        self.register_page_btn.setStyleSheet("QPushButton {border: none;}")
        self.register_page_btn.setFont(QFont("Arial", 12))
        self.register_page_btn.clicked.connect(self.register_page_onClick)
        layoutV.addWidget(self.register_page_btn)

        self.login_button = QPushButton('Zaloguj', self)
        self.login_button.setFont(QFont("Arial", 12))
        self.login_button.clicked.connect(self.login_onClick)
        layoutV.addWidget(self.login_button)

        self.back_btn = QPushButton('Back to Main Window!', self)
        self.back_btn.setFont(QFont("Arial", 12))
        self.back_btn.clicked.connect(self.MainWindowButton_onClick)
        layoutV.addWidget(self.back_btn)

        self.setLayout(layoutV)

    def login_onClick(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if login_user(username, password, self.connector):
            self.windows = MenuEditingWindow(username)
            self.windows.showMaximized()
            self.close()

    def register_page_onClick(self):
        self.windows = RegisterWindow()
        self.windows.showMaximized()
        self.close() 

    def MainWindowButton_onClick(self):
        self.windows = MainWindow("Aplikacja Restauracji")
        self.windows.showMaximized()
        self.close() 

class OptionsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Options')

        if LIGHT_THEME:
            self.setStyleSheet(f"{STYLE_SHEET['light-theme']['background-color']} {STYLE_SHEET['light-theme']['text-color-1']} ")
        else:
            self.setStyleSheet(f"{STYLE_SHEET['dark-theme']['background-color']} {STYLE_SHEET['dark-theme']['text-color-1']} ")

        # screen = QApplication.primaryScreen()
        # screen_geometry = screen.availableGeometry()
        # self.setMaximumSize(screen_geometry.width(), screen_geometry.height())

        layoutV = QVBoxLayout()
        layoutV.setSpacing(10)
        layoutV.setContentsMargins(400,10,400,100)
        layoutV.setAlignment(Qt.AlignHCenter)

        self.label = QLabel('OPTIONS', self)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.label.setFont(QFont("Arial", 12))
        layoutV.addWidget(self.label)

        self.toggle_theme_label = QLabel('Toggle Theme', self)
        self.toggle_theme_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.toggle_theme_label.setFont(QFont('Arial', 12))
        layoutV.addWidget(self.toggle_theme_label)

        self.theme_icon = QLabel("Light")
        self.theme_icon.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.theme_icon.resize(100, 100)
        self.theme_icon.setStyleSheet("border : 1px solid black; border-radius: 5px; font-weight: bold; font-size: 16px; background-color: white")
        layoutV.addWidget(self.theme_icon)

        self.theme_slider = QSlider(Qt.Horizontal, self)
        self.theme_slider.setMinimum(0)
        self.theme_slider.setMaximum(1)
        if LIGHT_THEME:
            self.theme_slider.setValue(0)
        else:
            self.theme_slider.setValue(1)
        self.theme_slider.setTickInterval(1)
        self.theme_slider.setTickPosition(QSlider.TicksBelow)
        self.theme_slider.valueChanged.connect(self.change_theme)
        self.theme_slider.setFixedSize(200, 20)
        layoutV.addWidget(self.theme_slider)

        self.setLayout(layoutV)

        self.language_label = QLabel("Change language", self)
        self.language_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.language_label.setFont(QFont('Arial', 12))
        layoutV.addWidget(self.language_label)

        self.image_container = QLabel(self)
        self.image_container.setAlignment(Qt.AlignHCenter)
        self.image_container.setPixmap(QPixmap('Static/Images/Icons/EnglishFlag.png'))
        layoutV.addWidget(self.image_container)

        self.language_combobox = QComboBox()
        self.language_combobox.addItem("English")
        self.language_combobox.addItem("Polish")
        self.language_combobox.addItem("Ukrainian")
        self.language_combobox.setFixedSize(200,20)
        self.language_combobox.currentTextChanged.connect(self.on_language_changed)
        layoutV.addWidget(self.language_combobox)

        # Dodaje toggle
        self.toggle_audio_label = QLabel("Toggle Audio",self)
        self.toggle_audio_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.toggle_audio_label.setFont(QFont('Arial', 12))
        layoutV.addWidget(self.toggle_audio_label)

        # Obrazek dzwięku (zmienia się gdy zmienia się volume, dzwięk ma być takim przyciskiem)
        self.volume_icon = QLabel(self)
        self.volume_icon.setAlignment(Qt.AlignHCenter)
        self.volume_icon.setPixmap(QPixmap('Static/Images/Icons/NoVolume.png'))
        layoutV.addWidget(self.volume_icon)

        # Dodaje Button (tekst się zmienia jak klikam oraz zmienia się wtedy obraz głośnika)
        self.volume_btn = QPushButton("Volume: OFF", self)
        self.volume_btn.clicked.connect(self.change_volume)
        layoutV.addWidget(self.volume_btn)

        self.window_size_label = QLabel("Change aspect ratio",self)
        self.window_size_label.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.window_size_label.setFont(QFont('Arial', 12))
        layoutV.addWidget(self.window_size_label)

        # Ustawienia rozmiaru okna (combobox jak w języku, ale początkowy rozmiar to maximized)
        self.window_size_combobox = QComboBox()
        self.window_size_combobox.addItem("Maximized")
        self.window_size_combobox.addItem("Fullscreen")
        self.window_size_combobox.addItem("Window mode")
        self.window_size_combobox.setFixedSize(200,20)
        self.window_size_combobox.currentTextChanged.connect(self.on_size_changed)
        layoutV.addWidget(self.window_size_combobox)

        self.back_btn = QPushButton('Back to Main Window!', self)
        self.back_btn.setFont(QFont("Arial", 12))
        self.back_btn.clicked.connect(self.MainWindowButton_onClick)
        layoutV.addWidget(self.back_btn)

        self.setLayout(layoutV)

    def MainWindowButton_onClick(self):
        self.windows = MainWindow("Aplikacja Restauracji")
        self.windows.showMaximized()
        self.close() 

    def change_theme(self, value):
        global LIGHT_THEME
        filepath = os.getcwd().replace('\\', '/') + "/Data/settings.json"
        # Wartość 0 oznacza motyw jasny, a wartość 1 oznacza motyw ciemny
        if value == 0:
            self.setStyleSheet("background-color: rgb(240,240,240); color: #333;")
            self.theme_icon.setStyleSheet("border : 1px solid black; border-radius: 5px; font-weight: bold; font-size: 16px; background-color: white; color: black")
            self.theme_icon.setText("Light")
        else:
            self.setStyleSheet("background-color: #1e1e1e; color: #f8f8f8;")
            self.theme_icon.setStyleSheet("border : 1px solid white; border-radius: 5px; font-weight: bold; font-size: 16px; background-color: black; color: white")
            self.theme_icon.setText("Dark")

        LIGHT_THEME ^= True
        # Zmiana wartości LIGHT_THEME w settings.json żeby to nadpisać
        with open(filepath, 'w', encoding='utf8') as out_file:
            json.dump({"LIGHT_THEME": LIGHT_THEME, "LANGUAGE" : LANGUAGE}, out_file, indent=4)

    # Funkcja obsługująca zmiane tekstu w combobox
    def on_language_changed(self):
        # Zmiana obrazu containera
        if self.language_combobox.currentText() == "English":
            self.image_container.setPixmap(QPixmap('Static/Images/Icons/EnglishFlag.png'))
        elif self.language_combobox.currentText() == "Polish":
            self.image_container.setPixmap(QPixmap('Static/Images/Icons/PolishFlag.png'))
        elif self.language_combobox.currentText() == "Ukrainian":
            self.image_container.setPixmap(QPixmap('Static/Images/Icons/UkrainianFlag.png'))
        

    def change_volume(self):
        if self.volume_btn.text() == "Volume: OFF":
            self.volume_btn.setText("Volume: ON")
            self.volume_icon.setPixmap(QPixmap('Static/Images/Icons/VolumeUp.png'))

        elif self.volume_btn.text() == "Volume: ON":
            self.volume_btn.setText("Volume: OFF")
            self.volume_icon.setPixmap(QPixmap('Static/Images/Icons/NoVolume.png'))

    def on_size_changed(self):
        if self.window_size_combobox.currentText() == "Maximized":
            self.showMaximized()    # BUG: Przekracza rozmiar!
        elif self.window_size_combobox.currentText() == "Fullscreen":
            self.showFullScreen()
        else:
            self.showNormal()

class RegisterWindow(QDialog):
    def __init__(self, value = None, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Register')
        self.setMinimumSize(300,400)
        self.setMaximumSize(500,600)

        self.connector = Connector()

        if LIGHT_THEME:
            self.setStyleSheet(f"{STYLE_SHEET['light-theme']['background-color']} {STYLE_SHEET['light-theme']['text-color-1']} ")
        else:
            self.setStyleSheet(f"{STYLE_SHEET['dark-theme']['background-color']} {STYLE_SHEET['dark-theme']['text-color-1']} ")

        layoutV = QVBoxLayout()
        layoutV.setSpacing(10)
        layoutV.setContentsMargins(10,10,10,10)


        self.username_label = QLabel('Nazwa użytkownika:', self)
        self.username_label.setFont(QFont("Arial", 12))
        layoutV.addWidget(self.username_label)

        self.username_input = QLineEdit(self)
        self.username_input.setFont(QFont("Arial", 20))
        layoutV.addWidget(self.username_input)

        self.password_label = QLabel('Hasło:', self)
        self.password_label.setFont(QFont("Arial", 12))
        layoutV.addWidget(self.password_label)

        self.password_input = QLineEdit(self)
        self.password_input.setFont(QFont("Arial", 20))
        layoutV.addWidget(self.password_input)

        self.confirm_password_label = QLabel('Potwierdź hasło:', self)
        self.confirm_password_label.setFont(QFont("Arial", 12))
        layoutV.addWidget(self.confirm_password_label)

        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setFont(QFont("Arial", 12))
        layoutV.addWidget(self.confirm_password_input)

        self.label_2 = QLabel("Posiadasz konto?", self)
        self.label_2.setFont(QFont("Arial", 12))
        layoutV.addWidget(self.label_2)

        self.login_page_btn = QPushButton("Zaloguj się", self)
        self.login_page_btn.setFont(QFont("Arial", 12))
        self.login_page_btn.setStyleSheet("QPushButton {border: none;}")
        self.login_page_btn.clicked.connect(self.login_page_onClick)
        layoutV.addWidget(self.login_page_btn)

        self.rejestr_button = QPushButton('Załóż konto', self)
        self.rejestr_button.setFont(QFont("Arial", 12))
        self.rejestr_button.clicked.connect(self.register_user_onClick)
        layoutV.addWidget(self.rejestr_button)

        self.back_btn = QPushButton('Back to Main Window!', self)
        self.back_btn.setFont(QFont("Arial", 12))
        self.back_btn.clicked.connect(self.MainWindowButton_onClick)
        layoutV.addWidget(self.back_btn)
        
        self.setLayout(layoutV)

    def register_user_onClick(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        validation_error = validate_registration_input(username, password, confirm_password)
        if validation_error is not None:
            QMessageBox.warning(self, "Błąd walidacji", validation_error)
            return

        if self.connector.add_user(username, password):
            # self.hide()
            self.windows = MenuEditingWindow(username)
            self.windows.showMaximized()
            self.close()
        else:
            QMessageBox.warning(self, "Błąd rejestracji")


    def login_page_onClick(self):
        self.windows = LoginWindow()
        self.windows.showMaximized()
        self.close() 

    def MainWindowButton_onClick(self):
        self.windows = MainWindow("Aplikacja Restauracji")
        self.windows.showMaximized()
        self.close()

class MenuEditingWindow(QDialog):
    def __init__(self, logged_username, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Menu Editing Screen")
        self.setMinimumSize(1400,800)
        self.setMaximumSize(1600,800)
        self.programmatic_close = False
        self.logged_username = logged_username

        self.connector = Connector()

        if LIGHT_THEME:
            self.setStyleSheet(f"{STYLE_SHEET['light-theme']['background-color']} {STYLE_SHEET['light-theme']['text-color-1']} ")
        else:
            self.setStyleSheet(f"{STYLE_SHEET['dark-theme']['background-color']} {STYLE_SHEET['dark-theme']['text-color-1']} ")

        # Grid layout zawierający dwie kolumny i jeden wiersz. (lewa kolumna zajmuje 1/3 gridlayoutu a prawa kolumna 2/3)
        grid = QGridLayout()
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 2)

        # Lewa część layoutu -----------------------------------------------------
        left_vbox = QVBoxLayout()

        # Starters vbox ------------------------
        starters_vbox = QVBoxLayout()
        starters_label = QLabel('Starters')
        starters_label.setStyleSheet('font-weight: bold')
        starters_vbox.addWidget(starters_label)

        self.starters_list = QListWidget()

        for starter in self.connector.get_all_starters():
            component = CustomListItem(starter["name"], f'{starter["price"]["price_usd"]} $')
            component.remove_button_clicked.connect(self.remove_starter)
            component.edit_button_clicked.connect(self.edit_starter)
            list_item = QListWidgetItem(self.starters_list)
            self.starters_list.addItem(list_item)
            list_item.setSizeHint(component.minimumSizeHint())
            self.starters_list.setItemWidget(list_item, component)

        starters_vbox.addWidget(self.starters_list)
        # --------------------------------------

        # Mains vbox ---------------------------
        mains_vbox = QVBoxLayout()
        mains_label = QLabel('Mains')
        mains_label.setStyleSheet('font-weight: bold')
        mains_vbox.addWidget(mains_label)

        self.mains_list = QListWidget()

        for main in self.connector.get_all_mains():
            component = CustomListItem(main["name"], f'{main["price"]["price_usd"]} $')
            component.remove_button_clicked.connect(self.remove_main)
            component.edit_button_clicked.connect(self.edit_main)
            list_item = QListWidgetItem(self.mains_list)
            self.mains_list.addItem(list_item)
            list_item.setSizeHint(component.minimumSizeHint())
            self.mains_list.setItemWidget(list_item, component)

        mains_vbox.addWidget(self.mains_list)
        # --------------------------------------

        # Desserts vbox ------------------------
        desserts_vbox = QVBoxLayout()
        desserts_label = QLabel('Desserts')
        desserts_label.setStyleSheet('font-weight: bold')
        desserts_vbox.addWidget(desserts_label)

        self.desserts_list = QListWidget()

        for dessert in self.connector.get_all_desserts():
            component = CustomListItem(dessert["name"], f'{dessert["price"]["price_usd"]} $')
            component.remove_button_clicked.connect(self.remove_dessert)
            component.edit_button_clicked.connect(self.edit_dessert)
            list_item = QListWidgetItem(self.desserts_list)
            self.desserts_list.addItem(list_item)
            list_item.setSizeHint(component.minimumSizeHint())
            self.desserts_list.setItemWidget(list_item, component)

        desserts_vbox.addWidget(self.desserts_list)
        # --------------------------------------

        left_vbox.addLayout(starters_vbox)
        left_vbox.addLayout(mains_vbox)
        left_vbox.addLayout(desserts_vbox)

        grid.addLayout(left_vbox, 0, 0)
        # -------------------------------------------------------------------------

        # Prawa część layoutu - Add Item
        right_layout = QGridLayout()
        
        self.layout_title = QLabel("Add dish")
        self.layout_title.setStyleSheet('font-weight: bold')
        right_layout.addWidget(self.layout_title,0,1)

        self.category_combobox = QComboBox()
        self.category_combobox.addItem(" -- Select a Category --")
        self.category_combobox.addItem("starters")
        self.category_combobox.addItem("mains")
        self.category_combobox.addItem("desserts")
        right_layout.addWidget(self.category_combobox,1,1)

        self.dish_name = QLineEdit()
        self.dish_name.setPlaceholderText("Insert the name of the dish")
        right_layout.addWidget(self.dish_name,2,1)

        # TODO: Add to QHBoxLayout
        
        self.cost = QLineEdit()
        self.cost.setPlaceholderText("Insert the cost of the dish")
        right_layout.addWidget(self.cost,3,1)

        self.currency = QComboBox()
        self.currency.addItem (" -- Currency --")
        self.currency.addItem ("PLN")
        self.currency.addItem ("USD")
        self.currency.addItem ("EURO")
        right_layout.addWidget(self.currency,3,2)

        self.description = QTextEdit()
        self.description.setPlaceholderText("Insert the description of the dish")
        right_layout.addWidget(self.description,4,1)

        self.ingredients = QTextEdit()
        self.ingredients.setPlaceholderText("Insert the ingredients of the dish")
        right_layout.addWidget(self.ingredients,5,1)

        self.radio_1 = QRadioButton("Vegan")
        self.radio_2 = QRadioButton("Vegetarian")
        self.radio_3 = QRadioButton("Meat")
        right_layout.addWidget(self.radio_1,6,1)
        right_layout.addWidget(self.radio_2,7,1)
        right_layout.addWidget(self.radio_3,8,1)

        self.cuisine = QComboBox()
        self.cuisine.addItem (" -- Select a cuisine --")
        self.cuisine.addItem ("Bulgarian")
        self.cuisine.addItem ("Italian")
        self.cuisine.addItem ("Polish")
        self.cuisine.addItem ("Spanish")
        self.cuisine.addItem ("Ukrainian")
        right_layout.addWidget(self.cuisine,9,1)

        self.add_button = QPushButton("Add dish")
        self.add_button.setFixedSize(200, 50)
        self.add_button.clicked.connect(self.onClick_add_button)
        right_layout.addWidget (self.add_button,10,1,alignment=Qt.AlignCenter)

        grid.addLayout(right_layout, 0, 1)

        self.setLayout(grid)

    def onClick_add_button(self):
        if self.add_button.text() == "Edit dish":
            self.connector.remove_dish(self.dish_to_edit.name, self.category_before)
        informations = self.get_all_info()
        if informations[0] == "starters":
            dish = Starter(informations[1], f"{informations[2]} {informations[3]}", informations[4], informations[5], informations[6], informations[7])
        elif informations[0] == "mains":
            dish = MainDish(informations[1], f"{informations[2]} {informations[3]}", informations[4], informations[5], informations[6], informations[7])
        elif informations[0] == "desserts":
            dish = Dessert(informations[1], f"{informations[2]} {informations[3]}", informations[4], informations[5], informations[6], informations[7])
        else:
            print("ERROR: windows.py -> MenuEditingWindow -> onClick_add_button: Unrecognized category")
            return
        
        if validate_dish_input(dish.get_dictionary_data()) == True:
            self.connector.add_dish(dish.get_tuple_data(), informations[0])
            self.update_gui()
        else:
            print("ERROR: windows.py -> MenuEditingWindow -> onClick_add_button: Dish not validated.")

    def edit_starter(self):
        sender = self.sender()
        self.dish_to_edit = self.connector.get_dish(sender.name_label.text(), "starters")
        self.category_before = "starters"
        self.set_all_info(self.dish_to_edit, "starters")
        self.add_button.setText("Edit dish")
    
    def edit_main(self):
        sender = self.sender()
        self.dish_to_edit = self.connector.get_dish(sender.name_label.text(), "mains")
        self.category_before = "mains"
        self.set_all_info(self.dish_to_edit, "mains")
        self.add_button.setText("Edit dish")

    def edit_dessert(self):
        sender = self.sender()
        self.dish_to_edit = self.connector.get_dish(sender.name_label.text(), "desserts")
        self.category_before = "desserts"
        self.set_all_info(self.dish_to_edit, "desserts")
        self.add_button.setText("Edit dish")

    def remove_starter(self):
        sender = self.sender()
        self.connector.remove_dish((sender.name_label.text(),), "starters")
        self.update_gui()

    def remove_main(self):
        sender = self.sender()
        self.connector.remove_dish((sender.name_label.text(),), "mains")
        self.update_gui()

    def remove_dessert(self):
        sender = self.sender()
        self.connector.remove_dish((sender.name_label.text(),), "desserts")
        self.update_gui()

    def set_all_info(self, dish: Dish, category: str) -> None:
        dish_data = dish.get_dictionary_data()

        # Ustawianie tekstu w combobox
        category_index = self.category_combobox.findText(category)
        self.category_combobox.setCurrentIndex(category_index)

        # Ustawianie tekstu nazwy dania
        self.dish_name.setText(dish_data["name"])
        
        # Ustawianie tekstu w polu kosztu dania
        self.cost.setText(str(dish_data["price"]["price_usd"]))

        # Ustawianie tekstu w polu waluty dania (Na dolary)
        self.currency.setCurrentIndex(2)

        # Ustawianie tekstu w polu opisu dania
        self.description.setText(dish_data["description"])

        # Ustawianie tekstu w polu składników dania
        self.ingredients.setText(",".join(dish_data["ingredients"]))

        # Ustawianie wartości radio button dla rodzaju dania
        if dish_data["diet_type"] == "Vegan":
            self.radio_1.setChecked(True)
        elif dish_data["diet_type"] == "Vegetarian":
            self.radio_2.setChecked(True)
        else:
            self.radio_3.setChecked(True)

        # Ustawianie tekstu rodzaju kuchni dla dania
        cuisine_index = self.cuisine.findText(dish_data["cuisine"])
        self.cuisine.setCurrentIndex(cuisine_index)

    def get_all_info(self) -> list[str]:
        category = self.category_combobox.currentText()
        name = self.dish_name.text()
        cost = self.cost.text()
        currency = self.currency.currentText()
        description = self.description.toPlainText()
        ingredients = self.ingredients.toPlainText()

        if self.radio_1.isChecked():
            dish_type = "Vegan"
        elif self.radio_2.isChecked():
            dish_type = "Vegetarian"
        elif self.radio_3.isChecked():
            dish_type = "Meat"
        else:
            dish_type = "None"

        cuisine = self.cuisine.currentText()
        return [category, name, cost, currency, description, ingredients, dish_type, cuisine]

    # Ta funkcja aktualizuje GUI, dodając nowe danie do odpowiedniej listy
    def update_gui(self) -> None:
        self.windows = MenuEditingWindow(self.logged_username)
        self.windows.showMaximized()
        self.close()

    def closeEvent(self, event):
        if self.programmatic_close:
            # Reset the flag
            self.programmatic_close = False
            event.accept()
        else:
            logout_user(self.logged_username, self.connector)
            event.accept()  # or event.ignore() if you want to prevent the window from closing