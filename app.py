from flask import Flask, render_template, request
import json
import requests
import datetime
from private.config import idfm_token
from bs4 import BeautifulSoup
from pdf2image import convert_from_path


def get_line(token, line_id):
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/navitia/coverage/fr-idf/lines?filter=line.id=' + \
          f"{line_id}" + '&disable_geojson=true&disable_disruption=true'
    headers = {
        'Accept': 'application/json',
        'apikey': token
    }
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        data = req.content.decode('utf-8')
        data = json.loads(data)
        line_type = data['lines'][0]['network']['name']
        line = data['lines'][0]['code']
        return line_type, line
    else:
        print('Error: ', req.status_code)


def get_line_map(line_name):
    url = 'https://www.transilien.com/fr/sites/transilien/files/plan-de-ligne-' + f"{line_name}" + '.pdf'
    req = requests.get(url)
    if req.status_code == 200:
        open('static/map/' + f"{line_name}" + '.pdf', 'wb').write(req.content)
        images = convert_from_path('static/map/' + f"{line_name}" + '.pdf',
                                   poppler_path=r'win\poppler-22.04.0\Library\bin')
        # get absolute path from a relative path
        images[0].save('static/map/' + f"{line_name}" + '.jpeg', 'JPEG')
        return '/static/map/' + f"{line_name}" + '.jpeg'
    else:
        print('Error: ', req.status_code)


def requests_trafic_api(token, line_id):
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/navitia/coverage/fr-idf/lines?filter=line.id=' + \
          f"{line_id}" + '&disable_geojson=true'
    headers = {
        'Accept': 'application/json',
        'apikey': token
    }
    req = requests.get(url, headers=headers)
    tab = []
    if req.status_code == 200:
        data = req.content.decode('windows-1252')
        data = json.loads(data)
        for i in data['disruptions']:
            for j in i['messages']:
                if j['channel']['types'][0] == 'web':
                    tab.append(BeautifulSoup(j['text'], 'html.parser').get_text())
    else:
        print('Error: ', req.status_code)
    return tab


def requests_horaires_api(token):
    stop_id = '411403'

    now = datetime.datetime.now().strftime("%H:%M")
    now = datetime.datetime.strptime(now, '%H:%M')
    tab = []
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF%3AStopPoint%3AQ%3A' + \
          stop_id + '%3A'
    headers = {
        'Accept': 'application/json',
        'apikey': token,

    }
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        data = req.content.decode('utf-8')
        data = json.loads(data)
        for i in data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit']:
            line_value = "line:IDFM:" + i['MonitoredVehicleJourney']['LineRef']['value'][11:-1]
            line, line_type = get_line(token, line_value)
            if 'ExpectedDepartureTime' in i['MonitoredVehicleJourney']['MonitoredCall']:
                time = i['MonitoredVehicleJourney']['MonitoredCall']['ExpectedDepartureTime']
                time = datetime.datetime.strptime(time[11:16], '%H:%M')
                time = time + datetime.timedelta(hours=2)
                if time < now:
                    continue
            elif 'AimedDepartureTime' in i['MonitoredVehicleJourney']['MonitoredCall']:
                time = i['MonitoredVehicleJourney']['MonitoredCall']['AimedDepartureTime']
                time = datetime.datetime.strptime(time[11:16], '%H:%M')
                time = time + datetime.timedelta(hours=2)
                if time < now:
                    continue
            else:
                time = 'error'
            if line == line_type:
                train_number = i['MonitoredVehicleJourney']['TrainNumbers']['TrainNumberRef'][0]['value']
                tab.append(line + ' ' + train_number + ': ' + time.strftime('%H:%M') + ' - Destination: ' +
                           i['MonitoredVehicleJourney']['MonitoredCall']['DestinationDisplay'][0]['value'])
            else:
                tab.append(line + ' ' + line_type + ': ' + time.strftime('%H:%M') + ' - Destination: ' +
                           i['MonitoredVehicleJourney']['MonitoredCall']['DestinationDisplay'][0]['value'])
        return tab
    else:
        print('Error: ', req.status_code)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plan', methods=['GET', 'POST'])
def plan():
    if request.method == 'POST':
        if request.form.get('RER A'):
            map = get_line_map('rer-a')
        elif request.form.get('RER B'):
            map = get_line_map('rer-b')
        elif request.form.get('RER C'):
            map = get_line_map('rer-c')
        elif request.form.get('RER D'):
            map = get_line_map('rer-d')
        elif request.form.get('RER E'):
            map = get_line_map('rer-e')
        return render_template('plan.html', content=map)
    return render_template('plan.html')


@app.route('/trafic', methods=['GET', 'POST'])
def trafic():
    if request.method == 'POST':
        if request.form.get('RER A'):
            line = 'line:IDFM:C01742'
        elif request.form.get('RER B'):
            line = 'line:IDFM:C01743'
        elif request.form.get('RER C'):
            line = 'line:IDFM:C01727'
        elif request.form.get('RER D'):
            line = 'line:IDFM:C01728'
        elif request.form.get('RER E'):
            line = 'line:IDFM:C01729'
        return render_template('trafic.html', content=requests_trafic_api(idfm_token, line))
    return render_template('trafic.html')


@app.route('/horaires')
def horaires():
    return render_template('horaires.html', content=requests_horaires_api(idfm_token))


if __name__ == '__main__':
    app.run()
