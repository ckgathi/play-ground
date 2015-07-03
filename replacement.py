from apps.bcpp_household.helpers import ReplacementHelper
helper = ReplacementHelper()
survey = Survey.objects.all()[0]
house_structure = HouseholdStructure.objects.filter(survey=survey)
replacebles = []
for hs in house_structure:
    helper.household_structure = hs
    if helper.replaceable_household:
        replacebles.append(hs.household.household_identifier)




options = dict(is_dispatched=True, item_app_label='bcpp_household', item_model_name='Plot')
options.update(producer__settings_key='bcpp011-bhp066')
from apps.bcpp_household.helpers import ReplacementHelper
helper = ReplacementHelper()
replacebles = []
survey = Survey.objects.all()[0]
for dispatch_item_register in DispatchItemRegister.objects.using('default').filter(**options):
    for household_structure in HouseholdStructure.objects.using('default').filter(survey__survey_name=survey.survey_name, household__replaced_by__isnull=True, household__plot__pk=dispatch_item_register.item_pk):
        helper.household_structure = household_structure
        if helper.replaceable_household:
            replacebles.append(household_structure.household.household_identifier)






        
"""For plot"""
from apps.bcpp_household.constants import (RESIDENTIAL_HABITABLE, NON_RESIDENTIAL,
                         RESIDENTIAL_NOT_HABITABLE, FIVE_PERCENT,
                         ELIGIBLE_REPRESENTATIVE_ABSENT, VISIT_ATTEMPTS)
plots = Plot.objects.filter(plot_identifier__in=['300099-08', '300104-02'])
replacebles = []
for p in plots:
    if not p.replaced_by and not p.bhs and (p.selected == FIVE_PERCENT):
        if p.status in [NON_RESIDENTIAL, RESIDENTIAL_NOT_HABITABLE] and p.replaces:
            print True
