# SAFPython Constructor
***
### Overview
SAFPython Constructor is a successor to [SAFBuilder](https://github.com/DSpace-Labs/SAFBuilder "SAFBuilder"), created by Zyad Ahmed for UMBC's Software Engineering graduate program capstone project. This project was sponsored by UMBC's dedicated library, the Albin O. Kuhn Library & Gallery.

I have also utilized some code from [PySAF](https://github.com/cstarcher/pysaf) which was altered and is properly credited in the related code block's comments.

### Usage
This tool is a standalone application made for the UMBC librarians. The way this application works is by first having one folder with the CSV file and necessary documents prepared to be used for the operation and a separate empty folder for the output destination. Next, the user should download the tool on the GitHub page and place it anywhere that isn't the input folder or the output folder. After the user runs the tool, they will be given the choice to select the CSV file you wish to convert with as well as the output folder destination to put the resulting files into. Once those are selected, the user can decide to check any options they wish to apply to the operation. When the user has selected the options they wished, they can press the start button which will present pop-ups whenever applicable based on the options selected or if there was an error encountered. After all of the necessary pop-ups have been passed, the operation will create the files in the output folder and will present the user with a pop-up confirming where those files were created. Finally,  the user can take these files and upload them directly to the institutional repository.

### Step-by-Step Instructions
1. Navigate to the GitHub page: [SAFPython Constructor](https://github.com/zahmed3/SAFPython_Constructor)

2. Click on the Releases Tab on the side of the page; I will provide a hyperlink in case you are not able to see it: [Releases](https://github.com/zahmed3/SAFPython_Constructor/releases/tag/v2)

3. Look under Assets and click on SAFPython_Constructor.exe to download the application.

4. After installing, simply double click on the downloaded SAFPython_Constructor.exe file to open the application. The location of this file is mostly of no concern, so you can place it anywhere except for the input folder. It will say that the file is unverified and give you a warning when trying to run it, but please ignore this warning as this file does not contain anything harmful.

5. When attempting to start the operation, please make sure that the CSV file is in the same folder directory as the document files you want to archive. Make sure that the CSV file is UTC-8 encoded.

6. Also make sure to check any options you wish to have applied to the operation prior to pressing the start button.


### UI Preview

![UI Preview](https://cdn.discordapp.com/attachments/430743889008263180/1366194364954579106/safpythonconstructorgui.png?ex=68100f27&is=680ebda7&hm=8385eb50d7d9fbe4505c4995d731dc130508b007dc3523d464fd61bf1d505ff7&format=webp&quality=lossless&width=1979&height=1160)


### Current Implemented Features
-Open CSV Files

-Select File Destination

-Start Operation

-Close Button

-Check for Unnecessary Files

-Create Zip Files(s)

-Open Folder on Completion

-Close App on Completion

-Check for Mismatched Files

### Cancelled Features
-Google Drive Upload

This was a major feature I had to unfortunately cancel as my current permission level in UMBC did not grant me access to the OAuth client ID and client secret of our UMBC emails which is necessary for uploading directly to Google Drive from the application (ProjectPro, 2023). Also, with the Google Cloud free plan, there is a user cap for authorization to upload to Google Drive that could only be solved with the premium version of Google Cloud (Google, n.d.). Therefore, I found it unfeasible for me to implement this feature into my application and have left this task to someone with the proper level of permissions at UMBC so that the library could continue my work on this idea after the capstone period has ended. This explanation is also provided on the GitHub page and a button is kept on the UI which will create a pop-up informing the user to refer to the explanation when pressed.
