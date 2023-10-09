from django import forms

imei_arr = ['300234069704440', '300234069704480', '300234069705500', '300234069701970', '300234069704960',
            '300234069806520', '300234069806570', '300234069807070', '300234069808520', '300234069808530']

permafrost_imei_arr = ['300234069806520', '300234069806570', '300234069807070', '300234069808520', '300234069808530']


class DownloadForm(forms.Form):
    device = forms.ChoiceField(choices=(('All_BTC', 'All_BTC'), *((imei, imei) for imei in imei_arr),
                                        ('WS_1256', 'WS_1256'), ('Marker', 'Marker'), ('AT_500', 'AT_500')))
    start = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'type': 'datetime-local'}))
    finish = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'type': 'datetime-local'}))
    show_by = forms.IntegerField(required=False, initial=50)


class DownloadFormPermafrost(forms.Form):
    device = forms.ChoiceField(choices=((imei, imei) for imei in permafrost_imei_arr))
    start = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'type': 'datetime-local'}))
    finish = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'type': 'datetime-local'}))
    show_by = forms.IntegerField(required=False, initial=50)


class TrackForm(forms.Form):
    device = forms.ChoiceField(choices=(*((imei, imei) for imei in imei_arr), ('WS_1256', 'WS_1256'), ('Marker', 'Marker'),
                                        ('AT_500', 'AT_500')))
    start = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'type': 'datetime-local'}))
    finish = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'type': 'datetime-local'}))
