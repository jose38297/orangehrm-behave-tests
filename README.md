venv\Scripts\activate# OrangeHRM Selenium Behave Tests

Projet de tests automatises Selenium + Behave (BDD) pour OrangeHRM Demo.
URL cible : https://opensource-demo.orangehrmlive.com

---

## Structure du projet

```
orangehrm_behave/
├── .github/
│   └── workflows/
│       └── selenium_tests.yml      # CI/CD GitHub Actions (windows-latest)
├── features/
│   ├── environment.py              # Hooks Behave (before/after)
│   ├── employee/
│   │   └── employee_crud.feature   # Scenarios CRUD employe
│   ├── leave/
│   │   └── leave_management.feature
│   ├── timesheet/
│   │   └── timesheet_management.feature
│   └── search/
│       └── search_filter.feature
├── steps/
│   ├── common_steps.py             # Steps partages (connexion, navigation)
│   ├── employee_steps.py
│   ├── leave_steps.py
│   ├── timesheet_steps.py
│   └── search_steps.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── employee_page.py
│   ├── leave_page.py
│   └── timesheet_page.py
├── utils/
│   ├── config.py
│   ├── driver_factory.py
│   └── helpers.py
├── .env                            # Variables d'environnement (non versionne)
├── .env.example                    # Modele de configuration
├── .gitignore
├── behave.ini
└── requirements.txt
```

---

## Installation

```bash
# 1. Cloner le depot
git clone https://github.com/jose38297/orangehrm-behave-tests.git
cd orangehrm-behave-tests

# 2. Creer un environnement virtuel
python -m venv venv
venv\Scripts\activate

# 3. Installer les dependances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
copy .env.example .env
```

---

## Execution des tests

### Tous les tests
```bash
behave
```

### Par tag
```bash
behave --tags=employee
behave --tags=leave
behave --tags=timesheet
behave --tags=search
```

### Scenarios specifiques
```bash
behave --tags=full_cycle
behave --tags=create
behave --tags=approve_leave
```

### Avec rapport JUnit
```bash
behave --junit --junit-directory=reports/junit
```

### En mode headless
```bash
set HEADLESS=true && behave --tags=employee
```

---

## Scenarios couverts

### 1. Cycle de vie complet d'un employe (CRUD)
| Tag | Description |
|-----|-------------|
| @create | Creation d'un employe |
| @create_with_photo | Creation avec photo de profil |
| @update | Modification des informations |
| @delete | Suppression d'un employe |
| @full_cycle | CRUD complet enchaine |

### 2. Gestion des conges
| Tag | Description |
|-----|-------------|
| @apply_leave | Soumission d'une demande |
| @leave_status_pending | Verification statut En attente |
| @approve_leave | Approbation par le manager |
| @full_leave_cycle | Cycle demande vers approbation |

### 3. Feuilles de temps
| Tag | Description |
|-----|-------------|
| @create_timesheet | Creation d'une feuille |
| @enter_hours | Saisie des heures |
| @submit_timesheet | Soumission |
| @approve_timesheet | Validation manager |
| @full_timesheet_cycle | Cycle complet |

### 4. Recherche et Filtrage
| Tag | Description |
|-----|-------------|
| @search_by_name | Recherche par nom |
| @search_no_results | Recherche sans resultat |
| @filter_by_department | Filtre par departement |
| @search_and_filter | Combinaison recherche et filtre |

---

## Identifiants de test (OrangeHRM Demo)

| Role | Username | Password |
|------|----------|----------|
| Admin | Admin | admin123 |
| Employe/Manager | Paul.T | Supervisor@1 |

---

## Secrets GitHub Actions a configurer

Aller dans : Settings > Secrets and variables > Actions > New repository secret

| Nom | Valeur |
|-----|--------|
| BASE_URL | https://opensource-demo.orangehrmlive.com |
| ADMIN_USERNAME | Admin |
| ADMIN_PASSWORD | admin123 |
| EMPLOYEE_USERNAME | Paul.T |
| EMPLOYEE_PASSWORD | Supervisor@1 |
