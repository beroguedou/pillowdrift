from flask import Flask, render_template
from mool.utils.numerical import continuous_data, numerical_distribution_sampler
from mool.utils.categorical import categorical_data, categorical_distribution_sampler
from mool.utils.load import load_config, load_data_from_csv

reference_datapath = "/Users/berangerguedou/projects/mool/data/sample_reference.csv"
current_datapath = "/Users/berangerguedou/projects/mool/data/sample_current.csv"
config_path = "/Users/berangerguedou/projects/mool/config.yaml"

config = load_config(config_path)

app = Flask(__name__)

@app.route('/ml', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
@app.route('/', methods=['GET'])
def ml_dashboard():
    elements = []
    
    reference_data, columns = load_data_from_csv(reference_datapath)
    current_data, columns = load_data_from_csv(current_datapath)
    # Numerical elements
    numerical_elements = continuous_data(reference_data, current_data, columns, config)
    numerical_elements = numerical_distribution_sampler(numerical_elements)
    elements.extend(numerical_elements)
    # Categorical elements
    categorical_elements = categorical_data(reference_data, current_data, columns, config)
    categorical_elements = categorical_distribution_sampler(categorical_elements)
    elements.extend(categorical_elements)

    return render_template('ml_dashboard.html', elements=elements)

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
    return render_template('system_monitoring.html', labels=labels, values=values)

if __name__ == '__main__':
    app.run(debug=True)