# MySQL Query Solution Finder

This project is a web application that helps users find MySQL query solutions by scraping multiple web pages and using fuzzy string matching to find relevant questions and their solutions.

## Features

- Scrapes multiple web pages for MySQL query exercises.
- Uses fuzzy string matching to find questions similar to the user's input.
- Displays the similarity score, source page, and solution link for each matching question.

## Requirements

- Python 3.x
- Flask
- Requests
- BeautifulSoup4
- RapidFuzz

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Debrah-exclusive/Query_finder.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Query_finder
    ```

3. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python web_scapper/app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter your MySQL query question in the textarea and click "Find Answer".

4. The application will display a list of matching questions, their similarity scores, source pages, and solution links.

## Project Structure
