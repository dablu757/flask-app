from flask import Flask
from common import success_responce, error_responce
from logger import LOGGER


app = Flask(__name__)

@app.route("/health", methods = ['GET'])
def home():
    LOGGER.info(f"health route started...")
    try:
        return success_responce(message='home call successfully')
    except Exception as e:
        pass



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )

