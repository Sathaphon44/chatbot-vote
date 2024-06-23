from app.config import Config
from confluent_kafka import Producer, Consumer, KafkaError


def create_kafka_producer():
    conf = {
        'bootstrap.servers': Config.KAFKA_BOOTSTRAP_SERVERS,
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': "smallest"},
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'SCRAM-SHA-512',
        'sasl.username': Config.CLOUDKAFKA_USERNAME,
        'sasl.password': Config.CLOUDKAFKA_PASSWORD
    }
    producer = Producer(**conf)
    return producer

def create_kafka_consumer():
    conf = {
        'bootstrap.servers': Config.KAFKA_BOOTSTRAP_SERVERS,
        'group.id': "%s-consumer" % Config.CLOUDKAFKA_USERNAME,
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'},
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'SCRAM-SHA-256',
        'sasl.username': Config.CLOUDKAFKA_USERNAME,
        'sasl.password': Config.CLOUDKAFKA_PASSWORD
    }

    consumer = Consumer(**conf)
    return consumer

def kafka_consumer_thread(app, stop_event):
    consumer = create_kafka_consumer()
    consumer.subscribe([Config.CLOUDKAFKA_TOPIC])

    try:
        while not stop_event.is_set():
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            with app.app_context():
                try:
                    app.services.process_message(msg.value())
                except Exception as e: 
                    print("error processing message: ", e)
                    pass
    except KeyboardInterrupt:
        print("Stopping Kafka consumer...")
    finally:
        consumer.close()