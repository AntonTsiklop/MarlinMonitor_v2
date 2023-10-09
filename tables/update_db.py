import csv
import requests
from bs4 import BeautifulSoup
from .models import *
from .parse_email import *


def update_db_sbd():
    imap_data = iridium_sbd_email("imap.mail.ru", "test.marlin-yug@mail.ru", "EvE0ppE4GE3V12G9iPSQ")
    msg_list_bin = imap_data[0]
    IMEI_list = imap_data[1]
    data_list = zip(msg_list_bin, IMEI_list)
    for data in data_list:
        print(data[1])
        if data[1] in ('300234069704440', '300234069704480', '300234069705500'):
            data_format = 'IceBTC'
            Table = TableIceBTC
        elif data[1] == '300234069701970':
            data_format = 'IceBTC11'
            Table = TableIceBTC11
        elif data[1] == '300234069704960':
            data_format = 'IceST'
            Table = TableIceST
        else:
            data_format = 'permafrost-32T'
            Table = TablePermafrost
        table_data = {}
        with open(f"tables/formats/{data_format}.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if 'GNSS' in row[0]:
                    row[0] = row[0][4:]
                table_data[row[0]] = parse2float(data[0], int(row[1]), int(row[2]), float(row[3]), float(row[4]))
            try:
                table_data['mdatetime'] = datetime.strptime(f'{int(table_data["Year"])} {int(table_data["Month"])} '
                                                            f'{int(table_data["Day"])} {int(table_data["Hour"])} '
                                                            f'{int(table_data["Minute"])} {int(table_data["Second"])}',
                                                            '%Y %m %d %H %M %S')
            except ValueError:
                table_data['mdatetime'] = None
            table_data = {key: table_data[key] for key in table_data if key not in ("Year", "Month", "Day", "Hour",
                                                                                    "Minute", "Second")}
            table_data['IMEI'] = data[1]
        Table.objects.create(**table_data)


def update_db_gonets():
    # imap_data = gonets_email("imap.mail.ru", "test.marlin-yug@mail.ru", "EvE0ppE4GE3V12G9iPSQ")
    imap_data = gonets_email("imap.yandex.ru", "meteogonets@yandex.ru", "pcbhacarjecuqmgd")
    with open(f"tables/formats/ws_gonets.csv") as f:
        reader = csv.reader(f)
        rl = list(reader)[0][0].split(';')
    for data in imap_data:
        row = zip(rl, data)
        table_data = {el[0]: el[1] for el in row}
        table_data['mdatetime'] = datetime.strptime(table_data['Date'] + table_data['Time'], '%Y-%m-%d%H:%M:%S')
        del table_data['Date']
        del table_data['Time']
        TableWeatherStation.objects.create(**table_data)


def update_db_html():
    TableMarker.objects.all().delete()
    request = requests.get('http://iotdata.iotstorage.su/viewer.php?carid=3221')
    data = request.text
    soup = BeautifulSoup(data, 'lxml')
    for el in soup.find_all('code'):
        data_row = el.text.split('&')
        table_data = {el.split('=')[0]: el.split('=')[1] for el in data_row}
        try:
            table_data['mdatetime'] = datetime.strptime(table_data['mdate'] + table_data['mtime'], "'%Y-%m-%d''%H:%M:%S'")
        except ValueError:
            continue
        del table_data['mdate']
        del table_data['mtime']
        table_data['Latitude'] = table_data.pop('lat')
        table_data['Longitude'] = table_data.pop('lon')
        TableMarker.objects.create(**table_data)


if __name__ == '__main__':
    update_db_sbd()
    update_db_gonets()




