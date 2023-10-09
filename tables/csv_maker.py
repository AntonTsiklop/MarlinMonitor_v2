import csv
from django.http import HttpResponse


def csv_maker(coords_date_list, device):

    response = HttpResponse(
        content_type='text/kml',
        headers={'Content-Disposition': 'attachment; '
                 'filename="Google_Earth_data_{device}.csv"'.format(device=device)},
    )

    writer = csv.writer(response)
    if len(coords_date_list[0]) == 4:
        writer.writerow(['Latitude', 'Longitude', 'datetime', 'IMEI'])
    else:
        writer.writerow(['Latitude', 'Longitude', 'datetime'])
    for el in coords_date_list:
        writer.writerow(el)
    return response

