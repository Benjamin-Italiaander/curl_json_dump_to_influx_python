# curl_json_dump_to_influx_python
curl a json from the web and process in to influxdb

This is a small example i use as a template to dump data into influxdb. It's for me the most simple way.
More complex ways i usally resolve with the pandas libary but in this way i keep it really lean and mean.

There is a small loop added becaus if i read influxdb into grafana it really needs to be assigned as a float otherways it will only be readable by 


[The script template is called run.py]https://github.com/Benjamin-Italiaander/curl_json_dump_to_influx_python/blob/main/run.py
