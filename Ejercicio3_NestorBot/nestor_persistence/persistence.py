import pymongo
import pika

def get_database_name():
	return "nestor"

def get_mongo_host():
	return "localhost"

def get_mongo_port():
	return 27017

def get_rabbitmq_host():
	return "localhost"

def connect_database(database_name):
	myclient = pymongo.MongoClient(host=get_mongo_host(),port=get_mongo_port())
	db = myclient[get_database_name]

	return db

def write_message_in_database(message,database_name,collection_name):
	database = connect_database(database_name)
	my_doc = {"message":message}
	print("Writing a new document in the database: "+str(my_doc))
	database[collection_name].insert_one(my_doc)

#def connect_rabbitmq(exchange,queue,routing_key):
#	connection = pika.BlockingConnection(pika.ConnectionParameters(host=get_rabbitmq_host()))
#	channel = connection.channel()
#	channel.exchange_declare
#NO ESTA TERMINADO COPIARRR EN GITHUB LO VAN A SUBIR