import requests
from datetime import datetime, timedelta
import pytz

url = "https://api.trafikinfo.trafikverket.se/v2/data.json"


def fetch_train_announcements(api_key, location_signature='M', hours_ahead=4):
    now = datetime.now(pytz.timezone('Europe/Stockholm'))
    future_time = now + timedelta(hours=hours_ahead)

    now_str = now.strftime('%Y-%m-%dT%H:%M:%S')
    future_str = future_time.strftime('%Y-%m-%dT%H:%M:%S')

    query = f"""
    <REQUEST>
        <LOGIN authenticationkey='{api_key}' />
        <QUERY objecttype='TrainAnnouncement' schemaversion='1.9'>
            <FILTER>
                <AND>
                    <EQ name='ActivityType' value='Ankomst' />
                    <EQ name='LocationSignature' value='{location_signature}' />
                    <GT name='AdvertisedTimeAtLocation' value='{now_str}' />
                    <LT name='AdvertisedTimeAtLocation' value='{future_str}' />
                </AND>
            </FILTER>
            <INCLUDE>AdvertisedTrainIdent</INCLUDE>
            <INCLUDE>AdvertisedTimeAtLocation</INCLUDE>
            <INCLUDE>EstimatedTimeAtLocation</INCLUDE>
            <INCLUDE>Operator</INCLUDE>
        </QUERY>
    </REQUEST>
    """

    headers = {'Content-Type': 'text/xml'}
    response = requests.post(url, data=query, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fel vid förfrågan: {response.status_code}")
        return None
