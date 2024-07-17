### Étapes pour Gérer le Package

1. **Créer les distributions :**
    
    ```bash
    python setup.py sdist bdist_wheel
    
    ```
    
2. **Installer le package localement :**
    
    ```bash
    pip install ./dist/ft_package-0.0.1.tar.gz
    # ou
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl
    
    ```
    
3. **Vérifier l'installation :**
    
    ```bash
    pip list
    pip show -v ft_package
    
    ```
    
4. **Tester le package avec un script :**
    
    Créez un fichier `test_script.py` :
    
    ```python
    # test_script.py
    
    from ft_package import ft_list
    
    print(ft_list.count(["toto", "tata", "toto"], "toto"))  # output: 2
    print(ft_list.count(["toto", "tata", "toto"], "tutu"))  # output: 0
    
    ```
    
    Exécutez le script :
```

    python test_script.py
```