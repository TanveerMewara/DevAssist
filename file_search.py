import os

def search_files(keyword, path):
    if not os.path.exists(path):
        print("Invalid path!")
        return
        
    found = False

    for root, dirs, files in os.walk(path):
        for file in files:
            if keyword.lower() in file.lower():
                print(os.path.join(root, file))
                found = True 

        if not found:
            print("No files found.")