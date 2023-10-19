import time

# Function - read soil moisture data from the sensor
def read_soil_moisture(crop):
    # Integrate sensor here
    soil_moisture_value = 50  # Example value, replace with real sensor data
    return soil_moisture_value

# Function - analyze soil moisture data and provide recommendations
def analyze_soil_moisture(soil_moisture_value, crop, season):
    if crop == "Rice":
        if season == "Summer":
            if soil_moisture_value < 30:
                return "The soil is too dry for Rice in Summer. Please irrigate immediately."
            elif soil_moisture_value >= 30 and soil_moisture_value < 60:
                return "Soil moisture is at an optimal level for Rice in Summer."
            else:
                return "The soil is too wet for Rice in Summer. Reduce irrigation."
        elif season == "Monsoon":
            if soil_moisture_value < 60:
                return "Soil moisture is low for Rice in Monsoon. Consider additional irrigation."
            elif soil_moisture_value >= 60 and soil_moisture_value < 85:
                return "Soil moisture is at an optimal level for Rice in Monsoon."
            else:
                return "The soil is too wet for Rice in Monsoon. Reduce irrigation."
        elif season == "Winter":
            if soil_moisture_value < 40:
                return "The soil is too dry for Rice in Winter. Please irrigate if necessary."
            elif soil_moisture_value >= 40 and soil_moisture_value < 70:
                return "Soil moisture is at an optimal level for Rice in Winter."
            else:
                return "The soil is too wet for Rice in Winter. Ensure proper drainage."
    elif crop == "Wheat":
        if season == "Summer":
            if soil_moisture_value < 25:
                return "The soil is too dry for Wheat in Summer. Please irrigate immediately."
            elif soil_moisture_value >= 25 and soil_moisture_value < 60:
                return "Soil moisture is at an optimal level for Wheat in Summer."
            else:
                return "The soil is too wet for Wheat in Summer. Reduce irrigation."
        elif season == "Monsoon":
            if soil_moisture_value < 60:
                return "Soil moisture is low for Wheat in Monsoon. Consider additional irrigation."
            elif soil_moisture_value >= 60 and soil_moisture_value < 85:
                return "Soil moisture is at an optimal level for Wheat in Monsoon."
            else:
                return "The soil is too wet for Wheat in Monsoon. Reduce irrigation."
        elif season == "Winter":
            if soil_moisture_value < 30:
                return "The soil is too dry for Wheat in Winter. Please irrigate if necessary."
            elif soil_moisture_value >= 30 and soil_moisture_value < 60:
                return "Soil moisture is at an optimal level for Wheat in Winter."
            else:
                return "The soil is too wet for Wheat in Winter. Ensure proper drainage."
    elif crop == "Cotton":
        if season == "Summer":
            if soil_moisture_value < 30:
                return "The soil is too dry for Cotton in Summer. Please irrigate immediately."
            elif soil_moisture_value >= 30 and soil_moisture_value < 60:
                return "Soil moisture is at an optimal level for Cotton in Summer."
            else:
                return "The soil is too wet for Cotton in Summer. Reduce irrigation."
        elif season == "Monsoon":
            if soil_moisture_value < 60:
                return "Soil moisture is low for Cotton in Monsoon. Consider additional irrigation."
            elif soil_moisture_value >= 60 and soil_moisture_value < 85:
                return "Soil moisture is at an optimal level for Cotton in Monsoon."
            else:
                return "The soil is too wet for Cotton in Monsoon. Reduce irrigation."
        elif season == "Winter":
            if soil_moisture_value < 35:
                return "The soil is too dry for Cotton in Winter. Please irrigate if necessary."
            elif soil_moisture_value >= 35 and soil_moisture_value < 70:
                return "Soil moisture is at an optimal level for Cotton in Winter."
            else:
                return "The soil is too wet for Cotton in Winter. Ensure proper drainage."
    else:
        return "Invalid crop selection."

# Function - read temperature data from the sensor
def read_temperature(crop):
    # Sensor Integration to be inserted here
    temperature_value = 25  #Example value
    return temperature_value

