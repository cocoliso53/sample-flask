from flask import Flask, render_template, request, Response
import requests

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello_world():
    return render_template('hello.html')

@app.route("/buy",methods=["POST"])
def buy():
    if request.method == 'POST':
        to_currency = request.form['to_currency']
        from_amount = request.form['from_amount']
        to_address = request.form['to_address']
        headers = {'accept': 'application/json','Authorization': 'Basic dGVzdGluZ0BzdWFybWkuY29tOnRlc3RpbmdFTUFJTA==',}
        json_data = {'user': 'cuaucortes@gmail.com','from_currency': 'MXN','from_amount': str(from_amount),'to_currency': to_currency,'to_address': to_address,'network': 'MATIC',}
        r = requests.post('https://www.suarmi.com/api/v1/order', headers=headers, json=json_data)
        data = r.json()
        data['to_amount'] = "{:.5f}".format(float(data["to_amount"]))
        print(r.json())
    return render_template('details.html',data=data,to_address=to_address)
