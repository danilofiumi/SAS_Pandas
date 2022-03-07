# SAS_Pandas
Questa repository contiene una serie di utilities per interagire con le tabelle proprietarie SAS (.sas7bdat) su Python sfruttando Pandas.

## libname
la funzione libname analogamente allo statement SAS, va a leggere tutti i file con estensione .sas7bdat nel path indicato, importandoli come dataframe pandas all'interno della sessione python. Viene mantenuta la stessa nomenclatura SAS, e l'encoding viene riadattato al formato in entrata.

uso --> libname("path\to\tables\")

## clear_libname
elimina tutti i dataframe dichiarati da un precedente chiamata di libname, liberando spazio in memoria e mantenendo ordine e pulizia in sessione.

uso --> clear_libname("path\to\tables\")

## export_libname
Questa utility importa in sessione tutti i .sas7bdat in un percorso come dataframe, ed esporta un unico file .xlsx contenente tanti fogli quante sono le tabelle lette nel punto precedente. La funzione ha 3 parametri in input:
 1) il path relativo alla cartella contenente le tabelle .sas7bdat
 2) il folder dove salvare l'excel di output
 3) il filename riferito al file di output 

uso --> export_libname("path\to\tables\","path\to\output\","out")
