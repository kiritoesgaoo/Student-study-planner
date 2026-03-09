# Student Study Planner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

A comprehensive Python application designed to help students manage their study tasks efficiently. Features include task scheduling, priority management, progress tracking, and study insights.

## Features

✅ **Task Management**
- Create, read, update, and delete study tasks
- Organize tasks by subject and topics
- Set priorities (high, medium, low)
- Track task completion status

✅ **Smart Scheduling**
- Set deadlines for assignments and exams
- View tasks sorted by priority and deadline
- Get notifications for upcoming deadlines

✅ **Progress Tracking**
- Monitor completed vs pending tasks
- View completion statistics by subject
- Track study time and progress

✅ **Data Persistence**
- JSON-based data storage for easy backup
- Automatic saving of all changes

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/kiritoesgao/student-study-planner.git
cd student-study-planner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

```python
from main import StudyPlanner

# Initialize the planner
planner = StudyPlanner()

# Add a new study task
task = planner.add_task(
    subject='Mathematics',
    topic='Calculus - Integration',
    deadline='2024-04-15',
    priority='high'
)

# View tasks by priority
tasks = planner.get_tasks_by_priority()
print(tasks)

# Mark a task as complete
planner.mark_complete(task_id=1)
```

## Project Structure

```
student-study-planner/
├── main.py              # Core StudyPlanner class
├── requirements.txt     # Project dependencies
├── README.md           # Project documentation
└── tests/              # Unit tests
```

## Future Enhancements

- [ ] Web UI with Flask
- [ ] SQLite database integration
- [ ] Email reminders for deadlines
- [ ] Study analytics and insights
- [ ] Multi-user support
- [ ] Mobile app integration

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

Run tests using pytest:

```bash
pytest tests/
pytest --cov  # With coverage report
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Kiritoe Sgao**
- GitHub: [@kiritoesgao](https://github.com/kiritoesgao)

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ for students everywhere**
