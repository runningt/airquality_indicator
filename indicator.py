import requests
import json
import os


class Indicator(object):
    API_URL = 'http://api.gios.gov.pl/pjp-api/rest/'
    DATA_TEMPLATE = 'data/getData/{}'
    AQ_INDEX_TEMPLATE = 'aqindex/getIndex/{}'
    SENSORS_TEMPLATE = 'station/sensors/{}'
    DEFAULT_STATION_ID = 400

    def __init__(self, stationId=DEFAULT_STATION_ID):
        self.stationId = stationId

    def _get_url_from_template(self, template, stationId):
        return os.path.join(self.API_URL, template.format(stationId))

    def get_data_url(self, stationId=None):
        stationId = stationId if stationId is not None else self.stationId
        return self._get_url_from_template(self.DATA_TEMPLATE, stationId)

    def get_sensors_url(self, stationId=None):
        stationId = stationId if stationId is not None else self.stationId
        return self._get_url_from_template(self.SENSORS_TEMPLATE, stationId)

    def get_aqindex_url(self, stationId=None):
        stationId = stationId if stationId is not None else self.stationId
        return self._get_url_from_template(self.AQ_INDEX_TEMPLATE, stationId)
