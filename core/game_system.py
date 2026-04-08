class GameSystem:
    def __init__(self):
        self.progress = 0
        self.levels = []
        self.difficulty = 'Normal'

    def add_level(self, level):
        self.levels.append(level)

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def update_progress(self, new_progress):
        self.progress = new_progress

    def get_status(self):
        return {
            'progress': self.progress,
            'levels': self.levels,
            'difficulty': self.difficulty
        }
