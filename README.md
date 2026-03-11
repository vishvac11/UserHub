# UserHub

A small **User Management System** built with **Flask** and **SQLite** that supports full **CRUD**:
create users, view users, edit users, and delete users — with a clean Vanilla CSS and Bootstrap UI.

## Features

- **Modern UI**: Bootstrap 5 layout + custom styling (`static/style.css`)
- **3-page flow**
  - **Home** (landing page)
  - **Add/Edit User** (better form + validation)
  - **View Users** (table with search + actions)
- **CRUD operations**
  - Create a new user
  - Read (list) all users
  - Update a user
  - Delete a user (with confirmation)
- **SQLite database**: auto-creates `database.db` and the `users` table on first run
- **Validation**
  - Name required
  - Email must look valid
  - Age must be a number between 0 and 150

## Pages (What you asked for)

- **Home page**: `/`
- **Form input page** (create): `/users/new`
- **User viewing page** (list): `/users`

Editing and deleting are available from the **View users** page.

## Tech Stack

- **Python**
- **Flask**
- **SQLite** (`sqlite3` from the standard library)
- **Bootstrap 5** (via CDN)

## Project Structure

```text
user_management_app/
  app.py
  database.db              # created automatically after first run
  README.md
  static/
    style.css
  templates/
    base.html
    home.html
    user_form.html
    users.html
```

## Setup (Windows)

### 1) Install dependencies

```powershell
pip install flask
```

### 3) Run the app

```powershell
python app.py
```

Then open the URL printed in the terminal (usually `http://127.0.0.1:5000`).

## CRUD Operations & Routes

### Read

- **Home**: `GET /`
- **List users**: `GET /users`

### Create

- **Show create form**: `GET /users/new`
- **Create user**: `POST /users/new`

### Update

- **Show edit form**: `GET /users/<user_id>/edit`
- **Save edits**: `POST /users/<user_id>/edit`

### Delete

- **Delete user**: `POST /users/<user_id>/delete`

> Note: Delete is a `POST` request to avoid accidental deletions from simple link clicks.

## Database

The application uses a local SQLite file: **`database.db`**.

Table schema:

```sql
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT,
  age INTEGER
);
```

#### Built with passion ❤️ by Vishva Chauhan
