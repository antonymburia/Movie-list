from flask import render_template
from app import app

@app.errorhandler(404)
def four_ow_four(error):
  '''
  function to render 404 error page
  '''
  return render_template('fouroWfour.html'),404