import json
import pandas
import newspaper
import base64
from io import BytesIO
from flask import Flask
from matplotlib.figure import Figure






app = Flask(__name__)




@app.route("/")
def hello():


    url = "https://api-sismologia-chile.herokuapp.com/"
    url_i = newspaper.Article(url="%s" %(url), language="es")
    url_i.download()
    url_i.parse()
    print(url_i.text)
    """ df = pandas.read_csv('hrdata.csv')
    print(df) """
    # Generate the figure **without using pyplot**.



  















