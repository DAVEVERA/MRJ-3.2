"""
WSGI entry point for Vercel serverless deployment
"""
from app import app

# Vercel will use this
if __name__ == "__main__":
    app.run()
