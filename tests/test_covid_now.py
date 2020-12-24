from unittest import TestCase
from covid_now.covid_now import csv_getter


class Test(TestCase):
    def test_csv_getter(self):
        URL = 'https://github.com/owid/covid-19-data/raw/master/public/data/latest/owid-covid-latest.csv'
        csv_header = "iso_code,continent,location,total_cases,new_cases,new_cases_smoothed,total_deaths,new_deaths,new_deaths_smoothed,total_cases_per_million,new_cases_per_million,new_cases_smoothed_per_million,total_deaths_per_million,new_deaths_per_million,new_deaths_smoothed_per_million,reproduction_rate,icu_patients,icu_patients_per_million,hosp_patients,hosp_patients_per_million,weekly_icu_admissions,weekly_icu_admissions_per_million,weekly_hosp_admissions,weekly_hosp_admissions_per_million,new_tests,total_tests,total_tests_per_thousand,new_tests_per_thousand,new_tests_smoothed,new_tests_smoothed_per_thousand,positive_rate,tests_per_case,tests_units,total_vaccinations,total_vaccinations_per_hundred,stringency_index,population,population_density,median_age,aged_65_older,aged_70_older,gdp_per_capita,extreme_poverty,cardiovasc_death_rate,diabetes_prevalence,female_smokers,male_smokers,handwashing_facilities,hospital_beds_per_thousand,life_expectancy,human_development_index"
        csv_end = "ZWE,Africa,Zimbabwe,12656.0,112.0,129.571,330.0,4.0,2.429,851.515,7.536,8.718,22.203,0.269,0.163,,,,,,,,,,1205.0,200096.0,13.463,0.081,1565.0,0.105,0.097,10.3,tests performed,,,69.44,14862927.0,42.729,19.6,2.822,1.882,1899.775,21.4,307.846,1.82,1.6,30.7,36.791,1.7,61.49,0.535"
        self.assertEqual(csv_getter(URL)[0], csv_header)
        self.assertEqual(csv_getter(URL)[192], csv_end)
