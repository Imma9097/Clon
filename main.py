import os
import sys

# Make sure 'app' folder is in Python's search path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from app import create_app

# Create the Flask application instance
app = create_app()

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)