import pandas as pd
data = pd.read_csv(r"/home/mapuntiy/Downloads/delhi.csv")


from  geopy.geocoders import Nominatim
geolocator = Nominatim()

array_lat = []
array_lon = []

for i in range(0, len(data)):

	value = data.iloc[i,0]
	print(value)
	
	loc = geolocator.geocode(value)
	if loc:
		print("===============")
		print(loc,"--->","latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
		array_lat.append(loc.latitude)
		array_lon.append(loc.longitude)


	else:
		print("---------------")
		print("SKIPPING")
		print(loc)
		array_lat.append("NIL")
		array_lon.append("NIL")
		print("===============")
	i = i+1
	

Cars = {'LAT': array_lat,
        'LON': array_lon
        }


df = pd.DataFrame(Cars, columns= ['LAT', 'LON'])


export_csv = df.to_csv (r'/home/mapuntiy/Downloads/delhi.csv', index = None, header=True)

