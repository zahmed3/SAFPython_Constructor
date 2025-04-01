from tkinter import *
from tkinter import filedialog
import gui as gui
import saf as saf

#This function will create a pop-up when the Google Sign-In button is pressed, letting the user know it is still a WIP.
def google_signin_error_popup():
    error_popup = Toplevel(gui.window)
    popup_width = 400
    popup_height = 150
    screen_width = gui.window.winfo_screenwidth()
    screen_height = gui.window.winfo_screenheight()
    x = (screen_width / 2) - (popup_width / 2)
    y = (screen_height / 2) - (popup_height / 2)
    error_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
    error_popup.title("Google Sign-In Error")
    label = Label(error_popup, text="Google Sign-Ins are currently unavailable in this version.", font=("Inter", 10))
    label.pack(padx=20, pady=20)
    close_button = Button(error_popup, text="Close Pop-up", font=("Inter", 10), command=error_popup.destroy)
    close_button.config(width="30", height="15")
    close_button.pack(pady=20)
    error_popup.grab_set()
    gui.window.wait_window(error_popup)

#This function will close the application when the button is pressed.
def close_application():
    gui.window.destroy()

#This function allows the user to select the CSV file they wish to convert.
def select_csv_file():
    gui.window.csvfilename = filedialog.askopenfilename(initialdir="/", title="Select CSV File", filetypes=(("csv files", "*.csv"),("all files", "*.*")))
    gui.selected_file = gui.window.csvfilename
    selected_file_popup = Toplevel(gui.window)
    popup_width = 1000
    popup_height = 150
    screen_width = gui.window.winfo_screenwidth()
    screen_height = gui.window.winfo_screenheight()
    x = (screen_width / 2) - (popup_width / 2)
    y = (screen_height / 2) - (popup_height / 2)
    selected_file_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
    selected_file_popup.title("Selected CSV File Chosen")
    label = Label(selected_file_popup, text="Selected '" + gui.selected_file + "' as chosen file.", font=("Inter", 10))
    label.pack(padx=20, pady=20)
    close_button = Button(selected_file_popup, text="Close Pop-up", font=("Inter", 10), command=selected_file_popup.destroy)
    close_button.config(width="30", height="15")
    close_button.pack(pady=20)
    selected_file_popup.grab_set()
    gui.window.wait_window(selected_file_popup)

#This function will let the user select the folder where they want the output to be created.
def select_folder_destination():
    gui.window.folderpath = filedialog.askdirectory(initialdir="/", title="Select File Destination")
    gui.selected_folder = gui.window.folderpath
    selected_folder_popup = Toplevel(gui.window)
    popup_width = 1000
    popup_height = 150
    screen_width = gui.window.winfo_screenwidth()
    screen_height = gui.window.winfo_screenheight()
    x = (screen_width / 2) - (popup_width / 2)
    y = (screen_height / 2) - (popup_height / 2)
    selected_folder_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
    selected_folder_popup.title("Selected Folder Destination Chosen")
    label = Label(selected_folder_popup, text="Selected '" + gui.selected_folder + "' as chosen folder destination.", font=("Inter", 10))
    label.pack(padx=20, pady=20)
    close_button = Button(selected_folder_popup, text="Close Pop-up", font=("Inter", 10), command=selected_folder_popup.destroy)
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
        label = Label(file_error_popup, text="Please select the file you wish to input.", font=("Inter", 10))
        label.pack(padx=20, pady=20)
        close_button = Button(file_error_popup, text="Close Pop-up", font=("Inter", 10), command=file_error_popup.destroy)
        close_button.config(width="30", height="15")
        close_button.pack(pady=20)
        file_error_popup.grab_set()
        gui.window.wait_window(file_error_popup)
    elif(len(gui.selected_folder) == 0 and len(gui.selected_file) != 0):
        folder_error_popup = Toplevel(gui.window)
        folder_error_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
        folder_error_popup.title("Folder Input Error")
        label = Label(folder_error_popup, text="Please select the folder destination to output to.", font=("Inter", 10))
        label.pack(padx=20, pady=20)
        close_button = Button(folder_error_popup, text="Close Pop-up", font=("Inter", 10), command=folder_error_popup.destroy)
        close_button.config(width="30", height="15")
        close_button.pack(pady=20)
        folder_error_popup.grab_set()
        gui.window.wait_window(folder_error_popup)
    elif(len(gui.selected_file) == 0 and len(gui.selected_folder) == 0):
        file_and_folder_error_popup = Toplevel(gui.window)
        file_and_folder_error_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
        file_and_folder_error_popup.title("File and Folder Input Error")
        label = Label(file_and_folder_error_popup, text="Please select the file you wish to input and the folder destination to output to.", font=("Inter", 10))
        label.pack(padx=20, pady=20)
        close_button = Button(file_and_folder_error_popup, text="Close Pop-up", font=("Inter", 10), command=file_and_folder_error_popup.destroy)
        close_button.config(width="30", height="15")
        close_button.pack(pady=20)
        file_and_folder_error_popup.grab_set()
        gui.window.wait_window(file_and_folder_error_popup)
    else:
        saf.open_csv()
        popup_width = 1000
        popup_height = 150
        x = (screen_width / 2) - (popup_width / 2)
        y = (screen_height / 2) - (popup_height / 2)
        saf_completion_popup = Toplevel(gui.window)
        saf_completion_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
        saf_completion_popup.title("SAF Operation Completed")
        label = Label(saf_completion_popup, text="SAF files have been created in '" + gui.selected_folder + "' .", font=("Inter", 10))
        label.pack(padx=20, pady=20)
        close_button = Button(saf_completion_popup, text="Close Pop-up", font=("Inter", 10), command=saf_completion_popup.destroy)
        close_button.config(width="30", height="15")
        close_button.pack(pady=20)
        saf_completion_popup.grab_set()
        gui.window.wait_window(saf_completion_popup)