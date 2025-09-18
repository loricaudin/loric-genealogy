# Loric Genealogy
Cette application web permet de visualiser et modifier un arbre généalogique.
L'arbre généalogique de la propre famille n'est pas accessible au public (seule la famille peut la visualiser),
seule une version prototype peut être visible du public (avec des informations bidons).

Technologies utilisées : Python, Django

## Démarrer le projet en local :

Créer un fichier .env et copier-coller le contenu suivant :
```env
ENV=dev
SECRET_KEY=choisirunecledesecuritetreslongue
```

### Sur Linux
Exécuter le projet dans un environnement virtuel Python :
``` bash
python3 -m venv venv
```
Activer le venv :
```bash
source venv/bin/activate
```

Installer les dépendances :
```bash
pip install -r requirements.txt
```
Démarrer le projet :
```bash
python3 manage.py runserver
```

### Sur Windows
Exécuter le projet dans un environnement virtuel Python :
```bash
python -m venv venv
```
Activer le venv :
```bash
venv\Scripts\activate
```

Installer les dépendances :
```bash
pip install -r requirements.txt
```
Démarrer le projet :
```bash
python manage.py runserver
```

## Insérer un jeu de données :
Taper la commande :
```bash
python manage.py makemigrations arbre_genealogique
python manage.py migrate
```

Créer un premier utilisateur :
```
python manage.py createsuperuser
```