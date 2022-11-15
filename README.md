# Travaux de recherche dans le but d'inclure les aides utilisées par le simulateur `Aides-Jeunes`

## Description :
Ce dépôt a pour but un travail d'exploration sur les aides utilisés par le simulateur [Aides-Jeunes](https://github.com/betagouv/aides-jeunes).

Les recherches sont conduites dans le but d'intégrer ces aides dans le dépôt [OpenFisca-France](https://github.com/openfisca/openfisca-france)

## Utilisation

Les travaux sont sont accessibles via les `notebooks Jupyter`:

	- experimentation_aide.ipynb
	- read_config_file.ipynb

Pour utiliser ces travaux, il est necessaire de spécifier le chemin d'accès au répertoire requis.

### Pour le notebook `experimentation_aide` :

Le dossier contenant les aides (avec l'extension `.yaml` ou `.yml`).

(Par défault, le projet pointe vers une copie du dossier original qui peut ne pas être à jour).

Deux variables sont à disposition :

`root` : pour spécifier le chemin racine du projet.

`path` : pour spécifier le chemin partant de la racine du projet vers le dossier qui contient les aides.

### Pour le notebook `read_config_file.ipynb` :

Le fichier de configuration.

(Par défault, le projet pointe vers une copie du fichier original qui peut ne pas être à jour).

`root` : pour spécifier le chemin racine du projet.

`config_file_location` : pour spécifier le chemin partant de la racine du projet vers le fichier de configuration.