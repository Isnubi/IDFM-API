from flask import Flask, render_template
import json
import requests
import datetime
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
            # check if the key "message" exists
            if 'message' in i['Content']:
                tab.append(i['Content']['message'][0]['messageText']['value'])
            else:
                tab.append("No message were find by the API")
    else:
        print('Error: ', req.status_code)
    return tab


def requests_horaires_api(token):
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF%3AStopPoint%3AQ%3A420637%3A'
    headers = {
        'Accept': 'application/json',
        'apikey': token,
    }
    req = requests.get(url, headers=headers)
    tab = []
    if req.status_code == 200:
        data = req.content.decode('utf-8')
        data = json.loads(data)
        for i in data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit']:
            time = i['MonitoredVehicleJourney']['MonitoredCall']['ExpectedDepartureTime']
            time = datetime.datetime.strptime(time[11:16], '%H:%M')
            time = time + datetime.timedelta(hours=2)
            tab.append(time.strftime('%H:%M') + ' - Next stop: ' +
                  i['MonitoredVehicleJourney']['MonitoredCall']['DestinationDisplay'][0]['value'])
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
    trafic_tab = requests_trafic_api(token)
    return render_template('trafic.html', content=trafic_tab)


@app.route('/horaires')
def horaires():
    horaires_tab = requests_horaires_api(token)
    return render_template('horaires.html', content=horaires_tab)


if __name__ == '__main__':
    app.run()

