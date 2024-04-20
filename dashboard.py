@app.route('/dashboard')
def dashboard():
    # Fetch and display students and quizzes from the database
    return render_template('dashboard.html', students=students, quizzes=quizzes)
