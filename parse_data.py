from utils import format_time


def parse_train_data(data):
    if 'RESPONSE' in data and 'RESULT' in data['RESPONSE']:
        trains = []
        for result in data['RESPONSE']['RESULT']:
            if 'TrainAnnouncement' in result:
                for train in result['TrainAnnouncement']:
                    if train.get('Operator') == 'SJ':  # Filtrera för SJ-tåg
                        advertised_time = train.get('AdvertisedTimeAtLocation', 'Ingen tid')
                        estimated_time = train.get('EstimatedTimeAtLocation', advertised_time)

                        train_data = {
                            'Tågnummer': train.get('AdvertisedTrainIdent', 'Ingen ID'),
                            'Annonserad tid': format_time(advertised_time),
                            'Beräknad tid': format_time(estimated_time),
                            'Operatör': train.get('Operator', 'Okänd operatör')
                        }
                        trains.append(train_data)
        return trains
    else:
        print("Ingen data hittades eller strukturen är annorlunda.")
        return []
