# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1286, 983)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_test_data = QPushButton(self.topMenu)
        self.btn_test_data.setObjectName(u"btn_test_data")
        sizePolicy.setHeightForWidth(self.btn_test_data.sizePolicy().hasHeightForWidth())
        self.btn_test_data.setSizePolicy(sizePolicy)
        self.btn_test_data.setMinimumSize(QSize(0, 45))
        self.btn_test_data.setFont(font)
        self.btn_test_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_test_data.setLayoutDirection(Qt.LeftToRight)
        self.btn_test_data.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_test_data)

        self.btn_config = QPushButton(self.topMenu)
        self.btn_config.setObjectName(u"btn_config")
        sizePolicy.setHeightForWidth(self.btn_config.sizePolicy().hasHeightForWidth())
        self.btn_config.setSizePolicy(sizePolicy)
        self.btn_config.setMinimumSize(QSize(0, 45))
        self.btn_config.setFont(font)
        self.btn_config.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_config.setLayoutDirection(Qt.LeftToRight)
        self.btn_config.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_config)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.groupBox = QGroupBox(self.home)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 30, 321, 611))
        self.setting_status = QPushButton(self.groupBox)
        self.setting_status.setObjectName(u"setting_status")
        self.setting_status.setGeometry(QRect(40, 50, 241, 41))
        self.mt8852b_status = QPushButton(self.groupBox)
        self.mt8852b_status.setObjectName(u"mt8852b_status")
        self.mt8852b_status.setGeometry(QRect(40, 100, 241, 41))
        self.left_box_status = QPushButton(self.groupBox)
        self.left_box_status.setObjectName(u"left_box_status")
        self.left_box_status.setGeometry(QRect(40, 150, 241, 41))
        self.right_box_status = QPushButton(self.groupBox)
        self.right_box_status.setObjectName(u"right_box_status")
        self.right_box_status.setGeometry(QRect(40, 200, 241, 41))
        self.left_bttc_status = QPushButton(self.groupBox)
        self.left_bttc_status.setObjectName(u"left_bttc_status")
        self.left_bttc_status.setGeometry(QRect(40, 250, 241, 41))
        self.right_bttc_status = QPushButton(self.groupBox)
        self.right_bttc_status.setObjectName(u"right_bttc_status")
        self.right_bttc_status.setGeometry(QRect(40, 300, 241, 41))
        self.signal_switch_status = QPushButton(self.groupBox)
        self.signal_switch_status.setObjectName(u"signal_switch_status")
        self.signal_switch_status.setGeometry(QRect(40, 350, 241, 41))
        self.mes_serice_status = QPushButton(self.groupBox)
        self.mes_serice_status.setObjectName(u"mes_serice_status")
        self.mes_serice_status.setGeometry(QRect(40, 400, 241, 41))
        self.left_channel_status = QPushButton(self.groupBox)
        self.left_channel_status.setObjectName(u"left_channel_status")
        self.left_channel_status.setGeometry(QRect(40, 450, 241, 41))
        self.right_channel_status = QPushButton(self.groupBox)
        self.right_channel_status.setObjectName(u"right_channel_status")
        self.right_channel_status.setGeometry(QRect(40, 500, 241, 41))
        self.start_test_btn = QPushButton(self.home)
        self.start_test_btn.setObjectName(u"start_test_btn")
        self.start_test_btn.setGeometry(QRect(40, 660, 141, 51))
        self.groupBox_2 = QGroupBox(self.home)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(390, 30, 741, 611))
        self.textEdit_4 = QTextEdit(self.groupBox_2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(0, 20, 741, 591))
        self.test_config_btn = QPushButton(self.home)
        self.test_config_btn.setObjectName(u"test_config_btn")
        self.test_config_btn.setGeometry(QRect(210, 660, 141, 51))
        self.stackedWidget.addWidget(self.home)
        self.test_config_page = QWidget()
        self.test_config_page.setObjectName(u"test_config_page")
        self.test_config_page.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.test_config_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.test_config_page)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.MT8852_ID = QLabel(self.frame_content_wid_1)
        self.MT8852_ID.setObjectName(u"MT8852_ID")

        self.gridLayout.addWidget(self.MT8852_ID, 0, 0, 1, 1)

        self.MT8852_status_label = QLabel(self.frame_content_wid_1)
        self.MT8852_status_label.setObjectName(u"MT8852_status_label")

        self.gridLayout.addWidget(self.MT8852_status_label, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.test_config_page)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setMaximumSize(QSize(1158, 16777215))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.row_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.left_box_com = QComboBox(self.row_2)
        self.left_box_com.setObjectName(u"left_box_com")

        self.horizontalLayout_8.addWidget(self.left_box_com)

        self.label_6 = QLabel(self.row_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.right_box_com = QComboBox(self.row_2)
        self.right_box_com.setObjectName(u"right_box_com")

        self.horizontalLayout_8.addWidget(self.right_box_com)


        self.verticalLayout_19.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.row_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.left_bbtc_com = QComboBox(self.row_2)
        self.left_bbtc_com.setObjectName(u"left_bbtc_com")

        self.horizontalLayout_10.addWidget(self.left_bbtc_com)

        self.label_8 = QLabel(self.row_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.right_bbtc_com = QComboBox(self.row_2)
        self.right_bbtc_com.setObjectName(u"right_bbtc_com")

        self.horizontalLayout_10.addWidget(self.right_bbtc_com)


        self.verticalLayout_19.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.row_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_9)

        self.signal_ctrl_com = QComboBox(self.row_2)
        self.signal_ctrl_com.setObjectName(u"signal_ctrl_com")

        self.horizontalLayout_11.addWidget(self.signal_ctrl_com)

        self.label_10 = QLabel(self.row_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.connect_time_le = QLineEdit(self.row_2)
        self.connect_time_le.setObjectName(u"connect_time_le")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.connect_time_le.sizePolicy().hasHeightForWidth())
        self.connect_time_le.setSizePolicy(sizePolicy3)

        self.horizontalLayout_11.addWidget(self.connect_time_le)


        self.verticalLayout_19.addLayout(self.horizontalLayout_11)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.test_config_page)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.row_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1160, 560))
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 10, 1121, 131))
        self.verticalLayout_22 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.leop_packet_cnt_le = QLineEdit(self.verticalLayoutWidget)
        self.leop_packet_cnt_le.setObjectName(u"leop_packet_cnt_le")

        self.horizontalLayout_13.addWidget(self.leop_packet_cnt_le)


        self.verticalLayout_22.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_16.addWidget(self.label_14)

        self.leop_freq_l_le = QLineEdit(self.verticalLayoutWidget)
        self.leop_freq_l_le.setObjectName(u"leop_freq_l_le")

        self.horizontalLayout_16.addWidget(self.leop_freq_l_le)

        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.leop_avg_ucl_le = QLineEdit(self.verticalLayoutWidget)
        self.leop_avg_ucl_le.setObjectName(u"leop_avg_ucl_le")

        self.horizontalLayout_16.addWidget(self.leop_avg_ucl_le)


        self.verticalLayout_22.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_16 = QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_17.addWidget(self.label_16)

        self.leop_freq_m_le = QLineEdit(self.verticalLayoutWidget)
        self.leop_freq_m_le.setObjectName(u"leop_freq_m_le")

        self.horizontalLayout_17.addWidget(self.leop_freq_m_le)

        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.leop_avg_lcl_le = QLineEdit(self.verticalLayoutWidget)
        self.leop_avg_lcl_le.setObjectName(u"leop_avg_lcl_le")

        self.horizontalLayout_17.addWidget(self.leop_avg_lcl_le)


        self.verticalLayout_22.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_18 = QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_18.addWidget(self.label_18)

        self.leop_freq_h = QLineEdit(self.verticalLayoutWidget)
        self.leop_freq_h.setObjectName(u"leop_freq_h")

        self.horizontalLayout_18.addWidget(self.leop_freq_h)

        self.label_19 = QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_18.addWidget(self.label_19)

        self.leop_peak_ucl_le = QLineEdit(self.verticalLayoutWidget)
        self.leop_peak_ucl_le.setObjectName(u"leop_peak_ucl_le")

        self.horizontalLayout_18.addWidget(self.leop_peak_ucl_le)


        self.verticalLayout_22.addLayout(self.horizontalLayout_18)

        self.verticalLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 150, 1121, 175))
        self.verticalLayout_24 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_29 = QLabel(self.verticalLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_23.addWidget(self.label_29)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_3)

        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_23.addWidget(self.label_13)

        self.leicd_packet_cnt_le = QLineEdit(self.verticalLayoutWidget_2)
        self.leicd_packet_cnt_le.setObjectName(u"leicd_packet_cnt_le")

        self.horizontalLayout_23.addWidget(self.leicd_packet_cnt_le)


        self.verticalLayout_24.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_30 = QLabel(self.verticalLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_24.addWidget(self.label_30)

        self.leicd_freq_l_le = QLineEdit(self.verticalLayoutWidget_2)
        self.leicd_freq_l_le.setObjectName(u"leicd_freq_l_le")

        self.horizontalLayout_24.addWidget(self.leicd_freq_l_le)

        self.label_31 = QLabel(self.verticalLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_24.addWidget(self.label_31)

        self.leice_p_fn_ucl_le = QLineEdit(self.verticalLayoutWidget_2)
        self.leice_p_fn_ucl_le.setObjectName(u"leice_p_fn_ucl_le")

        self.horizontalLayout_24.addWidget(self.leice_p_fn_ucl_le)


        self.verticalLayout_24.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_32 = QLabel(self.verticalLayoutWidget_2)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_27.addWidget(self.label_32)

        self.leicd_freq_m_le = QLineEdit(self.verticalLayoutWidget_2)
        self.leicd_freq_m_le.setObjectName(u"leicd_freq_m_le")

        self.horizontalLayout_27.addWidget(self.leicd_freq_m_le)

        self.label_33 = QLabel(self.verticalLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_27.addWidget(self.label_33)

        self.leicd_n_fn_lcl_le = QLineEdit(self.verticalLayoutWidget_2)
        self.leicd_n_fn_lcl_le.setObjectName(u"leicd_n_fn_lcl_le")

        self.horizontalLayout_27.addWidget(self.leicd_n_fn_lcl_le)


        self.verticalLayout_24.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_34 = QLabel(self.verticalLayoutWidget_2)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_28.addWidget(self.label_34)

        self.leicd_freq_h_le = QLineEdit(self.verticalLayoutWidget_2)
        self.leicd_freq_h_le.setObjectName(u"leicd_freq_h_le")

        self.horizontalLayout_28.addWidget(self.leicd_freq_h_le)

        self.label_35 = QLabel(self.verticalLayoutWidget_2)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_28.addWidget(self.label_35)

        self.leicd_drift_rate_le = QLineEdit(self.verticalLayoutWidget_2)
        self.leicd_drift_rate_le.setObjectName(u"leicd_drift_rate_le")

        self.horizontalLayout_28.addWidget(self.leicd_drift_rate_le)


        self.verticalLayout_24.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_36 = QLabel(self.verticalLayoutWidget_2)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_31.addWidget(self.label_36)

        self.leicd_drift_range_le = QLineEdit(self.verticalLayoutWidget_2)
        self.leicd_drift_range_le.setObjectName(u"leicd_drift_range_le")

        self.horizontalLayout_31.addWidget(self.leicd_drift_range_le)

        self.label_37 = QLabel(self.verticalLayoutWidget_2)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_31.addWidget(self.label_37)

        self.leicd_packet_drift_rang_le = QLineEdit(self.verticalLayoutWidget_2)
        self.leicd_packet_drift_rang_le.setObjectName(u"leicd_packet_drift_rang_le")

        self.horizontalLayout_31.addWidget(self.leicd_packet_drift_rang_le)


        self.verticalLayout_24.addLayout(self.horizontalLayout_31)

        self.verticalLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 340, 1121, 161))
        self.verticalLayout_25 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_39 = QLabel(self.verticalLayoutWidget_3)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_32.addWidget(self.label_39)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_2)

        self.label_38 = QLabel(self.verticalLayoutWidget_3)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_32.addWidget(self.label_38)

        self.less_packet_cnt_le = QLineEdit(self.verticalLayoutWidget_3)
        self.less_packet_cnt_le.setObjectName(u"less_packet_cnt_le")

        self.horizontalLayout_32.addWidget(self.less_packet_cnt_le)


        self.verticalLayout_25.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_42 = QLabel(self.verticalLayoutWidget_3)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_37.addWidget(self.label_42)

        self.less_freq_l_le = QLineEdit(self.verticalLayoutWidget_3)
        self.less_freq_l_le.setObjectName(u"less_freq_l_le")

        self.horizontalLayout_37.addWidget(self.less_freq_l_le)

        self.label_43 = QLabel(self.verticalLayoutWidget_3)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_37.addWidget(self.label_43)

        self.less_IFR_LE = QLineEdit(self.verticalLayoutWidget_3)
        self.less_IFR_LE.setObjectName(u"less_IFR_LE")

        self.horizontalLayout_37.addWidget(self.less_IFR_LE)


        self.verticalLayout_25.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_44 = QLabel(self.verticalLayoutWidget_3)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_38.addWidget(self.label_44)

        self.less_freq_m_le = QLineEdit(self.verticalLayoutWidget_3)
        self.less_freq_m_le.setObjectName(u"less_freq_m_le")

        self.horizontalLayout_38.addWidget(self.less_freq_m_le)

        self.label_45 = QLabel(self.verticalLayoutWidget_3)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_38.addWidget(self.label_45)

        self.less_op_le = QLineEdit(self.verticalLayoutWidget_3)
        self.less_op_le.setObjectName(u"less_op_le")

        self.horizontalLayout_38.addWidget(self.less_op_le)


        self.verticalLayout_25.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_40 = QLabel(self.verticalLayoutWidget_3)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_33.addWidget(self.label_40)

        self.less_freq_h_le = QLineEdit(self.verticalLayoutWidget_3)
        self.less_freq_h_le.setObjectName(u"less_freq_h_le")

        self.horizontalLayout_33.addWidget(self.less_freq_h_le)

        self.label_41 = QLabel(self.verticalLayoutWidget_3)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_33.addWidget(self.label_41)

        self.less_fer_le = QLineEdit(self.verticalLayoutWidget_3)
        self.less_fer_le.setObjectName(u"less_fer_le")

        self.horizontalLayout_33.addWidget(self.less_fer_le)


        self.verticalLayout_25.addLayout(self.horizontalLayout_33)

        self.cfg_save_btn = QPushButton(self.scrollAreaWidgetContents)
        self.cfg_save_btn.setObjectName(u"cfg_save_btn")
        self.cfg_save_btn.setGeometry(QRect(890, 510, 111, 31))
        self.default_btn = QPushButton(self.scrollAreaWidgetContents)
        self.default_btn.setObjectName(u"default_btn")
        self.default_btn.setGeometry(QRect(1020, 510, 111, 31))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_12.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.test_config_page)
        self.test_data_page = QWidget()
        self.test_data_page.setObjectName(u"test_data_page")
        self.verticalLayout_20 = QVBoxLayout(self.test_data_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.test_data_page)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_20.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_4 = QLabel(self.test_data_page)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_15.addWidget(self.label_4)

        self.left_sn_in = QLineEdit(self.test_data_page)
        self.left_sn_in.setObjectName(u"left_sn_in")

        self.horizontalLayout_15.addWidget(self.left_sn_in)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)


        self.verticalLayout_21.addLayout(self.horizontalLayout_14)

        self.line = QFrame(self.test_data_page)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_21.addWidget(self.line)

        self.left_test_result_bar = QProgressBar(self.test_data_page)
        self.left_test_result_bar.setObjectName(u"left_test_result_bar")
        self.left_test_result_bar.setValue(24)

        self.verticalLayout_21.addWidget(self.left_test_result_bar)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_2 = QLabel(self.test_data_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_29.addWidget(self.label_2)

        self.left_leop_result = QLabel(self.test_data_page)
        self.left_leop_result.setObjectName(u"left_leop_result")
        self.left_leop_result.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.left_leop_result)


        self.verticalLayout_21.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_21 = QLabel(self.test_data_page)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_19.addWidget(self.label_21)

        self.label_22 = QLabel(self.test_data_page)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_19.addWidget(self.label_22)

        self.label_23 = QLabel(self.test_data_page)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_19.addWidget(self.label_23)

        self.label_20 = QLabel(self.test_data_page)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_19.addWidget(self.label_20)

        self.label_93 = QLabel(self.test_data_page)
        self.label_93.setObjectName(u"label_93")

        self.horizontalLayout_19.addWidget(self.label_93)


        self.verticalLayout_21.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_58 = QLabel(self.test_data_page)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_26.addWidget(self.label_58)

        self.left_leop_l_max = QLabel(self.test_data_page)
        self.left_leop_l_max.setObjectName(u"left_leop_l_max")

        self.horizontalLayout_26.addWidget(self.left_leop_l_max)

        self.left_leop_m_max = QLabel(self.test_data_page)
        self.left_leop_m_max.setObjectName(u"left_leop_m_max")

        self.horizontalLayout_26.addWidget(self.left_leop_m_max)

        self.left_leop_h_max = QLabel(self.test_data_page)
        self.left_leop_h_max.setObjectName(u"left_leop_h_max")

        self.horizontalLayout_26.addWidget(self.left_leop_h_max)

        self.left_leop_avg_ucl = QLabel(self.test_data_page)
        self.left_leop_avg_ucl.setObjectName(u"left_leop_avg_ucl")

        self.horizontalLayout_26.addWidget(self.left_leop_avg_ucl)


        self.verticalLayout_21.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_54 = QLabel(self.test_data_page)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_25.addWidget(self.label_54)

        self.left_leop_l_avg = QLabel(self.test_data_page)
        self.left_leop_l_avg.setObjectName(u"left_leop_l_avg")

        self.horizontalLayout_25.addWidget(self.left_leop_l_avg)

        self.left_leop_m_avg = QLabel(self.test_data_page)
        self.left_leop_m_avg.setObjectName(u"left_leop_m_avg")

        self.horizontalLayout_25.addWidget(self.left_leop_m_avg)

        self.left_leop_h_avg = QLabel(self.test_data_page)
        self.left_leop_h_avg.setObjectName(u"left_leop_h_avg")

        self.horizontalLayout_25.addWidget(self.left_leop_h_avg)

        self.label_53 = QLabel(self.test_data_page)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_25.addWidget(self.label_53)


        self.verticalLayout_21.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_50 = QLabel(self.test_data_page)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_22.addWidget(self.label_50)

        self.left_leop_l_min = QLabel(self.test_data_page)
        self.left_leop_l_min.setObjectName(u"left_leop_l_min")

        self.horizontalLayout_22.addWidget(self.left_leop_l_min)

        self.left_leop_m_min = QLabel(self.test_data_page)
        self.left_leop_m_min.setObjectName(u"left_leop_m_min")

        self.horizontalLayout_22.addWidget(self.left_leop_m_min)

        self.left_leop_h_min = QLabel(self.test_data_page)
        self.left_leop_h_min.setObjectName(u"left_leop_h_min")

        self.horizontalLayout_22.addWidget(self.left_leop_h_min)

        self.left_leop_avg_lcl = QLabel(self.test_data_page)
        self.left_leop_avg_lcl.setObjectName(u"left_leop_avg_lcl")

        self.horizontalLayout_22.addWidget(self.left_leop_avg_lcl)


        self.verticalLayout_21.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_46 = QLabel(self.test_data_page)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_21.addWidget(self.label_46)

        self.left_leop_l_peak = QLabel(self.test_data_page)
        self.left_leop_l_peak.setObjectName(u"left_leop_l_peak")

        self.horizontalLayout_21.addWidget(self.left_leop_l_peak)

        self.left_leop_m_peak = QLabel(self.test_data_page)
        self.left_leop_m_peak.setObjectName(u"left_leop_m_peak")

        self.horizontalLayout_21.addWidget(self.left_leop_m_peak)

        self.left_leop_h_peak = QLabel(self.test_data_page)
        self.left_leop_h_peak.setObjectName(u"left_leop_h_peak")

        self.horizontalLayout_21.addWidget(self.left_leop_h_peak)

        self.left_leop_peak_ucl = QLabel(self.test_data_page)
        self.left_leop_peak_ucl.setObjectName(u"left_leop_peak_ucl")

        self.horizontalLayout_21.addWidget(self.left_leop_peak_ucl)


        self.verticalLayout_21.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_25 = QLabel(self.test_data_page)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_20.addWidget(self.label_25)

        self.left_leop_l_status = QLabel(self.test_data_page)
        self.left_leop_l_status.setObjectName(u"left_leop_l_status")

        self.horizontalLayout_20.addWidget(self.left_leop_l_status)

        self.left_leop_m_status = QLabel(self.test_data_page)
        self.left_leop_m_status.setObjectName(u"left_leop_m_status")

        self.horizontalLayout_20.addWidget(self.left_leop_m_status)

        self.left_leop_h_status = QLabel(self.test_data_page)
        self.left_leop_h_status.setObjectName(u"left_leop_h_status")

        self.horizontalLayout_20.addWidget(self.left_leop_h_status)

        self.label_24 = QLabel(self.test_data_page)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_20.addWidget(self.label_24)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)

        self.line_2 = QFrame(self.test_data_page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_21.addWidget(self.line_2)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_62 = QLabel(self.test_data_page)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_34.addWidget(self.label_62)

        self.left_leicd_result = QLabel(self.test_data_page)
        self.left_leicd_result.setObjectName(u"left_leicd_result")
        self.left_leicd_result.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.left_leicd_result)


        self.verticalLayout_21.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_99 = QLabel(self.test_data_page)
        self.label_99.setObjectName(u"label_99")

        self.horizontalLayout_46.addWidget(self.label_99)

        self.label_98 = QLabel(self.test_data_page)
        self.label_98.setObjectName(u"label_98")

        self.horizontalLayout_46.addWidget(self.label_98)

        self.label_97 = QLabel(self.test_data_page)
        self.label_97.setObjectName(u"label_97")

        self.horizontalLayout_46.addWidget(self.label_97)

        self.label_96 = QLabel(self.test_data_page)
        self.label_96.setObjectName(u"label_96")

        self.horizontalLayout_46.addWidget(self.label_96)

        self.label_103 = QLabel(self.test_data_page)
        self.label_103.setObjectName(u"label_103")

        self.horizontalLayout_46.addWidget(self.label_103)


        self.verticalLayout_21.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_67 = QLabel(self.test_data_page)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_41.addWidget(self.label_67)

        self.left_leicd_l_avg_fn = QLabel(self.test_data_page)
        self.left_leicd_l_avg_fn.setObjectName(u"left_leicd_l_avg_fn")

        self.horizontalLayout_41.addWidget(self.left_leicd_l_avg_fn)

        self.left_leicd_m_avg_fn = QLabel(self.test_data_page)
        self.left_leicd_m_avg_fn.setObjectName(u"left_leicd_m_avg_fn")

        self.horizontalLayout_41.addWidget(self.left_leicd_m_avg_fn)

        self.left_leicd_h_avg_fn = QLabel(self.test_data_page)
        self.left_leicd_h_avg_fn.setObjectName(u"left_leicd_h_avg_fn")

        self.horizontalLayout_41.addWidget(self.left_leicd_h_avg_fn)

        self.left_leicd_avg = QLabel(self.test_data_page)
        self.left_leicd_avg.setObjectName(u"left_leicd_avg")

        self.horizontalLayout_41.addWidget(self.left_leicd_avg)


        self.verticalLayout_21.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_71 = QLabel(self.test_data_page)
        self.label_71.setObjectName(u"label_71")

        self.horizontalLayout_45.addWidget(self.label_71)

        self.left_leicd_l_max_p_fn = QLabel(self.test_data_page)
        self.left_leicd_l_max_p_fn.setObjectName(u"left_leicd_l_max_p_fn")

        self.horizontalLayout_45.addWidget(self.left_leicd_l_max_p_fn)

        self.left_leicd_m_max_p_fn = QLabel(self.test_data_page)
        self.left_leicd_m_max_p_fn.setObjectName(u"left_leicd_m_max_p_fn")

        self.horizontalLayout_45.addWidget(self.left_leicd_m_max_p_fn)

        self.left_leicd_h_max_p_fn = QLabel(self.test_data_page)
        self.left_leicd_h_max_p_fn.setObjectName(u"left_leicd_h_max_p_fn")

        self.horizontalLayout_45.addWidget(self.left_leicd_h_max_p_fn)

        self.left_leicd_p_fn_ucl = QLabel(self.test_data_page)
        self.left_leicd_p_fn_ucl.setObjectName(u"left_leicd_p_fn_ucl")

        self.horizontalLayout_45.addWidget(self.left_leicd_p_fn_ucl)


        self.verticalLayout_21.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_75 = QLabel(self.test_data_page)
        self.label_75.setObjectName(u"label_75")

        self.horizontalLayout_44.addWidget(self.label_75)

        self.left_leicd_l_max_n_fn = QLabel(self.test_data_page)
        self.left_leicd_l_max_n_fn.setObjectName(u"left_leicd_l_max_n_fn")

        self.horizontalLayout_44.addWidget(self.left_leicd_l_max_n_fn)

        self.left_leicd_m_max_n_fn = QLabel(self.test_data_page)
        self.left_leicd_m_max_n_fn.setObjectName(u"left_leicd_m_max_n_fn")

        self.horizontalLayout_44.addWidget(self.left_leicd_m_max_n_fn)

        self.left_leicd_h_max_n_fn = QLabel(self.test_data_page)
        self.left_leicd_h_max_n_fn.setObjectName(u"left_leicd_h_max_n_fn")

        self.horizontalLayout_44.addWidget(self.left_leicd_h_max_n_fn)

        self.left_leicd_n_fn_ucl = QLabel(self.test_data_page)
        self.left_leicd_n_fn_ucl.setObjectName(u"left_leicd_n_fn_ucl")

        self.horizontalLayout_44.addWidget(self.left_leicd_n_fn_ucl)


        self.verticalLayout_21.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_77 = QLabel(self.test_data_page)
        self.label_77.setObjectName(u"label_77")

        self.horizontalLayout_43.addWidget(self.label_77)

        self.left_leicd_l_max_dirft_rate = QLabel(self.test_data_page)
        self.left_leicd_l_max_dirft_rate.setObjectName(u"left_leicd_l_max_dirft_rate")

        self.horizontalLayout_43.addWidget(self.left_leicd_l_max_dirft_rate)

        self.left_leicd_m_max_dirft_rate = QLabel(self.test_data_page)
        self.left_leicd_m_max_dirft_rate.setObjectName(u"left_leicd_m_max_dirft_rate")

        self.horizontalLayout_43.addWidget(self.left_leicd_m_max_dirft_rate)

        self.left_leicd_h_max_dirft_rate = QLabel(self.test_data_page)
        self.left_leicd_h_max_dirft_rate.setObjectName(u"left_leicd_h_max_dirft_rate")

        self.horizontalLayout_43.addWidget(self.left_leicd_h_max_dirft_rate)

        self.left_leicd_drift_rate = QLabel(self.test_data_page)
        self.left_leicd_drift_rate.setObjectName(u"left_leicd_drift_rate")

        self.horizontalLayout_43.addWidget(self.left_leicd_drift_rate)


        self.verticalLayout_21.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_82 = QLabel(self.test_data_page)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_42.addWidget(self.label_82)

        self.left_leicd_l_max_dirft = QLabel(self.test_data_page)
        self.left_leicd_l_max_dirft.setObjectName(u"left_leicd_l_max_dirft")

        self.horizontalLayout_42.addWidget(self.left_leicd_l_max_dirft)

        self.left_leicd_m_max_dirft = QLabel(self.test_data_page)
        self.left_leicd_m_max_dirft.setObjectName(u"left_leicd_m_max_dirft")

        self.horizontalLayout_42.addWidget(self.left_leicd_m_max_dirft)

        self.left_leicd_h_max_dirft = QLabel(self.test_data_page)
        self.left_leicd_h_max_dirft.setObjectName(u"left_leicd_h_max_dirft")

        self.horizontalLayout_42.addWidget(self.left_leicd_h_max_dirft)

        self.left_leicd_drift_range = QLabel(self.test_data_page)
        self.left_leicd_drift_range.setObjectName(u"left_leicd_drift_range")

        self.horizontalLayout_42.addWidget(self.left_leicd_drift_range)


        self.verticalLayout_21.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_87 = QLabel(self.test_data_page)
        self.label_87.setObjectName(u"label_87")

        self.horizontalLayout_40.addWidget(self.label_87)

        self.left_leicd_l_avg_dirft = QLabel(self.test_data_page)
        self.left_leicd_l_avg_dirft.setObjectName(u"left_leicd_l_avg_dirft")

        self.horizontalLayout_40.addWidget(self.left_leicd_l_avg_dirft)

        self.left_leicd_m_avg_dirft = QLabel(self.test_data_page)
        self.left_leicd_m_avg_dirft.setObjectName(u"left_leicd_m_avg_dirft")

        self.horizontalLayout_40.addWidget(self.left_leicd_m_avg_dirft)

        self.left_leicd_h_avg_dirft = QLabel(self.test_data_page)
        self.left_leicd_h_avg_dirft.setObjectName(u"left_leicd_h_avg_dirft")

        self.horizontalLayout_40.addWidget(self.left_leicd_h_avg_dirft)

        self.label_84 = QLabel(self.test_data_page)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_40.addWidget(self.label_84)


        self.verticalLayout_21.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_91 = QLabel(self.test_data_page)
        self.label_91.setObjectName(u"label_91")

        self.horizontalLayout_39.addWidget(self.label_91)

        self.left_leicd_l_state = QLabel(self.test_data_page)
        self.left_leicd_l_state.setObjectName(u"left_leicd_l_state")

        self.horizontalLayout_39.addWidget(self.left_leicd_l_state)

        self.left_leicd_m_state = QLabel(self.test_data_page)
        self.left_leicd_m_state.setObjectName(u"left_leicd_m_state")

        self.horizontalLayout_39.addWidget(self.left_leicd_m_state)

        self.left_leicd_h_state = QLabel(self.test_data_page)
        self.left_leicd_h_state.setObjectName(u"left_leicd_h_state")

        self.horizontalLayout_39.addWidget(self.left_leicd_h_state)

        self.label_88 = QLabel(self.test_data_page)
        self.label_88.setObjectName(u"label_88")

        self.horizontalLayout_39.addWidget(self.label_88)


        self.verticalLayout_21.addLayout(self.horizontalLayout_39)

        self.line_3 = QFrame(self.test_data_page)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_21.addWidget(self.line_3)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.left_less_label = QLabel(self.test_data_page)
        self.left_less_label.setObjectName(u"left_less_label")
        self.left_less_label.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_35.addWidget(self.left_less_label)

        self.left_less_result = QLabel(self.test_data_page)
        self.left_less_result.setObjectName(u"left_less_result")
        self.left_less_result.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.left_less_result)


        self.verticalLayout_21.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_116 = QLabel(self.test_data_page)
        self.label_116.setObjectName(u"label_116")

        self.horizontalLayout_48.addWidget(self.label_116)

        self.label_115 = QLabel(self.test_data_page)
        self.label_115.setObjectName(u"label_115")

        self.horizontalLayout_48.addWidget(self.label_115)

        self.label_114 = QLabel(self.test_data_page)
        self.label_114.setObjectName(u"label_114")

        self.horizontalLayout_48.addWidget(self.label_114)

        self.label_113 = QLabel(self.test_data_page)
        self.label_113.setObjectName(u"label_113")

        self.horizontalLayout_48.addWidget(self.label_113)

        self.label_112 = QLabel(self.test_data_page)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_48.addWidget(self.label_112)


        self.verticalLayout_21.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_118 = QLabel(self.test_data_page)
        self.label_118.setObjectName(u"label_118")

        self.horizontalLayout_51.addWidget(self.label_118)

        self.left_less_l_over_fer = QLabel(self.test_data_page)
        self.left_less_l_over_fer.setObjectName(u"left_less_l_over_fer")

        self.horizontalLayout_51.addWidget(self.left_less_l_over_fer)

        self.left_less_m_over_fer = QLabel(self.test_data_page)
        self.left_less_m_over_fer.setObjectName(u"left_less_m_over_fer")

        self.horizontalLayout_51.addWidget(self.left_less_m_over_fer)

        self.left_less_h_over_fer = QLabel(self.test_data_page)
        self.left_less_h_over_fer.setObjectName(u"left_less_h_over_fer")

        self.horizontalLayout_51.addWidget(self.left_less_h_over_fer)

        self.left_less_fer = QLabel(self.test_data_page)
        self.left_less_fer.setObjectName(u"left_less_fer")

        self.horizontalLayout_51.addWidget(self.left_less_fer)


        self.verticalLayout_21.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_125 = QLabel(self.test_data_page)
        self.label_125.setObjectName(u"label_125")

        self.horizontalLayout_50.addWidget(self.label_125)

        self.left_less_l_total_frames_sent_tester = QLabel(self.test_data_page)
        self.left_less_l_total_frames_sent_tester.setObjectName(u"left_less_l_total_frames_sent_tester")

        self.horizontalLayout_50.addWidget(self.left_less_l_total_frames_sent_tester)

        self.left_less_m_total_frames_sent_tester = QLabel(self.test_data_page)
        self.left_less_m_total_frames_sent_tester.setObjectName(u"left_less_m_total_frames_sent_tester")

        self.horizontalLayout_50.addWidget(self.left_less_m_total_frames_sent_tester)

        self.left_less_h_total_frames_sent_tester = QLabel(self.test_data_page)
        self.left_less_h_total_frames_sent_tester.setObjectName(u"left_less_h_total_frames_sent_tester")

        self.horizontalLayout_50.addWidget(self.left_less_h_total_frames_sent_tester)

        self.label_122 = QLabel(self.test_data_page)
        self.label_122.setObjectName(u"label_122")

        self.horizontalLayout_50.addWidget(self.label_122)


        self.verticalLayout_21.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_130 = QLabel(self.test_data_page)
        self.label_130.setObjectName(u"label_130")

        self.horizontalLayout_49.addWidget(self.label_130)

        self.left_less_l_total_frames_counted_dut = QLabel(self.test_data_page)
        self.left_less_l_total_frames_counted_dut.setObjectName(u"left_less_l_total_frames_counted_dut")

        self.horizontalLayout_49.addWidget(self.left_less_l_total_frames_counted_dut)

        self.left_less_m_total_frames_counted_dut = QLabel(self.test_data_page)
        self.left_less_m_total_frames_counted_dut.setObjectName(u"left_less_m_total_frames_counted_dut")

        self.horizontalLayout_49.addWidget(self.left_less_m_total_frames_counted_dut)

        self.left_less_h_total_frames_counted_dut = QLabel(self.test_data_page)
        self.left_less_h_total_frames_counted_dut.setObjectName(u"left_less_h_total_frames_counted_dut")

        self.horizontalLayout_49.addWidget(self.left_less_h_total_frames_counted_dut)

        self.label_127 = QLabel(self.test_data_page)
        self.label_127.setObjectName(u"label_127")

        self.horizontalLayout_49.addWidget(self.label_127)


        self.verticalLayout_21.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_135 = QLabel(self.test_data_page)
        self.label_135.setObjectName(u"label_135")

        self.horizontalLayout_52.addWidget(self.label_135)

        self.left_less_l_status = QLabel(self.test_data_page)
        self.left_less_l_status.setObjectName(u"left_less_l_status")

        self.horizontalLayout_52.addWidget(self.left_less_l_status)

        self.left_less_m_status = QLabel(self.test_data_page)
        self.left_less_m_status.setObjectName(u"left_less_m_status")

        self.horizontalLayout_52.addWidget(self.left_less_m_status)

        self.left_less_h_status = QLabel(self.test_data_page)
        self.left_less_h_status.setObjectName(u"left_less_h_status")

        self.horizontalLayout_52.addWidget(self.left_less_h_status)

        self.label_132 = QLabel(self.test_data_page)
        self.label_132.setObjectName(u"label_132")

        self.horizontalLayout_52.addWidget(self.label_132)


        self.verticalLayout_21.addLayout(self.horizontalLayout_52)

        self.line_4 = QFrame(self.test_data_page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.HLine)

        self.verticalLayout_21.addWidget(self.line_4)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_138 = QLabel(self.test_data_page)
        self.label_138.setObjectName(u"label_138")

        self.horizontalLayout_53.addWidget(self.label_138)

        self.left_test_time_point = QLabel(self.test_data_page)
        self.left_test_time_point.setObjectName(u"left_test_time_point")

        self.horizontalLayout_53.addWidget(self.left_test_time_point)

        self.label_139 = QLabel(self.test_data_page)
        self.label_139.setObjectName(u"label_139")

        self.horizontalLayout_53.addWidget(self.label_139)

        self.left_test_time_during = QLabel(self.test_data_page)
        self.left_test_time_during.setObjectName(u"left_test_time_during")

        self.horizontalLayout_53.addWidget(self.left_test_time_during)


        self.verticalLayout_21.addLayout(self.horizontalLayout_53)

        self.line_5 = QFrame(self.test_data_page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_21.addWidget(self.line_5)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_144 = QLabel(self.test_data_page)
        self.label_144.setObjectName(u"label_144")

        self.horizontalLayout_54.addWidget(self.label_144)

        self.label_143 = QLabel(self.test_data_page)
        self.label_143.setObjectName(u"label_143")

        self.horizontalLayout_54.addWidget(self.label_143)

        self.label_142 = QLabel(self.test_data_page)
        self.label_142.setObjectName(u"label_142")

        self.horizontalLayout_54.addWidget(self.label_142)

        self.label_141 = QLabel(self.test_data_page)
        self.label_141.setObjectName(u"label_141")

        self.horizontalLayout_54.addWidget(self.label_141)


        self.verticalLayout_21.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.left_test_count = QLabel(self.test_data_page)
        self.left_test_count.setObjectName(u"left_test_count")

        self.horizontalLayout_47.addWidget(self.left_test_count)

        self.left_pass_count = QLabel(self.test_data_page)
        self.left_pass_count.setObjectName(u"left_pass_count")

        self.horizontalLayout_47.addWidget(self.left_pass_count)

        self.left_fail_count = QLabel(self.test_data_page)
        self.left_fail_count.setObjectName(u"left_fail_count")

        self.horizontalLayout_47.addWidget(self.left_fail_count)

        self.left_fail_rate = QLabel(self.test_data_page)
        self.left_fail_rate.setObjectName(u"left_fail_rate")

        self.horizontalLayout_47.addWidget(self.left_fail_rate)


        self.verticalLayout_21.addLayout(self.horizontalLayout_47)


        self.horizontalLayout_7.addLayout(self.verticalLayout_21)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_3 = QLabel(self.test_data_page)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_55.addWidget(self.label_3)

        self.right_sn_in = QLineEdit(self.test_data_page)
        self.right_sn_in.setObjectName(u"right_sn_in")

        self.horizontalLayout_55.addWidget(self.right_sn_in)


        self.verticalLayout_26.addLayout(self.horizontalLayout_55)

        self.line_7 = QFrame(self.test_data_page)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout_26.addWidget(self.line_7)

        self.right_test_result_bar = QProgressBar(self.test_data_page)
        self.right_test_result_bar.setObjectName(u"right_test_result_bar")
        self.right_test_result_bar.setValue(24)

        self.verticalLayout_26.addWidget(self.right_test_result_bar)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_149 = QLabel(self.test_data_page)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_56.addWidget(self.label_149)

        self.right_leop_result = QLabel(self.test_data_page)
        self.right_leop_result.setObjectName(u"right_leop_result")
        self.right_leop_result.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.right_leop_result)


        self.verticalLayout_26.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_153 = QLabel(self.test_data_page)
        self.label_153.setObjectName(u"label_153")

        self.horizontalLayout_58.addWidget(self.label_153)

        self.label_155 = QLabel(self.test_data_page)
        self.label_155.setObjectName(u"label_155")

        self.horizontalLayout_58.addWidget(self.label_155)

        self.label_154 = QLabel(self.test_data_page)
        self.label_154.setObjectName(u"label_154")

        self.horizontalLayout_58.addWidget(self.label_154)

        self.label_152 = QLabel(self.test_data_page)
        self.label_152.setObjectName(u"label_152")

        self.horizontalLayout_58.addWidget(self.label_152)

        self.label_151 = QLabel(self.test_data_page)
        self.label_151.setObjectName(u"label_151")

        self.horizontalLayout_58.addWidget(self.label_151)


        self.verticalLayout_26.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_159 = QLabel(self.test_data_page)
        self.label_159.setObjectName(u"label_159")

        self.horizontalLayout_60.addWidget(self.label_159)

        self.right_leop_l_max = QLabel(self.test_data_page)
        self.right_leop_l_max.setObjectName(u"right_leop_l_max")

        self.horizontalLayout_60.addWidget(self.right_leop_l_max)

        self.right_leop_m_max = QLabel(self.test_data_page)
        self.right_leop_m_max.setObjectName(u"right_leop_m_max")

        self.horizontalLayout_60.addWidget(self.right_leop_m_max)

        self.right_leop_h_max = QLabel(self.test_data_page)
        self.right_leop_h_max.setObjectName(u"right_leop_h_max")

        self.horizontalLayout_60.addWidget(self.right_leop_h_max)

        self.right_leop_avg_ucl = QLabel(self.test_data_page)
        self.right_leop_avg_ucl.setObjectName(u"right_leop_avg_ucl")

        self.horizontalLayout_60.addWidget(self.right_leop_avg_ucl)


        self.verticalLayout_26.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_164 = QLabel(self.test_data_page)
        self.label_164.setObjectName(u"label_164")

        self.horizontalLayout_61.addWidget(self.label_164)

        self.right_leop_l_avg = QLabel(self.test_data_page)
        self.right_leop_l_avg.setObjectName(u"right_leop_l_avg")

        self.horizontalLayout_61.addWidget(self.right_leop_l_avg)

        self.right_leop_m_avg = QLabel(self.test_data_page)
        self.right_leop_m_avg.setObjectName(u"right_leop_m_avg")

        self.horizontalLayout_61.addWidget(self.right_leop_m_avg)

        self.right_leop_h_avg = QLabel(self.test_data_page)
        self.right_leop_h_avg.setObjectName(u"right_leop_h_avg")

        self.horizontalLayout_61.addWidget(self.right_leop_h_avg)

        self.label_161 = QLabel(self.test_data_page)
        self.label_161.setObjectName(u"label_161")

        self.horizontalLayout_61.addWidget(self.label_161)


        self.verticalLayout_26.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_170 = QLabel(self.test_data_page)
        self.label_170.setObjectName(u"label_170")

        self.horizontalLayout_63.addWidget(self.label_170)

        self.right_leop_l_min = QLabel(self.test_data_page)
        self.right_leop_l_min.setObjectName(u"right_leop_l_min")

        self.horizontalLayout_63.addWidget(self.right_leop_l_min)

        self.right_leop_m_min = QLabel(self.test_data_page)
        self.right_leop_m_min.setObjectName(u"right_leop_m_min")

        self.horizontalLayout_63.addWidget(self.right_leop_m_min)

        self.right_leop_h_min = QLabel(self.test_data_page)
        self.right_leop_h_min.setObjectName(u"right_leop_h_min")

        self.horizontalLayout_63.addWidget(self.right_leop_h_min)

        self.right_leop_avg_lcl = QLabel(self.test_data_page)
        self.right_leop_avg_lcl.setObjectName(u"right_leop_avg_lcl")

        self.horizontalLayout_63.addWidget(self.right_leop_avg_lcl)


        self.verticalLayout_26.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_174 = QLabel(self.test_data_page)
        self.label_174.setObjectName(u"label_174")

        self.horizontalLayout_62.addWidget(self.label_174)

        self.right_leop_l_peak = QLabel(self.test_data_page)
        self.right_leop_l_peak.setObjectName(u"right_leop_l_peak")

        self.horizontalLayout_62.addWidget(self.right_leop_l_peak)

        self.right_leop_m_peak = QLabel(self.test_data_page)
        self.right_leop_m_peak.setObjectName(u"right_leop_m_peak")

        self.horizontalLayout_62.addWidget(self.right_leop_m_peak)

        self.right_leop_h_peak = QLabel(self.test_data_page)
        self.right_leop_h_peak.setObjectName(u"right_leop_h_peak")

        self.horizontalLayout_62.addWidget(self.right_leop_h_peak)

        self.right_leop_peak_ucl = QLabel(self.test_data_page)
        self.right_leop_peak_ucl.setObjectName(u"right_leop_peak_ucl")

        self.horizontalLayout_62.addWidget(self.right_leop_peak_ucl)


        self.verticalLayout_26.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_180 = QLabel(self.test_data_page)
        self.label_180.setObjectName(u"label_180")

        self.horizontalLayout_59.addWidget(self.label_180)

        self.right_leop_l_status = QLabel(self.test_data_page)
        self.right_leop_l_status.setObjectName(u"right_leop_l_status")

        self.horizontalLayout_59.addWidget(self.right_leop_l_status)

        self.right_leop_m_status = QLabel(self.test_data_page)
        self.right_leop_m_status.setObjectName(u"right_leop_m_status")

        self.horizontalLayout_59.addWidget(self.right_leop_m_status)

        self.right_leop_h_status = QLabel(self.test_data_page)
        self.right_leop_h_status.setObjectName(u"right_leop_h_status")

        self.horizontalLayout_59.addWidget(self.right_leop_h_status)

        self.label_176 = QLabel(self.test_data_page)
        self.label_176.setObjectName(u"label_176")

        self.horizontalLayout_59.addWidget(self.label_176)


        self.verticalLayout_26.addLayout(self.horizontalLayout_59)

        self.line_6 = QFrame(self.test_data_page)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_26.addWidget(self.line_6)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_182 = QLabel(self.test_data_page)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_65.addWidget(self.label_182)

        self.right_leicd_result = QLabel(self.test_data_page)
        self.right_leicd_result.setObjectName(u"right_leicd_result")
        self.right_leicd_result.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.right_leicd_result)


        self.verticalLayout_26.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_222 = QLabel(self.test_data_page)
        self.label_222.setObjectName(u"label_222")

        self.horizontalLayout_79.addWidget(self.label_222)

        self.label_259 = QLabel(self.test_data_page)
        self.label_259.setObjectName(u"label_259")

        self.horizontalLayout_79.addWidget(self.label_259)

        self.label_258 = QLabel(self.test_data_page)
        self.label_258.setObjectName(u"label_258")

        self.horizontalLayout_79.addWidget(self.label_258)

        self.label_221 = QLabel(self.test_data_page)
        self.label_221.setObjectName(u"label_221")

        self.horizontalLayout_79.addWidget(self.label_221)

        self.label_219 = QLabel(self.test_data_page)
        self.label_219.setObjectName(u"label_219")

        self.horizontalLayout_79.addWidget(self.label_219)


        self.verticalLayout_26.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_187 = QLabel(self.test_data_page)
        self.label_187.setObjectName(u"label_187")

        self.horizontalLayout_66.addWidget(self.label_187)

        self.right_leicd_l_avg_fn = QLabel(self.test_data_page)
        self.right_leicd_l_avg_fn.setObjectName(u"right_leicd_l_avg_fn")

        self.horizontalLayout_66.addWidget(self.right_leicd_l_avg_fn)

        self.right_leicd_m_avg_fn = QLabel(self.test_data_page)
        self.right_leicd_m_avg_fn.setObjectName(u"right_leicd_m_avg_fn")

        self.horizontalLayout_66.addWidget(self.right_leicd_m_avg_fn)

        self.right_leicd_h_avg_fn = QLabel(self.test_data_page)
        self.right_leicd_h_avg_fn.setObjectName(u"right_leicd_h_avg_fn")

        self.horizontalLayout_66.addWidget(self.right_leicd_h_avg_fn)

        self.right_leicd_avg = QLabel(self.test_data_page)
        self.right_leicd_avg.setObjectName(u"right_leicd_avg")

        self.horizontalLayout_66.addWidget(self.right_leicd_avg)


        self.verticalLayout_26.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_192 = QLabel(self.test_data_page)
        self.label_192.setObjectName(u"label_192")

        self.horizontalLayout_69.addWidget(self.label_192)

        self.right_leicd_l_max_p_fn = QLabel(self.test_data_page)
        self.right_leicd_l_max_p_fn.setObjectName(u"right_leicd_l_max_p_fn")

        self.horizontalLayout_69.addWidget(self.right_leicd_l_max_p_fn)

        self.right_leicd_m_max_p_fn = QLabel(self.test_data_page)
        self.right_leicd_m_max_p_fn.setObjectName(u"right_leicd_m_max_p_fn")

        self.horizontalLayout_69.addWidget(self.right_leicd_m_max_p_fn)

        self.right_leicd_h_max_p_fn = QLabel(self.test_data_page)
        self.right_leicd_h_max_p_fn.setObjectName(u"right_leicd_h_max_p_fn")

        self.horizontalLayout_69.addWidget(self.right_leicd_h_max_p_fn)

        self.right_leicd_p_fn_ucl = QLabel(self.test_data_page)
        self.right_leicd_p_fn_ucl.setObjectName(u"right_leicd_p_fn_ucl")

        self.horizontalLayout_69.addWidget(self.right_leicd_p_fn_ucl)


        self.verticalLayout_26.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_197 = QLabel(self.test_data_page)
        self.label_197.setObjectName(u"label_197")

        self.horizontalLayout_78.addWidget(self.label_197)

        self.right_leicd_l_max_n_fn = QLabel(self.test_data_page)
        self.right_leicd_l_max_n_fn.setObjectName(u"right_leicd_l_max_n_fn")

        self.horizontalLayout_78.addWidget(self.right_leicd_l_max_n_fn)

        self.right_leicd_m_max_n_fn = QLabel(self.test_data_page)
        self.right_leicd_m_max_n_fn.setObjectName(u"right_leicd_m_max_n_fn")

        self.horizontalLayout_78.addWidget(self.right_leicd_m_max_n_fn)

        self.right_leicd_h_max_n_fn = QLabel(self.test_data_page)
        self.right_leicd_h_max_n_fn.setObjectName(u"right_leicd_h_max_n_fn")

        self.horizontalLayout_78.addWidget(self.right_leicd_h_max_n_fn)

        self.right_leicd_n_fn_ucl = QLabel(self.test_data_page)
        self.right_leicd_n_fn_ucl.setObjectName(u"right_leicd_n_fn_ucl")

        self.horizontalLayout_78.addWidget(self.right_leicd_n_fn_ucl)


        self.verticalLayout_26.addLayout(self.horizontalLayout_78)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_202 = QLabel(self.test_data_page)
        self.label_202.setObjectName(u"label_202")

        self.horizontalLayout_73.addWidget(self.label_202)

        self.right_leicd_l_max_dirft_rate = QLabel(self.test_data_page)
        self.right_leicd_l_max_dirft_rate.setObjectName(u"right_leicd_l_max_dirft_rate")

        self.horizontalLayout_73.addWidget(self.right_leicd_l_max_dirft_rate)

        self.right_leicd_m_max_dirft_rate = QLabel(self.test_data_page)
        self.right_leicd_m_max_dirft_rate.setObjectName(u"right_leicd_m_max_dirft_rate")

        self.horizontalLayout_73.addWidget(self.right_leicd_m_max_dirft_rate)

        self.right_leicd_h_max_dirft_rate = QLabel(self.test_data_page)
        self.right_leicd_h_max_dirft_rate.setObjectName(u"right_leicd_h_max_dirft_rate")

        self.horizontalLayout_73.addWidget(self.right_leicd_h_max_dirft_rate)

        self.right_leicd_drift_rate = QLabel(self.test_data_page)
        self.right_leicd_drift_rate.setObjectName(u"right_leicd_drift_rate")

        self.horizontalLayout_73.addWidget(self.right_leicd_drift_rate)


        self.verticalLayout_26.addLayout(self.horizontalLayout_73)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_207 = QLabel(self.test_data_page)
        self.label_207.setObjectName(u"label_207")

        self.horizontalLayout_74.addWidget(self.label_207)

        self.right_leicd_l_max_dirft = QLabel(self.test_data_page)
        self.right_leicd_l_max_dirft.setObjectName(u"right_leicd_l_max_dirft")

        self.horizontalLayout_74.addWidget(self.right_leicd_l_max_dirft)

        self.right_leicd_m_max_dirft = QLabel(self.test_data_page)
        self.right_leicd_m_max_dirft.setObjectName(u"right_leicd_m_max_dirft")

        self.horizontalLayout_74.addWidget(self.right_leicd_m_max_dirft)

        self.right_leicd_h_max_dirft = QLabel(self.test_data_page)
        self.right_leicd_h_max_dirft.setObjectName(u"right_leicd_h_max_dirft")

        self.horizontalLayout_74.addWidget(self.right_leicd_h_max_dirft)

        self.right_leicd_drift_range = QLabel(self.test_data_page)
        self.right_leicd_drift_range.setObjectName(u"right_leicd_drift_range")

        self.horizontalLayout_74.addWidget(self.right_leicd_drift_range)


        self.verticalLayout_26.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_211 = QLabel(self.test_data_page)
        self.label_211.setObjectName(u"label_211")

        self.horizontalLayout_77.addWidget(self.label_211)

        self.right_leicd_l_avg_dirft = QLabel(self.test_data_page)
        self.right_leicd_l_avg_dirft.setObjectName(u"right_leicd_l_avg_dirft")

        self.horizontalLayout_77.addWidget(self.right_leicd_l_avg_dirft)

        self.right_leicd_m_avg_dirft = QLabel(self.test_data_page)
        self.right_leicd_m_avg_dirft.setObjectName(u"right_leicd_m_avg_dirft")

        self.horizontalLayout_77.addWidget(self.right_leicd_m_avg_dirft)

        self.right_leicd_h_avg_dirft = QLabel(self.test_data_page)
        self.right_leicd_h_avg_dirft.setObjectName(u"right_leicd_h_avg_dirft")

        self.horizontalLayout_77.addWidget(self.right_leicd_h_avg_dirft)

        self.label_208 = QLabel(self.test_data_page)
        self.label_208.setObjectName(u"label_208")

        self.horizontalLayout_77.addWidget(self.label_208)


        self.verticalLayout_26.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_217 = QLabel(self.test_data_page)
        self.label_217.setObjectName(u"label_217")

        self.horizontalLayout_72.addWidget(self.label_217)

        self.right_leicd_l_state = QLabel(self.test_data_page)
        self.right_leicd_l_state.setObjectName(u"right_leicd_l_state")

        self.horizontalLayout_72.addWidget(self.right_leicd_l_state)

        self.right_leicd_m_state = QLabel(self.test_data_page)
        self.right_leicd_m_state.setObjectName(u"right_leicd_m_state")

        self.horizontalLayout_72.addWidget(self.right_leicd_m_state)

        self.right_leicd_h_state = QLabel(self.test_data_page)
        self.right_leicd_h_state.setObjectName(u"right_leicd_h_state")

        self.horizontalLayout_72.addWidget(self.right_leicd_h_state)

        self.label_213 = QLabel(self.test_data_page)
        self.label_213.setObjectName(u"label_213")

        self.horizontalLayout_72.addWidget(self.label_213)


        self.verticalLayout_26.addLayout(self.horizontalLayout_72)

        self.line_8 = QFrame(self.test_data_page)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setFrameShape(QFrame.HLine)

        self.verticalLayout_26.addWidget(self.line_8)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_220 = QLabel(self.test_data_page)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_71.addWidget(self.label_220)

        self.right_less_result = QLabel(self.test_data_page)
        self.right_less_result.setObjectName(u"right_less_result")
        self.right_less_result.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.right_less_result)


        self.verticalLayout_26.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_227 = QLabel(self.test_data_page)
        self.label_227.setObjectName(u"label_227")

        self.horizontalLayout_76.addWidget(self.label_227)

        self.label_226 = QLabel(self.test_data_page)
        self.label_226.setObjectName(u"label_226")

        self.horizontalLayout_76.addWidget(self.label_226)

        self.label_225 = QLabel(self.test_data_page)
        self.label_225.setObjectName(u"label_225")

        self.horizontalLayout_76.addWidget(self.label_225)

        self.label_224 = QLabel(self.test_data_page)
        self.label_224.setObjectName(u"label_224")

        self.horizontalLayout_76.addWidget(self.label_224)

        self.label_223 = QLabel(self.test_data_page)
        self.label_223.setObjectName(u"label_223")

        self.horizontalLayout_76.addWidget(self.label_223)


        self.verticalLayout_26.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_232 = QLabel(self.test_data_page)
        self.label_232.setObjectName(u"label_232")

        self.horizontalLayout_75.addWidget(self.label_232)

        self.right_less_l_over_fer = QLabel(self.test_data_page)
        self.right_less_l_over_fer.setObjectName(u"right_less_l_over_fer")

        self.horizontalLayout_75.addWidget(self.right_less_l_over_fer)

        self.right_less_m_over_fer = QLabel(self.test_data_page)
        self.right_less_m_over_fer.setObjectName(u"right_less_m_over_fer")

        self.horizontalLayout_75.addWidget(self.right_less_m_over_fer)

        self.right_less_h_over_fer = QLabel(self.test_data_page)
        self.right_less_h_over_fer.setObjectName(u"right_less_h_over_fer")

        self.horizontalLayout_75.addWidget(self.right_less_h_over_fer)

        self.right_less_fer = QLabel(self.test_data_page)
        self.right_less_fer.setObjectName(u"right_less_fer")

        self.horizontalLayout_75.addWidget(self.right_less_fer)


        self.verticalLayout_26.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_237 = QLabel(self.test_data_page)
        self.label_237.setObjectName(u"label_237")

        self.horizontalLayout_68.addWidget(self.label_237)

        self.right_less_l_total_frames_sent_tester = QLabel(self.test_data_page)
        self.right_less_l_total_frames_sent_tester.setObjectName(u"right_less_l_total_frames_sent_tester")

        self.horizontalLayout_68.addWidget(self.right_less_l_total_frames_sent_tester)

        self.right_less_m_total_frames_sent_tester = QLabel(self.test_data_page)
        self.right_less_m_total_frames_sent_tester.setObjectName(u"right_less_m_total_frames_sent_tester")

        self.horizontalLayout_68.addWidget(self.right_less_m_total_frames_sent_tester)

        self.right_less_h_total_frames_sent_tester = QLabel(self.test_data_page)
        self.right_less_h_total_frames_sent_tester.setObjectName(u"right_less_h_total_frames_sent_tester")

        self.horizontalLayout_68.addWidget(self.right_less_h_total_frames_sent_tester)

        self.label_233 = QLabel(self.test_data_page)
        self.label_233.setObjectName(u"label_233")

        self.horizontalLayout_68.addWidget(self.label_233)


        self.verticalLayout_26.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_241 = QLabel(self.test_data_page)
        self.label_241.setObjectName(u"label_241")

        self.horizontalLayout_70.addWidget(self.label_241)

        self.right_less_l_total_frames_counted_dut = QLabel(self.test_data_page)
        self.right_less_l_total_frames_counted_dut.setObjectName(u"right_less_l_total_frames_counted_dut")

        self.horizontalLayout_70.addWidget(self.right_less_l_total_frames_counted_dut)

        self.right_less_m_total_frames_counted_dut = QLabel(self.test_data_page)
        self.right_less_m_total_frames_counted_dut.setObjectName(u"right_less_m_total_frames_counted_dut")

        self.horizontalLayout_70.addWidget(self.right_less_m_total_frames_counted_dut)

        self.right_less_h_total_frames_counted_dut = QLabel(self.test_data_page)
        self.right_less_h_total_frames_counted_dut.setObjectName(u"right_less_h_total_frames_counted_dut")

        self.horizontalLayout_70.addWidget(self.right_less_h_total_frames_counted_dut)

        self.label_238 = QLabel(self.test_data_page)
        self.label_238.setObjectName(u"label_238")

        self.horizontalLayout_70.addWidget(self.label_238)


        self.verticalLayout_26.addLayout(self.horizontalLayout_70)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_246 = QLabel(self.test_data_page)
        self.label_246.setObjectName(u"label_246")

        self.horizontalLayout_67.addWidget(self.label_246)

        self.right_less_l_status = QLabel(self.test_data_page)
        self.right_less_l_status.setObjectName(u"right_less_l_status")

        self.horizontalLayout_67.addWidget(self.right_less_l_status)

        self.right_less_m_status = QLabel(self.test_data_page)
        self.right_less_m_status.setObjectName(u"right_less_m_status")

        self.horizontalLayout_67.addWidget(self.right_less_m_status)

        self.right_less_h_status = QLabel(self.test_data_page)
        self.right_less_h_status.setObjectName(u"right_less_h_status")

        self.horizontalLayout_67.addWidget(self.right_less_h_status)

        self.label_243 = QLabel(self.test_data_page)
        self.label_243.setObjectName(u"label_243")

        self.horizontalLayout_67.addWidget(self.label_243)


        self.verticalLayout_26.addLayout(self.horizontalLayout_67)

        self.line_9 = QFrame(self.test_data_page)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setFrameShape(QFrame.HLine)

        self.verticalLayout_26.addWidget(self.line_9)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_249 = QLabel(self.test_data_page)
        self.label_249.setObjectName(u"label_249")

        self.horizontalLayout_64.addWidget(self.label_249)

        self.right_test_time_point = QLabel(self.test_data_page)
        self.right_test_time_point.setObjectName(u"right_test_time_point")

        self.horizontalLayout_64.addWidget(self.right_test_time_point)

        self.label_251 = QLabel(self.test_data_page)
        self.label_251.setObjectName(u"label_251")

        self.horizontalLayout_64.addWidget(self.label_251)

        self.right_test_time_during = QLabel(self.test_data_page)
        self.right_test_time_during.setObjectName(u"right_test_time_during")

        self.horizontalLayout_64.addWidget(self.right_test_time_during)


        self.verticalLayout_26.addLayout(self.horizontalLayout_64)

        self.line_10 = QFrame(self.test_data_page)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setFrameShape(QFrame.HLine)

        self.verticalLayout_26.addWidget(self.line_10)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_262 = QLabel(self.test_data_page)
        self.label_262.setObjectName(u"label_262")

        self.horizontalLayout_80.addWidget(self.label_262)

        self.label_263 = QLabel(self.test_data_page)
        self.label_263.setObjectName(u"label_263")

        self.horizontalLayout_80.addWidget(self.label_263)

        self.label_261 = QLabel(self.test_data_page)
        self.label_261.setObjectName(u"label_261")

        self.horizontalLayout_80.addWidget(self.label_261)

        self.label_260 = QLabel(self.test_data_page)
        self.label_260.setObjectName(u"label_260")

        self.horizontalLayout_80.addWidget(self.label_260)


        self.verticalLayout_26.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.right_test_count = QLabel(self.test_data_page)
        self.right_test_count.setObjectName(u"right_test_count")

        self.horizontalLayout_57.addWidget(self.right_test_count)

        self.right_pass_count = QLabel(self.test_data_page)
        self.right_pass_count.setObjectName(u"right_pass_count")

        self.horizontalLayout_57.addWidget(self.right_pass_count)

        self.right_fail_count = QLabel(self.test_data_page)
        self.right_fail_count.setObjectName(u"right_fail_count")

        self.horizontalLayout_57.addWidget(self.right_fail_count)

        self.right_fail_rate = QLabel(self.test_data_page)
        self.right_fail_rate.setObjectName(u"right_fail_rate")

        self.horizontalLayout_57.addWidget(self.right_fail_rate)


        self.verticalLayout_26.addLayout(self.horizontalLayout_57)


        self.horizontalLayout_7.addLayout(self.verticalLayout_26)


        self.verticalLayout_20.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.test_data_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_6.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"HCD-BTTP", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Bluetooth Test Platform</p></body></html>", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.btn_test_data.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u754c\u9762", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u914d\u7f6e", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"**                HCD - BTTP** \n"
