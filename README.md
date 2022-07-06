# esercizi_1
## Qualche esercizio per iniziare a conoscere Python3

Benvenuto!

In questa repository sono raccolti degli esercizi per inizare a destreggiarti nel mondo di Python3.

Ogni file python (con estensione `.py`) contiene due sezioni: nella prima ti verr&agrave; richiesto di implementare codice, nella seconda ci saranno una serie di test che verificheranno la tua implementazione.

Gli esercizi sono numerati in ordine di complessit&agrave;.

---

## Checkout

Innanzitutto, procedi con il download di questo codice.

Per semplicit&agrave; puoi procedere scaricando il file `.zip` che GitHub ti fornisce. Puoi scaricarlo cliccando su `Code` (il tasto verde in alto a destra in questa pagina) e poi su `Download ZIP` nel men&ugrave; a tendina che ti sar&agrave;  comparso.

Decomprimi la cartella e visualizzala col tuo gestore di file (Finder o Esplora Risorse). Dovresti avere davanti praticamente la stessa struttura dei file che vedi su questa pagina.

---
## IDE

Per sviluppare, l'ideale sarebbe quella di usare uno strumento che ti aiuti nello sviluppo del codice. Un Integrated Development Environment &egrave; ci&ograve; che fa al caso tuo.

Consiglio [Visual Studio Code](https://code.visualstudio.com/download).

Installalo e aprilo. Dopodich&egrave; vai su `File` -> `Apri cartella` e seleziona la cartella decompressa nel punto precedente.

A questo punto dovresti avere la possibilit&agrave; sfogliare i file di questo progetto, incluso il file che stai attualmente leggendo!

---
## Python3

Prima di continuare, assicuriamoci di aver installato `python3` nel tuo sistema: In Visual Studio Code, nell'angolo in basso a destra, c'&egrave; un quadrato contentente un simbolo del maggiore (`>`): Cliccaci sopra: l'IDE aprir&agrave; una finestra a parte: Hai appena aperto un terminale: useremo questo strumento per eseguire i file python che completerai.

Grazie al terminale sar&agrave; possibile eseguire sia file specifici, ma anche dialogare direttamente con python3!

Nel terminale, scrivi `python3` e premi invio. Qualcosa del genere dovrebbe essere stampata:

```python
Python 3.8.9 (default, Apr 13 2022, 08:48:07) 
[Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Questo &egrave; l'interprete di Python! Significa che sei pronto per sviluppare codice!

Terminamo l'interprete scrivendo `exit()` e premendo invio all'interno della finestra del terminale che hai aperto. Dovrebbe ricomparire la stessa scritta di quando hai aperto il terminale per la prima volta.

---
## Come svolgere gli esercizi

In alcuni esercizi, dovrai decommentare il codice.

Il codice commentato viene preceduto da un cancelletto (`#`).

Basta eliminare il cancelletto (o i pi&ugrave; cancelletti sulla stessa linea) per decommentare il codice.

```python
# Questo è un commento
# Un altro commento

# print(1+1)
# ^ Codice commentato

print(3 + 2)
# ^ Codice non commentato

#### Commento con più cancelletti

## A Python non importa quanti ne metti...

ciao
# ^ Questo codice non può essere interpretato da python correttamente.

```

Non scrivere codice dopo la scritta:
```python3
# === Non modificare dopo questo punto ===
```
e non prima di:
```python3
# === Modifica dopo questo punto ===
```


Una volta completato l'esercizio, apri il terminale se non l'hai aperto, e scrivi:

```bash
python3 ex1.py
```



In questo caso stiamo eseguendo il codice contentuto dentro il file chiamato `ex1.py`.

La stessa logica dovrà essere applicata per gli esercizi successivi.

Premi invio per eseguire il codice.

Dopo poco tempo ti troverai in una di queste due situazioni: In caso di errore, un messaggio verrà riportato, simile al seguente:

```bash

Traceback (most recent call last):
  File ... in <module>
...
```

In questo caso ci sarà qualche errore nel codice.

Generalmente cercare su Google l'errore riportato porta alla risoluzione dello stesso. *Generalmente*.

Con il passare del tempo interpreterai i messaggi di errore con più confidenza.

Se tutto dovesse essere andato bene, nessun messaggio verrà riportato, e dovresti essere in una situazione simile:
```bash
➜  esercizi_1 git:(main) ✗ python3 ex1.py 
➜  esercizi_1 git:(main) ✗ 
```


Sei pronto! Apri il primo esercizio (`ex1.py`) e buona fortuna 🚀