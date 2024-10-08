from flask import Flask

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)
    app.static_folder = 'static'  # Ensure static files are served from here

    # Import and register the routes
    from app.routes import main
    app.register_blueprint(main)
    return app
