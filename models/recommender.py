def generate_recommendations(location, home_type, transport, diet):
    tips = []

    # Transport
    if transport == "Car":
        tips.append("Try public transit or biking 1–2 times a week to reduce emissions.")
    elif transport == "Public Transit":
        tips.append("Switching to a bike or walking when possible can reduce your footprint even more.")
    elif transport == "Bicycle":
        tips.append("Consider joining a cycling advocacy group in your area.")
    elif transport == "Walk":
        tips.append("Great job! Walking is zero-emission!")

    # Housing
    if home_type == "Detached house":
        tips.append("Install a smart thermostat or improve insulation to reduce energy use.")
    else:
        tips.append("Use energy-efficient appliances and LED lighting in your home.")

    # Diet
    if diet == "Meat-heavy":
        tips.append("Reducing red meat once a week can significantly cut emissions.")
    elif diet == "Balanced":
        tips.append("Eating local and seasonal food further reduces environmental impact.")
    elif diet == "Vegetarian":
        tips.append("Well done! Consider switching to plant-based dairy alternatives.")
    elif diet == "Vegan":
        tips.append("Fantastic! Your diet is one of the most climate-friendly.")

    # Location-specific
    if "Toronto" in location:
        tips.append("Check out Toronto’s TransformTO plan for community programs.")
    elif "Vancouver" in location:
        tips.append("Join local eco-projects with Vancouver’s Greenest City initiative.")

    return tips
