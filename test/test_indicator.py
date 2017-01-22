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

    def test_get_data_url(self, indicator):
        assert indicator.get_data_url(10) == \
            'http://powietrze.gios.gov.pl/pjp/current/station_details/table/10/1/0'
        assert indicator.get_data_url('test') == \
            'http://powietrze.gios.gov.pl/pjp/current/station_details/table/test/1/0'
        assert indicator.get_data_url('') == \
            'http://powietrze.gios.gov.pl/pjp/current/station_details/table//1/0'

    def test_get_details_url(self, indicator):
        assert indicator.get_details_url(400) == \
            'http://powietrze.gios.gov.pl/pjp/current/station_details/info/400'
        assert indicator.get_details_url('test') == \
            'http://powietrze.gios.gov.pl/pjp/current/station_details/info/test'
        assert indicator.get_details_url('') == \
            'http://powietrze.gios.gov.pl/pjp/current/station_details/info/'
