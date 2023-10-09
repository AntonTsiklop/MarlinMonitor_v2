import folium
from django.shortcuts import render
from .models import *
from .forms import *
from .xlsx_maker import xlsx_maker
from django.core.paginator import Paginator
from .kml_maker import kml_maker


def main(request):
    form = DownloadForm()
    if request.GET.get('start') and request.GET.get('finish'):

        device = request.GET.get('device')
        start = request.GET.get('start')
        finish = request.GET.get('finish')
        show_by = request.GET.get('show_by')
        page_number = request.GET.get('page')

        if device in ('300234069704440', '300234069704480', '300234069705500', 'All_BTC'):
            Table = TableIceBTC
            columns = Table.get_model_fields(Table)[1:]
        elif device == '300234069701970':
            Table = TableIceBTC11
            columns = Table.get_model_fields(Table)[1:]
        elif device == '300234069704960':
            Table = TableIceST
            columns = Table.get_model_fields(Table)[1:]
        elif device == 'WS_1256':
            Table = TableWeatherStation
            columns = Table.get_model_fields(Table)[1:]
        elif device == 'Marker':
            Table = TableMarker
            columns = Table.get_model_fields(Table)[1:]
        elif device == 'AT_500':
            Table = TableAT500
            columns = Table.get_model_fields(Table)[1:]
        else:
            Table = TablePermafrost
            columns = Table.get_model_fields(Table)[1:]

        if device in ('All_BTC', 'Marker', 'AT_500'):
            Table_queryset = Table.objects.filter(mdatetime__gt=start) & Table.objects.filter(
                mdatetime__lt=finish).order_by('-mdatetime')
        elif device == 'WS_1256':
            Table_queryset = Table.objects.filter(mdatetime__gt=start) & Table.objects.filter(
                mdatetime__lt=finish).order_by('-Num')
        else:
            Table_queryset = Table.objects.filter(IMEI=int(device)) & Table.objects.filter(
                mdatetime__gt=start) & Table.objects.filter(mdatetime__lt=finish).order_by('-mdatetime')

        if 'xlsx_all' in request.GET:
            return xlsx_maker(Table_queryset, columns, device)

        request.session["device"] = device
        request.session["start"] = start
        request.session["finish"] = finish
        request.session["show_by"] = show_by
        request.session['cur_page_num'] = 1

        paginator = Paginator(Table_queryset, show_by)
        page_obj = paginator.get_page(page_number)

        if 'xlsx_page' in request.GET:
            return xlsx_maker(page_obj, columns, device)
        return render(request, 'tables/main.html', {'form': form, 'page_obj': page_obj, 'columns': columns})

    try:
        device = request.session["device"]
        start = request.session["start"]
        finish = request.session["finish"]
        show_by = request.session["show_by"]

        if device in ('300234069704440', '300234069704480', '300234069705500', 'All_BTC'):
            Table = TableIceBTC
            columns = Table.get_model_fields(Table)[1:]
        elif device == '300234069701970':
            Table = TableIceBTC11
            columns = Table.get_model_fields(Table)[1:]
        elif device == '300234069704960':
            Table = TableIceST
            columns = Table.get_model_fields(Table)[1:]
        elif device == 'WS_1256':
            Table = TableWeatherStation
            columns = Table.get_model_fields(Table)[1:]
        elif device == 'Marker':
            Table = TableMarker
            columns = Table.get_model_fields(Table)[1:]
        elif device == 'AT_500':
            Table = TableAT500
            columns = Table.get_model_fields(Table)[1:]
        else:
            Table = TablePermafrost
            columns = Table.get_model_fields(Table)[1:]

        if device in ('All_BTC', 'Marker', 'AT_500'):
            Table_queryset = Table.objects.filter(mdatetime__gt=start) & Table.objects.filter(
                mdatetime__lt=finish).order_by('-mdatetime')
        elif device == 'WS_1256':
            Table_queryset = Table.objects.filter(mdatetime__gt=start) & Table.objects.filter(
                mdatetime__lt=finish).order_by('-Num')
        else:
            Table_queryset = Table.objects.filter(IMEI=int(device)) & Table.objects.filter(
                mdatetime__gt=start) & Table.objects.filter(mdatetime__lt=finish).order_by('-mdatetime')

        if 'xlsx_page' not in request.GET:
            page_number = request.GET.get('page')
            request.session['cur_page_num'] = page_number
            paginator = Paginator(Table_queryset, show_by)
            page_obj = paginator.get_page(page_number)
            return render(request, 'tables/main.html', {'form': form, 'page_obj': page_obj, 'columns': columns})
        else:
            page_number = request.session['cur_page_num']
            paginator = Paginator(Table_queryset, show_by)
            page_obj = paginator.get_page(page_number)
            return xlsx_maker(page_obj, columns, device)

    except KeyError:
        return render(request, 'tables/main.html', {'form': form})


