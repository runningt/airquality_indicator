import pytest
import mock
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

    def test_get_all_stations_url(self, indicator):
        assert indicator.get_all_stations_url() == \
            'http://api.gios.gov.pl/pjp-api/rest/station/findAll'

    @pytest.mark.parametrize('json, keys, expected',
        [('[{}, {"key": "value"}]', (1, "key"), "value"),
        ('{"key": "value"}', ("key",), "value"),
        ('{"key": ["value", "value2"]}', ("key", 0), "value")],
        )
    def test_get_detail_from_json(self, indicator, json, keys, expected):
        with mock.patch( 'builtins.open', mock.mock_open(read_data=json)):
            f = open('/tmp/json', 'rw')
            assert indicator.get_detail_from_json(f, *keys) == expected

    @pytest.mark.parametrize('json, keys',
        [('[{"key": "value"}]', (1, "key")),
        ('{"key": "value"}', ("key2",)),
        ('{}', ("key", 0, 1, 2, 3))]
        )
    def test_get_detail_from_json_raised_keyerror(self, indicator, json, keys):
        with mock.patch('builtins.open' , mock.mock_open(read_data=json)):
            with pytest.raises(KeyError) as e:
                f = open('/tmp/json', 'rw')
                indicator.get_detail_from_json(f, *keys)
                assert e.args[0] == str(keys)
