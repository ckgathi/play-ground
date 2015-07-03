name = '/Users/ckgathi//Dropbox/mescelleneus/LANDMARKS/all_landmarks/landmarks5.csv'
f = open(name, 'r')
lines = f.readlines()
landmarks = []
from edc.map.classes import site_mappers
mapper = site_mappers.get_registry('mmandunyane')()
for line in lines:
    line = line.strip()
    line = line.split(',')
    if len(line) < 4:
        mark = line[0]
        lat = float(line[-3])
        lon = float(line[-2])
        dist = mapper.gps_distance_between_points(lat, lon)
        if dist < 11.5:
            landmarks.append([mark, lat, lon])
            print [mark, lat, lon]
    elif len(line) >= 4:
        if line[-1] == '1':
            mark = str(line[0])
        else:
            mark = str(line[0]) + ' ' + str(line[1])
        lat = float(line[-3])
        lon = float(line[-2])
        dist = mapper.gps_distance_between_points(lat, lon)
        if dist < 11.5:
            landmarks.append([mark, lat, lon])
            print [mark, lat, lon]
