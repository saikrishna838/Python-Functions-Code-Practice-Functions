def get_weather_report(temperature):
    if temperature < 22:
        report = "Cold"
    elif (temperature >= 22) and (temperature < 35):
        report = "Warm"
    else:
        report = "Hot"
    return report


temperature = int(input())
result = get_weather_report(temperature)
print(result)
