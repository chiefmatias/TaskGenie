class Task():
    def __init__(self, title, due, priority, description = None):
        self.title = title
        self.due = due
        self.priority = priority
        self.description = description #description is not required
        
    def __repr__(self) -> str:
        return f"Task({self.title}, is due {self.due}, with {self.priority} priority. Description: {self.description})"