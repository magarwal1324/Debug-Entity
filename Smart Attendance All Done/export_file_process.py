# import module
from tkinter import * 
from tkinter.filedialog import asksaveasfile
import csv

# Save attendance sheet in excel format
def save(heading,body,exported_file_name):
    export_status=""
    file_location=""
    if len(heading)==len(body[0]):
        files = [('Excel Document', '*.csv')]
        file_location_path = asksaveasfile(initialdir=":/downloads", initialfile=exported_file_name, title = "Select a file", filetypes=files, defaultextension =files)
        
        if file_location_path != None:
        
            file_location=file_location_path.name
            file_location_path.close()
            with open(file_location,'w', newline='') as f:
                fieldnames = heading
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()

                for i in range(len(body)):
                    data={}
                    for j in range(len(heading)):
                        data[heading[j]]=body[i][j]

                    writer.writerow(data)

            export_status="done"
        else:
            export_status="not done"
            
    else:
        export_status="not data available"

    return export_status,file_location


