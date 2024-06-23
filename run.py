from app import create_app
import signal
import sys

app = create_app()

# Print all routes
for rule in app.url_map.iter_rules():
    print(rule)

def signal_handler(sig, frame):
    print("Exiting gracefully...")
    app.stop_event.set()  # Signal the consumer thread to stop
    app.consumer_thread.join()  # Wait for the thread to finish
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    app.run(debug=True)
