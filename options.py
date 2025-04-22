import gui as gui
import os
import os.path
import saf
import shutil

#Will alert the user with a pop-up on operation run if they want to continue with operation or end operation early.
def alert_unnecessary_files():
    gui.unnecessary_file_count = 0
    input_folder_path = os.path.dirname(gui.selected_file)
    for file in os.listdir(input_folder_path):
        if not(file.endswith(".pdf") or file.endswith(".csv") or file.endswith(".docx") or file.endswith(".mp3")
               or file.endswith(".mp4")):
            gui.unnecessary_file_count += 1

#Creates ZIP archives of the operation's output within the SAF folder.
def create_zip():
    saf_folder_path = os.path.join(gui.selected_folder + "/SimpleArchiveFormat")
    for folder in os.listdir(saf_folder_path):
        if folder in os.listdir(saf_folder_path) and os.path.isdir(os.path.join(saf_folder_path, folder)):
            shutil.make_archive(os.path.join(saf_folder_path, folder), 'zip',
                                os.path.join(saf_folder_path, folder))

#This function will close the application when the button is pressed.
def close_application():
    gui.window.destroy()

#Opens the folder containing the output when the option is checked.
def open_output_folder():
    os.startfile(gui.selected_folder)