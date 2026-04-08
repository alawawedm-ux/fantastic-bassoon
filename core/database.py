import json
from kivy.storage.jsonstore import JsonStore

class DatabaseManager:
    def __init__(self, filename):
        self.store = JsonStore(filename)

    def save_progress(self, user_id, progress_data):
        self.store.put(user_id, **progress_data)

    def load_progress(self, user_id):
        if self.store.exists(user_id):
            return self.store.get(user_id)
        return None

    def delete_progress(self, user_id):
        if self.store.exists(user_id):
            self.store.delete(user_id)