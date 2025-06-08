import json
import os

class Assistant:
    def __init__(self, filename='notes.json'):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if not os.path.exists(self.filename):
            self.save_notes()
        try:
            with open(self.filename, 'r') as f:
                self.notes = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            self.notes = []
            self.save_notes()

    def save_notes(self):
        with open(self.filename, 'w') as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self, note: str):
        self.notes.append({"text": note, "tag": None})
        self.save_notes()

    def list_notes(self):
        return self.notes

    def search_notes(self, keyword: str):
        return [n for n in self.notes if keyword.lower() in n["text"].lower()]


    def add_note_with_tag(self, note: str, tag: str):
        self.notes.append({"text": note, "tag": tag})
        self.save_notes()

    def search_by_tag(self, tag: str):
        return [n["text"] for n in self.notes if n.get("tag") == tag]
