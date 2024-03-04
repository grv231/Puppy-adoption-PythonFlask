from myproject import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

# Driver Code
if __name__ == "__main__":
    app.run(debug=True)
