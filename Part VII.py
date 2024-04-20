@app.route('/dashboard')
def dashboard():
    # Fetch and display students from the database
    students = fetch_students()  # Replace with your function to fetch students from the database
    return render_template('dashboard.html', students=students)

@app.route('/results/add', methods=['GET', 'POST'])
def add_quiz_result():
    if request.method == 'POST':
        student_id = request.form['student_id']
        quiz_id = request.form['quiz_id']
        score = request.form['score']
        
        # Insert the quiz result into the database
        # Replace with your function to execute SQL commands to insert quiz results into the database
        
        return redirect('/dashboard')  # Redirect to dashboard after adding quiz result
    return render_template('add_quiz_result.html')  # Render the form template for adding a quiz result
