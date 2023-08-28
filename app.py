from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/get_client_details', methods=['POST'])
def get_client_details():
    client_name = request.form['client_name']
    # Replace this with your logic to fetch client details
    # Example: client_details = get_client_details_from_database(client_name)
    
    #client_details = get_client_details_from_database(client_name)
    client_details = {'name': 'John Doe', 'email': 'john@example.com', 'Cellphone': '08177662200'}
    return jsonify(client_details)

if __name__ == '__main__':
    app.run(debug=True)