def permafrost(request):
    form = DownloadFormPermafrost()
    if request.GET.get('start') and request.GET.get('finish'):

        device = request.GET.get('device')
        start = request.GET.get('start')
        finish = request.GET.get('finish')
        show_by = request.GET.get('show_by')
        page_number = request.GET.get('page')

        Table = TablePermafrost
        columns = Table.get_model_fields(Table)[1:]

        try:
            Table_queryset = Table.objects.filter(IMEI=int(device)) & Table.objects.filter(
                mdatetime__gt=start) & Table.objects.filter(mdatetime__lt=finish).order_by('-mdatetime')
        except ValueError:
            return render(request, 'tables/main.html', {'form': form})

        if 'xlsx_all' in request.GET:
            return xlsx_maker(Table_queryset, columns, device)

        request.session["device"] = device
        request.session["start"] = start
        request.session["finish"] = finish
        request.session["show_by"] = show_by
        request.session['cur_page_num'] = 1

        paginator = Paginator(Table_queryset, show_by)
        page_obj = paginator.get_page(page_number)

        if 'xlsx_page' in request.GET:
            return xlsx_maker(page_obj, columns, device)
        return render(request, 'tables/main.html', {'form': form, 'page_obj': page_obj, 'columns': columns})

    try:
        device = request.session["device"]
        start = request.session["start"]
        finish = request.session["finish"]
        show_by = request.session["show_by"]

        Table = TablePermafrost
        columns = Table.get_model_fields(Table)[1:]

        try:
            Table_queryset = Table.objects.filter(IMEI=int(device)) & Table.objects.filter(
                mdatetime__gt=start) & Table.objects.filter(mdatetime__lt=finish).order_by('-mdatetime')
        except ValueError:
            return render(request, 'tables/main.html', {'form': form})

        if 'xlsx_page' not in request.GET:
            page_number = request.GET.get('page')
            request.session['cur_page_num'] = page_number
            paginator = Paginator(Table_queryset, show_by)
            page_obj = paginator.get_page(page_number)
            return render(request, 'tables/main.html', {'form': form, 'page_obj': page_obj, 'columns': columns})
        else:
            page_number = request.session['cur_page_num']
            paginator = Paginator(Table_queryset, show_by)
            page_obj = paginator.get_page(page_number)
            return xlsx_maker(page_obj, columns, device)

    except KeyError:
        return render(request, 'tables/main.html', {'form': form})


def track(request):
    form = TrackForm()
    if request.GET.get('start') and request.GET.get('finish'):

        device = request.GET.get('device')
        start = request.GET.get('start')
        finish = request.GET.get('finish')

        if device in ('300234069704440', '300234069704480', '300234069705500'):
            Table = TableIceBTC
        elif device == '300234069701970':
            Table = TableIceBTC11
        elif device == '300234069704960':
            Table = TableIceST
        elif device == 'WS_1256':
            Table = TableWeatherStation
        elif device == 'Marker':
            Table = TableMarker
        elif device == 'AT_500':
            Table = TableAT500
        else:
            Table = TablePermafrost

        if device in ('300234069704440', '300234069704480', '300234069705500'):
            Table_queryset = Table.objects.filter(IMEI=int(device)) & Table.objects.filter(
                mdatetime__gt=start) & Table.objects.filter(mdatetime__lt=finish).order_by('-mdatetime')
        else:
            Table_queryset = Table.objects.filter(mdatetime__gt=start) & Table.objects.filter(
                mdatetime__lt=finish).order_by('-mdatetime')

        try:
            coords_date_list = []
            Arctic = False
            for obj in Table_queryset:
                if hasattr(obj, 'IMEI'):
                    coords_date_list.append((obj.Latitude, obj.Longitude, obj.mdatetime, obj.IMEI))
                else:
                    coords_date_list.append((obj.Latitude, obj.Longitude, obj.mdatetime))
                if obj.Latitude > 80:
                    Arctic = True

            if Arctic or 'download' in request.GET:
                return kml_maker(coords_date_list, device)

            coords_list = [el[:2] for el in coords_date_list]
            m = folium.Map(location=coords_list[0], zoom_start=10, crs='EPSG3857')
            folium.PolyLine(coords_list, tooltip="track").add_to(m)
            folium.Marker(location=coords_list[0], popup='Start').add_to(m)
            folium.Marker(location=coords_list[-1], popup='Finish').add_to(m)
            m.save('tables/templates/tables/track_on_map.html')
            return render(request, 'tables/track_on_map.html')

        except IndexError:
            return render(request, 'tables/track.html')

    return render(request, 'tables/track.html', {'form': form})

