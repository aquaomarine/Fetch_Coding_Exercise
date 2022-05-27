

import markdown
import os
import shelve
from webargs import fields

from webargs.flaskparser import parser
from flask import Flask, g
from flask_restful import Resource, Api


# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("fetch.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

fetch_args = {
    "payer" : fields.Str(required=True),
    "points" : fields.Int(required=True),
    "timestamp" : fields.Str(required=True )
}

@app.route("/")
def index():
    
    #open the readme file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        
        #read contents of the file
        content = markdown_file.read()

        #convert to HTML
        return markdown.markdown(content)

class PayerList(Resource):
  
    #get request to access payers
    def get(self):
        #opening database
        shelf = get_db()
        #shelve open and list keys
        keys = list(shelf.keys())

        payers = []
        
        for key in keys:
            #appending payers in db
            payers.append(shelf[key])

        return {'message': 'Success', 'data': payers}, 200
      
    #post requst for new receipts
    def post(self):
        #parse argument into an object
        args = parser.parse(fetch_args)
        #getting db , assigning openning with shef
        shelf = get_db()
        #assigning arguments to the db
        shelf[args['timestamp']] = args

        return {'message': 'Receipt registered', 'data': args}, 201


api.add_resource(PayerList, '/payers')
