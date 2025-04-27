import gui as gui
from tkinter import *

#Will pop up when clicking the Google Sign In button.
def google_signin_error():
    error_popup = Toplevel(gui.window)
    popup_width = 1000
    popup_height = 150
    screen_width = gui.window.winfo_screenwidth()
    screen_height = gui.window.winfo_screenheight()
    x = (screen_width / 2) - (popup_width / 2)
    y = (screen_height / 2) - (popup_height / 2)
    error_popup.geometry(f'{popup_width}x{popup_height}+{int(x)}+{int(y)}')
    error_popup.title("Google Drive Upload Feature Cancelled")
    label = Label(error_popup,
                  text="This feature has unfortunately been cancelled. Please refer to the GitHub page and documentation for more information.",
                  font=("Inter", 10))
    label.pack(padx=20, pady=20)
    close_button = Button(error_popup, text="Close Pop-up", font=("Inter", 10), command=error_popup.destroy)
    close_button.config(width="30", height="15")
    close_button.pack(pady=20)
    error_popup.grab_set()
    gui.window.wait_window(error_popup)