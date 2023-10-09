from django.db import models


class TableIceBTC(models.Model):
    FormatID = models.IntegerField(default=0)
    IMEI = models.TextField(default=0)
    mdatetime = models.DateTimeField(null=True, blank=False)
    STD = models.IntegerField(default=0)
    STR = models.IntegerField(default=0)
    Vbat = models.FloatField(default=0)
    HIT = models.FloatField(default=0)
    HIP = models.FloatField(default=0)
    HIH = models.FloatField(default=0)
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    SatNum = models.IntegerField(default=0)
    HDOP = models.FloatField(default=0)
    TTFF = models.IntegerField(default=0)
    AP = models.FloatField(default=0)
    APT = models.FloatField(default=0)
    Subm = models.FloatField(default=0)
    T1 = models.FloatField(default=0)
    T2 = models.FloatField(default=0)
    T3 = models.FloatField(default=0)
    T4 = models.FloatField(default=0)
    T5 = models.FloatField(default=0)
    T6 = models.FloatField(default=0)
    T7 = models.FloatField(default=0)
    T8 = models.FloatField(default=0)
    T9 = models.FloatField(default=0)
    T10 = models.FloatField(default=0)
    T11 = models.FloatField(default=0)
    T12 = models.FloatField(default=0)
    T13 = models.FloatField(default=0)
    T14 = models.FloatField(default=0)
    T15 = models.FloatField(default=0)
    T16 = models.FloatField(default=0)
    T17 = models.FloatField(default=0)
    HP = models.FloatField(default=0)

    def get_field(self, field_name):
        return self.__getattribute__(field_name)

    def get_model_fields(self):
        fields = [field.name for field in self._meta.fields]
        return fields


class TableIceST(models.Model):
    FormatID = models.IntegerField(default=0)
    IMEI = models.TextField(default=0)
    STD = models.IntegerField(default=0)
    STR = models.IntegerField(default=0)
    Vbat = models.FloatField(default=0)
    HIT = models.FloatField(default=0)
    HIP = models.FloatField(default=0)
    HIH = models.FloatField(default=0)
    mdatetime = models.DateTimeField(null=True, blank=False)
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    SatNum = models.IntegerField(default=0)
    HDOP = models.FloatField(default=0)
    TTFF = models.IntegerField(default=0)
    AP = models.FloatField(default=0)
    APT = models.FloatField(default=0)
    Subm = models.FloatField(default=0)
    T1 = models.FloatField(default=0)

    def get_field(self, field_name):
        return self.__getattribute__(field_name)

    def get_model_fields(self):
        fields = [field.name for field in self._meta.fields]
        return fields


class TableIceBTC11(models.Model):
    FormatID = models.IntegerField(default=0)
    IMEI = models.TextField(default=0)
    STD = models.IntegerField(default=0)
    STR = models.IntegerField(default=0)
    Vbat = models.FloatField(default=0)
    HIT = models.FloatField(default=0)
    HIP = models.FloatField(default=0)
    HIH = models.FloatField(default=0)
    mdatetime = models.DateTimeField(null=True, blank=False)
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    SatNum = models.IntegerField(default=0)
    HDOP = models.FloatField(default=0)
    TTFF = models.IntegerField(default=0)
    AP = models.FloatField(default=0)
    APT = models.FloatField(default=0)
    Subm = models.FloatField(default=0)
    T1 = models.FloatField(default=0)
    T2 = models.FloatField(default=0)
    T3 = models.FloatField(default=0)
    T4 = models.FloatField(default=0)
    T5 = models.FloatField(default=0)
    T6 = models.FloatField(default=0)
    T7 = models.FloatField(default=0)
    T8 = models.FloatField(default=0)
    T9 = models.FloatField(default=0)
    T10 = models.FloatField(default=0)
    T11 = models.FloatField(default=0)
    T12 = models.FloatField(default=0)
    T13 = models.FloatField(default=0)

    def get_field(self, field_name):
        return self.__getattribute__(field_name)

    def get_model_fields(self):
        fields = [field.name for field in self._meta.fields]
        return fields


