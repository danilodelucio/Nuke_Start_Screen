# -----------------------------------------------------------------------------------
#  Nuke_Start_Screen
#  Version: v1.0
#  Author: Danilo de Lucio
#  Website: www.danilodelucio.com
#  Create Date: 10/Dec/2024
#  Update Date: 20/Dec/2024
# -----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------
#  [Summary]
#  Displays a window containing the last seven recent files when opening Nuke.
#
# -----------------------------------------------------------------------------------

import os

import nuke

from Qt import QtWidgets, QtCompat, QtCore, QtGui

# CONSTANT VARIABLES
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(SCRIPT_PATH, "imgs", "{}.png")
TOOL_NAME = "Nuke Start Screen"
TOOL_VERSION = "v1.0"

# Global variable
window_shown = False

class NukeStartScreen(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(NukeStartScreen, self).__init__(parent)

        # Load UI file
        path_ui = SCRIPT_PATH + "/nkss.ui"
        self.nkss = QtCompat.loadUi(path_ui, self)

        # Load Cover image
        self.label_cover = self.nkss.label_cover
        self.label_cover.setPixmap(QtGui.QPixmap(IMG_PATH.format("cover")))

        self.setModal(True)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        ###################################### ASSIGNING WIDGETS ######################################
        self.explorer_1 = self.nkss.pushButton_explorer_1
        self.explorer_2 = self.nkss.pushButton_explorer_2
        self.explorer_3 = self.nkss.pushButton_explorer_3
        self.explorer_4 = self.nkss.pushButton_explorer_4
        self.explorer_5 = self.nkss.pushButton_explorer_5
        self.explorer_6 = self.nkss.pushButton_explorer_6
        self.explorer_7 = self.nkss.pushButton_explorer_7

        self.filename_1 = self.nkss.pushButton_filename_1
        self.filename_2 = self.nkss.pushButton_filename_2
        self.filename_3 = self.nkss.pushButton_filename_3
        self.filename_4 = self.nkss.pushButton_filename_4
        self.filename_5 = self.nkss.pushButton_filename_5
        self.filename_6 = self.nkss.pushButton_filename_6
        self.filename_7 = self.nkss.pushButton_filename_7

        self.filepath_1 = self.nkss.label_filepath_1
        self.filepath_2 = self.nkss.label_filepath_2
        self.filepath_3 = self.nkss.label_filepath_3
        self.filepath_4 = self.nkss.label_filepath_4
        self.filepath_5 = self.nkss.label_filepath_5
        self.filepath_6 = self.nkss.label_filepath_6
        self.filepath_7 = self.nkss.label_filepath_7

        self.open_button = self.nkss.pushButton_open
        self.open_button.setText("Open another Nuke Script")
        self.new_button = self.nkss.pushButton_new
        self.new_button.setText("New Nuke Script")

        self.label_footer = self.nkss.label_footer

        ###################################### GETTING INFO ######################################
        self.recent_projects_list = self.recent_projects()

        self.fill_list(self.recent_projects_list)

        self.filename_list = []
        self.filepath_list = []

        for recent_project in self.recent_projects_list:
            if recent_project == None:
                self.filename_list.append(None)
                self.filepath_list.append(None)
            else:
                self.filename_list.append(self.filename_and_directory(recent_project)[0])
                self.filepath_list.append(self.filename_and_directory(recent_project)[1])


        self.filename_buttons_list = [self.filename_1, self.filename_2, self.filename_3, self.filename_4,
                                      self.filename_5, self.filename_6, self.filename_7]
        
        self.filepath_labels_list = [self.filepath_1, self.filepath_2, self.filepath_3, self.filepath_4,
                                     self.filepath_5, self.filepath_6, self.filepath_7]
        
        self.explorer_buttons_list = [self.explorer_1, self.explorer_2, self.explorer_3, self.explorer_4,
                                      self.explorer_5, self.explorer_6, self.explorer_7]
        
        for explorer_button in self.explorer_buttons_list:
            explorer_button.setIcon(QtGui.QIcon(IMG_PATH.format("folder")))

        ###################################### SIGNALS ######################################
        self.explorer_1.clicked.connect(lambda: self.press_explorerButton(0))
        self.explorer_2.clicked.connect(lambda: self.press_explorerButton(1))
        self.explorer_3.clicked.connect(lambda: self.press_explorerButton(2))
        self.explorer_4.clicked.connect(lambda: self.press_explorerButton(3))
        self.explorer_5.clicked.connect(lambda: self.press_explorerButton(4))
        self.explorer_6.clicked.connect(lambda: self.press_explorerButton(5))
        self.explorer_7.clicked.connect(lambda: self.press_explorerButton(6))

        self.filename_1.clicked.connect(lambda: self.press_filenameButton(0))
        self.filename_2.clicked.connect(lambda: self.press_filenameButton(1))
        self.filename_3.clicked.connect(lambda: self.press_filenameButton(2))
        self.filename_4.clicked.connect(lambda: self.press_filenameButton(3))
        self.filename_5.clicked.connect(lambda: self.press_filenameButton(4))
        self.filename_6.clicked.connect(lambda: self.press_filenameButton(5))
        self.filename_7.clicked.connect(lambda: self.press_filenameButton(6))

        self.new_button.clicked.connect(self.press_newButton)
        self.open_button.clicked.connect(self.press_openButton)
        ###################################### SETTING WIDGETS ######################################

        self.label_footer.setText('<a style="color: {0}">{1} {2} | Developed by Danilo de Lucio | <a href="http://www.danilodelucio.com"; style="color: {0}"; text-decoration: underline;">www.danilodelucio.com</a> | <a href="https://github.com/danilodelucio/Nuke_Start_Screen"; style="color: {0}"; text-decoration: underline;">GitHub</a></a>'.format("grey", TOOL_NAME, TOOL_VERSION))
        self.label_footer.setOpenExternalLinks(True)
        
        self.set_text()
        self.disable_buttons()


    def fill_list(self, input_list):
        """Fill the input list with None if it has less than 7 elements."""
        while len(input_list) < 7:
            input_list.append(None)

        return input_list

    def recent_projects(self):
        """Get the file paths from the recent_files file on .nuke directory."""
        recent_files = []

        for files in range(1, 8):
            try:
                recent_files.append(nuke.recentFile(files))
            except:
                pass

        return recent_files

    def filename_and_directory(self, path):
        """Split the input list into 2 lists, containing the filename and filepath."""
        return [os.path.basename(path), os.path.dirname(path)]

    def set_text(self):
        """Set text for all buttons and labels."""
        for button, label, filename, filepath in zip(self.filename_buttons_list, self.filepath_labels_list, self.filename_list, self.filepath_list):
            if filename == None or filepath == None:
                button.setText("")
                label.setText("")
            else:
                button.setText(filename)
                label.setText(filepath)
        
        # Even displaying the info, disable the button if the path doesn't exist and set the label color to red
        for filename_button, label, recent_project, explorer_button in zip(self.filename_buttons_list, self.filepath_labels_list, self.recent_projects_list, self.explorer_buttons_list):
            if recent_project != None and not os.path.exists(recent_project):
                filename_button.setEnabled(False)
                label.setStyleSheet("color: rgb(225, 60, 50);")

                explorer_button.setEnabled(False)

    def disable_buttons(self):
        """Disable and Hide all buttons if they have None as value."""
        for recent_project, explorer_button, filename_button in zip(self.recent_projects_list, self.explorer_buttons_list, self.filename_buttons_list):
            if recent_project == None:
                filename_button.setEnabled(False)
                filename_button.hide()

                explorer_button.setEnabled(False)
                explorer_button.hide()

    # PRESS BUTTONS
    def press_explorerButton(self, filepath_index):
        filepath = self.filepath_list[filepath_index]

        if os.path.exists(filepath):
            os.startfile(filepath)
        else:
            nuke.message("The filepath does not exist!")

    def press_filenameButton(self, filename_index):
        filepath = self.recent_projects_list[filename_index]

        if os.path.exists(filepath):
            self.close()
            nuke.scriptOpen(filepath)
        else:
            nuke.message("The filepath does not exist!")

    def press_newButton(self):
        self.close()
        nuke.scriptClose()

    def press_openButton(self):
        if nuke.env['nc']:
            nuke_version = "nknc"
        else:
            nuke_version = "nk"
            
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Nuke Script", "", "Nuke Scripts (*.{})".format(nuke_version)) 
        
        if filepath: 
            try: 
                self.close() 
                nuke.scriptOpen(filepath) 
            except Exception as e: 
                nuke.message(e) 
                self.show() 


def show_start_screen():
    app = QtWidgets.QApplication.instance()
    if not app:
        app = QtWidgets.QApplication([])

    dialog = NukeStartScreen()
    dialog.show()

    if not app.applicationPid(): 
        app.exec_()

def callback_load_UI():
    global window_shown

    if not window_shown and nuke.script_directory() == "":
        show_start_screen()
        window_shown = True

nuke.callbacks.addUpdateUI(callback_load_UI)

if __name__ == "__main__":
    show_start_screen()