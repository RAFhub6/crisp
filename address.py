from flask import Flask, json

hosts = {{"id": "02000E", "adr": "4-61620a", {"id": "02001E", "adr": "4-61621a"}}

api = Flask(__name__)
         
@api.route('/hosts', methods=['GET'])
def get_hosts():
         return json.dumps(hosts)
         
if __name__ == '__main':
         api.run()
         
@api.route('/host', methods=['POST'])
def post_hosts:
         return json.dumps({"success: True}), 201
