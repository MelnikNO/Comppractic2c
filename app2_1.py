from flask import Flask, render_template, request
import datetime
import json

app = Flask(__name__)
MOODLE_LOGIN = "1149288"

@app.route("/", methods=['GET', 'POST'])
def do_get():
    if request.method == 'POST':
        moodle_login = request.form['moodle_login']
        now = datetime.datetime.now()
        data = {'login': moodle_login, 'time': now.strftime("%d.%m.%y %H:%M:%S")}

        with open('data.json', 'a') as f:
            json.dump(data, f)
            f.write('\n')

        return render_template('success.html', login=moodle_login, time=now.strftime("%d.%m.%y %H:%M:%S"))
    else:
        return render_template('form.html')

app.run(host='localhost', port=8080,  debug=True)
