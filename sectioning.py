""" export sectioning"""

import csv
plots= Plot.objects.filter(selected=1)
section = []
for p in plots:
    section.append([p.plot_identifier, p.section, p.sub_section])
community = 'mathangwane_sectioning.csv'
f = open(community, 'wb')
writer = csv.writer(f)
writer.writerows(section)


""" import sectioning"""

community = '/Users/django/community_maps/mathangwane_sectioning.csv'
f = open(community, 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    line = line.split(',')
    p = Plot.objects.get(plot_identifier=line[0])
    p.section=line[1]
    p.sub_section=line[2]
    p.save()
