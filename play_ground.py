plots = Plot.objects.filter(plot_identifier__in=['300099-08', '300104-02'])
house = Household.objects.filter(replaced_by__in=['300099-08', '300104-02'])




"""Where to try code"""
from bhp066_project.bhp066.apps.bcpp_household.models import Plot, Household
# all 20% and 5% plots
plots = Plot.objects.filter(selected__in=[1, 2], community='shoshong')
replacement_plots_dict = {}
replaced_plots_ids = []
plot_replacing_plots_ids = []
for p in plots:
    if p.replaced_by:
        replacement_plots_dict[p.plot_identifier] = p.replaced_by
        replaced_plots_ids.append(p.plot_identifier)
        plot_replacing_plots_ids.append(p.replaced_by)
households = Household.objects.filter(plot__in=plots)
h_ids = []
for h in households:
    h_ids.append(h.household_identifier)
p_ids = []
for p in plots:
    p_ids.append(p.plot_identifier)
pp3 = h_ids + p_ids
replacement_households_dict = {}
replaced_households_ids = []
plot_replacing_households = []
for h in households:
    if h.replaced_by:
        replacement_households_dict[h.household_identifier] = h.replaced_by
        replaced_households_ids.append(h.household_identifier)
        plot_replacing_households.append(h.replaced_by)
pp1 = Plot.objects.filter(replaces__in=h_ids)
pp2 = Plot.objects.filter(replaces__in=p_ids)
plot_rr = []
for p in pp1:
    plot_rr.append(p.plot_identifier)
for p in pp2:
    plot_rr.append(p.plot_identifier)
plot_used_twice = []
plot_re = plot_replacing_households + plot_replacing_plots_ids
def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    seen_twice = set( x for x in seq if x in seen or seen_add(x) )
    return list( seen_twice )
list_duplicates(plot_re)
list_duplicates(plot_rr)


mixed = ['250885-08', '250868-02', '250951-08', '250861-06', '253006-06', '250870-04', '250556-09', '250887-10']
plot_mix = Plot.objects.filter(plot_identifier__in=mixed)
house_mix = Household.objects.filter(household_identifier__in=mixed)
for p in plot_mix:
    print p.replaced_by, p.plot_identifier, p.replaces
for h in house_mix:
    print h.replaced_by, h.household_identifier
h = Household.objects.filter(replaced_by=p8.plot_identifier)
p = Plot.objects.filter(replaced_by=p8.plot_identifier)
hl = Household.objects.filter(plot=p8)
h = hl[0]

s1, s2, s3 = Survey.objects.all()
hs = HouseholdStructure.objects.get(survey=s1, household=h)
members = HouseholdMember.objects.filter(household_structure=hs)





    


c = SubjectConsent.objects.filter(community='shoshong')
households = []
for j in c:
    if j.household_member.household_structure.household.plot.community == 'shoshong':
        households.append(j.household_member.household_structure.household.household_identifier)
        if j.household_member.household_structure.household.replaced_by:
            print j.household_member.household_structure.household.household_identifier
plots = []
for j in c:
    if j.household_member.household_structure.household.plot.community == 'shoshong':
        plots.append(j.household_member.household_structure.household.plot.plot_identifier)
plots = list(set(plots))

for p in plots:
    plot = Plot.objects.get(plot_identifier=p)
    if p.replaced_by:
        print "plot", plot
    if plot.htc:
        print "htc", plot
    