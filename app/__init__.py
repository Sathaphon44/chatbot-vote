from threading import Event, Thread
from flask import Flask
from app.kafka import create_kafka_producer, kafka_consumer_thread
from .services import Services
from .extensions.database import MongoDatabase





def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    app.mongo = MongoDatabase().connect('mydatabase')

    from .main import main as main_blueprint
    # Register blueprints
    app.register_blueprint(main_blueprint, url_prefix='/api')

    app.services = Services(app)
    app.kafka_producer = create_kafka_producer()

    stop_event = Event()

    # Start Kafka consumer thread
    app.consumer_thread = Thread(target=kafka_consumer_thread, args=(app, stop_event))
    app.consumer_thread.start()

    # Add stop_event to the app context so it can be accessed later
    app.stop_event = stop_event

    return app

