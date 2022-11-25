    
from flask import Flask, json

# two company objects
companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

# initialize Flask
api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies(): # GET request, two companies will be returned
  return json.dumps(companies)

# Add another company using the POST method
@api.route('/companies', methods=['POST'])
def post_companies():
    return json.dumps({"success": True}), 201

if __name__ == '__main__':
    api.run()