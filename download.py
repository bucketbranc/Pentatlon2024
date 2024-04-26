import os
import shutil
import time
import argparse
import playsound
from playsound import playsound

# Arguments
parser = argparse.ArgumentParser(description='Donload Code into E6-RCU, Fast and Reliable')
parser.add_argument('filename') 
parser.add_argument('disk') 

args = parser.parse_args()
print (os.getcwd())
# Keep checking for the USB drive every 5 seconds
while True:
    try:
        # Check if the target directory exists (USB drive is connected)
        if os.path.exists("{}:/".format(args.disk)) and os.path.exists('{}\\scr\\{}.py'.format(os.getcwd(), args.filename)):
            # Copy the file to the target directory
            shutil.copyfile('{}\\scr\\{}.py'.format(os.getcwd(), args.filename), '{}:/{}.py'.format(args.disk, args.filename))
            print("File copied successfully!")
            playsound(os.getcwd() + "\\notification.mp3")
            time.sleep(3)
    except Exception as e:
          print(e)

    time.sleep(1)  # Wait for 5 seconds before checking again