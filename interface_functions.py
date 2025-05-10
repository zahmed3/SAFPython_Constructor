from tkinter import *
from tkinter import filedialog
import gui as gui
import saf as saf
import options as opt
import os
import google_drive_upload as gdu
import time

#This function allows the user to select the CSV file they wish to convert.
def select_csv_file():
    gui.window.csvfilename = filedialog.askopenfilename(initialdir="/",
                                                        title="Select CSV File",
                                                        filetypes=(("csv files", "*.csv"),("all files", "*.*")))
    gui.selected_file = gui.window.csvfilename
    selected_file_popup = Toplevel(gui.window)
    popup_width = 1000
    popup_height = 150
    screen_width = gui.window.winfo_screenwidth()
    screen_height = gui.window.winfo_screenheight()
    x = (screen_width / 2) - (popup_width / 2)
    y = (screen_height / 2) - (popup_height / 2)
    selected_file_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
    if gui.selected_file == "":
        selected_file_popup.title("Error: CSV File Not Selected")
        label = Label(selected_file_popup,
                      text="Error when selecting CSV file, please try again.",
                      font=("Inter", 10))
    else:
        selected_file_popup.title("Selected CSV File Chosen")
        label = Label(selected_file_popup,
                      text="Selected '" + gui.selected_file + "' as chosen file.",
                      font=("Inter", 10))
    label.pack(padx=20, pady=20)
    close_button = Button(selected_file_popup,
                          text="Close Pop-up",
                          font=("Inter", 10),
                          command=selected_file_popup.destroy)
    close_button.config(width="30", height="15")
    close_button.pack(pady=20)
    selected_file_popup.grab_set()
    gui.window.wait_window(selected_file_popup)

#This function will let the user select the folder where they want the output to be created.
def select_folder_destination():
    gui.window.folderpath = filedialog.askdirectory(initialdir="/",
                                                    title="Select File Destination")
    gui.selected_folder = gui.window.folderpath
    selected_folder_popup = Toplevel(gui.window)
    popup_width = 1000
    popup_height = 150
    screen_width = gui.window.winfo_screenwidth()
    screen_height = gui.window.winfo_screenheight()
    x = (screen_width / 2) - (popup_width / 2)
    y = (screen_height / 2) - (popup_height / 2)
    selected_folder_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
    if gui.selected_folder == "":
        selected_folder_popup.title("Error: Folder Destination Not Selected")
        label = Label(selected_folder_popup,
                      text="Error when selecting folder destination, please try again.",
                      font=("Inter", 10))
    else:
        selected_folder_popup.title("Selected Folder Destination Chosen")
        label = Label(selected_folder_popup,
                      text="Selected '" + gui.selected_folder + "' as chosen folder destination.",
                      font=("Inter", 10))
    label.pack(padx=20, pady=20)
    close_button = Button(selected_folder_popup,
                          text="Close Pop-up",
                          font=("Inter", 10),
                          command=selected_folder_popup.destroy)
    close_button.config(width="30", height="15")
    close_button.pack(pady=20)
    selected_folder_popup.grab_set()
    gui.window.wait_window(selected_folder_popup)

