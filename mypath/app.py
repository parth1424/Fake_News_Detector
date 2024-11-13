
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define route for the homepage
@app.route('/')
def home():
    # Render the HTML file located in the 'templates' folder
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
