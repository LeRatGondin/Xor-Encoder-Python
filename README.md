# Xor-Encoder-Python
### Langage utilisé 
Python 3.9.4
## Systeme de chiffrage
Le systeme de chiffrage est le XOR qui a pour principe d'utiliser la fonction binaire OU exclusif ou plus souvent appellée ["XOR"](https://fr.wikipedia.org/wiki/Fonction_OU_exclusif).

# Comment ça marche ?
## Pour le chiffrage
Le script converti le message en binaire et il converti la clé en [sha256](https://fr.wikipedia.org/wiki/SHA-2) , puis en binaire ensuite il utilise la fonction XOR 
pour creer le code chiffré 
## Pour le dechiffrage
Le script converti la clé en sha256 , et il refait le chifrement XOR mais dans l'autre sens pour pouvoir le decoder
### Screenshot
![Alt text](https://www.zupimages.net/up/21/16/i2qp.png) 
