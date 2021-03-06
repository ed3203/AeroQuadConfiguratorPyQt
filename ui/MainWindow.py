# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sat May 25 15:28:17 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(991, 586)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/AQ/AeroQuadMacIcon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.side_menu = QtGui.QToolBox(self.centralwidget)
        self.side_menu.setMinimumSize(QtCore.QSize(180, 0))
        self.side_menu.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.side_menu.setFont(font)
        self.side_menu.setFrameShape(QtGui.QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QtGui.QFrame.Plain)
        self.side_menu.setObjectName(_fromUtf8("side_menu"))
        self.side_menu_info_page = QtGui.QWidget()
        self.side_menu_info_page.setEnabled(False)
        self.side_menu_info_page.setGeometry(QtCore.QRect(0, 0, 178, 385))
        self.side_menu_info_page.setObjectName(_fromUtf8("side_menu_info_page"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("resources/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.side_menu.addItem(self.side_menu_info_page, icon1, _fromUtf8(""))
        self.side_menu_setting_page = QtGui.QWidget()
        self.side_menu_setting_page.setEnabled(False)
        self.side_menu_setting_page.setGeometry(QtCore.QRect(0, 0, 178, 385))
        self.side_menu_setting_page.setObjectName(_fromUtf8("side_menu_setting_page"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("resources/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.side_menu.addItem(self.side_menu_setting_page, icon2, _fromUtf8(""))
        self.side_menu_troubleshooting_page = QtGui.QWidget()
        self.side_menu_troubleshooting_page.setEnabled(False)
        self.side_menu_troubleshooting_page.setGeometry(QtCore.QRect(0, 0, 178, 385))
        self.side_menu_troubleshooting_page.setObjectName(_fromUtf8("side_menu_troubleshooting_page"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("resources/graphic.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.side_menu.addItem(self.side_menu_troubleshooting_page, icon3, _fromUtf8(""))
        self.side_menu_mission_planer_page = QtGui.QWidget()
        self.side_menu_mission_planer_page.setEnabled(False)
        self.side_menu_mission_planer_page.setGeometry(QtCore.QRect(0, 0, 178, 385))
        self.side_menu_mission_planer_page.setObjectName(_fromUtf8("side_menu_mission_planer_page"))
        self.side_menu.addItem(self.side_menu_mission_planer_page, _fromUtf8(""))
        self.gridLayout.addWidget(self.side_menu, 0, 0, 1, 1)
        self.panel_container = QtGui.QStackedWidget(self.centralwidget)
        self.panel_container.setObjectName(_fromUtf8("panel_container"))
        self.gridLayout.addWidget(self.panel_container, 0, 1, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setMinimumSize(QtCore.QSize(200, 0))
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName(_fromUtf8("status"))
        self.horizontalLayout.addWidget(self.status)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.comPort = QtGui.QComboBox(self.centralwidget)
        self.comPort.setMinimumSize(QtCore.QSize(0, 0))
        self.comPort.setEditable(True)
        self.comPort.setObjectName(_fromUtf8("comPort"))
        self.horizontalLayout.addWidget(self.comPort)
        self.baudRate = QtGui.QComboBox(self.centralwidget)
        self.baudRate.setMinimumSize(QtCore.QSize(0, 0))
        self.baudRate.setEditable(True)
        self.baudRate.setObjectName(_fromUtf8("baudRate"))
        self.horizontalLayout.addWidget(self.baudRate)
        self.buttonConnect = QtGui.QPushButton(self.centralwidget)
        self.buttonConnect.setObjectName(_fromUtf8("buttonConnect"))
        self.horizontalLayout.addWidget(self.buttonConnect)
        self.buttonDisconnect = QtGui.QPushButton(self.centralwidget)
        self.buttonDisconnect.setObjectName(_fromUtf8("buttonDisconnect"))
        self.horizontalLayout.addWidget(self.buttonDisconnect)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.button_home = QtGui.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_home.setIcon(icon4)
        self.button_home.setObjectName(_fromUtf8("button_home"))
        self.gridLayout.addWidget(self.button_home, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QtGui.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 991, 21))
        self.menu_bar.setObjectName(_fromUtf8("menu_bar"))
        self.menu_file = QtGui.QMenu(self.menu_bar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_settings = QtGui.QMenu(self.menu_file)
        self.menu_settings.setObjectName(_fromUtf8("menu_settings"))
        self.menu_calibration = QtGui.QMenu(self.menu_file)
        self.menu_calibration.setObjectName(_fromUtf8("menu_calibration"))
        self.menu_preferences = QtGui.QMenu(self.menu_file)
        self.menu_preferences.setObjectName(_fromUtf8("menu_preferences"))
        self.menu_view = QtGui.QMenu(self.menu_bar)
        self.menu_view.setObjectName(_fromUtf8("menu_view"))
        self.menu_help = QtGui.QMenu(self.menu_bar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        MainWindow.setMenuBar(self.menu_bar)
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.action_open_settings = QtGui.QAction(MainWindow)
        self.action_open_settings.setObjectName(_fromUtf8("action_open_settings"))
        self.action_save_settings = QtGui.QAction(MainWindow)
        self.action_save_settings.setObjectName(_fromUtf8("action_save_settings"))
        self.action_open_calibrations = QtGui.QAction(MainWindow)
        self.action_open_calibrations.setObjectName(_fromUtf8("action_open_calibrations"))
        self.action_save_calibrations = QtGui.QAction(MainWindow)
        self.action_save_calibrations.setObjectName(_fromUtf8("action_save_calibrations"))
        self.action_bootup_delay = QtGui.QAction(MainWindow)
        self.action_bootup_delay.setObjectName(_fromUtf8("action_bootup_delay"))
        self.action_comm_timeout = QtGui.QAction(MainWindow)
        self.action_comm_timeout.setObjectName(_fromUtf8("action_comm_timeout"))
        self.menu_settings.addAction(self.action_open_settings)
        self.menu_settings.addAction(self.action_save_settings)
        self.menu_calibration.addAction(self.action_open_calibrations)
        self.menu_calibration.addAction(self.action_save_calibrations)
        self.menu_preferences.addAction(self.action_bootup_delay)
        self.menu_preferences.addAction(self.action_comm_timeout)
        self.menu_file.addAction(self.menu_settings.menuAction())
        self.menu_file.addAction(self.menu_calibration.menuAction())
        self.menu_file.addAction(self.menu_preferences.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_about)
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_view.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.side_menu.setCurrentIndex(0)
        self.side_menu.layout().setSpacing(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AeroQuad Configurator", None))
        self.side_menu.setItemText(self.side_menu.indexOf(self.side_menu_info_page), _translate("MainWindow", "Info", None))
        self.side_menu.setItemText(self.side_menu.indexOf(self.side_menu_setting_page), _translate("MainWindow", "Settings", None))
        self.side_menu.setItemText(self.side_menu.indexOf(self.side_menu_troubleshooting_page), _translate("MainWindow", "Data plot", None))
        self.side_menu.setItemText(self.side_menu.indexOf(self.side_menu_mission_planer_page), _translate("MainWindow", "Page", None))
        self.status.setText(_translate("MainWindow", "Not connected to AeroQuad", None))
        self.buttonConnect.setText(_translate("MainWindow", "Connect", None))
        self.buttonDisconnect.setText(_translate("MainWindow", "Disconnect", None))
        self.button_home.setText(_translate("MainWindow", "Home", None))
        self.menu_file.setTitle(_translate("MainWindow", "File", None))
        self.menu_settings.setTitle(_translate("MainWindow", "Settings", None))
        self.menu_calibration.setTitle(_translate("MainWindow", "Calibrations", None))
        self.menu_preferences.setTitle(_translate("MainWindow", "Preferences", None))
        self.menu_view.setTitle(_translate("MainWindow", "View", None))
        self.menu_help.setTitle(_translate("MainWindow", "Help", None))
        self.action_exit.setText(_translate("MainWindow", "Exit", None))
        self.action_about.setText(_translate("MainWindow", "About", None))
        self.action_open_settings.setText(_translate("MainWindow", "Open...", None))
        self.action_save_settings.setText(_translate("MainWindow", "Save...", None))
        self.action_open_calibrations.setText(_translate("MainWindow", "Open...", None))
        self.action_save_calibrations.setText(_translate("MainWindow", "Save....", None))
        self.action_bootup_delay.setText(_translate("MainWindow", "Boot Up Delay...", None))
        self.action_comm_timeout.setText(_translate("MainWindow", "Comm Timeout...", None))

import AQresources_rc
