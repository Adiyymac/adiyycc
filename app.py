from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the program page
@app.route('/program/')
def program():
    return render_template('program.html')

# Route for the union page
@app.route('/union/')
def union():
    return render_template('union.html')

# Route for the contact page
@app.route('/contact/')
def contact():
    return render_template('contact.html')

# Route for the about us page
@app.route('/about/')
def about():
    return render_template('about us.html')

if __name__ == '__main__':
    app.run(debug=True)
