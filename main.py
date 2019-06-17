#!/usr/bin/env python
import sys
from indicator import Indicator, DEFAULT_STATION_ID


def main():
    stationId = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_STATION_ID
    ind = Indicator(stationId)
    print(ind.get_aqindex_url())
    print(ind.get_details_url())
    return 0

if __name__ == '__main__':
    sys.exit(main())
