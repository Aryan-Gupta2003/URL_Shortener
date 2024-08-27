# URL Shortener

## Overview

A simple URL Shortener web application built with Flask. This application allows users to shorten long URLs and easily manage them through a simple interface.

## Features

- Shorten long URLs into concise, manageable links.
- Redirect shortened URLs to their original long URLs.
- Database storage of URL mappings using SQLite.

## Project Structure

```plaintext
URL-Shortener/
│
├── app.py          # Main application file
├── config.py       # Configuration settings
├── models.py       # Database models and utility functions
├── utils.py        # Utility functions for URL generation and validation
├── templates/
│   └── index.html  # HTML template for the web interface
├── static/
│   └── style.css   # CSS styling for the web interface
├── test.py         # Script to initialize the database
├── requirements.txt  # List of dependencies
└── README.md       # Project documentation
```

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Aryan-Gupta2003/URL_Shortener.git
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**:
   Edit the config.py file to set the path for the SQLite database:

   ```python
   import os

   BASE_DIR = os.path.abspath(os.path.dirname(__file__))
   DATABASE_PATH = os.path.join(BASE_DIR, 'url_shortener.db')

   class Config:
       SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

5. **Initialize the database**:
   Run the test.py script to create the necessary database tables:

   ```bash
   python test.py
   ```

6. **Run the application**:
   Start the Flask development server:
   ```bash
   python app.py
   ```
   The application will be available at http://localhost:5000.

## Usage

- Navigate to the homepage.
- Enter the long URL you want to shorten.
- Click "Shorten URL" to receive a shortened link.
- Use the shortened link to be redirected to the original URL.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements.
