from flask import render_template
#from app import app
from . import main




#@app.errorhandler(404)
@main.app_errorhandler(404)
def error_page(error):
    '''
    to render the 404 page
    '''
    return render_template('error_page.html'),404