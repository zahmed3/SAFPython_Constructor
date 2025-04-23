import gui as gui
import os
import os.path
import saf
import shutil
import pandas as pd

#Will alert the user with a pop-up on operation run if they want to continue with operation or end operation early.
def alert_unnecessary_files():
    gui.unnecessary_file_count = 0
    input_folder_path = os.path.dirname(gui.selected_file)
    for file in os.listdir(input_folder_path):
        if not(file.endswith(".pdf") or file.endswith(".csv") or file.endswith(".docx") or file.endswith(".mp3")
               or file.endswith(".mp4") or file.endswith(".zip")):
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

#Will check if there are any mismatched files between the CSV file and input folder and alert the user if mismatched.
def check_filenames_from_csv():
    df = pd.read_csv(gui.selected_file, usecols=["filename"])
    updated_df = df[df["filename"].notnull()]
    csv_filename_list = updated_df["filename"].tolist()
    updated_csv_filename_list = []
    for line in csv_filename_list:
        for item in line.split("||"):
            updated_csv_filename_list.append(item)

    input_folder_filename_list = []
    input_folder_path = os.path.dirname(gui.selected_file)
    for file in os.listdir(input_folder_path):
        if (file.endswith(".pdf") or file.endswith(".docx") or file.endswith(".mp3") or file.endswith(".mp4")
                or file.endswith(".zip")):
            input_folder_filename_list.append(file)

    mismatched_filename_list = list(set(updated_csv_filename_list).difference(input_folder_filename_list))
    return mismatched_filename_list