#This function will check the conditions of whether the selected file and folder are selected.
#It will present the respective error message depending on what still needs to be selected.
#Otherwise, if both options are chosen, it will start the SAF operation.
def start_operation():
    popup_width = 500
    popup_height = 150
    screen_width = gui.window.winfo_screenwidth()
    screen_height = gui.window.winfo_screenheight()
    x = (screen_width / 2) - (popup_width / 2)
    y = (screen_height / 2) - (popup_height / 2)
    if(len(gui.selected_file) == 0 and len(gui.selected_folder) != 0):
        file_error_popup = Toplevel(gui.window)
        file_error_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
        file_error_popup.title("File Input Error")
        label = Label(file_error_popup,
                      text="Please select the file you wish to input.",
                      font=("Inter", 10))
        label.pack(padx=20, pady=20)
        close_button = Button(file_error_popup,
                              text="Close Pop-up",
                              font=("Inter", 10),
                              command=file_error_popup.destroy)
        close_button.config(width="30", height="15")
        close_button.pack(pady=20)
        file_error_popup.grab_set()
        gui.window.wait_window(file_error_popup)
    elif(len(gui.selected_folder) == 0 and len(gui.selected_file) != 0):
        folder_error_popup = Toplevel(gui.window)
        folder_error_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
        folder_error_popup.title("Folder Input Error")
        label = Label(folder_error_popup,
                      text="Please select the folder destination to output to.",
                      font=("Inter", 10))
        label.pack(padx=20, pady=20)
        close_button = Button(folder_error_popup,
                              text="Close Pop-up",
                              font=("Inter", 10),
                              command=folder_error_popup.destroy)
        close_button.config(width="30", height="15")
        close_button.pack(pady=20)
        folder_error_popup.grab_set()
        gui.window.wait_window(folder_error_popup)
    elif(len(gui.selected_file) == 0 and len(gui.selected_folder) == 0):
        file_and_folder_error_popup = Toplevel(gui.window)
        file_and_folder_error_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
        file_and_folder_error_popup.title("File and Folder Input Error")
        label = Label(file_and_folder_error_popup,
                      text="Please select the file you wish to input and the folder destination to output to.",
                      font=("Inter", 10))
        label.pack(padx=20, pady=20)
        close_button = Button(file_and_folder_error_popup,
                              text="Close Pop-up",
                              font=("Inter", 10),
                              command=file_and_folder_error_popup.destroy)
        close_button.config(width="30", height="15")
        close_button.pack(pady=20)
        file_and_folder_error_popup.grab_set()
        gui.window.wait_window(file_and_folder_error_popup)
    else:
        if gui.alert_var.get() == "On":
            popup_width = 1000
            popup_height = 300
            x = (screen_width / 2) - (popup_width / 2)
            y = (screen_height / 2) - (popup_height / 2)
            unused_list = opt.alert_unused_files()
            if gui.unused_file_count != 0:
                alert_popup = Toplevel(gui.window)
                alert_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
                alert_popup.title("Alert: Unused Files Found")
                label = Label(alert_popup,
                              text="There were " + str(gui.unused_file_count) + " unused file(s) found:",
                              font=("Inter", 10))
                label.pack(padx=20, pady=20)
                unused_list_label = Label(alert_popup,
                                          text=repr(unused_list),
                                          font=("Inter", 10))
                unused_list_label.bind('<Configure>',
                                           lambda e: unused_list_label.config(
                                               wraplength=unused_list_label.winfo_width()))
                unused_list_label.pack()
                end_button = Button(alert_popup,
                                    text="End Operation",
                                    font=("Inter", 10),
                                    command=alert_popup.destroy)
                end_button.config(width="15", height="5")
                end_button.pack(pady=20, side="bottom")
                alert_popup.grab_set()
                gui.window.wait_window(alert_popup)
                gui.unused_filename_list.clear()
                return
            else:
                popup_width = 500
                popup_height = 150
                x = (screen_width / 2) - (popup_width / 2)
                y = (screen_height / 2) - (popup_height / 2)
                no_unused_popup = Toplevel(gui.window)
                no_unused_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
                no_unused_popup.title("No Unused Files Found")
                label = Label(no_unused_popup,
                              text="There were no unused files found in the input folder.",
                              font=("Inter", 10))
                label.pack(padx=20, pady=20)
                continue_button = Button(no_unused_popup,
                                         text="Continue",
                                         font=("Inter", 10),
                                         command=no_unused_popup.destroy)
                continue_button.config(width="30", height="15")
                continue_button.pack(pady=20)
                no_unused_popup.grab_set()
                gui.window.wait_window(no_unused_popup)
                continue_start_operation()
        else:
            continue_start_operation()