"\n"
"Test Framework Design by: emmovo \n"
"\n"
"Created by: Wanderson M. Pimenta\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">                HCD - BTTP</span> </p>\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Test Framework Design by: emmovo </p>\n"
"<p style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Created by: Wanderson M. Pimenta</p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyDracula APP - Theme with colors based on Dracula for Python.", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u72b6\u6001\uff1a", None))
        self.setting_status.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u6587\u4ef6\u52a0\u8f7d...", None))
        self.mt8852b_status.setText(QCoreApplication.translate("MainWindow", u"MT8852B\u521d\u59cb\u5316...", None))
        self.left_box_status.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u5c4f\u853d\u7bb1\u8fde\u63a5...", None))
        self.right_box_status.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u5c4f\u853d\u7bb1\u8fde\u63a5...", None))
        self.left_bttc_status.setText(QCoreApplication.translate("MainWindow", u"\u5de6BTTC\u8fde\u63a5...", None))
        self.right_bttc_status.setText(QCoreApplication.translate("MainWindow", u"\u53f3BTTC\u8fde\u63a5...", None))
        self.signal_switch_status.setText(QCoreApplication.translate("MainWindow", u"\u5c04\u9891\u4fe1\u53f7\u5207\u6362\u5668\u8fde\u63a5...", None))
        self.mes_serice_status.setText(QCoreApplication.translate("MainWindow", u"MES\u670d\u52a1\u5668\u5668\u8fde\u63a5...", None))
        self.left_channel_status.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u6d4b\u8bd5\u901a\u9053-\u5173\u95ed", None))
        self.right_channel_status.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u6d4b\u8bd5\u901a\u9053-\u5173\u95ed", None))
        self.start_test_btn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6d4b\u8bd5", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"LOG \u6570\u636e\u663e\u793a\uff1a", None))
        self.test_config_btn.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u8bbe\u7f6e", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"MT8852B \u8fde\u63a5\u72b6\u6001", None))
        self.MT8852_ID.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.MT8852_status_label.setText(QCoreApplication.translate("MainWindow", u"\u672a\u8fde\u63a5", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u5c4f\u853d\u7bb1\u901a\u8baf\u7aef\u53e3", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u5c4f\u853d\u7bb1\u901a\u8baf\u7aef\u53e3", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u7535\u6e90\u63a7\u5236\u5668\u901a\u8baf\u7aef\u53e3", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u7535\u6e90\u63a7\u5236\u5668\u901a\u8baf\u7aef\u53e3", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5c04\u9891\u4fe1\u53f7\u6e90\u5207\u6362\u7aef\u53e3", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u8d85\u65f6\u65f6\u95f4\uff08s\uff09", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"BLE\u8f93\u51fa\u529f\u7387\u6d4b\u8bd5", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5c01\u5305\u6570", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u9891\u9891\u7387(kHz) ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u529f\u7387\u4e0a\u9650(dBm) >=", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u9891\u9891\u7387(kHz) ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u529f\u7387\u4e0b\u9650(dBm) <=", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u9891\u9891\u7387(kHz) ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u5cf0\u503c\u529f\u7387\u4e0a\u9650(dBm) <=", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"BLE\u9891\u504f\u6f02\u79fb\u6d4b\u8bd5", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u5c01\u5305\u6570", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u9891\u9891\u7387(kHz) ", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5411\u6700\u5927\u504f\u5dee(kHz) <=", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u9891\u9891\u7387(kHz) ", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u5411\u6700\u5927\u504f\u5dee(kHz) <=", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u9891\u9891\u7387(kHz) ", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u6f02\u79fb\u901f\u7387(kHz) +/-", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u6f02\u79fb\u8303\u56f4(kHz) +/-", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5305\u6f02\u79fb\u8303\u56f4(kHz) +/-", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"BLE\u7075\u654f\u5ea6\u6d4b\u8bd5", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u5c01\u5305\u6570", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u9891\u9891\u7387(kHz) ", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"                  \u6709\u6270\u6d4b\u8bd5", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u9891\u9891\u7387(kHz) ", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"         \u53d1\u5c04\u529f\u7387(dBm)", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u9891\u9891\u7387(kHz) ", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"              FER\u4e0a\u9650(%)", None))
        self.cfg_save_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.default_btn.setText(QCoreApplication.translate("MainWindow", u"\u6062\u590d\u9ed8\u8ba4\u503c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SN\u7801\u8f93\u5165\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u529f\u7387\u6d4b\u8bd5\u7ed3\u679c\uff1a", None))
        self.left_leop_result.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u901a\u9053", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u901a\u9053", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u901a\u9053", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"\u9608\u503c", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u529f\u7387\uff1a", None))
        self.left_leop_l_max.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_m_max.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_h_max.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_avg_ucl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u529f\u7387\uff1a", None))
        self.left_leop_l_avg.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_m_avg.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_h_avg.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u529f\u7387\uff1a", None))
        self.left_leop_l_min.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_m_min.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_h_min.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_avg_lcl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u5cf0\u503c\u529f\u7387\uff1a", None))
        self.left_leop_l_peak.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_m_peak.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_h_peak.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_peak_ucl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7ed3\u679c\uff1a", None))
        self.left_leop_l_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_m_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leop_h_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u8f7d\u6ce2\u9891\u504f\u548c\u6f02\u79fb\u6d4b\u8bd5\uff1a", None))
        self.left_leicd_result.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u901a\u9053", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u901a\u9053", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u901a\u9053", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"\u9608\u503c", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u9891\u504f\uff1a", None))
        self.left_leicd_l_avg_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_m_avg_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_h_avg_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_avg.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u9891\u504f+ve\uff1a", None))
        self.left_leicd_l_max_p_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_m_max_p_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_h_max_p_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_p_fn_ucl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u9891\u504f-ve\uff1a", None))
        self.left_leicd_l_max_n_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_m_max_n_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_h_max_n_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_n_fn_ucl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u6f02\u79fb\u901f\u7387\uff1a", None))
        self.left_leicd_l_max_dirft_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_m_max_dirft_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_h_max_dirft_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_drift_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u6f02\u79fb\uff1a", None))
        self.left_leicd_l_max_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_m_max_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_h_max_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_drift_range.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u6f02\u79fb\uff1a", None))
        self.left_leicd_l_avg_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_m_avg_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_h_avg_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7ed3\u679c\uff1a", None))
        self.left_leicd_l_state.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_m_state.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_leicd_h_state.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_label.setText(QCoreApplication.translate("MainWindow", u"\u7075\u654f\u5ea6\u6d4b\u8bd5\uff1a", None))
        self.left_less_result.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u901a\u9053", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u901a\u9053", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u901a\u9053", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"\u9608\u503c", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5e27\u7387\uff1a", None))
        self.left_less_l_over_fer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_m_over_fer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_h_over_fer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_fer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5305\u6570\uff1a", None))
        self.left_less_l_total_frames_sent_tester.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_m_total_frames_sent_tester.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_h_total_frames_sent_tester.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u5305\u6570\uff1a", None))
        self.left_less_l_total_frames_counted_dut.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_m_total_frames_counted_dut.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_h_total_frames_counted_dut.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7ed3\u679c\uff1a", None))
        self.left_less_l_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_m_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_less_h_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u65f6\u95f4\uff1a", None))
        self.left_test_time_point.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7528\u65f6\uff1a", None))
        self.left_test_time_during.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u603b\u6570", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8fc7\u4e2a\u6570", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"\u5931\u8d25\u4e2a\u6570", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"\u574f\u7387", None))
        self.left_test_count.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_pass_count.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_fail_count.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.left_fail_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SN\u7801\u8f93\u5165\uff1a", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u529f\u7387\u6d4b\u8bd5\u7ed3\u679c\uff1a", None))
        self.right_leop_result.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u901a\u9053", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u901a\u9053", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u901a\u9053", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"\u9608\u503c", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u529f\u7387\uff1a", None))
        self.right_leop_l_max.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_m_max.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_h_max.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_avg_ucl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u529f\u7387\uff1a", None))
        self.right_leop_l_avg.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_m_avg.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_h_avg.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u529f\u7387\uff1a", None))
        self.right_leop_l_min.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_m_min.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_h_min.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_avg_lcl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"\u5cf0\u503c\u529f\u7387\uff1a", None))
        self.right_leop_l_peak.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_m_peak.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_h_peak.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_peak_ucl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7ed3\u679c\uff1a", None))
        self.right_leop_l_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_m_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leop_h_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"\u8f7d\u6ce2\u9891\u504f\u548c\u6f02\u79fb\u6d4b\u8bd5\uff1a", None))
        self.right_leicd_result.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u901a\u9053", None))
        self.label_258.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u901a\u9053", None))
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u901a\u9053", None))
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"\u9608\u503c", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u9891\u504f\uff1a", None))
        self.right_leicd_l_avg_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_m_avg_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_h_avg_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_avg.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u9891\u504f+ve\uff1a", None))
        self.right_leicd_l_max_p_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_m_max_p_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_h_max_p_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_p_fn_ucl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u9891\u504f-ve\uff1a", None))
        self.right_leicd_l_max_n_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_m_max_n_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_h_max_n_fn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_n_fn_ucl.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"\u6f02\u79fb\u901f\u7387\uff1a", None))
        self.right_leicd_l_max_dirft_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_m_max_dirft_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_h_max_dirft_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_drift_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u6f02\u79fb\uff1a", None))
        self.right_leicd_l_max_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_m_max_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_h_max_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_drift_range.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u6f02\u79fb\uff1a", None))
        self.right_leicd_l_avg_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_m_avg_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_h_avg_dirft.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7ed3\u679c\uff1a", None))
        self.right_leicd_l_state.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_m_state.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_leicd_h_state.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"\u7075\u654f\u5ea6\u6d4b\u8bd5\uff1a", None))
        self.right_less_result.setText(QCoreApplication.translate("MainWindow", u"NULL", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u901a\u9053", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u901a\u9053", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u901a\u9053", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"\u9608\u503c", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5e27\u7387\uff1a", None))
        self.right_less_l_over_fer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_less_m_over_fer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_less_h_over_fer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_less_fer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001\u5305\u6570\uff1a", None))
        self.right_less_l_total_frames_sent_tester.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_less_m_total_frames_sent_tester.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_less_h_total_frames_sent_tester.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u5305\u6570\uff1a", None))
        self.right_less_l_total_frames_counted_dut.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_less_m_total_frames_counted_dut.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_less_h_total_frames_counted_dut.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7ed3\u679c\uff1a", None))
        self.right_less_l_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_less_m_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_less_h_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_249.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u65f6\u95f4\uff1a", None))
        self.right_test_time_point.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u7528\u65f6\uff1a", None))
        self.right_test_time_during.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u603b\u6570", None))
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8fc7\u4e2a\u6570", None))
        self.label_261.setText(QCoreApplication.translate("MainWindow", u"\u5931\u8d25\u4e2a\u6570", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"\u574f\u7387", None))
        self.right_test_count.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_pass_count.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_fail_count.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.right_fail_rate.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: emmovo", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

