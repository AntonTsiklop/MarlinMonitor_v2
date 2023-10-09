from django.http import HttpResponse


def kml_maker(coords_date_list, device):

    response = HttpResponse(
        content_type='text/kml',
        headers={'Content-Disposition': 'attachment; '
                 'filename="google_earth_track_{device}.kml"'.format(device=device)},
    )

    response.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    response.write("<kml xmlns='http://earth.google.com/kml/2.1'>\n")
    response.write("<Document>\n")
    response.write(f"   <name>" + f'google_earth_track_{device}.kml' +"</name>\n")
    response.write('   <Style id="style1">\n')
    response.write('       <IconStyle>\n')
    response.write('           <Icon>\n')
    response.write('                <href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle_highlight.png</href>\n')
    response.write('           </Icon>\n')
    response.write('       </IconStyle>\n')
    response.write('   </Style>\n')

    for el in coords_date_list:
        response.write("   <Placemark>\n")
        if len(coords_date_list[0]) == 4:
            response.write("       <description>" + str(el[2]) + "; " + str(el[3]) + "</description>\n")
        else:
            response.write("       <description>" + str(el[2]) + "</description>\n")
        response.write("       <styleUrl>#style1</styleUrl>")
        response.write("       <Point>\n")
        response.write("           <coordinates>" + str(el[1]) + "," + str(el[0]) + "," + '0' + "</coordinates>\n")
        response.write("       </Point>\n")
        response.write("   </Placemark>\n")
    response.write("</Document>\n")
    response.write("</kml>\n")
    response.close()

    return response


