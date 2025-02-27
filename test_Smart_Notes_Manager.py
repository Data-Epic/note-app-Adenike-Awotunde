# Import pytest and the script to test
import pytest
import datetime
import Smart_Notes_Manager as Smart_Note

class test_Note :
    def setup_method(self):
        """ set up method to initialize a class based test for the parent class"""
        self. creatd_at = datetime(2025, 2, 27, 8, 52, 0)
        self.content = "This is a unit testing task"
        self.note = (self.creatd_at, self.content)
  
    def test_init(self):
        # Testing if note list is empty at initialization
        assert len(Note) ==0
        
    def test_display(self):
        # Testing if the display method will return the expected formatted string
        expected_result = f"{self.created_at} ({self.content})"
        assert self.note.display == expected_result
        
    
class test_TextNote:
    def setup_method(self):
        """ set up method to intiallise class based test for the subclass TextNote"""
        self.creatd_at = datetime(2025, 2, 27, 8, 52, 0)
        self.content = "This is a text note"
        self.title = "Test Title"
        self.text_note =TextNote(self.created_time, self.content, self.title)
        
    def test_TextNote_inherit_from_Note(self):
        # Testing if text note is inheriting from the parent class Note
        assert isinstance(self.text_note, Note)
        assert isinstance(self.text_note, TextNote)
        
    def test_display(self):
        # Testing if the display method will return the expected formatted string
        expected_result = f"{self.created_at} ({self.content})"
        assert self.note.display == expected_result
        
        
class test_ReminderNote:
    def setup_method(self):
        """ set up method to intiallise class based test for the subclass Reminder Note"""
        self.creatd_at = datetime(2025, 2, 27, 8, 52, 0)
        self.content = "This is a reminder to complete your task"
        self.reminder_time = "10am"
        self.reminder_note = ReminderNote(self.created_time, self.content, self.reminder_time)
        
    def test_ReminderNote_inherit_from_Note(self):
        # Testing if text note is inheriting from the parent class Note
        assert isinstance(self.reminder_note_note, Note)
        assert isinstance(self.reminder_note_note, ReminderNote)
        
    def test_display(self):
        # Testing if the display method will return the expected formatted string
        expected_result = f"ReminderNote: {self.reminder_time} | {self.created_at} ({self.content})"
        assert self.note.display == expected_result      
                     
    

    


