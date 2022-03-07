def export_libname(path,folder,filename):
    import pandas as pd
    import os

    libname(path)

    sep = '.'

    la_table = os.listdir(path)

    dataset=[]
    for table in la_table:

        if table.partition(sep)[2] == 'sas7bdat':
            dataset.append(table.split(sep, 1)[0])

    Excelwriter = pd.ExcelWriter(folder+"/"+filename+".xlsx",engine="xlsxwriter")

    
    for i, df in enumerate (dataset):
        print(type(eval(df)))
        try:
            eval(df).to_excel(Excelwriter, sheet_name=str(dataset[i]),index=False)
        except AttributeError:
            pass

    Excelwriter.save()
