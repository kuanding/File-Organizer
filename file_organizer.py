import os
import shutil
import datetime

# get the current working directory
directory = os.getcwd()

# get the current year
current_year = datetime.datetime.now().year

# loop through all the files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # check if the file was last modified more than a year ago
    last_modified_year = datetime.datetime.fromtimestamp(os.path.getmtime(filepath)).year
    if current_year - last_modified_year >= 1:
        
        # create the destination folder based on the last modified year
        destination_folder = os.path.join(directory, str(last_modified_year))
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            
        # move the file to the destination folder
        shutil.move(filepath, os.path.join(destination_folder, filename))
