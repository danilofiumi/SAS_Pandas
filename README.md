# SAS_Pandas
Questa repository contiene una serie di utilities per interagire con le tabelle sas7bdat proprietarie SAS su Python sfruttando Pandas

## libname
la funzione libname analogamente allo statement SAS, va a leggere tutti i file con estensione .sas7bdat, importandoli come dataframe pandas all'interno della sessione python, con nomenclatura SAS e encoding riadattato al formato in entrata.
(es: libname("path\to\tables\"))

## clear_libname
Al contrario di libname, clear_libname elimina tutti i dataframe dichiarati in sessione sulla base della nomenclatura SAS. 
(es: clear_libname("path\to\tables\"))

##export_libname
Questa utility importa in sessione tutti i .sas7bdat in un percorso come dataframe, ed esporta un unico file .xlsx contenente tanti fogli quante sono le tabelle lette nel punto precedente. La funzione ha 3 parametri in input:
 1) il path relativo alla cartella contenente le tabelle .sas7bdat
 2) il folder dove salvare l'excel di output
 3) il filename riferito al file di output
