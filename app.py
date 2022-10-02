from flask import Flask, render_template
import json, requests
from private.config import token


def requests_trafic_api(token):
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/general-message?LineRef=STIF%3ALine%3A%3AC01743%3A'
    headers = {
        'Accept': 'application/json',
        'apikey': token
    }
    req = requests.get(url, headers=headers)
    tab = []
    if req.status_code == 200:
        data = req.content.decode('utf-8')
        data = json.loads(data)
        for i in data['Siri']['ServiceDelivery']['GeneralMessageDelivery'][0]['InfoMessage']:
            # show each message on the browser
            if i['Content']['message'][0]['messageText']['value'] is not None:
                tab.append(i['Content']['message'][0]['messageText']['value'])
    else:
        print('Error: ', req.status_code)
    return tab


def requests_horaires_api(token):
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=IDFM%3AmonomodalStopPlace%3A46725'
    headers = {
        'Accept': 'application/json',
        'apikey': token
    }
    req = requests.get(url, headers=headers)
    tab = []
    if req.status_code == 200:
        data = req.content.decode('utf-8')
        data = json.loads(data)
        for i in data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit']:
            # show each message on the browser
            if i['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime'] is not None:
                tab.append(i['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime'])
    else:
        print('Error: ', req.status_code)
    return tab


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plan')
def plan():
    return render_template('plan.html')


@app.route('/trafic')
def trafic():
    tab = requests_api(token)
    return render_template('trafic.html', content=tab)


@app.route('/horaires')
def horaires():
    return 1


if __name__ == '__main__':
    app.run()

