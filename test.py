import requests
import json
import datetime
from private.config import idfm_token
from bs4 import BeautifulSoup
from pdf2image import convert_from_path


def get_line_map(line_name):
    """
    Get map of a line
    :param line_name: Name of the train line
    :return:
    """
    url = 'https://www.transilien.com/fr/sites/transilien/files/plan-de-ligne-' + f"{line_name}" + '.pdf'
    req = requests.get(url)
    if req.status_code == 200:
        open('static/map/' + f"{line_name}" + '.pdf', 'wb').write(req.content)
        images = convert_from_path('static/map/' + f"{line_name}" + '.pdf',
                                   poppler_path=r'win\poppler-22.04.0\Library\bin')
        images[0].save('static/map/' + f"{line_name}" + '.jpeg', 'JPEG')
    else:
        print('Error: ', req.status_code)


def get_line(token, line_id):
    """
    Get line type and name
    :param token: API token
    :param line_id: ID of the train line
    :return:
    """
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/navitia/coverage/fr-idf/lines?filter=line.id=' + \
          f"{line_id}" + '&disable_geojson=true&disable_disruption=true'
    headers = {
        'Accept': 'application/json',
        'apikey': token}
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        data = req.content.decode('windows-1252')
        data = json.loads(data)
        line_type = data['lines'][0]['network']['name']
        line = data['lines'][0]['code']
        return line_type, line
    else:
        print('Error: ', req.status_code)


def get_trafic(token, line_id):
    """
    Get trafic for a line
    :param token: API token
    :param line_id: ID of the train line
    :return:
    """
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/navitia/coverage/fr-idf/lines?filter=line.id=' + \
          f"{line_id}"
    headers = {
        'Accept': 'application/json',
        'apikey': token}
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        data = req.content.decode('windows-1252')
        data = json.loads(data)
        for i in data['disruptions']:
            for j in i['messages']:
                if j['channel']['types'][0] == 'web':
                    print(BeautifulSoup(j['text'], 'html.parser').get_text())
    else:
        print('Error: ', req.status_code)


def get_schedules(token, stop_id):
    """
    Get schedules for a stop
    :param token: API token
    :param stop_id: ID of the train station
    :return:
    """
    now = datetime.datetime.now()
    now = now.strftime("%H:%M")
    now = datetime.datetime.strptime(now, '%H:%M')

    url = 'https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF%3AStopPoint%3AQ%3A' + \
          stop_id + '%3A'
    headers = {
        'Accept': 'application/json',
        'apikey': token}
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
                print(line + ' ' + train_number + ': ' + time.strftime('%H:%M') + ' - Destination: ' +
                      i['MonitoredVehicleJourney']['MonitoredCall']['DestinationDisplay'][0]['value'])
            else:
                print(line + ' ' + line_type + ': ' + time.strftime('%H:%M') + ' - Destination: ' +
                      i['MonitoredVehicleJourney']['MonitoredCall']['DestinationDisplay'][0]['value'])
    else:
        print('Error: ', req.status_code)

