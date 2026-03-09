"""Student Study Planner - Main Application

This is the main entry point for the Student Study Planner application.
It manages study tasks, schedules, and provides insights for effective learning.
"""

import json
from datetime import datetime
from pathlib import Path

class StudyPlanner:
    """Main class for managing study tasks and schedules."""
    
    def __init__(self, data_file='study_data.json'):
        self.data_file = data_file
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file."""
        if Path(self.data_file).exists():
            with open(self.data_file, 'r') as f:
                self.tasks = json.load(f)
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)
    
    def add_task(self, subject, topic, deadline, priority='medium'):
        """Add a new study task."""
        task = {
            'id': len(self.tasks) + 1,
            'subject': subject,
            'topic': topic,
            'deadline': deadline,
            'priority': priority,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_tasks_by_priority(self):
        """Get all tasks sorted by priority."""
        priority_order = {'high': 1, 'medium': 2, 'low': 3}
        return sorted(self.tasks, key=lambda x: priority_order.get(x['priority'], 4))
    
    def mark_complete(self, task_id):
        """Mark a task as complete."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                return True
        return False

if __name__ == '__main__':
    planner = StudyPlanner()
    print('Student Study Planner initialized successfully!')
