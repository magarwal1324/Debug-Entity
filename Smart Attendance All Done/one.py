import Admin_Area_File
import Dashboard
import todays_attendance
import previous_attendance
import current_attendance
import account_settings
import add_student
import update_student
import monthly_view
import delete_teacher
import student_details
import delete_student

# delete_student.delete_student_main()

# student_details.student_details_main()

# delete_teacher.Delete_Teacher_Main()

# monthly_view.current_monthly_view_main()

# update_student.update_student_main()

# add_student.add_student_main()

# current_attendance.Current_Attendance_Main("Absent")

Dashboard.Dashboard_Main()

# Admin_Area_File.Admin_Area_Main() 

# todays_attendance.Todays_Attendance_Main()

# previous_attendance.Previous_Attendance_Main()

# account_settings.Account_Settings_Main()

# from tkinter import filedialog
# import pandas as pd
# from collections import defaultdict

# file = filedialog.asksaveasfilename(title="Select file","nameOfFile.xlsx",filetypes=[("Excel file", "*.xlsx")])
# if file:
#     ids=tree.get_children()
#     dict = defaultdict(list)
#     for id in ids:
#         date=dt.datetime.strptime(tree.set(id, "#13"), '%Y-%m-%d %H:%M:%S')
#         dateChosed=dt.datetime.strptime(monthToExport.get(), "%B-%Y")
#         if (date.year == dateChosed.year) and (date.month == dateChosed.month):
#             dict["1"].append(tree.item(id)["text"])
#             dict["2"].append(tree.item(id)["values"][0])

#     dict = pd.DataFrame.from_dict(dict)
#     try:
#         dict.to_excel(file, engine='xlsxwriter',index= False)
#     except:
#         print("Close the file than retry")
# else:
#     print("You did not save the file")

# from tkinter import filedialog
# import pandas as pd
# from collections import defaultdict

# file = filedialog.asksaveasfilename(title="Select file","nameOfFile.xlsx",filetypes[("Excel file", "*.xlsx")])
# if file:
#     ids=tree.get_children()
#     dict = defaultdict(list)
#     for id in ids:
#         date=dt.datetime.strptime(tree.set(id, "#13"), '%Y-%m-%d %H:%M:%S')
#         dateChosed=dt.datetime.strptime(monthToExport.get(), "%B-%Y")
#         if (date.year == dateChosed.year) and (date.month == dateChosed.month):
#             dict["1"].append(tree.item(id)["text"])
#             dict["2"].append(tree.item(id)["values"][0])

#     dict = pd.DataFrame.from_dict(dict)
#     try:
#        dict.to_excel(file, engine='xlsxwriter',index= False)
#     except:
#        print("Close the file than retry")
# else:
#     print("You did not save the file")