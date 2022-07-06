# In questo esercizio iniziamo a scoprire i tipi standard di python.
# Un tipo è un modo di distinguere il potenziale contenuto di una variabile.
# Python offre di base dei tipi, appunto detti "standard". 
# Questi saranno sempre utilizzabili durante tutta l'esecuzione di un processo di python,
# o in qualunque tempo durante la scrittura del codice.
# Non tutti i tipi standard verranno trattati.

# La documentazione riguardo i tipi standard è qui: https://docs.python.org/3/library/stdtypes.html

# I tipi sono strettamente collegati ad una variabile.
# Per semplicità assumeremo che una variabile ha un solo tipo.
# Per dichiarare una variabile devi assegnare un nome ed un valore
# a questa. Il tipo verrà automaticamente riconosciuto
# in base al valore che assegni alla variabile.

# La creazione di una variabile avviene con la seguente sintassi:
# [NOME DELLA VARIABILE] = [VALORE DELLA VARIABILE]

# Assegnando, ad esempio, un valore intero ad una variabile,
# farà in modo che quella variabile sarà dello stesso tipo
# del valore assegnato.

# Per questo esercizio assicurati che, prima della dichiarazione
# delle variabili, non ci siano spazi, nè <TAB>: python li interpreterà
# in un modo che per ora non ci serve.

# === Modifica dopo questo punto ===

# Crea una variabile di tipo booleano.
# Un tipo booleano rappresenta due stati: vero e falso.
# L'origine di questi stati deriva dai bit, una "binary digit" (ridotto "bi-t").
# Un bit, come le variabili booleane, può avere due stati: 1 e 0 (acceso e spento).

# variabile_booleana = 
# ^ Decommenta e implementa

# Crea una variabile di tipo intero.
# I valori interi sono utilizzati per rappresentare quantità indivisibili.
# Ad esempio, il numero di petali di un fiore, i granelli di sabbia nel mondo
# o le volte che hai fatto un incidente in moto.

# variabile_intera = ...
# ^ Decommenta e implementa

# Crea una variabile di tipo stringa.
# Una stringa è una sequenza di caratteri.
# I caratteri sono dei simboli che vengono usati
# per comunicare, ad esempio.
# Il testo che stai leggendo ora è composto da caratteri.
# Tra i caratteri sono inclusi anche numeri, spazi, trattini,
# praticamente tutto ciò che è rappresentabile su uno schermo.
# Le stringhe sono caratterizzate dall'essere contenute da apici (') o virgolette (")
# L'importante è delimitare la stessa stringa o solo con apici,
# o solo con virgolette.

# variabile_stringa = ...
# ^ Decommenta e implementa

# Crea una variabile di tipo float.

# Un float, similmente ad un intero, indica un valore numerico,
# ma questa volta con più precisione, usando anche i decimali.
# La virgola che comunemente usiamo viene rimpiazzata dal punto in python.

# variabile_float = ...
# ^ Decommenta e implementa

# Crea una variabile di tipo lista.

# Una lista è un insieme ordinato di valori.
# In una lista è possibile inserire valori di tipo diverso,
# ma generalmente è buona cosa evitare di inserire valori
# diversi nella stessa lista.
# Una lista è caratterizzata dall'essere delimitata dalle parentesi quadre ('[' e ']', senza apici).
# In una lista è anche possibile aggiungere variabili precedentemente dichiarate.

# variabile_lista = ...
# ^ Decommenta e implementa

# Crea una variabile di tipo tupla.
# Una tupla è simile ad una lista, la maggiore differenza è che
# dopo aver assegnato i valori alla tupla, non è possibile aggiornarli.
# Le tuple sono delimitate da parentesi tonde.
# Anche nelle tuple possiamo inserire valori di tipo diverso.

# variabile_tupla = ...
# ^ Decommenta e implementa




# === Non modificare dopo questo punto ===

assert type(variabile_booleana) == bool
assert type(variabile_intera) == int
assert type(variabile_stringa) == str
assert type(variabile_float) == float
assert type(variabile_lista) == list
assert type(variabile_tupla) == tuple