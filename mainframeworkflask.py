from flask import Flask
import datetime

app = Flask(__name__)
MOODLE_LOGIN = "1149288"

@app.route("/")
def do_get():
    now = datetime.datetime.now()
    formatted_date_time = now.strftime("%d.%m.%y %H:%M:%S")
    return f"{MOODLE_LOGIN}, {formatted_date_time}"

app.run(host='localhost', port=8080,  debug=True)
