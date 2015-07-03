# Members from the first plot
plot1 = Plot.objects.get(plot_identifier='')
household1 = Household.objects.get(household_identifier='3208971-07')
survey = Survey.objects.get(survey_slug='bcpp-year-1')
household_structure1 = HouseholdStructure.objects.get(survey=survey, household=household1)
members1 = HouseholdMember.objects.filter(household_structure=household_structure1)


# Members from the second plot
plot2 = Plot.objects.get(plot_identifier='321160-04')
household2 = Household.objects.get(household_identifier='3211601-08')
household_structure2 = HouseholdStructure.objects.get(survey=survey, household=household2)
members2 = HouseholdMember.objects.filter(household_structure=household_structure2)


representative_eligibility = RepresentativeEligibility.objects.get(household_structure=household_structure2)
representative_eligibility.household_structure = household_structure2
representative_eligibility.save()

h_head_eligibility = HouseholdHeadEligibility.objects.get(household_structure=household_structure2)
h_head_eligibility.household_structure = household_structure2
h_head_eligibility.save()


for member in members1:
    member.household_structure = household_structure2
    member.save()


enrolled = household_structure2.enrolled
enrolled_household_member = household_structure2.enrolled_household_member
enrolled_datetime = household_structure2.enrolled_datetime
enumerated = household_structure2.enumerated
enumeration_attempts = household_structure2.enumeration_attempts
refused_enumeration = household_structure2.refused_enumeration
failed_enumeration_attempts = household_structure2.failed_enumeration_attempts
failed_enumeration = household_structure2.failed_enumeration
no_informant = household_structure2.no_informant


# Change household sturcture values
household_structure2.enrolled = household_structure1.enrolled
household_structure2.enrolled_household_member = household_structure1.enrolled_household_member
household_structure2.enrolled_datetime = household_structure1.enrolled_datetime
household_structure2.enumerated = household_structure1.enumerated
household_structure2.enumeration_attempts = household_structure1.enumeration_attempts
household_structure2.refused_enumeration = household_structure1.refused_enumeration
household_structure2.failed_enumeration_attempts = household_structure1.failed_enumeration_attempts
household_structure2.failed_enumeration = household_structure1.failed_enumeration
household_structure2.no_informant = household_structure1.no_informant
household_structure2.save()

# Change household and plot values
consents = SubjectConsent.objects.filter(household_member__in=members2)
if consents:
    household2.enrolled = household_structure2.enrolled
    household2.enrolled_datetime = household_structure2.enrolled_datetime
    plot2.enrolled_datetime = household_structure2.enrolled_datetime
    plot2.bhs
    plot2.save()
    household2.save()


"""********************************************************************************************"""


for member in members2:
    member.household_structure = household_structure1
    member.save()

consents = SubjectConsent.objects.filter(household_member__in=members2)
if consents:
    household2.enrolled = household_structure1.enrolled
    household2.enrolled_datetime = household_structure1.enrolled_datetime
    plot2.enrolled_datetime
    plot2.bhs
    plot2.save()
    household2.save()

    household_structure1.enrolled = enrolled
    household_structure1.enrolled_household_member = enrolled_household_member
    household_structure1.enrolled_datetime = enrolled_datetime
    household_structure1.enumerated = enumerated
    household_structure1.enumeration_attempts = enumeration_attempts
    household_structure1.refused_enumeration = refused_enumeration
    household_structure1.failed_enumeration_attempts = failed_enumeration_attempts
    household_structure1.failed_enumeration = failed_enumeration
    household_structure1.no_informant = no_informant
    household_structure1.save()
else:

household1 = Household.objects.get(household_identifier='3208971-07')
survey = Survey.objects.get(survey_slug='bcpp-year-1')
household_structure1 = HouseholdStructure.objects.get(survey=survey, household=household1)
members1 = HouseholdMember.objects.filter(household_structure=household_structure1)

plot1 = household1.plot
household1.enrolled = household_structure1.enrolled
household1.enrolled_datetime = household_structure1.enrolled_datetime
plot1.enrolled_datetime = household_structure1.enrolled_datetime
plot1.bhs=False
plot1.save()
household1.save()
