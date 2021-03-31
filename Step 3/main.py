# needs to be the same name as th function file name that you want to call
import sensor

sensorPattern = "Source: {} - Value: {}"

sensorData = sensor.read_sensor()

print(sensorPattern.format(sensorData["source"], sensorData["value"]))
