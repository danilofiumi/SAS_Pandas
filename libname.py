def libname(path):
    import pandas as pd
    import os

    la_table=os.listdir(path)
    sep = '.'

    for table in la_table:
        if table.partition(sep)[2]=='sas7bdat':
            globals()[table.split(sep, 1)[0]]=pd.read_sas(path+'/'+table,format = 'sas7bdat', encoding="ISO-8859-1")
