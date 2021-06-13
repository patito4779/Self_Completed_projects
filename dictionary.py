# This project involves collecting a list of information of students in a particular department of a university and then manipulating the #
# data to get some particular individuals of intesrests, say a list of students above a certain age group


# To execute this project, we should first create a python dictionary of students

student1 = {
    "FirstName" : "Lucky",
    "OtherNames" : "Chinonso",
    "Sex" : "Male",
    "Current_Semester" : 4,
    "Country_of_origin" : "Nigeria",
    "Age" : 32,
    "Major" : "Physics",
    "Religion" : "Christian"

}

student2 = {
    "FirstName" : "Patrick",
    "OtherNames" : "Edward",
    "Sex" : "Male",
    "Current_Semester" : 4,
    "Country_of_origin" : "Nigeria",
    "Age" : 30,
    "Major" : "Physics",
    "Religion" : "Christian"

}
student3 = {
    "FirstName" : "James",
    "OtherNames" : "Bond",
    "Sex" : "Male",
    "Current_Semester" : 2,
    "Country_of_origin" : "India",
    "Age" : 28,
    "Major" : "Engineering",
    "Religion" : "Muslim"

}
student4 = {
    "FirstName" : "Kamasunya",
    "OtherNames" : "Panda",
    "Sex" : "Male",
    "Current_Semester" : 6,
    "Country_of_origin" : "Bangladesh",
    "Age" : 34,
    "Major" : "Engineering",
    "Religion" : "Christian"

}

student5 = {
    "FirstName" : "Mike",
    "OtherNames" : "Mavrec",
    "Sex" : "Male",
    "Current_Semester" : 2,
    "Country_of_origin" : "Germany",
    "Age" : 31,
    "Major" : "Mathematics",
    "Religion" : "Atheist"

}
student5 = {
    "FirstName" : "Anja",
    "OtherNames" : "Schmidt",
    "Sex" : "Female",
    "Current_Semester" : 6,
    "Country_of_origin" : "Germany",
    "Age" : 25,
    "Major" : "Polymers",
    "Religion" : "Christian"

}



ICAMS = {
    "student1" : student1,
    "student2" : student2,
    "student3" : student3,
    "student4" : student4,
    "student5" : student5,
    
}

print("\n")



# we want to get those students who are above the age of 30, and are not from Germany
for students in ICAMS.values():
    if (students["Age"] < 30 or students["Country_of_origin"] == "Germany"):
        students.clear()

        print("Find the list of required students below: ")
        
        print(ICAMS)