import pandas as pd
data={
    "Student Name":["Rahul","Raj","Rohan","Arjun","Priya"],
    "Roll Number" :[1,3,5,8,6],
    "Marks":[99,65,78,82,52],
    "Attandamce":[90,95,91,87,98]

}
df=pd.DataFrame(data)

def grade(mark):
    if mark>=90:
        return "A"
    elif mark>=80:
        return "B"
    elif mark>=70:
        return "C"
    elif mark>=60:
        return "D"
    else:
        return "F"
df["Grade"]=df["Marks"].apply(grade)
print(df)   
