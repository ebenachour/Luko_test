import datetime
import random
import time
from influxdb import InfluxDBClient
 
INFLUXDB_USER = 'admin'
INFLUXDB_PASSWORD = 'theadminpassword'
INFLUXDB_DB = 'telegraf'
INFLUXDB_HOST = "172.17.0.1"
INFLUXDB_PORT = 8086

def main():
    nb_day = 1  # number of day to generate time series
    timeinterval_min = 1  # create an event every minute
    total_records =24 * nb_day
    now = datetime.datetime.today()
    metric = "cpu"
    series = []

    for i in range(0, total_records):
        past_date = now - datetime.timedelta(minutes=i * timeinterval_min)
        value = random.randint(0, 200)
        host = "LT-ebenachour{}".format(random.randint(1, 5))
        
        total =  171647836160
        free = 171647836160 - random.randint(1716478361, 171647836160)
        used_percent = float((total -free)/total )
        pointValues = {
                "time": past_date.strftime ("%Y-%m-%d %H:%M:%S"),
                "measurement": 'disk',
                'fields':  {
                    'free': str(free),
                    'used_percent': str(used_percent),
                    'total': str(total),
                },
                'tags': {
                    "device": "sda10",
                    "fstype": "vfat",
                    "mode": "rw",
                    "path": "/home/influxdb",
                    "host": host
                },
            }
        series.append(pointValues)
    import pdb; pdb.set_trace()

    print(series)
    client = InfluxDBClient(INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_USER, INFLUXDB_PASSWORD, INFLUXDB_DB)
 
    #print("Create a retention policy")
    #retention_policy = 'awesome_policy'
    #client.create_retention_policy(retention_policy, '3m', 3, default=True)
 
    print("Write points #: {0}".format(total_records))
    client.write_points(series, time_precision='ms')
 
if __name__ == '__main__':
    main()