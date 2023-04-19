employees = []                                                  #if I declare my list outside of the file read, I can keep using it after the file has closed

with open("hr_system.txt") as hr_file:
    for line in hr_file: 
        employee = line.strip().split(' ')                      #store the list from the line into a new variable
        employees.append(employee)                              #append that list to my big list declared earlier

for employee in employees:
    name = employee[0]                                          #employees name is in the first spot
    job_id = employee[1]                                        #employee ID is in the second spot
    job_title = employee[2]                                     #employee job title is in the third spot
    wage = float(employee[3])                                   #employee wage is in the fourth spot
    if job_title.lower() == 'engineer':
        monthly_wage = (wage / 24) + 1000                       #if title is engineer, wage bonus of $1000
    else:
        monthly_wage = wage / 24
    
    print(f'{name} (ID: {job_id}), {job_title} - ${monthly_wage:.2f}')