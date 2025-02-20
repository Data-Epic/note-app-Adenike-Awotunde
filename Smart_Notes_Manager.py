import datetime

class Note:
    # Creating a base class 
    def __init__(self, created_at, content):
        """ Initialize a note object
            created_at(datetime): The time the note was created.
            content(str): The content of the note.
        """
        self.created_at = created_at
        self.content = content
        
    # Display Note
    def display(self):
        """ Display the content of a note """
        return f"{self.created_at} ({self.content})"
        
class TextNote(Note):
    # A subclass for Text note
    def __init__(self, created_at, content, title):
        super().__init__(created_at, content)
        self.title = title
        
    def display(self):
        super().display()
        return f"({self.title}) {self.created_at} ({self.content})"
    
class Reminder(Note):
    # A subclass for Reminder note
    def __init__(self, created_at, content, reminder_time):
        super().__init__(created_at, content)
        self.reminder_time = reminder_time
        
    def display(self):
        super().display()
        return f"Reminder: {self.reminder_time} | {self.created_at} ({self.content})"
    
class NoteManager:
    # A class for note manager
    def __init__(self):
        self.notes = []
        self.note_ID = 0 
        
    def add_note(self, note_type, content, title=None, reminder_time=None):
        self.note_ID += 1  # Increment ID
        
        if note_type == "TextNote":
            if title is None:
                raise ValueError("TextNote requires a title.")
            note = TextNote(datetime.datetime.now(), content, title)
            
        elif note_type == "Reminder": 
            if reminder_time is None:
                raise ValueError("Reminder requires a reminder_time.")
            note = Reminder(datetime.datetime.now(), content, reminder_time)
            
        else:
            raise ValueError("Wrong note type")
        
        self.notes.append((self.note_ID, note))
        
    def delete_note(self, note_ID):
        # Delete a Note
        self.notes = [(id, note) for id, note in self.notes if id != note_ID]
        print(f"Note with ID {note_ID} has been deleted")
    
    def show_note(self):
        """ Display all stored notes"""
        for id, note in self.notes:
            print(f"{id}: {note.display()}")
            
    def search_note(self, keyword):
        """Find note that contains a specific keyword"""
        results = [note.display() for _, note in self.notes if keyword.lower() in note.content.lower()]
        if results:
            for result in results:
                print(result)
        else: 
            print('There is no note with this keyword')

if __name__ == "__main__":
    my_notes = NoteManager()
    
    my_notes.add_note("TextNote", "I am Adenike Awotunde", title="Introduction")
    my_notes.add_note("Reminder", "Task submission", reminder_time="2025-10-10 10:00 AM")

    my_notes.show_note()
    
    my_notes.search_note("Task")
    
    my_notes.delete_note(1)
