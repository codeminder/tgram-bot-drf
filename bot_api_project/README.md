# Telegram Bot with Django and Django Rest Framework

## Project Overview

This project is a simple Telegram bot that interacts with a Django backend. The bot has two main features:
1. It returns the current date and time.
2. It provides random pieces of advice.

## Features

- Telegram bot built with `aiogram`.
- Django web app with a simple API.
- `DRF` (Django Rest Framework) for API endpoints.
- Environment variables management using `django-environ`.

## Project Structure
```
bot_api_project/
│
├── bot_api_project/
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── bot_quiz/
│   ├── templates/
│          ├── init.py
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── bot.py
├── manage.py
├── requirements.txt
├── .env
└── README.md
```
## Getting Started

### Prerequisites

- Python 3.8+
- Django 4.2+
- aiogram 3.10.0
- SQLite (for local development)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the environment variables:
Create a .env file in the root directory of the project and add the following variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

5. Apply migrations and start the Django development server:
```bash
python manage.py migrate
python manage.py runserver
```

6. Run the Telegram bot:
```bash
python bot.py
```

## API Endpoints
- Current DateTime: GET /api/current-datetime/ - Returns the current date and time.
- Random Advices: GET /api/random-advises/ - Returns three random pieces of advice.

## Usage
- Start the Django development server.
- Start the Telegram bot.
- Interact with the bot using Telegram. The bot provides two buttons:
  - Котра година: Returns the current date and time.
  - Надати поради: Returns three random pieces of advice.

## Deployment
To deploy the project to DigitalOcean or another server:

1. Set up your server with Python, virtual environment, and a database.
2. Transfer your project files to the server.
3. Set up the environment variables on the server.
4. Apply migrations and start the Django server.
5. Configure your bot to run as a service or use a process manager like supervisor or systemd.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Django
- Django Rest Framework
- aiogram
- markdown

### Explanation:

- **Project Overview:** The beginning of the README provides a brief overview of the project and its main features.
- **Project Structure:** This section gives an overview of the file structure of the project, which can help new developers quickly understand where things are located.
- **Getting Started:** Detailed instructions on how to set up the project locally, including setting up a virtual environment, installing dependencies, and setting environment variables.
- **API Endpoints:** Describes the available API endpoints.
- **Usage:** Instructions on how to use the bot once everything is set up.
- **Deployment:** Brief instructions on how to deploy the project to a server.
- **License:** Information about the project’s license.
- **Acknowledgments:** Credits to the technologies and frameworks used in the project.
