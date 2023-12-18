# I still need to make a household to remove data after a specific time 
# not sure how to build a standard template for this

#Some inpiration here >>>>> 
SHOW MEASUREMENTS ON "<db_name> eg: homeassistant"
SHOW TAG KEYS ON "<db_name>" FROM "<measurement_name> eg: °C"

Query template:
USE "<***db_name***>"; DELETE FROM "<***measurement_name***>" WHERE "<***tag***>" = '***tag_value***' AND time < '2021-04-04'

Actual query eg:
USE "homeassistant"; DELETE FROM "°C " WHERE "entity_id" = 'tasmota_analog_temperature_2' AND time < '2021-04-04'
