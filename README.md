
# BackpackServer
Un simple projet avec Python et Flask pour fournir une API rest en python. Verions de python utilisee 3.11 (`https://www.python.org/downloads/release/python-3112/`).

voici quelques elements requis pour installer l'application serveur :

## Base de donnees
Dans mysql Creer la schema `Backpack`, puis jouer le script `script01.sql`. Cela va creer la table `Inventory` et quelque lignes.

## Connexion a la base de donees
Pour editer la connexion avec la base de donnees, editer la fonction `getDb`.

## Packages a installer:
Ouvrir le termninal powershell et se placer dans le dossier `BackpackServer`

### mysql-connector-python
Connecteur pour la base de donnees Mysql.
Lancer la commande a partir du terminal powershell `pip install mysql-connector-python`

### Flask
Serveur web pour notre api.
Lancer la commande a partir du terminal powershell `pip install Flask`

### Flask-cors
Gestionnaires des permssion cors pour Flask
Lancer la commande a partir du terminal powershell `pip install -U flask-cors`

## Lancer le serveur 
Une fois ces elements installes, vous devriez etre capable de lancer le serveur avec la commande a partir du terminal powershell : `python app.py`. Un messae de la forme suivante devrais s'afficher dans le console :

> Collecting flask-cors
>  Using cached Flask_Cors-3.0.10-py2.py3-none-any.whl (14 kB)
> Requirement already satisfied: Flask>=0.9 in c:\python311\lib\site-packages (from flask-cors) (2.2.3)
>  * Running on http://127.0.0.1:8000
>  * Running on http://192.168.0.36:8000
> Press CTRL+C to quit
>  * Restarting with stat
>  * Debugger is active!
>  * Debugger PIN: 853-972-815





### Pour tester
Ouvrir un navigateur et aller sur la page : `http://127.0.0.1:8000/`. Un message `Hello, World!` devrais s'afficher.
De plus la page `http://127.0.0.1:8000/api/InventoryItems`  devrais afficher la liste des elements de la table Inventory.



# BackpackClient
Une simple application Angular qui permet d'afficher les donnees du serveur.

## Lancer l'application
Lancer l'application sever (ci dessus) puis dans un autre terminal de commande, se placer de le repertoire BackpackClient et lancer la commande `ng serve`
