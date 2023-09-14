from flask import Flask, make_response, request, jsonify
from flask_restful import Resource,Api
from flask_pymongo import PyMongo
import pymongo;

app = Flask(__name__)
api = Api(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
mongo = PyMongo(app)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.corider
collection = db.users

#id (a unique identifier for the user) --> Integer
#name (the name of the user) --> String
#email (the email address of the user) --> String (maybe check constraint)
#password (the password of the user) --> String

class Data(Resource):
    def get(self):
        try:
            a = collection.find()

        #No documents in the collection
            if a is None:
                return make_response(jsonify({"error":'Please enter data'}),400)
        
        #List to hold all the users
            L = []
            for i in a:
                L.append(i)
            return L
        except Exception as e:
            return make_response(jsonify({"error":str(e)}),500)
        
    def post(self):
        try:
            data = request.json
        
        #No body added
            if data is None:
                return make_response(jsonify({"error":'Please enter data'}),400)
        
        #Inserting the user
            collection.insert_one(data)
            return 'Data has been added successfull!'
        except Exception as e:
            return make_response(jsonify({"error":str(e)}),500)
    
class DataSpecific(Resource):
    def get(self,user_id):
        try:
            a = collection.find({"_id":user_id})

        #No such document found
            if a is None:
                return make_response(jsonify({"response":'User not found !'}),401)
        
        #Document found
            else:
                L = []
                for i in a:
                    L.append(i)
                return L
        except Exception as e:
            return make_response(jsonify({"error":str(e)}),500)
    
    def put(self,user_id):
        try:
            a = request.json
        #If no changes made
            if a is None:
                return make_response(jsonify({"response":'Please enter some update'}),401)
        
        #Whatever is entered is updated
            newvalues = {"$set":a}
            collection.update_one({"_id":user_id},newvalues)
            return make_response(jsonify({"response":'Document successfully updated !'}),200)
        except Exception as e:
            return make_response(jsonify({"error":str(e)}),500)
    
    def delete(self,user_id):
        try:
        #Delete according to the given id
            collection.delete_one({"_id":user_id})
            return make_response(jsonify({"response":"Successfully Deleted"}),200)
        except Exception as e:
            return make_response(jsonify({"error":str(e)}), 500)


        
api.add_resource(Data,'/users')
api.add_resource(DataSpecific,'/users/<string:user_id>')


if "__name__" == "__main__":
    app.run(debug=True)



'''
@app.route('/')
def index():
    return "Hello World"

@app.route('/users/<string:user_id>',methods=['GET'])
def get_specific_data(user_id):
    try:
        a = collection.find({"_id":user_id})

        #No such document found
        if a is None:
            return jsonify({"response":'User not found !'}),401
        
        #Document found
        else:
            L = []
            for i in a:
                L.append(i)
            return L
    except Exception as e:
        return jsonify({"error":str(e)}),500
    

@app.route('/users',methods=['GET'])
def get_all_data():
    try:
        a = collection.find()

        #No documents in the collection
        if a is None:
            return jsonify({"error":'Please enter data'}),400
        
        #List to hold all the users
        L = []
        for i in a:
            L.append(i)
        return L
    except Exception as e:
        return jsonify({"error":str(e)}),500


@app.route('/users',methods=['POST'])
def add_user():
    try:
        data = request.json
        
        #No body added
        if data is None:
            return jsonify({"error":'Please enter data'}),400
        
        #Inserting the user
        collection.insert_one(data)
        return 'Data has been added successfull!'
    except Exception as e:
        return jsonify({"error":str(e)}),500
    

@app.route('/users/<string:user_id>',methods=['PUT'])
def update_specific_user(user_id):
    try:
        a = request.json
        #If no changes made
        if a is None:
            return jsonify({"response":'Please enter some update'}),401
        
        #Whatever is entered is updated
        newvalues = {"$set":a}
        collection.update_one({"_id":user_id},newvalues)
        return jsonify({"response":'Document successfully updated !'}),200
    except Exception as e:
        return jsonify({"error":str(e)}),500


@app.route('/users/<string:user_id>',methods=['DELETE'])
def delete_specific_user(user_id):
    try:
        #Delete according to the given id
        collection.delete_one({"_id":user_id})
        return jsonify({"response":"Successfully Deleted"}),200
    except Exception as e:
        return jsonify({"error":str(e)}),500
    

if "__name__" == "__main__":
    app.run(debug=True)

'''