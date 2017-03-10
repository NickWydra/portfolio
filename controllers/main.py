from flask import *

from extensions import connect_to_database

main = Blueprint('main', __name__, template_folder='templates')

# Secret string is: lfkza0k6

@main.route('/')
def main_route():
    return render_template("index.html")
