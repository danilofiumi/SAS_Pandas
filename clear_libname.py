def clear_libname(path):
    import pandas as pd
    import os

    la_table=os.listdir(path)
    sep = '.'

    for table in la_table:
        if table.partition(sep)[2] == 'sas7bdat':
            del globals()[table.split(sep, 1)[0]]
