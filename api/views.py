from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from tables.models import TableAT500


class AT500Updater(APIView):

    @staticmethod
    def post(request):
        data = request.body.decode()
        table_data = {el.split('=')[0]: el.split('=')[1] for el in data.split('&')}
        try:
            table_data['mdatetime'] = datetime.strptime(table_data['mdate'] + table_data['mtime'], "'%Y-%m-%d''%H:%M:%S'")
        except ValueError:
            table_data['mdatetime'] = datetime.strptime("'2000-01-01''00:00:00'", "'%Y-%m-%d''%H:%M:%S'")
        del table_data['mdate']
        del table_data['mtime']
        table_data['Latitude'] = table_data.pop('lat')
        table_data['Longitude'] = table_data.pop('lon')
        table_data['Subm'] = table_data.pop('submergence')
        TableAT500.objects.create(**table_data)
        resp = Response('123456')
        resp.__dict__['headers'] = {'resp': '123456'}
        print(resp.__dict__)
        return resp
