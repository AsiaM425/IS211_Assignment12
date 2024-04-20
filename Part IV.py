from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        
        # Insert the student into the database (Assuming you have a function to execute SQL commands)
        # Replace 'execute_sql_command' with the function you use to execute SQL commands
        # Example:
        # execute_sql_command("INSERT INTO Students (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        
        return redirect('/dashboard')  # Redirect to dashboard after adding student
    return render_template('add_student.html')  # Render the form template for adding a student
