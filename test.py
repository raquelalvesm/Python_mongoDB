<<<<<<< HEAD
# Importa biblioteca Flask
from flask import Flask
from pymongo import MongoClient
from flask import request, jsonify

# Inicializa a aplicacao instanciando Flask
app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.cadastrodb

# Atribui uma rota ao hello_world
@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/star',  methods=['GET'])
def get():
	output = []
	collection = db.mydb
	for s in collection.find():
		output.append({"nome":s['nome'],"idade":s['idade']})
	return jsonify({"status":"ok", "data": output})

@app.route('/star/<nome>',  methods=['GET'])
def get_one_collection(nome):
	collection = db.mydb
	s = collection.find_one({'nome': nome})
	if s:
		output = {"nome":s['nome'],"idade":s['idade']}
	else:
		output = "Nenhum resultado encontrado!"
	return jsonify({'result': output})


@app.route('/star',  methods=['POST'])
def post():
	collection = db.mydb
	nome = request.json['nome']
	idade = request.json['idade']
	collection_id = collection.insert({"nome":nome,"idade":idade})
	new_collection = collection.find_one({'_id':collection_id})
	output = {"nome":new_collection['nome'],"idade":new_collection['idade']}
	return jsonify({"data":output})


@app.route('/star/<nome>',  methods=['DELETE'])
def get_delete(nome):
	collection = db.mydb
	s = collection.find_one({'nome': nome})
	if s:
		output = "Cadastro Deletado"
	return jsonify({'result': output})



# Roda a aplicacao em: http://localhost:8085
app.run(debug=True,port=8085)
=======
# Importa biblioteca Flask
from flask import Flask
from pymongo import MongoClient
from flask import request, jsonify

# Inicializa a aplicacao instanciando Flask
app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.cadastrodb

# Atribui uma rota ao hello_world
@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/star',  methods=['GET'])
def get():
	output = []
	collection = db.mydb
	for s in collection.find():
		output.append({"nome":s['nome'],"idade":s['idade']})
	return jsonify({"status":"ok", "data": output})

@app.route('/star/<nome>',  methods=['GET'])
def get_one_collection(nome):
	collection = db.mydb
	s = collection.find_one({'nome': nome})
	if s:
		output = {"nome":s['nome'],"idade":s['idade']}
	else:
		output = "Nenhum resultado encontrado!"
	return jsonify({'result': output})


@app.route('/star',  methods=['POST'])
def post():
	collection = db.mydb
	nome = request.json['nome']
	idade = request.json['idade']
	collection_id = collection.insert({"nome":nome,"idade":idade})
	new_collection = collection.find_one({'_id':collection_id})
	output = {"nome":new_collection['nome'],"idade":new_collection['idade']}
	return jsonify({"data":output})


@app.route('/star/<nome>',  methods=['DELETE'])
def get_delete(nome):
	collection = db.mydb
	s = collection.find_one({'nome': nome})
	if s:
		output = "Cadastro Deletado"
	return jsonify({'result': output})



# Roda a aplicacao em: http://localhost:8085
app.run(debug=True,port=8085)
>>>>>>> e8671410614a5adfd5afd89890ec4441ccd51e01
