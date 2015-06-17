h_ids = ['1431941-05', '1336911-04']
house = Household.objects.filter(household_identifier__in=h_ids)
h1, h2 = house

