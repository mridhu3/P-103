import os 
import shutil
import sys
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir = "C:\\Users\\Shradha\\Downloads"
todir = "D:\\projects\\P-103"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class File_Movement_Handler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(f"Hey! {event.src_path} has been created.")
        
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}.")

    def on_modified(self, event):
        print(f"What! {event.src_path} has been modified!")

    def on_moved(self, event):
        print(f"Someone has moved {event.src_path}.")
    
          
        for key,value in dir_tree.items():
            
            time.sleep(1)
            
            if extension in value:
                
                file_name = os.path.basename(event.src_path)
                
                print("Downloaded " + file_name )
                path1 = fromdir + "/" + file_name
                path2 = todir + "/" + key
                path3 = todir + "/" + key + "/" + file_name
                
                time.sleep(1)
                
                if os.path.exists(path2):
                    
                    print("Folder exists")
                    time.sleep(1)
                      
                    if os.path.exists(path3):
                        print("File already exists in " + key)
                        print("Renaming File " + file_name)
                        
                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0, 999)) + os.path.splitext(file_name)[1] 
                        
                        path4 = todir + "/" + key + "/" + new_file_name
                        
                        print("Moving " + file_name )
                        
                        shutil.move(path1, path4)
                        time.sleep(1)
                        
                    else:
                        print("Moving " + file_name )
                        shutil.move(path1, path3)
                else:
                    print("Making Directory")
                    
                    os.makedirs(path2)
                    print("Moving " + file_name)
                    shutil.move(path1, path3)
                    time.sleep(1)

#Initializing the event handler class
event_handler = File_Movement_Handler()

#Initializing Observer
observer = Observer()

#Scheduling the Observer
observer.schedule(event_handler, fromdir, recursive=True)

#Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()
                        