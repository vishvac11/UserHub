from __future__ import annotations
import os

import re
import sqlite3
from typing import Any

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "My-name-is-Vishva-but-friends-usually-call-me-Vishu"

DB_PATH = "database.db"


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def normalize(s: str) -> str:
    return (s or "").strip()


EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")

# Create database and table
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            age INTEGER
        )
    """
    )
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/users")
def users_list():
    conn = get_db_connection()
    users = conn.execute("SELECT id, name, email, age FROM users ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("users.html", users=users)


@app.route("/users/new", methods=["GET", "POST"])
def user_create():
    if request.method == "GET":
        return render_template(
            "user_form.html",
            mode="create",
            user={"name": "", "email": "", "age": ""},
        )

    name = normalize(request.form.get("name", ""))
    email = normalize(request.form.get("email", ""))
    age_raw = normalize(request.form.get("age", ""))

    errors: list[str] = []
    if not name:
        errors.append("Name is required.")
    if not email or not EMAIL_RE.match(email):
        errors.append("Please enter a valid email address.")
    try:
        age = int(age_raw)
        if age < 0 or age > 150:
            errors.append("Age must be between 0 and 150.")
    except ValueError:
        errors.append("Age must be a number.")

    if errors:
        for e in errors:
            flash(e, "danger")
        return render_template(
            "user_form.html",
            mode="create",
            user={"name": name, "email": email, "age": age_raw},
        )

    conn = get_db_connection()
    conn.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    conn.commit()
    conn.close()

    flash("User created successfully.", "success")
    return redirect(url_for("users_list"))


@app.route("/users/<int:user_id>/edit", methods=["GET", "POST"])
def user_edit(user_id: int):
    conn = get_db_connection()
    user = conn.execute("SELECT id, name, email, age FROM users WHERE id = ?", (user_id,)).fetchone()

    if user is None:
        conn.close()
        flash("User not found.", "warning")
        return redirect(url_for("users_list"))

    if request.method == "GET":
        conn.close()
        return render_template("user_form.html", mode="edit", user=user)

    name = normalize(request.form.get("name", ""))
    email = normalize(request.form.get("email", ""))
    age_raw = normalize(request.form.get("age", ""))

    errors: list[str] = []
    if not name:
        errors.append("Name is required.")
    if not email or not EMAIL_RE.match(email):
        errors.append("Please enter a valid email address.")
    try:
        age = int(age_raw)
        if age < 0 or age > 150:
            errors.append("Age must be between 0 and 150.")
    except ValueError:
        errors.append("Age must be a number.")

    if errors:
        conn.close()
        for e in errors:
            flash(e, "danger")
        return render_template(
            "user_form.html",
            mode="edit",
            user={"id": user_id, "name": name, "email": email, "age": age_raw},
        )

    conn.execute(
        "UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?",
        (name, email, age, user_id),
    )
    conn.commit()
    conn.close()

    flash("User updated successfully.", "success")
    return redirect(url_for("users_list"))


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def user_delete(user_id: int):
    conn = get_db_connection()
    existing = conn.execute("SELECT id FROM users WHERE id = ?", (user_id,)).fetchone()
    if existing is None:
        conn.close()
        flash("User not found.", "warning")
        return redirect(url_for("users_list"))

    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

    flash("User deleted.", "info")
    return redirect(url_for("users_list"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)