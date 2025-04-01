import interface_functions as intfun
from pathlib import *
from tkinter import *
import os
import sys

#Image file names are temporary and will be updated in future checkpoints.

#This function will create the GUI that is used by the software.
def create_gui():
    #Declares the global variables and sets the starting value for selected_file and selected_folder.
    global window
    global selected_file
    global selected_folder
    selected_file = ""
    selected_folder = ""

    #I found this function solution in the provided link below:
    #https://pythonprogramming.altervista.org/auto-py-to-exe-only-one-file-with-images-for-our-python-apps/
    #This function helped fix my issue with images not being carried over in the .exe file.
    def image_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    #Sets up the window for the GUI.
    window = Tk()
    ui_width = 1280
    ui_height = 720
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (ui_width / 2)
    y = (screen_height / 2) - (ui_height / 2)
    window.geometry(f'{ui_width}x{ui_height}+{int(x)}+{int(y)}')
    window.configure(bg = "#F0F0F0")
    window.title("SAFPython Constructor")
    icon = PhotoImage(file=image_path("saficon.png"))
    window.iconphoto(True, icon)

    #Determines the size and background color of the interface.
    canvas = Canvas(
        window,
        bg = "#F0F0F0",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    #Determines the size and color of the top bar
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        120.0,
        fill="#83D3FE",
        outline="")

    #Places the text in the top colored rectangle
    canvas.create_text(
        55.0,
        31.0,
        anchor="nw",
        text="SAFPython Constructor",
        fill="#000000",
        font=("Inter", 48 * -1)
    )

    #Places the image for the 'Open CSV File' text's background.
    image_image_1 = PhotoImage(file=image_path("image_1.png"))
    image_1 = canvas.create_image(
        205.0,
        274.0,
        image=image_image_1
    )

    #Places the image for the 'Select File Destination' text's background.
    image_image_2 = PhotoImage(file=image_path("image_2.png"))
    image_2 = canvas.create_image(
        599.0,
        274.0,
        image=image_image_2
    )

    #Places the image for the 'Options' text's background.
    image_image_3 = PhotoImage(file=image_path("image_3.png"))
    image_3 = canvas.create_image(
        1042.0,
        174.0,
        image=image_image_3
    )

    #Creates the text for 'Open CSV File.'
    canvas.create_text(
        137.0,
        262.0,
        anchor="nw",
        text="Open CSV File",
        fill="#000000",
        font=("Inter SemiBold", 20 * -1)
    )

    #Creates the text for 'Select File Destination.'
    canvas.create_text(
        499.0,
        262.0,
        anchor="nw",
        text="Select File Destination",
        fill="#000000",
        font=("Inter SemiBold", 20 * -1)
    )

    #Creates the button and assigns the place for 'Select CSV File's operation.
    button_image_1 = PhotoImage(file=image_path("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=intfun.select_csv_file,
        relief="flat"
    )
    button_1.place(
        x=105.0,
        y=304.0,
        width=200.0,
        height=200.0
    )

    #Adds the hover feature for the 'Select CSV File' button.
    button_image_hover_1 = PhotoImage(file=image_path("button_hover_1.png"))
    def button_1_hover(e):
        button_1.config(
            image=button_image_hover_1
        )
    def button_1_leave(e):
        button_1.config(
            image=button_image_1
        )
    button_1.bind('<Enter>', button_1_hover)
    button_1.bind('<Leave>', button_1_leave)

    #Creates the button and assigns the place for 'Select File Destination's operation.
    button_image_2 = PhotoImage(file=image_path("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=intfun.select_folder_destination,
        relief="flat"
    )
    button_2.place(
        x=499.0,
        y=308.0,
        width=200.0,
        height=200.0
    )

    #Adds the hover feature for the 'Select File Destination' button.
    button_image_hover_2 = PhotoImage(file=image_path("button_hover_2.png"))
    def button_2_hover(e):
        button_2.config(
            image=button_image_hover_2
        )
    def button_2_leave(e):
        button_2.config(
            image=button_image_2
        )
    button_2.bind('<Enter>', button_2_hover)
    button_2.bind('<Leave>', button_2_leave)

    #Creates the line on the interface separating the Options and other operations.
    canvas.create_rectangle(
        802.9999990057371,
        119.0,
        804.0,
        720.0,
        fill="#000000",
        outline="")

    #Creates the text for 'Options.'
    canvas.create_text(
        1003.0,
        162.0,
        anchor="nw",
        text="Options",
        fill="#000000",
        font=("Inter SemiBold", 20 * -1)
    )

    #Creates the first checkbox.
    image_image_4 = PhotoImage(file=image_path("image_4.png"))
    image_4 = canvas.create_image(
        894.0,
        286.0,
        image=image_image_4
    )

    #Creates the second checkbox.
    image_image_5 = PhotoImage(file=image_path("image_5.png"))
    image_5 = canvas.create_image(
        894.0,
        568.0,
        image=image_image_5
    )

    #Creates the third checkbox.
    image_image_6 = PhotoImage(file=image_path("image_6.png"))
    image_6 = canvas.create_image(
        894.0,
        474.0,
        image=image_image_6
    )

    #Creates the fourth checkbox.
    image_image_7 = PhotoImage(file=image_path("image_7.png"))
    image_7 = canvas.create_image(
        894.0,
        380.0,
        image=image_image_7
    )

    #Creates the fifth checkbox.
    image_image_8 = PhotoImage(file=image_path("image_8.png"))
    image_8 = canvas.create_image(
        894.0,
        662.0,
        image=image_image_8
    )

    #Creates the text for the first option.
    canvas.create_text(
        920.0,
        277.0,
        anchor="nw",
        text="Enable Dark Mode",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    #Creates the text for the second option.
    canvas.create_text(
        920.0,
        371.0,
        anchor="nw",
        text="Create ZIP file",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    #Creates the text for the third option.
    canvas.create_text(
        920.0,
        465.0,
        anchor="nw",
        text="Open Folder with Output on Completion",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    #Creates the text for the fourth option.
    canvas.create_text(
        920.0,
        559.0,
        anchor="nw",
        text="Close App on Completion",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    #Creates the text for the fifth option.
    canvas.create_text(
        920.0,
        653.0,
        anchor="nw",
        text="Upload Directly to Your Google Drive",
        fill="#000000",
        font=("Inter", 15 * -1)
    )

    #Creates and sets the place of the 'Start' button.
    button_image_3 = PhotoImage(file=image_path("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=intfun.start_operation,
        relief="flat"
    )
    button_3.place(
        x=91.0,
        y=619.0,
        width=228.0,
        height=56.0
    )

    #Adds the hover feature for the 'Start' button.
    button_image_hover_3 = PhotoImage(file=image_path("button_hover_3.png"))
    def button_3_hover(e):
        button_3.config(
            image=button_image_hover_3
        )
    def button_3_leave(e):
        button_3.config(
            image=button_image_3
        )
    button_3.bind('<Enter>', button_3_hover)
    button_3.bind('<Leave>', button_3_leave)

    #Creates and sets the place of the 'Close' button.
    button_image_4 = PhotoImage(file=image_path("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=intfun.close_application,
        relief="flat"
    )
    button_4.place(
        x=485.0,
        y=619.0,
        width=228.0,
        height=56.0
    )

    #Adds the hover feature for the 'Close' button.
    button_image_hover_4 = PhotoImage(file=image_path("button_hover_4.png"))
    def button_4_hover(e):
        button_4.config(
            image=button_image_hover_4
        )
    def button_4_leave(e):
        button_4.config(
            image=button_image_4
        )
    button_4.bind('<Enter>', button_4_hover)
    button_4.bind('<Leave>', button_4_leave)

    #Creates and sets the place of the 'Sign in with Google' button.
    button_image_5 = PhotoImage(file=image_path("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=intfun.google_signin_error_popup,
        relief="flat"
    )
    button_5.place(
        x=553.0,
        y=143.0,
        width=220.0,
        height=40.0
    )

    #Adds the hover feature for the 'Sign in with Google' button.
    button_image_hover_5 = PhotoImage(file=image_path("button_hover_5.png"))
    def button_5_hover(e):
        button_5.config(
            image=button_image_hover_5
        )
    def button_5_leave(e):
        button_5.config(
            image=button_image_5
        )
    button_5.bind('<Enter>', button_5_hover)
    button_5.bind('<Leave>', button_5_leave)

    #Creates the placeholder image for the WIP tabs.
    image_image_9 = PhotoImage(file=image_path("image_9.png"))
    image_9 = canvas.create_image(
        159.0,
        145.0,
        image=image_image_9
    )

    #Does not allow the user to resize the window and sets the window loop.
    window.resizable(False, False)
    window.mainloop()