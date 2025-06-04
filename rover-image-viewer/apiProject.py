# apiProject.py
# Author: Veer Sawhney
# Description: This script uses NASA's Mars Rover Photos API to retrieve and display
# a front-facing camera image taken by the Curiosity rover on a specified Martian sol (day).
# It also downloads and saves the image locally as 'rover.jpg'.

import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Prompt user for sol number (Martian day)
sol = input("Which image do you want to see? (min 14/max 3291)\n")

# Send request to NASA API for Curiosity rover photos using front-facing hazard camera
nasa = requests.get(
    f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=" + sol +
    "&camera=fhaz&api_key=YQNyezTDvGhf8WZQfBRhIfeCPkitfmHWuCWOgqsc"
)

# Parse JSON response
nasa_json = nasa.json()
print(nasa_json)  # Print full JSON (for debugging or info)

# Basic input validation: check if the sol is within the valid range
if int(sol) <= 14 or int(sol) >= 3291:
    print("Sorry, that sol is outside of the parameters. Please try again.")
    sol = input("Which image do you want to see? (min 14/max 3291 - does not work from sol 237 to sol 268)\n")

# Print all top-level keys in the JSON to see structure
for key in nasa_json:
    print(key)

# Extract image URL from the JSON
nasa_url = nasa_json['photos'][0]['img_src']
print(nasa_url)  # Print image URL

# Request the image file from the extracted URL
im_response = requests.get(nasa_url)
print(im_response)  # Print HTTP response

# Save image content as 'rover.jpg'
with open("rover.jpg", 'wb') as f:
    f.write(im_response.content)

# Read and display the image using matplotlib
img = mpimg.imread("rover.jpg")
plt.imshow(img)
plt.title("Rover: Sol " + sol)
plt.show()




