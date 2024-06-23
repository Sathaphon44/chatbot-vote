import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGODB_URI')
    KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
    CLOUDKAFKA_TOPIC = os.getenv('CLOUDKAFKA_TOPIC')
    CLOUDKAFKA_USERNAME = os.getenv('CLOUDKAFKA_USERNAME')
    CLOUDKAFKA_PASSWORD = os.getenv('CLOUDKAFKA_PASSWORD')
    LINE_ACCESS_TOKEN = os.getenv('LINE_ACCESS_TOKEN')
    API_LINE = os.getenv('API_LINE')
