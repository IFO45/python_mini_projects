def getapp():
    applications = {}
    numapp = int(input("Enter the number of applicants: "))
    for i in range(1, numapp + 1):
        print(f"\nEnter details for applicant {i}:")
        name = input("Name: ")
        age = int(input("Age: "))
        exp = int(input("Years of Experience: "))
        applications[i] = {"name": name, "age": age, "exp": exp}
    return applications

def sortapp(applications, criteria, order="asc"):
    reverse = True if order == "desc" else False
    application_list = list(applications.items())
    n = len(application_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if reverse:
                if application_list[j][1][criteria] < application_list[j + 1][1][criteria]:
                    application_list[j], application_list[j + 1] = application_list[j + 1], application_list[j]
            else:
                if application_list[j][1][criteria] > application_list[j + 1][1][criteria]:
                    application_list[j], application_list[j + 1] = application_list[j + 1], application_list[j]
                    
    return application_list

def sortprint(jobapp, criteria):
    if criteria in ['age', 'experience']:
        order = input("Enter sorting order ('asc' for ascending or 'desc' for descending): ").strip().lower()
        sorted_applications = sortapp(job_applications, criteria, order)
        print(f"\nSorted by {criteria.capitalize()} ({'Descending' if order == 'desc' else 'Ascending'}):")
        for app_id, details in sorted_applications:
            print(f"ID: {app_id}, Name: {details['name']}, Age: {details['age']}, Experience: {details['exp']} years")
    else:
        print("Invalid criteria. Please enter 'age' or 'experience'.")
        criteria = input("Enter the criteria for sorting (age/experience): ").strip().lower()
        sortprint(job_applications, criteria)

jobapp = getapp()
criteria = input("Enter the criteria for sorting ('age'/'experience'): ").strip().lower()
sortprint(jobapp, criteria)
