import requests
import json
import datetime


def requests_api(token):
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/general-message?LineRef=STIF%3ALine%3A%3AC01743%3A'
    headers = {
        'Accept': 'application/json',
        'apikey': token
    }
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        data = req.content.decode('utf-8')
        data = json.loads(data)
        for i in data['Siri']['ServiceDelivery']['GeneralMessageDelivery'][0]['InfoMessage']:
            print(i['Content']['message'][0]['messageText']['value'])
    else:
        print('Error: ', req.status_code)


def requests_horaires_api(token):
    url = 'https://prim.iledefrance-mobilites.fr/marketplace/stop-monitoring?MonitoringRef=STIF%3AStopPoint%3AQ%3A420637%3A'
    headers = {
        'Accept': 'application/json',
        'apikey': token,

    }
    req = requests.get(url, headers=headers)
    if req.status_code == 200:
        data = req.content.decode('utf-8')
        data = json.loads(data)
        for i in data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit']:
            time = i['MonitoredVehicleJourney']['MonitoredCall']['ExpectedDepartureTime']
            time = datetime.datetime.strptime(time[11:16], '%H:%M')
            time = time + datetime.timedelta(hours=2)
            print(time.strftime('%H:%M') + ' - Next stop: ' + i['MonitoredVehicleJourney']['MonitoredCall']['DestinationDisplay'][0]['value'])
    else:
        print('Error: ', req.status_code)


token = "pQSYhdJZcm4B2RcUCWjhksjxSYALRWPu"
# requests_api(token)
requests_horaires_api(token)
