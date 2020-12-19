from w1thermsensor import W1ThermSensor


while 1:
    sensor = W1ThermSensor( )
    temperature_in_celsius = sensor.get_temperature()
    print ("Actual Temperature = {}".format(temperature_in_celsius))


