import gui as gui
import os

#Will alert the user with a pop-up on operation run if they want to continue with operation or end operation early.
def alert_unnecessary_files():
    #read files

    #if none found, pop up saying none found

    #if found, pop up saying some files were found

    pass

#May move to saf if it does not work properly
def create_zip():
    pass

#This function will close the application when the button is pressed.
def close_application():
    gui.window.destroy()

#Opens the folder containing the output when the option is checked.
def open_output_folder():
    os.startfile(gui.selected_folder)