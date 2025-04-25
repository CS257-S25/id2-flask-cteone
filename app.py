"""Module for Flask app"""

from flask import Flask, abort

from ProductionCode.search import search_author, search_genre, search_title

app = Flask(__name__)

usage = 'To search for banned books, go to "/search/&lt;field&gt;/&lt;query&gt;". \
    The options for field are title, author, and genre.'


@app.route("/")
def homepage():
    return usage


@app.route("/search/<field>/<query>", strict_slashes=False)
def search(field, query):
    """The endpoint for searching for a field

    Args:
        field (str): the category the search query is for; title, author, or genre
        query (str): the search term
    Returns:
        (str): a string of search results, separated by line breaks
    """
    output = ""
    match field:
        case "title":
            output = search_title(query)
        case "author":
            output = search_author(query)
        case "genre":
            output = search_genre(query)
        case _:
            abort(
                400,
                "Invalid search field, options for field are title, author, or genre.",
            )
    return format_list_with_linebreak(output)
    # return output


@app.errorhandler(404)
def generic_page_not_found(e):
    """404 endpoint for when a page is not found"""
    return f"<h1>404: Page not found</h1> {usage}"


def format_list_with_linebreak(list_of_strings):
    """Helper method for joining a list of strings with line breaks
    Args:
        list_of_strings (str[]): a list of strings
    Returns:
        (str): a string composed of each element of the list joined by line breaks
    """
    return "<br>".join(list_of_strings)


if __name__ == "__main__":
    app.run()
