import json
import os

FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "data", "notes.json")) #"data/notes.json"

def load_notes():
    try:
        with open(FILE_PATH,"r") as file:
            data = json.load(file)      #print("Loaded notes:", data)
            if isinstance(data, list):
                return data
            else:
                return json.load(file)
    except:
        return []

def save_notes(notes):  
    with open(FILE_PATH,"w") as file:
        json.dump(notes, file, indent=4) 

def add_note(note):
    notes = load_notes()

    if not isinstance(notes,list):
        notes = []

    notes.append(note)
    save_notes(notes)
    print("Note added!")

def view_notes():
    notes = load_notes()

    if not isinstance(notes, list) or not notes:
        print("No notes found.")
        return 
    
    for i, n in enumerate(notes, start=1):
        print(f"{i}. {n}")

def search_notes(keyword):
    notes = load_notes()

    if not isinstance(notes, list):
        print("No matching notes found.")
        return

    found = False

    for i, n in enumerate(notes, start=1):
        if keyword.lower() in n.lower():
            print(f"{i}. {n}")
            found = True

    if not found:
        print("No matching notes found.")

# DELETE NOTE
def delete_note(index):
    notes = load_notes()

    if 0 < index <= len(notes):
        removed = notes.pop(index - 1)
        save_notes(notes)
        print("Deleted:", removed)
    else:
        print("Invalid note number")

#EDIT NOTE
def edit_note(index, new_text):
    notes = load_notes()

    if 0 < index <= len(notes):
        old = notes[index - 1]
        notes[index - 1] = new_text
        save_notes(notes)
        print("Updated:", old, "->", new_text)
    else:
        print("Invalid note number")
