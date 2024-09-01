# Social Media App

## Overview

This is a social media application built using Django, where users can register, log in, and interact with each other's posts. The app features a user-friendly interface styled with Tailwind CSS, and uses Jinja templates for rendering dynamic content. It supports core social media functionalities such as creating, editing, deleting, and searching posts. Additionally, users can like, comment, and share posts on external platforms like Twitter, Facebook, and WhatsApp via API integration.

## Features

- **User Authentication**
  - Register a new account
  - Log in and log out securely

- **Post Management**
  - Create new posts
  - Edit and delete existing posts
  - Search for posts by content or user

- **Interactions**
  - Like posts from other users
  - Comment on posts
  - View comments and likes on posts

- **Social Sharing**
  - Share posts via API to Twitter, Facebook, and WhatsApp

## Technology Stack

- **Backend:** Django
- **Frontend:** HTML, Tailwind CSS, Jinja Templates
- **Database:** SQLite3
- **APIs:** Integration with Twitter, Facebook, and WhatsApp for sharing posts

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/social-media-app.git
   cd social-media-app
   ```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
venv\Scripts\activate`  # On Mac use `source venv/bin/activate`
```
3. **Install the dependencies**

```bash
pip install -r requirements.txt
```
4. **Apply migrations**

```bash
python manage.py migrate
```
5. **Run the development server**

```bash
python manage.py runserver
```

6.  **Access the app -**
     Open your browser and go to 'http://127.0.0.1:8000/'


