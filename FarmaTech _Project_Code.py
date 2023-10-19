import time
optimal_ranges = {
    'Wheat': {
        'Summer': {'temperature': (60, 75), 'humidity': (50, 70)},
        'Winter': {'temperature': (40, 60), 'humidity': (50, 70)},
        'Monsoon': {'temperature': (70, 85), 'humidity': (70, 80)},
    },
    'Rice': {
        'Summer': {'temperature': (70, 85), 'humidity': (80, 100)},
        'Winter': {'temperature': (50, 70), 'humidity': (60, 80)},
        'Monsoon': {'temperature': (77, 86), 'humidity': (80, 100)},
    },
    'Cotton': {
        'Summer': {'temperature': (70, 100), 'humidity': (50, 70)},
        'Winter': {'temperature': (55, 75), 'humidity': (50, 60)},
        'Monsoon': {'temperature': (70, 95), 'humidity': (50, 70)},
    }
}
# Function - read temperature data from the sensor
def read_temperature_humidity():
    try:
        dht_pin = board.D4  # Adjust the pin as per your wiring
        dht_sensor = adafruit_dht.DHT22(dht_pin)

        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        return temperature, humidity
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    
# Function - analyze temperature data and provide recommendations
def compare_with_optimal_ranges(crop, season, temperature, humidity):
    if crop in optimal_ranges and season in optimal_ranges[crop]:
        temp_range = optimal_ranges[crop][season]['temperature']
        hum_range = optimal_ranges[crop][season]['humidity']
        if temp_range[0] <= temperature <= temp_range[1] and hum_range[0] <= humidity <= hum_range[1]:
            return "Conditions are optimal."
        else:
            instructions = []
            if temperature < temp_range[0]:
                instructions.append("Provide shade to lower the temperature.")
            if temperature > temp_range[1]:
                instructions.append("Ensure proper ventilation to cool the environment.")
            if humidity < hum_range[0]:
                instructions.append("Increase irrigation to maintain humidity.")
            if humidity > hum_range[1]:
                instructions.append("Reduce irrigation to control humidity.")
            return "\n".join(instructions)
    else:
        return "Invalid crop or season."


# Main function for crop selection and season selection
'''def crop_selection():
    while True:
        
        crop = input("Enter the crop (Wheat, Rice, Cotton): ")
        season = input("Enter the season (Summer, Winter, Monsoon): ")
        temperature, humidity = read_temperature_humidity()
        decision = make_decision(crop)

        instructions = compare_with_optimal_ranges(crop, season, temperature, humidity)
        print(instructions)

        time.sleep(3600)  # Check every hour'''
def main():
    while True:
        temperature, humidity = read_temperature_humidity()
        if temperature is not None and humidity is not None:
            crop = input("Enter the crop (Wheat, Rice, Cotton): ")
            season = input("Enter the season (Summer, Winter, Monsoon): ")
            instructions = compare_with_optimal_ranges(crop, season, temperature, humidity)
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(instructions)
        time.sleep(3600)  # Read every hour (adjust as needed)

if _name_ == "_main_":
    main()
