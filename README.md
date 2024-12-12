# Quiz App

This project is a **Quiz Generator** web application built with Django and Python. It allows users to generate quizzes on various topics, take the quiz, and see their results. The app provides functionality for creating and displaying multiple-choice questions dynamically.

## Features
- Generate quizzes based on a user-provided topic.
- View quiz results and review answers.
- Simple and clean user interface.
- Error handling and feedback messages.

## Prerequisites

Before you begin, make sure you have the following installed on your local machine:
- **Python** 
- **Django** 

## Installation Instructions

### Step 1: Clone the repository

Clone the repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/quiz-app.git
```

Navigate into the project directory:

```bash
cd quiz-app
```

### Step 2: Set up a Virtual Environment (Optional but Recommended)
It's recommended to create a virtual environment for this project to avoid conflicts with other Python packages. You can create a virtual environment by running the following commands:

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
Once the virtual environment is activated, install the required Python packages from requirements.txt:

```bash
pip install -r requirements.txt
```

### Step 4: Configure Static Files
Make sure that the static files (e.g., CSS) are properly configured. Ensure that the static folder is in the project root and contains your styles.css file.

### Step 5: Apply Migrations
Run the following commands to set up the database and apply migrations:

```bash
python manage.py migrate
```

### Step 6: Create a Superuser (Optional)
If you want to access the Django admin panel, you can create a superuser with the following command:

```bash
python manage.py createsuperuser
```

Follow the prompts to set the username, email, and password.

### Step 7: Run the Development Server
Now you can run the Django development server:

```bash
python manage.py runserver
```

This will start the server on http://127.0.0.1:8000/. Open this URL in your web browser to view the app.

### Step 8: Test the Application
- Visit the Home Page: Go to http://127.0.0.1:8000/. You should see a page to enter a quiz topic.
- Generate a Quiz: Enter a topic (e.g., Python programming) and the number of questions, and click on "Generate Quiz".
- Take the Quiz: The quiz will be displayed with multiple-choice questions. Select the correct answers and submit the quiz.
- View Results: After submitting the quiz, you will be shown your score along with the correct answers.

## Folder Structure
The project follows this folder structure:

```
quiz-app/
│
├── quiz/
│   ├── migrations/
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   ├── index.html
│   │   ├── quiz_form.html
│   │   ├── quiz_results.html
│   │   └── start_quiz.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
│   └──.env
│
├── manage.py
├── requirements.txt
├── settings.py
└── urls.py
```

## Troubleshooting

### Issue 1: Static files not loading
If your CSS files are not being loaded, ensure that the static directory is correctly configured. In your settings.py, check that you have:

```python
STATIC_URL = '/static/'
```

### Issue 2: Database errors
If you encounter issues related to the database, try running the following:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue 3: Template errors
If templates do not load correctly, ensure the `{% load static %}` tag is present in the header of each HTML file.