class TablePermafrost(models.Model):
    FormatID = models.IntegerField(default=0)
    IMEI = models.TextField(default=0)
    STD = models.IntegerField(default=0)
    STR = models.IntegerField(default=0)
    Vbat = models.FloatField(default=0)
    HIT = models.FloatField(default=0)
    mdatetime = models.DateTimeField(null=True, blank=False)
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    SatNum = models.IntegerField(default=0)
    HDOP = models.FloatField(default=0)
    TTFF = models.IntegerField(default=0)
    T1 = models.FloatField(default=0)
    T2 = models.FloatField(default=0)
    T3 = models.FloatField(default=0)
    T4 = models.FloatField(default=0)
    T5 = models.FloatField(default=0)
    T6 = models.FloatField(default=0)
    T7 = models.FloatField(default=0)
    T8 = models.FloatField(default=0)
    T9 = models.FloatField(default=0)
    T10 = models.FloatField(default=0)
    T11 = models.FloatField(default=0)
    T12 = models.FloatField(default=0)
    T13 = models.FloatField(default=0)
    T14 = models.FloatField(default=0)
    T15 = models.FloatField(default=0)
    T16 = models.FloatField(default=0)
    T17 = models.FloatField(default=0)
    T18 = models.FloatField(default=0)
    T19 = models.FloatField(default=0)
    T20 = models.FloatField(default=0)
    T21 = models.FloatField(default=0)
    T22 = models.FloatField(default=0)
    T23 = models.FloatField(default=0)
    T24 = models.FloatField(default=0)
    T25 = models.FloatField(default=0)
    T26 = models.FloatField(default=0)
    T27 = models.FloatField(default=0)
    T28 = models.FloatField(default=0)
    T29 = models.FloatField(default=0)
    T30 = models.FloatField(default=0)
    T31 = models.FloatField(default=0)
    T32 = models.FloatField(default=0)

    def get_field(self, field_name):
        return self.__getattribute__(field_name)

    def get_model_fields(self):
        fields = [field.name for field in self._meta.fields]
        return fields


class TableWeatherStation(models.Model):
    StID = models.IntegerField(default=0)
    Num = models.IntegerField(default=0)
    mdatetime = models.DateTimeField(null=True, blank=False)
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    AP = models.FloatField(default=0)
    APT = models.FloatField(default=0)
    AT = models.FloatField(default=0)
    WS = models.FloatField(default=0)
    WD = models.FloatField(default=0)
    WSmax = models.FloatField(default=0)
    HT = models.FloatField(default=0)
    Vbat = models.FloatField(default=0)
    TD = models.FloatField(default=0)
    datetime_from_email = models.DateTimeField(null=True, blank=False)

    def get_field(self, field_name):
        return self.__getattribute__(field_name)

    def get_model_fields(self):
        fields = [field.name for field in self._meta.fields]
        return fields


class TableMarker(models.Model):
    carid = models.IntegerField(default=0)
    mdatetime = models.DateTimeField(null=True, blank=False)
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    HDOP = models.FloatField(default=0)
    sats = models.IntegerField(default=0)
    platform_type = models.TextField(default=0)
    count = models.IntegerField(default=0)
    t_surf = models.FloatField(default=0)
    level_plc = models.FloatField(default=0)
    pwr_v_main = models.FloatField(default=0)

    def get_field(self, field_name):
        return self.__getattribute__(field_name)

    def get_model_fields(self):
        fields = [field.name for field in self._meta.fields]
        return fields


class TableAT500(models.Model):
    carid = models.IntegerField(default=0)
    Latitude = models.FloatField(default=0)
    Longitude = models.FloatField(default=0)
    sats = models.IntegerField(default=0)
    HDOP = models.FloatField(default=0)
    platform_type = models.TextField(default=0)
    count = models.IntegerField(default=0)
    AT500_temp = models.FloatField(default=0)
    AT500_cond = models.FloatField(default=0)
    AT500_salt = models.FloatField(default=0)
    AT500_density = models.FloatField(default=0)
    AT500_tds = models.FloatField(default=0)
    AT500_turb = models.FloatField(default=0)
    AT500_Ph = models.FloatField(default=0)
    AT500_redox = models.FloatField(default=0)
    AT500_oxygen = models.FloatField(default=0)
    Subm = models.FloatField(default=0)
    rough = models.FloatField(default=0)
    level_plc = models.FloatField(default=0)
    pwr_v_main = models.FloatField(default=0)
    mdatetime = models.DateTimeField(null=True, blank=False)

    def get_field(self, field_name):
        return self.__getattribute__(field_name)

    def get_model_fields(self):
        fields = [field.name for field in self._meta.fields]
        return fields

