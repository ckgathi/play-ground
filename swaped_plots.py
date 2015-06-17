"""Set plot 1 coordinates to None"""
plot1 = Plot.objects.get(plot_identifier='300717-10')
lat = -21.25815335
lon = 27.48109696
plot1.gps_target_lat
plot1.gps_target_lon
plot1.gps_target_lat = None
plot1.gps_target_lon = None
# plot1.gps_lat = None
# plot1.gps_lon = None
# plot1.gps_degrees_s = None
# plot1.gps_minutes_s = None
# plot1.gps_degrees_e = None
# plot1.gps_minutes_e = None
plot1.save()
dec_s, min_s = divmod(float(lat) * 60, 60)
dec_s = int(dec_s)
dec_e, min_e = divmod(float(lon) * 60, 60)
dec_e =int(dec_e)


plot2 = Plot.objects.get(plot_identifier='300474-09')
lat1 = -21.25816197
lon1 = 27.48126203
plot2.gps_target_lat = None
plot2.gps_target_lon = None
plot2.gps_lat = None
plot2.gps_lon = None
plot2.gps_degrees_s = None
plot2.gps_minutes_s = None
plot2.gps_degrees_e = None
plot2.gps_minutes_e = None
plot2.save()
dec_s1, min_s1 = divmod(float(lat1) * 60, 60)
dec_s1 = int(dec_s1)
dec_e1, min_e1 = divmod(float(lon1) * 60, 60)
dec_e1 =int(dec_e1)

plot1 = Plot.objects.get(plot_identifier='300717-10')
plot1.gps_target_lon = lon1
plot1.gps_target_lat = lat1
plot1.gps_degrees_s = dec_s1
plot1.gps_minutes_s = min_s1
plot1.gps_degrees_e = dec_e1
plot1.gps_minutes_e = min_e1
plot1.save()

plot2 = Plot.objects.get(plot_identifier='300474-09')
plot2.gps_target_lat = -21.25815335
plot2.gps_target_lon = 27.48109696
lat = -21.25815335
lon = 27.48109696
plot2.save()
plot2.gps_degrees_s = 21
plot2.gps_minutes_s = 15.489201
plot2.gps_degrees_e = 27
plot2.gps_minutes_e = 28.8658176
plot2.save()


from edc.map.classes import site_mappers
mapper = site_mappers.get_registry('tati_siding')()
dist = mapper.gps_distance_between_points(lat, lon)



lat1 = mapper.get_gps_lat(21, 15.972)
lon1 = mapper.get_gps_lon(27, 28.891)