#Will continue the start operation when the conditions in the start_operation function are met.
#Also manages conditions for when some options are selected on the interface.
def continue_start_operation():
    screen_width = gui.window.winfo_screenwidth()
    screen_height = gui.window.winfo_screenheight()
    popup_width = 1000
    popup_height = 150
    x = (screen_width / 2) - (popup_width / 2)
    y = (screen_height / 2) - (popup_height / 2)
    if len(os.listdir(gui.selected_folder)) != 0:
        folder_not_empty_popup = Toplevel(gui.window)
        folder_not_empty_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
        folder_not_empty_popup.title("Output Folder Selected Not Empty")
        label = Label(folder_not_empty_popup,
                      text="Please empty the folder at '" + gui.selected_folder + "' path to continue the operation.",
                      font=("Inter", 10))
        label.pack(padx=20, pady=20)
        close_button = Button(folder_not_empty_popup,
                              text="Close Pop-up",
                              font=("Inter", 10),
                              command=folder_not_empty_popup.destroy)
        close_button.config(width="30", height="15")
        close_button.pack(pady=20)
        folder_not_empty_popup.grab_set()
        gui.window.wait_window(folder_not_empty_popup)
        return
    else:
        pass
    if gui.mismatched_files_var.get() == "On":
        mismatched_list = opt.check_filenames_from_csv()
        list_length = len(mismatched_list)
        if list_length != 0:
            mismatched_popup = Toplevel(gui.window)
            mismatched_popup_width = 1000
            mismatched_popup_height = 300
            mismatched_x = (screen_width / 2) - (mismatched_popup_width / 2)
            mismatched_y = (screen_height / 2) - (mismatched_popup_height / 2)
            mismatched_popup.geometry(
                f'{mismatched_popup_width}x{mismatched_popup_height}+{int(mismatched_x)}+{int(mismatched_y)}')
            mismatched_popup.title("Alert: Mismatched Files Detected")
            mismatched_label = Label(mismatched_popup,
                                     text="The following mismatched file(s) was/were found. Please resolve this issue before starting operation again:",
                                     font=("Inter", 10))
            mismatched_label.pack(padx=20, pady=20)
            mismatched_list_label = Label(mismatched_popup,
                                          text=repr(mismatched_list),
                                          font=("Inter", 10))
            mismatched_list_label.bind('<Configure>',
                                       lambda e: mismatched_list_label.config(
                                           wraplength=mismatched_list_label.winfo_width()))
            mismatched_list_label.pack()
            end_button = Button(mismatched_popup,
                                text="End Operation",
                                font=("Inter", 10),
                                command=mismatched_popup.destroy)
            end_button.config(width="15", height="5")
            end_button.pack(pady=20, side="bottom")
            mismatched_popup.grab_set()
            gui.window.wait_window(mismatched_popup)
            gui.mismatched_filename_list.clear()
            return
        else:
            all_matches_popup = Toplevel(gui.window)
            all_matches_popup_width = 500
            all_matches_popup_height = 150
            all_matches_x = (screen_width / 2) - (all_matches_popup_width / 2)
            all_matches_y = (screen_height / 2) - (all_matches_popup_height / 2)
            all_matches_popup.geometry(
                f'{all_matches_popup_width}x{all_matches_popup_height}+{int(all_matches_x)}+{int(all_matches_y)}')
            all_matches_popup.title("No Mismatched Files Found")
            all_matches_label = Label(all_matches_popup,
                                     text="There were no mismatched files found in the input folder.",
                                     font=("Inter", 10))
            all_matches_label.pack(padx=20, pady=20)
            continue_button = Button(all_matches_popup,
                                     text="Continue",
                                     font=("Inter", 10),
                                     command=all_matches_popup.destroy)
            continue_button.config(width="30", height="15")
            continue_button.pack(pady=20)
            all_matches_popup.grab_set()
            gui.window.wait_window(all_matches_popup)
            pass
    operation_loading_popup = Toplevel(gui.window)
    loading_popup_width = 500
    loading_popup_height = 150
    loading_x = (screen_width / 2) - (loading_popup_width / 2)
    loading_y = (screen_height / 2) - (loading_popup_height / 2)
    operation_loading_popup.geometry(f'{loading_popup_width}x{loading_popup_height}+{int(loading_x)}+{int(loading_y)}')
    operation_loading_popup.title("SAF Operation in Progress")
    loading_label = Label(operation_loading_popup,
                          text="Loading...",
                          font=("Inter", 10))
    loading_label.pack(padx=20, pady=20, anchor="center")
    operation_loading_popup.grab_set()
    operation_loading_popup.focus_set()
    operation_loading_popup.update()
    saf.open_csv()
    saf_completion_popup = Toplevel(gui.window)
    saf_completion_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
    saf_completion_popup.title("SAF Operation Completed")
    label = Label(saf_completion_popup,
                  text="SAF files have been created in '" + gui.selected_folder + "' .",
                  font=("Inter", 10))
    label.pack(padx=20, pady=20)
    close_button = Button(saf_completion_popup,
                          text="Close Pop-up",
                          font=("Inter", 10),
                          command=lambda:[operation_loading_popup.destroy(), saf_completion_popup.destroy()])
    close_button.config(width="30", height="15")
    close_button.pack(pady=20)
    saf_completion_popup.grab_set()
    saf_completion_popup.focus_set()
    gui.window.wait_window(saf_completion_popup)
    if gui.zip_var.get() == "On":
        zip_popup = Toplevel(gui.window)
        zip_popup_width = 1000
        zip_popup_height = 150
        zip_x = (screen_width / 2) - (zip_popup_width / 2)
        zip_y = (screen_height / 2) - (zip_popup_height / 2)
        zip_popup.geometry(f'{zip_popup_width}x{zip_popup_height}+{int(zip_x)}+{int(zip_y)}')
        zip_popup.title("ZIP Archive Creation in Progress")
        zip_label = Label(zip_popup,
                          text="The application will be unresponsive for a few seconds, please give it some time to complete your request.",
                          font=("Inter", 10))
        zip_label.pack(padx=20, pady=20)
        close_button = Button(zip_popup,
                              text="Continue",
                              font=("Inter", 10),
                              command=zip_popup.destroy)
        close_button.config(width="30", height="15")
        close_button.pack(pady=20)
        zip_popup.grab_set()
        gui.window.wait_window(zip_popup)
        opt.create_zip()
        zip_complete_popup = Toplevel(gui.window)
        zip_complete_popup_width = 500
        zip_complete_popup_height = 150
        zip_complete_x = (screen_width / 2) - (zip_complete_popup_width / 2)
        zip_complete_y = (screen_height / 2) - (zip_complete_popup_height / 2)
        zip_complete_popup.geometry(
            f'{zip_complete_popup_width}x{zip_complete_popup_height}+{int(zip_complete_x)}+{int(zip_complete_y)}')
        zip_complete_popup.title("ZIP Archive Completion")
        zip_complete_label = Label(zip_complete_popup,
                          text="ZIP files have been created. Thank you for waiting.",
                          font=("Inter", 10))
        zip_complete_label.pack(padx=20, pady=20)
        zip_finish_button = Button(zip_complete_popup,
                              text="Close Pop-up",
                              font=("Inter", 10),
                              command=zip_complete_popup.destroy)
        zip_finish_button.config(width="30", height="15")
        zip_finish_button.pack(pady=20)
        zip_complete_popup.grab_set()
        gui.window.wait_window(zip_complete_popup)
    if gui.open_folder_var.get() == "On":
        opt.open_output_folder()
    if gui.close_app_var.get() == "On":
        opt.close_application()