# Function - analyze temperature data and provide recommendations
def analyze_temperature(temperature_value, crop):
    if crop == "Rice":
        if temperature_value < 20:
            return "The temperature is too low for Rice. Consider using heating methods."
        elif temperature_value >= 20 and temperature_value < 30:
            return "Temperature is within the optimal range for Rice cultivation."
        else:
            return "The temperature is too high for Rice. Provide shade if possible."
    elif crop == "Wheat":
        if temperature_value < 10:
            return "The temperature is too low for Wheat. Consider using heating methods."
        elif temperature_value >= 10 and temperature_value < 25:
            return "Temperature is within the optimal range for Wheat cultivation."
        else:
            return "The temperature is too high for Wheat. Provide shade if possible."
    elif crop == "Cotton":
        if temperature_value < 25:
            return "The temperature is too low for Cotton. Consider using heating methods."
        elif temperature_value >= 25 and temperature_value < 35:
            return "Temperature is within the optimal range for Cotton cultivation."
        else:
            return "The temperature is too high for Cotton. Provide shade if possible."
    else:
        return "Invalid crop selection."

# Function - read humidity data from the sensor
def read_humidity(crop):
    # Integrate sensor data here
    humidity_value = 60  # Example value for sensor
    return humidity_value

# Function - analyze humidity data
def analyze_humidity(humidity_value, crop):
    if crop == "Rice":
        if humidity_value < 40:
            return "The air is too dry for Rice. Consider increasing humidity."
        elif humidity_value >= 40 and humidity_value < 70:
            return "Humidity is at an optimal level for Rice cultivation."
        else:
            return "The air is too humid for Rice. Ventilate the area."
    elif crop == "Wheat":
        if humidity_value < 30:
            return "The air is too dry for Wheat. Consider increasing humidity."
        elif humidity_value >= 30 and humidity_value < 60:
            return "Humidity is at an optimal level for Wheat cultivation."
        else:
            return "The air is too humid for Wheat. Ventilate the area."
    elif crop == "Cotton":
        if humidity_value < 40:
            return "The air is too dry for Cotton. Consider increasing humidity."
        elif humidity_value >= 40 and humidity_value < 70:
            return "Humidity is at an optimal level for Cotton cultivation."
        else:
            return "The air is too humid for Cotton. Ventilate the area."
    else:
        return "Invalid crop selection."

# Function to make decisions based on sensor readings, crop, and season
def make_decision(crop, season):
    soil_moisture_value = read_soil_moisture(crop)
    temperature_value = read_temperature(crop)
    humidity_value = read_humidity(crop)

    soil_moisture_recommendations = analyze_soil_moisture(soil_moisture_value, crop, season)
    temperature_recommendations = analyze_temperature(temperature_value, crop)
    humidity_recommendations = analyze_humidity(humidity_value, crop)

    # Decision-making logic
    if "too wet" in soil_moisture_recommendations and "too hot" in temperature_recommendations:
        return "It's too hot and the soil is too wet for {}. Consider shade and reduce irrigation.".format(crop)
    elif "too dry" in soil_moisture_recommendations and "too low" in temperature_recommendations:
        return "It's too dry and too cold for {}. Increase irrigation and use heating methods.".format(crop)
    else:
        return "Follow the recommendations for {} in {} season:\nSoil Moisture: {}\nTemperature: {}\nHumidity: {}".format(
            crop, season, soil_moisture_recommendations, temperature_recommendations, humidity_recommendations
        )

# Main function for crop selection and season selection
def crop_and_season_selection():
    while True:
        crop = input("Select the crop (Rice, Wheat, Cotton): ").strip().capitalize()

        if crop not in ["Rice", "Wheat", "Cotton"]:
            print("Invalid crop selection. Please enter a valid crop.")
            continue

        season = input("Enter the current season (Summer, Monsoon, Winter): ").strip().capitalize()

        if season not in ["Summer", "Monsoon", "Winter"]:
            print("Invalid season selection. Please enter a valid season.")
            continue

        decision = make_decision(crop, season)

        print("{} Crop Recommendations for {} season:".format(crop, season))
        print(decision)

        time.sleep(3600)  # Check every hour

if __name__ == "__main__":
    crop_and_season_selection()
