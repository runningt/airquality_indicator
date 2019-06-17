import requests
import json
import os


class Indicator(object):
    API_URL = 'http://api.gios.gov.pl/pjp-api/rest/'
    DATA_TEMPLATE = 'data/getData/{}'
    AQ_INDEX_TEMPLATE = 'aqindex/getIndex/{}'
    SENSOR_TEMPLATE = 'station/sensors/{}'
    DETAILS_TEMPLATE = 'station/findAll'
    DEFAULT_STATION_ID = 400

    def __init__(self, stationId=DEFAULT_STATION_ID):
        self.stationId = stationId

    def _get_url_from_template(self, template, stationId=None):
        if stationId is None:
            return os.path.join(self.API_URL, template)
        else:
            return os.path.join(self.API_URL, template.format(stationId))

    def get_data_url(self, stationId=None):
        stationId = stationId if stationId is not None else self.stationId
        return self._get_url_from_template(self.DATA_TEMPLATE, stationId)

    def get_sensor_url(self, sensorId):
        return self._get_url_from_template(self.SENSOR_TEMPLATE, sensorId)

    def get_aqindex_url(self, stationId=None):
        stationId = stationId if stationId is not None else self.stationId
        return self._get_url_from_template(self.AQ_INDEX_TEMPLATE, stationId)

    def get_details_url(self):
        return self._get_url_from_template(self.DETAILS_TEMPLATE)

    def get_detail_from_json(self, json_file, *keys):
        json_obj = json.load(json_file)
        try:
            for k in keys:
                json_obj = json_obj[k]
        except (IndexError, KeyError):
            keys = [str(k) for k in keys]
            raise KeyError(str(keys))
        return json_obj
