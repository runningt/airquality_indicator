import pytest
from indicator import Indicator

class TestIndicator(object):
    @pytest.fixture
    def indicator(self):
        return Indicator()

    def test_indicator(self, indicator):
        assert indicator is not None

    def test_station_id(self, indicator):
        assert indicator.stationId == 400

    @pytest.mark.parametrize('defaultStationId', (400, 10, 'test', ''))
    def test_get_data_url_default(self, indicator, defaultStationId):
        indicator.stationId =defaultStationId
        assert indicator.get_data_url() == \
            'http://api.gios.gov.pl/pjp-api/rest/data/getData/%s' % defaultStationId

    @pytest.mark.parametrize('stationId', (400, 10, 'test', ''))
    def test_get_data_url(self, indicator, stationId):
        assert indicator.get_data_url(stationId) == \
            'http://api.gios.gov.pl/pjp-api/rest/data/getData/%s' % stationId

    @pytest.mark.parametrize('defaultStationId', (400, 10, 'test', ''))
    def test_get_aqindex_url_default(self, indicator, defaultStationId):
        indicator.stationId =defaultStationId
        assert indicator.get_aqindex_url() == \
            'http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/%s' % defaultStationId

    @pytest.mark.parametrize('stationId', (400, 10, 'test', ''))
    def test_get_aqindex_url(self, indicator, stationId):
        assert indicator.get_aqindex_url(stationId) == \
            'http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/%s' % stationId

    @pytest.mark.parametrize('defaultStationId, sensorId',
            ((400, 1), (10, 1), (10, 2), ('test', 10), ('', ''), (None, 10)))
    def test_get_sensor_url(self, indicator, defaultStationId, sensorId):
        indicator.stationId =defaultStationId
        assert indicator.get_sensor_url(sensorId) == \
            'http://api.gios.gov.pl/pjp-api/rest/station/sensors/%s' % sensorId

    def test_get_details_url(self, indicator):
        assert indicator.get_details_url() == \
            'http://api.gios.gov.pl/pjp-api/rest/station/findAll'
