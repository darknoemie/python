# Les exemples du cours Python



## 01.py : commentaire et commande print

## 02.py : Utiliser les chiffes

## 03.py : Les caractères spéciaux

## 04.py : Triple quotes : Les chaines sur plusieurs lignes
 
## 05.py : Multiplicateur de chaines de caracteres

## 06.py : Concatenation de string

## 07.py : Les chaines de caracteres

## 08.py : Les listes

## 09.py : Les  instructions de controle de flux

## 10.py : Les fonctions: le crible d'Eratosthènes

## 11.py : Les fonctions : Arguments nommes

## 12.py : Les fonctions : Parametres multiples

## 13.py : Les fonctions : fonction lambda

## 14.py : Les listes: l'operateur in

## 15.py : Les ensembles

## 16.py : Formatages des donnees

## 17.py : Les fichiers

## 18.py : 

## 19.py : 

## 20.py : Les variables d'environnement

## 21.py : Création d'un fichier Excel

## 22.py : Modification d'un fichier Excel


## crible.py : Crible d'Eratosthène

## matplot-01.py : Dessin d'une sinusoïde avec matplot

## matplot-02.py : Afficher les valeurs d'une liste dans un graphique

## tk-01.py : Premier porgramme TK. Affiche un bouton et affiche un message dans la console à chaque clic.

## TP1-tk.py : 

### Etape 1 
Réaliser un formulaire de saisie lancement d'un test
Il faut saisir le n° de test
La date se remplit automatiquement

## TP2-tk.py : 
TP: TK

### Etape 1 
Réaliser un formulaire de saisie lancement d'un test
Il faut saisir le n° de test
La date se remplit automatiquement

Générer de manière aléatoire les valeurs du test.
Sauvegarder les valeurs dans un fichier au format CSV

### Etape 2 
Enregistrer les valeurs dans une base de données.

Créer les tables pour stocker les valeurs
- le nom du test
- la date du test 
- les valeurs

La table des tests
create sequence seq_test
start with 1
increment 1;

create table test (
id int8 primary key default nextval('seq_test'),
nom varchar null,
datetest timestamp null
);

La table des valeurs
create sequence seq_valeur
start with 1
increment 1;

create table valeur (
id int8 primary key default nextval('seq_valeur'),
idTest int8,
valeur float8 null
);

### Etape 3 

Afficher les valeurs sur un graphique







## Le dossier poo 
Le dossier poo contient les exemples liée à la partie POO en Python.
Les classes du dossier
*  Personne et Main 
*  Figure
*  Cercle
*  Dessin


