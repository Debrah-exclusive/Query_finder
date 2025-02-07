from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from rapidfuzz import fuzz  # Fuzzy string matching

app = Flask(__name__)

# List of URLs to scrape
urls = [
    "https://www.w3resource.com/mysql-exercises/subquery-exercises/",
    "https://www.w3resource.com/mysql-exercises/insert-into-statement/",
    "https://www.w3resource.com/mysql-exercises/create-table-exercises/",
    "https://www.w3resource.com/mysql-exercises/update-table-statement/",
    "https://www.w3resource.com/mysql-exercises/alter-table-statement/",
    "https://www.w3resource.com/mysql-exercises/string-exercises/",
    "https://www.w3resource.com/mysql-exercises/basic-simple-exercises/",
    "https://www.w3resource.com/mysql-exercises/restricting-and-sorting-data-exercises/",
    "https://www.w3resource.com/mysql-exercises/aggregate-function-exercises/",
    "https://www.w3resource.com/mysql-exercises/join-exercises/",
    "https://www.w3resource.com/mysql-exercises/date-time-exercises/",
    "https://www.w3resource.com/mysql-exercises/northwind/products-table-exercises/"
]

SIMILARITY_THRESHOLD = 80  # Adjust for sensitivity

def scrape_for_question(search_term):
    results = []
    
    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            elements = soup.find_all(['p', 'h2', 'h3', 'li'])

            for element in elements:
                question = " ".join(element.text.split())  # Clean text
                similarity_score = fuzz.ratio(search_term.lower(), question.lower())

                if similarity_score >= SIMILARITY_THRESHOLD:
                    solution_link = element.find_next('p').find('a', href=True)
                    link_url = url + solution_link.get('href') if solution_link else "No link found"

                    results.append({
                        "question": question,
                        "similarity": similarity_score,
                        "solution_link": link_url,
                        "source_url": url  # Include the page where the question was found
                    })

    return results

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    
    if request.method == "POST":
        search_term = request.form["search_term"]
        results = scrape_for_question(search_term)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
