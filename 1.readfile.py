import csv
file_path = "weatherHistory.csv"
results = []
with open(file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        temperature = float(row["temperature"])
        humidity = float(row["humidity"])
        pressure = float(row["pressure"])
        a = 0.01
        b = -0.5
        c = 25
        precipitation = a * temperature**2 + b * humidity + c
        results.append({"temperature": temperature, "humidity": humidity, "pressure": pressure, "precipitation": precipitation})
for result in results:
    print(f"Temperature: {result['temperature']}°C, Humidity: {result['humidity']}%,"
          f" Pressure: {result['pressure']}hPa, Precipitation: {result['precipitation']}")