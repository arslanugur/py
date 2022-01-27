from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent = "geoapiExercises")
la = input("Enter the Keyword")
print("Location Address:", la)
location = geolocator.geocode(la)
print("Street address, street name: ")
print(location.address)

