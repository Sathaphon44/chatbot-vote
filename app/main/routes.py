from flask import json, jsonify, request, current_app
from . import main
# from .. import mongo
from confluent_kafka import KafkaException


@main.route('/v1/publish', methods=['POST'])
def publish_message():
    try:
        message = json.dumps(request.json)
        producer = current_app.kafka_producer
        topic = current_app.config['CLOUDKAFKA_TOPIC']

        try:
            producer.produce(topic, value=message)
            producer.flush()
            return jsonify({"status": "Message published"}), 200
        except KafkaException as e:
            return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Message is required"}), 400