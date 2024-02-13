from flask import Flask
from logs.log_individual import get_log_individual
from logs.logs_all import get_log_ids
from build.run_build import build_application


app = Flask(__name__)

app.add_url_rule('/build', 'build', build_application, methods=['POST'])

app.add_url_rule('/logs/all', 'logs_all', get_log_ids, methods=['GET'])
app.add_url_rule('/logs/<string:id>', 'logs_id', get_log_individual, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True, port=8024)
