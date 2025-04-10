#Definizione variabili
nome_programma = "Calcoliamo il perimetro insieme"
lista_figure = ["quadrato", "cerchio", "rettangolo"]

#Inizio programma

print("Ciao, benvenuto in" + ' ' + nome_programma)
print("Oggi calcoleremo insime il perimetro. Iniziamo!")
print ("Scegli una figura geometrica: ", lista_figure)

figura_scelta = input()

if figura_scelta == "quadrato":
    print("Metti  il valore del lato:")
    numero_scelto = int(input())
    perimetro_quadrato = numero_scelto*4
    print ('Il perimetro del quadrato è:' , perimetro_quadrato)
elif figura_scelta == "cerchio":
    print("Metti il valore del raggio")
    numero_scelto = int(input())
    circonferenza_cerchio = (numero_scelto*2)*3.14
    print('La circonferenza  del cerchio è:', circonferenza_cerchio)
elif figura_scelta == "rettangolo":
    print("Metti il numero per la base qui: ")
    numero_base = int(input())
    print("Metti il numero per l'altezza qui:")
    numero_altezza = int(input())
    perimetro_rettangolo = (numero_base*2) + (numero_altezza*2)
    print ('Il perimetro del rettangolo è:' , perimetro_rettangolo)
else:
    print ("Abbiamo terminato. Riavvia il programma per selezionare un'opzione corretta")


print ("Alla prossima")