# language: fr
@timesheet @feuille_de_temps
Fonctionnalite: Saisie et validation des feuilles de temps
  En tant qu'employe
  Je veux saisir mes heures et mon manager doit pouvoir les valider
  Afin de garantir le suivi correct du temps de travail

  @create_timesheet
  Scenario: Creation d'une nouvelle feuille de temps
    Etant donne que je suis connecte en tant qu'employe
    Lorsque je navigue vers mes feuilles de temps
    Et que je cree une feuille de temps pour la semaine courante
    Alors la feuille de temps doit etre creee avec succes

  @enter_hours
  Scenario: Saisie des heures dans une feuille de temps
    Etant donne que je suis connecte en tant qu'employe
    Lorsque je navigue vers mes feuilles de temps
    Et que je cree une feuille de temps pour la semaine courante
    Et que je saisis "8" heures de travail
    Et que je sauvegarde la feuille de temps
    Alors la feuille de temps doit etre enregistree

  @submit_timesheet
  Scenario: Soumission d'une feuille de temps remplie
    Etant donne que je suis connecte en tant qu'employe
    Lorsque je navigue vers mes feuilles de temps
    Et que je cree une feuille de temps pour la semaine courante
    Et que je saisis "8" heures de travail
    Et que je sauvegarde la feuille de temps
    Et que je soumets la feuille de temps
    Alors le statut de la feuille doit etre "Submitted"

  @approve_timesheet
  Scenario: Validation d'une feuille de temps par le manager
    Etant donne que je suis connecte en tant qu'admin
    Lorsque je navigue vers les feuilles de temps des employes
    Et que j'approuve la feuille de temps du premier employe
    Alors le statut de la feuille doit etre "Approved"

  @full_timesheet_cycle
  Scenario: Cycle complet - Saisie et validation de feuille de temps
    Etant donne que je suis connecte en tant qu'employe
    Lorsque je navigue vers mes feuilles de temps
    Et que je cree une feuille de temps pour la semaine courante
    Et que je saisis "8" heures de travail
    Et que je sauvegarde la feuille de temps
    Et que je soumets la feuille de temps
    Alors le statut de la feuille doit etre "Submitted"
    Etant donne que je suis connecte en tant qu'admin
    Lorsque je navigue vers les feuilles de temps des employes
    Et que j'approuve la feuille de temps du premier employe
    Alors le statut de la feuille doit etre "Approved"
