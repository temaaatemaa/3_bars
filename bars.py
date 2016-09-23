import json
import math

#открытие файла
def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)

#рассчет дистанции на основе координат
def distanciya(l1,ll1,l2,ll2):
    #pi - число pi, rad - радиус сферы (Земли)
    rad = 6372795
        
    llat1 = l1
    llong1 = ll1
                
    llat2 = l2
    llong2 = ll2
            
                    #в радианах
    lat1 = llat1*math.pi/180.
    lat2 = llat2*math.pi/180.
    long1 = llong1*math.pi/180.
    long2 = llong2*math.pi/180.
            
                                    #косинусы и синусы широт и разницы долгот
    cl1 = math.cos(lat1)
    cl2 = math.cos(lat2)
    sl1 = math.sin(lat1)
    sl2 = math.sin(lat2)
    delta = long2 - long1
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)
                                                                    
                                                                    #вычисления длины большого круга
    y = math.sqrt(math.pow(cl2*sdelta,2)+math.pow(cl1*sl2-sl1*cl2*cdelta,2))
    x = sl1*sl2+cl1*cl2*cdelta
    ad = math.atan2(y,x)
    dist = ad*rad
    
    return dist


def get_biggest_bar(data):
    
    max_storage=0
    for dict in data :
        Seats_Count=dict['Cells']['SeatsCount']
        if Seats_Count>max_storage:
            max_storage=Seats_Count
            name_of_biggest=dict['Cells']['Name']
    print('Max storage is ',max_storage,' in ',name_of_biggest)



def get_smallest_bar(data):
    min_storage=1000
    for dict in data :
        Seats_Count=dict['Cells']['SeatsCount']
        if Seats_Count<min_storage:
            min_storage=Seats_Count
            name_of_smallest=dict['Cells']['Name']
    print('Min storage is ', min_storage, ' in ', name_of_smallest)



def get_closest_bar(data, longitude, latitude):
    min_distanciya=1000000
    number=0
    for dict in file :
        long_from_text=dict['Cells']['geoData']['coordinates'][0]
        lat_from_text=dict['Cells']['geoData']['coordinates'][1]
        if min_distanciya>distanciya(lat_from_text,long_from_text,latitude,longitude) :
            min_distanciya=distanciya(lat_from_text,long_from_text,latitude,longitude)
            name_of_closest_bar=dict['Cells']['Name']
    print('Closest bar in ', min_distanciya,'meters with name ',name_of_closest_bar)


if __name__ == '__main__':
    
    pass

file=load_data('barr.json')
latitude_from_user=float(input("Input latitude:"))
longitude_from_user=float(input("Input longitude"))
get_smallest_bar(file)
get_biggest_bar(file)
get_closest_bar(file,longitude_from_user,latitude_from_user)

