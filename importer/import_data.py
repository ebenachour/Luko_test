import datetime
import random
import time
from influxdb import InfluxDBClient

INFLUXDB_USER = 'admin'
INFLUXDB_PASSWORD = 'theadminpassword'
INFLUXDB_DB = 'telegraf'
INFLUXDB_HOST = "localhost"
INFLUXDB_PORT = 8086

def main():
    nb_day = 90  # number of day to generate time series
    timeinterval_sec = 1  # create an event every minute
    total_records =24 * 60 * 60 * nb_day
    now = datetime.datetime.today()
    series = []

    for i in range(0, total_records):
        past_date = now - datetime.timedelta(seconds=i * timeinterval_sec)
        value = random.randint(0, 200)
        host= "LT-ebenachour"
        total =  171647836160
        free = 171647836160 - random.randint(1716478361, 171647836160)
        used_percent = float((total -free)/total )
        pointValues = {
                "time": past_date.strftime ("%Y-%m-%dT%H:%M:%SZ'"),
                "measurement": 'disk',
                'fields':  {
                    'free': free,
                    'used_percent': used_percent,
                    'total': total,
                },
                'tags': {
                    "device": "sda{}".format(random.randint(1,3)),
                    "fstype": "vfat",
                    "mode": "rw",
                    "path": "/home/ebenachour/.Private",
                    "host": host
                },
            }
        series.append(pointValues)

    client = InfluxDBClient(INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_USER, INFLUXDB_PASSWORD, INFLUXDB_DB)
    print("Write points #: {0}".format(total_records))
    client.write_points(series, time_precision='ms')

if __name__ == '__main__':
    main()
