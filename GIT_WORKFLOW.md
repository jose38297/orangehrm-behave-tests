# Guide Depot Git - OrangeHRM Selenium Tests

---

## ETAPE 1 - Creer le depot sur GitHub

1. Aller sur https://github.com/jose38297
2. Cliquer "New repository"
3. Nom : orangehrm-behave-tests
4. Description : Tests automatises Selenium Behave pour OrangeHRM
5. Visibilite : Public
6. Ne pas cocher "Initialize with README"
7. Ne pas cocher "Add .gitignore"
8. Cliquer "Create repository"

---

## ETAPE 2 - Initialiser Git en local

Ouvrir le terminal dans VS Code (Terminal > Nouveau terminal) :

```bash
git config --global user.name "jose38297"
git config --global user.email "votre@email.com"
```

---

## ETAPE 3 - Premier commit et push

```bash
git init
git add .
git status
git commit -m "feat: initialisation projet OrangeHRM Behave Tests"
git branch -M main
git remote add origin https://github.com/jose38297/orangehrm-behave-tests.git
git push -u origin main
```

---

## ETAPE 4 - Workflow quotidien (GitFlow simplifie)

```
main        <-- Production stable
  |
develop     <-- Integration continue
  |
feature/xxx <-- Nouvelle fonctionnalite
fix/xxx     <-- Correction de bug
```

### Creer une branche feature

```bash
git checkout -b feature/nom-de-la-fonctionnalite

# Faire les modifications dans VS Code...

git add .
git commit -m "feat: description de ce qui a ete fait"
git push origin feature/nom-de-la-fonctionnalite
```

### Ouvrir une Pull Request

1. Aller sur GitHub dans votre depot
2. Cliquer "Compare & pull request"
3. Base : main  <--  Compare : feature/nom-de-la-fonctionnalite
4. Remplir le titre et la description
5. Cliquer "Create pull request"

### Merger et nettoyer

```bash
git checkout main
git pull origin main
git branch -d feature/nom-de-la-fonctionnalite
git push origin --delete feature/nom-de-la-fonctionnalite
```

---

## ETAPE 5 - Conventions de commits

```
feat:      Nouveau scenario ou feature
fix:       Correction d'un test casse
refactor:  Reorganisation sans changement de comportement
docs:      Documentation uniquement
ci:        Modifications CI/CD
chore:     Maintenance (dependances, gitignore...)
```

Exemples :
```bash
git commit -m "feat(employee): ajout scenario suppression en masse"
git commit -m "fix(leave): correction selecteur date de conge"
git commit -m "refactor(pages): extraction BasePage commune"
git commit -m "ci: passage a windows-latest dans GitHub Actions"
```

---

## ETAPE 6 - Configurer les Secrets GitHub

Aller sur :
https://github.com/jose38297/orangehrm-behave-tests/settings/secrets/actions

Cliquer "New repository secret" pour chaque ligne :

| Nom du secret       | Valeur                                           |
|---------------------|--------------------------------------------------|
| BASE_URL            | https://opensource-demo.orangehrmlive.com        |
| ADMIN_USERNAME      | Admin                                            |
| ADMIN_PASSWORD      | admin123                                         |
| EMPLOYEE_USERNAME   | Paul.T                                           |
| EMPLOYEE_PASSWORD   | Supervisor@1                                     |

---

## ETAPE 7 - Declencher les tests manuellement

1. Aller sur : https://github.com/jose38297/orangehrm-behave-tests/actions
2. Cliquer "OrangeHRM Selenium Tests"
3. Cliquer "Run workflow"
4. Choisir le tag ou laisser vide pour tout executer
5. Cliquer le bouton vert "Run workflow"

---

## ETAPE 8 - Commandes Git utiles au quotidien

```bash
# Voir l'etat des fichiers
git status

# Voir l'historique
git log --oneline --graph --all

# Annuler un fichier modifie (non commite)
git restore nom_fichier.py

# Annuler le dernier commit en gardant les changements
git reset --soft HEAD~1

# Voir les differences
git diff

# Mettre de cote des changements temporairement
git stash
git stash pop

# Recuperer les dernieres modifications
git pull origin main
```
