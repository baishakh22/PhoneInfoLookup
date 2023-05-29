import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Get phone number with country code.
phoneNum = input("Please Enter the Phone Number with Country Code: ")
phoneNum = phonenumbers.parse(phoneNum)  # Get the string value of phone number, it's using "parse" function

# Check the validating the phone number
print("Valid Phone Number: ", phonenumbers.is_valid_number(phoneNum))

# Get the Timezone from this number
print("Timezone: ", timezone.time_zones_for_number(phoneNum))

# Get information of a Phone Carrier
print("Carrier: ", carrier.name_for_number(phoneNum, "en"))

# Get information about region
region = geocoder.description_for_number(phoneNum, "en")
print("Region: ", region)

# api use for geolocation
key = 'cb64918f54ac4f5d87211c7306e8c7be'
from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)
queue = str(region)
location = geocoder.geocode(queue)
print(location)

lat = location[0]['geometry']['lat']
lng = location[0]['geometry']['lng']
print("Latitude: ", lat, "Longitude: ", lng)
