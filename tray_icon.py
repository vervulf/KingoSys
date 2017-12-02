from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction, qApp
from PyQt5.QtGui import QIcon
import system_commands as sys_cmds


class TrayIcon(QSystemTrayIcon):
    def __init__(self, icon_name):
        QSystemTrayIcon.__init__(self)

        self.setIcon(QIcon(icon_name))

        self.screen_rotate = QAction("Screen Inverted", self, checkable=True)
        self.screen_rotate.triggered.connect(lambda item: self.__screen_rotate())

        sys_cmds.cmd_exec(sys_cmds.touchscreen_disable)
        self.touch_screen = QAction("Touchscreen", self, checkable=True)
        self.touch_screen.triggered.connect(lambda item: self.__touch_trigger())

        self.keyboard = QAction("Keyboard", self, checkable=True)
        self.keyboard.triggered.connect(lambda item: self.__keyboard_triger())

        self.__update_all_states()

        quit_action = QAction("Exit", self)
        quit_action.triggered.connect(qApp.quit)

        tray_menu = QMenu()
        tray_menu.addAction(self.screen_rotate)
        tray_menu.addAction(self.touch_screen)
        tray_menu.addAction(self.keyboard)
        tray_menu.addSeparator()
        tray_menu.addAction(quit_action)
        self.setContextMenu(tray_menu)

        self.activated.connect(lambda reason: self.__show_menu())

    def __show_menu(self):
        pos = self.geometry().bottomLeft()
        self.contextMenu().move(pos)
        self.contextMenu().show()

    def __touch_state(self):
        self.touch_enabled = '1' in sys_cmds.cmd_exec(sys_cmds.touchscreen_state)

    def __screen_state(self):
        self.screen_inverted = 'inverted' in sys_cmds.cmd_exec(sys_cmds.screen_state)

    def __keyboard_state(self):
        self.keyboard_enabled = '1' in sys_cmds.cmd_exec(sys_cmds.keyboard_state)

    def __update_all_states(self):
        self.__touch_state()
        self.touch_screen.setChecked(self.touch_enabled)

        self.__screen_state()
        self.screen_rotate.setChecked(self.screen_inverted)

        self.__keyboard_state()
        self.keyboard.setChecked(self.keyboard_enabled)

    def __keyboard_triger(self):
        if self.keyboard_enabled:
            sys_cmds.cmd_exec(sys_cmds.keyboard_disable)
        else:
            sys_cmds.cmd_exec(sys_cmds.keyboard_enable)
        self.__update_all_states()

    def __touch_trigger(self):
        if self.touch_enabled:
            sys_cmds.cmd_exec(sys_cmds.touchscreen_disable)
        else:
            sys_cmds.cmd_exec(sys_cmds.touchscreen_enable)
        self.__update_all_states()

    def __screen_rotate(self):
        if self.screen_inverted:
            sys_cmds.cmd_exec(sys_cmds.screen_normal)
        else:
            sys_cmds.cmd_exec(sys_cmds.screen_inverted)
        self.__update_all_states()