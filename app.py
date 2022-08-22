from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ml', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
@app.route('/', methods=['GET'])
def ml_dashboard():
    data = [
        ("01-01-2020", 1597),
        ("02-01-2020", 1456),
        ("02-01-2020", 1908),
        ("04-01-2020", 896),
        ("05-01-2020", - 753),
        ("06-01-2020", 1597),
        ("07-01-2020", 159),
        ("08-01-2020", 15),
        ("09-01-2020", 197),
        ("10-01-2020", 157)
    ]
    labels = [row[0] for row in data]
    values1 = [row[1] for row in data]
    values2 = [row[1] + 224 for row in data]
    name = "Variable: Montant net (euros) <br> Drift: not detected <br> P-value: {}".format(0.13679)
    return render_template('ml_dashboard.html', name=name, labels=labels, values1=values1, values2=values2)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/system', methods=['GET'])
def system_monitoring():
    data = [
        ("13h", 1597),
        ("14h", 1456),
        ("15h", 1908),
        ("16h", 896),
        ("17h", 53),
        ("18h", 1597),
        ("19h", 159),
        ("20h", 15),
        ("21h", 197),
        ("22h", 157),
        ("23h", 1597),
        ("00h", 1456),
        ("01h", 2908),
        ("02h", 896),
        ("03h", 53),
        ("04h", 1597),
        ("05h", 159),
        ("06h", 55),
        ("07h", 187),
        ("08h", 253)
    ]
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    name = "Mean requests per second for each hour"
    return render_template('system_monitoring.html', name=name, labels=labels, values=values)

if __name__ == '__main__':
    app.run(debug=True)