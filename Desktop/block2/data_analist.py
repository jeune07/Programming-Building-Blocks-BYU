year_of_interest = input("Enter the year of interest: ")
min_life = 100
min_life_expectancy_country = None
max_life = 0
max_Life_expectancy_country = None
age_list=[]
sum_age=0
average_age=None


with open("C:/Users/Mon Pepe/Desktop/life-expectancy.csv") as countries:
    for country in countries:
        each_country = country.split(',')
        if each_country[2] == year_of_interest:
            each_age=float(each_country[3])            
            age_list.append(each_age)

            for i in age_list:
                sum_age= sum_age +i
            
            average_age =sum_age/len(age_list)

            if float(each_country[3]) > max_life:
                max_life = float(each_country[3])
                max_life_expectancy_country = each_country[0]
            if float(each_country[3]) < min_life:
                min_life = float(each_country[3])
                min_life_expectancy_country = each_country[0]
            

if max_life_expectancy_country:
    print(f"The country with the max life expectancy was {max_life_expectancy_country} with {max_life} years in {year_of_interest}")
else:
    print(f"No countries were found with data for the year {year_of_interest}")

if min_life_expectancy_country:
    print(f"The country with the min life expectancy was {min_life_expectancy_country} with {min_life} years in {year_of_interest}")
else:
    print(f"No countries were found with data for the year {year_of_interest}")

print(f"The average life expectancy across all countries was {average_age}")
