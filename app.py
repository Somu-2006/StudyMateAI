from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define the routes and views
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)




