# Projet de session - IFT785 : Lucas ARIES et Terry TEMPESTINI

## Configuration initiale

1. **Première installation** :
    ```bash
    make venv
    source .venv/bin/activate # différent selon l'OS
    make install
    ```


## Lancer l'application
```bash
# dans l'env après make install 
make run
```

## Lancer les tests
```bash
# dans l'env après make install 
make test
```

## Linting du code
```bash
make lint
```

## Formatage automatique
```bash
make format
```

## Nettoyer les fichiers temporaires et caches
```bash
make clean
```

## Supprimer l'environnement virtuel
```bash
make clean-venv
```
