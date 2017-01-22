#import lxml


class Indicator(object):
    DATA_URL_TEMPLATE = 'http://powietrze.gios.gov.pl/pjp/current/station_details/table/{}/1/0'
    DETAILS_URL_TEMPLATE = 'http://powietrze.gios.gov.pl/pjp/current/station_details/info/{}'
    DEFAULT_STATION_ID = 400

    def __init__(self, stationId = DEFAULT_STATION_ID):
        self.stationId = stationId

    def _get_url_from_template(self, template, stationId):
        return template.format(stationId)

    def get_data_url(self, stationId):
        return self._get_url_from_template(self.DATA_URL_TEMPLATE, stationId)

    def get_details_url(self, stationId):
        return self._get_url_from_template(self.DETAILS_URL_TEMPLATE, stationId)
