# JTyping Test

![Logo](static/img/JTypingTestFavicon.ico)

JTyping Test is a Django-based web application that allows users to practice typing and improve their speed and accuracy. It provides real-time feedback, scores, and a user-friendly interface to make typing practice engaging and efficient.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Docker](#docker)

## Features

- Practice typing with real-time feedback and scoring.
- Track typing speed (words per minute) and accuracy
- Responsive design for mobile and desktop views.
- Admin panel to manage user contact.

## Setup

**Create a virtual environment and activate it:**

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**Install the required packages:**

    pip install -r requirements.txt

**Apply migrations:**

    python manage.py migrate

### Technologies Used

- **Python**: 3.11.4
- **Django**: 5.1.2
- **Gunicorn**: For serving the application in production
- **ASGIREF**: For asynchronous handling
- **Sqlparse**: For SQL query formatting

**Run the development server:**

    python manage.py runserver

**Open your browser and navigate to:** `http://127.0.0.1:8000`

# Usage

## URLs and Views

Below is the list of available URLs for the application:

### **Welcome Page:**
- **URL:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Description:** This is the initial landing page where users can navigate to home page.

### **Home Page:**
- **URL:** [http://127.0.0.1:8000/home](http://127.0.0.1:8000/home)
- **Description:** The home page, which navigate to the english_typing page.

### **English Typing Test Page:**
- **URL:** [http://127.0.0.1:8000/english_typing](http://127.0.0.1:8000/english_typing)
- **Description:** This page allows users to select and start typing tests based on sections and difficulty levels.

### **Typing Test:**
- **URL:** [http://127.0.0.1:8000/typing_test](http://127.0.0.1:8000/typing_test)
- **Description:** This view handles the generation of typing tests based on the difficulty level and the test type selected. It provides an interactive typing test using a list of predefined words and phrases categorized by difficulty.

### **About Page:**
- **URL:** [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about)
- **Description:** This page provides information about the application, its features, and the team behind it.

### **Contact Page:**
- **URL:** [http://127.0.0.1:8000/contact](http://127.0.0.1:8000/contact)
- **Description:** A page for users to get in touch with the team, including a contact form and additional contact details.

---

## Detailed Flow of the Typing Test

The `typing_test` view dynamically generates the typing test based on the difficulty and test type selected:

### **Sections:**
- **Words:** A series of typing tests based on words.
- **Paragraphs:** A series of typing tests based on paragraphs.

### **Difficulties:**
- **Easy:** Suitable for beginners, featuring a list of simple words.
- **Moderate:** A middle-ground difficulty with more complex words.
- **Difficult:** A challenging list of difficult words and phrases.

---

## Test Result Flow

After completing a typing test, users are automatically directed to the results page:

### **Result Page:**
- **URL:** Displayed after completing the test.
- **Description:** Compares the user's typed text with the original, showing correctness and statistics.

---

## How to Use

1. **Start** by visiting the **Welcome Page**.
2. **Navigate** to the **Home Page** for detailed options.
3. Go to the **English Typing Test Page** for typing practice.
4. Choose a section (Words or Paragraph) and difficulty level.
5. Click relevant buttons to start the test.
6. Review your performance on the **Result Page**.

#### Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin` with the following credentials:

- **Username:** admin
- **Password:** admin_password

### Project Structure

```plaintext
JTypingTest/
├── JTypingTestApp/
│   ├── migrations/
│   ├── static/
│   │   └── img/
│   ├── templates/
│   │   ├── about.html
│   │   ├── base.html
│   │   └── contact.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── Image_Uploader_Website/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
│   ├── cover_pictures/
│   ├── profile_pictures/
│   └── timeline_pictures/
├── manage.py
└── requirements.txt

```
## Docker

Docker support is available for this project. For detailed instructions on how to build and run the application using Docker, please refer to the [Docker-specific README](README.Docker.md).
