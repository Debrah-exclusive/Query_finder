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
pip install -r requirements.txt
cd mysql-query-solution-finder