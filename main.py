import pandas

# new_dict ={new_key:new_value for item in list}
# new_dict ={new_key:new_value for (key, value) in dict.items() if test}

# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]

student_dict = {
    "student": ["angela", "james", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

# # Loop thru data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "angela":
        print(row.score)
