from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'a_random_key_which_is_hard_to_guess'  # secure key

# Use SQLite database
db = SQL("sqlite:///tasks.db")

#defining login required function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

#defining register function
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            flash('Please provide both username and password')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)", username, hashed_password)
            flash('Registration successful! You can now log in.')
            return redirect(url_for('login'))
        except Exception:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))

    return render_template('register.html')

#defining login function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(user) != 1 or not check_password_hash(user[0]['password'], password):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        session['user_id'] = user[0]['id']
        return redirect(url_for('index'))

    return render_template('login.html')

#defining logout function
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

#defining home
@app.route('/')
@login_required
def index():
    tasks = db.execute("SELECT * FROM tasks WHERE archived = 0")  # Only fetch non-archived tasks
    return render_template('index.html', tasks=tasks)

#defining add task function
@app.route('/add', methods=['POST'])
@login_required
def add_task():
    task = request.form.get('task')
    if task:
        db.execute("INSERT INTO tasks (task, completed, archived, user_id) VALUES (?, ?, ?, ?)",
                   task, 0, 0, session['user_id'])
    return redirect(url_for('index'))

#defining complete task function
@app.route('/complete/<int:task_id>')
@login_required
def complete_task(task_id):
    task = db.execute("SELECT completed FROM tasks WHERE id = ? AND user_id = ?", task_id, session['user_id'])
    if task:
        current_status = task[0]['completed']
        db.execute("UPDATE tasks SET completed = ? WHERE id = ? AND user_id = ?", int(not current_status), task_id, session['user_id'])
    return redirect(url_for('index'))

#defining delete task function
@app.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    db.execute("DELETE FROM tasks WHERE id = ? AND user_id = ?", task_id, session['user_id'])
    flash('Task deleted successfully.')
    return redirect(url_for('index'))

#defining completed function
@app.route('/completed')
@login_required
def completed():
    tasks = db.execute("SELECT * FROM tasks WHERE completed = 1 AND user_id = ?", session['user_id'])
    return render_template('completed.html', tasks=tasks)


@app.route('/undo/<int:task_id>')
@login_required
def undo_task(task_id):
    db.execute("UPDATE tasks SET archived = 0 WHERE id = ?", (task_id,))
    flash('Task unarchived successfully.')
    return redirect(url_for('index'))


#defining archieved function
@app.route('/archived')
@login_required
def archived():
    tasks = db.execute("SELECT * FROM tasks WHERE archived = 1 AND user_id = ?", session['user_id'])
    return render_template('archived.html', tasks=tasks)

#defining archieve task function
@app.route('/archive/<int:task_id>')
@login_required
def archive_task(task_id):
    db.execute("UPDATE tasks SET archived = 1 WHERE id = ?", task_id)
    flash('Task archived successfully.')
    return redirect(url_for('index'))

#defining timer function
@app.route('/timer')
@login_required
def timer():
    return render_template('timer.html')
#defining notes function
@app.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            db.execute("INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
                       session['user_id'], title, content)
            flash('Note added successfully.')
            return redirect(url_for('notes'))

    user_notes = db.execute("SELECT * FROM notes WHERE user_id = ?", session['user_id'])
    return render_template('notes.html', notes=user_notes)

#defining add note function
@app.route('/add_note', methods=['POST'])
@login_required
def add_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if title and content:
        db.execute("INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)",
                   session['user_id'], title, content)
        return '', 201  # Return HTTP 201 Created
    return '', 400  # Return HTTP 400 Bad Request

#defining delete note function
@app.route('/delete_note/<int:note_id>', methods=['DELETE'])
@login_required
def delete_note(note_id):
    db.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", note_id, session['user_id'])
    flash('Note deleted successfully.')
    return render_template('notes.html')


#defining get notes function
@app.route('/get_notes')
@login_required
def get_notes():
    user_notes = db.execute("SELECT * FROM notes WHERE user_id = ?", session['user_id'])
    return jsonify(user_notes)  # Return as JSON


if __name__ == '__main__':
    app.run(debug=True)
