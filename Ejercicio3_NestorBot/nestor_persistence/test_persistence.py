from persistence import connect_database,get_mongo_port, get_database_name,write_message_in_database,test_connect_rabbitmq
import pytest

@pytest.fixture
def database_name():
	return "nestor"

@pytest.fixture
def collection_name():
	return "test_persistence"

def test_connect_database():
	db = connect_database("nestor")
	assert db is not None

def test_check_port_type():
	port = get_mongo_port()
	assert type(port) is int

def test_check_database_name():
	name = get_database_name()
	assert name == "nestor"

def test_write_message_in_database(database_name,collection_name):
	db = connect_database(database_name)
	nb_doc_before = db[collection_name].count_documents({})
	message = "Hola"
	write_message_in_database(message,database_name,collection_name)
	nb_doc_before = db[collection_name].count_documents({})
	assert nb_doc_before == nb_doc_before-1 

def test_connect_rabbitmq():
	exchange = "nestor"
	queue = "test_persistence"
	routing_key = "mensajes"
	channel = connect_rabbitmq(exchange,queue,routing_key)
	assert channel is not None