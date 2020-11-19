# Les différentes routes du projet 

## Endpoints API Route
En méthode GET uniquement

**A tester dans le navigateur ou sous POSTMAN**

> Endpoint par id (int)
`http://127.0.0.1:5000/api/books/<id>`
> exemple : http://127.0.0.1:5000/api/books/1

> Endpoint par title (string)
>`http://127.0.0.1:5000/api/books/<title>`
> exemple : http://127.0.0.1:5000/api/books/un%20titre

## Accès routes (parse fichier.json)

> Route books 'all'
`http://127.0.0.1:5000/books/json`
> exemple : http://127.0.0.1:5000/books/json

> Route book spécifique par (int)
`http://127.0.0.1:5000/books/json/<id>`
> exemple : http://127.0.0.1:5000/books/json/416

> Route book spécifique par titre (string)
`http://127.0.0.1:5000/books/json/<title>`
> exemple : http://127.0.0.1:5000/books/json/Coffeehouse

## TP Flask 

**Quickstart** 
Ecrire une application flask suivant le modele ci-dessus avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello DC"
* une route qui renvoie "hello name", ou name est une variable string 
	* on devra donc trouver "hello name" à la route (http:localhost:5000/ma_route/name) avec la possibilité de changer la variable name. 
* refaite la meme chose en ajoutant un template 

**Contexte**

Vous avez répondu à l'appel d'offre d'une mairie qui consiste à digitaliser la bibliothèque de la commune. Il faudra pour cela proposer un "catalogue" en ligne de leur ressources et donner la possibilité au utilisateur du site de faire des recherches de livre. On supposera que la bibliothèque nous met à disposition ces livres via un fichier `.json` ci-dessous. 
Vous devez donc construire une api (application flask) avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello my app"
* instancier une variable `book` dans votre aopplication tel que : 
```
book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
```
* faite une route `/api/books` avec une méthode `GET` qui retourne cette variable sous forme de json 
* faite une route qui retourne un book selon son `id` 
* faite une route qui retourne un book selon son titre 
* chager le fichier [books.json](https://drive.google.com/file/d/1UdRCm5d5UAPnfjGes_rHZl2kDQ9NNAsG/view?usp=sharing) et faite de même avec ce fichier
* **(bonus)** écrire un template pour le résultat de la recherche

