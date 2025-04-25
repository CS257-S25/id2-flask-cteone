from flask import Flask, Response, abort

from ProductionCode.most_banned import most_banned_titles, most_banned_authors
from ProductionCode.search import search_author, search_genre, search_title

app = Flask(__name__)


@app.route("/")
def homepage():
    return 'To search for banned books, go to "/search/&lt;field&gt;/&lt;query&gt;". The options for field are title, author, and genre.'


@app.route("/search/<field>/<query>", strict_slashes=False)
def search(field, query):
    """
    The endpoint for searching for a field
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
            abort(400, "Invalid search field, options are title, author, or genre")
    return format_list_with_linebreak(output)
    # return output


@app.errorhandler(404)
def generic_page_not_found(e):
    return '<h1>404: Page not found</h1> <p> To search for banned books, go to "/search/&lt;field&gt;/&lt;query&gt;". The options for field are title, author, and genre.</p>'


def format_list_with_linebreak(list):
    return "<br>".join(list)


if __name__ == "__main__":
    app.run()
