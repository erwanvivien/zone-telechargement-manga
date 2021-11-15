- [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/1200px-Flag_of_France.svg.png" height=12 width=20/> Français](#-zone-telechargement-extracteur-durl-pour-mangas)
- [<img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/1200px-Flag_of_the_United_Kingdom.svg.png" height=12 width=20/> English](#-zone-telechargement-url-extractor)

# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/1200px-Flag_of_France.svg.png" height=20 width=30/> Zone-telechargement extracteur d'url pour Mangas

- [Télécharger chromedriver](https://chromedriver.chromium.org/downloads)
- [Télécharger Geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.30.0)

## Comment l'utiliser

```bash
# installation
python3 -m pip install -r requirements.txt
```

```powershell
# powershell
./Run.ps1 # Va vous demandez toutes les informations nécessaires
```
```bash
# bash
./run.sh # Va vous demandez toutes les informations nécessaires
```

### Questions

- **Où trouver le cookie ?**

Ouvrir n'importe quel lien ZT/ZA, aller sur votre hébergeur de liens préféré (1fichier, par exemple). Aller jusqu'à la page où vous devez cliquer pour voir le lien.

À cette étape, vous faire F12 (ouvrir la console), vous allez dans l'onglet réseau / network puis vous cliquez sur le bouton pour afficher le lien, affichez toutes les requêtes et filtrez la requêtes content "link" dedans

Vous récupérez le cookie dans les headers (en-têtes) de la requête

- **Quels lien donner au script ?**

Donner le lien qui contient tous les sous liens (Episode 1 à X)

## Pourquoi l'utiliser ?

Récupérer les liens dans mangas, c'est pénible mais surtout très long...

## Merci ♥️


# <img src="https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/1200px-Flag_of_the_United_Kingdom.svg.png" height=20 width=30/> Zone-telechargement url extractor

- [Get chromedriver](https://chromedriver.chromium.org/downloads)
- [Get Geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.30.0)

## How to run

```bash
# installation
python3 -m pip install -r requirements.txt
```

```powershell
# powershell
./Run.ps1 # Will prompt all the needed information
```
```bash
# bash
./run.sh # Will prompt all the needed information
```

### Questions

- **Where can I find the cookie ?**

Open any ZT/ZA link, click on any sublink (1fichier, for example). Go until the final "see link" page.

Here, press F12 (open console), go to network tab, click on "All" and filter requests containing "link".

Here, grab the cookie in the headers of the request

- **What link should I provide to the script ?**

Provide the link containing all sub links (episode 1 to X)

## Why ?

Retrieving manga links is tedious and it's not fun at all.

## Thanks ♥️
