@timesheet @feuille_de_temps
Feature: Saisie et validation des feuilles de temps
  En tant qu'employe
  Je veux saisir mes heures et mon manager doit pouvoir les valider
  Afin de garantir le suivi correct du temps de travail

  @create_timesheet
  Scenario: Creation d'une nouvelle feuille de temps
    Given je suis connecte en tant qu'employe
    When je navigue vers mes feuilles de temps
    And je cree une feuille de temps pour la semaine courante
    Then la feuille de temps doit etre creee avec succes

  @enter_hours
  Scenario: Saisie des heures dans une feuille de temps
    Given je suis connecte en tant qu'employe
    When je navigue vers mes feuilles de temps
    And je cree une feuille de temps pour la semaine courante
    And je saisis "8" heures de travail
    And je sauvegarde la feuille de temps
    Then la feuille de temps doit etre enregistree

  @submit_timesheet
  Scenario: Soumission d'une feuille de temps remplie
    Given je suis connecte en tant qu'employe
    When je navigue vers mes feuilles de temps
    And je cree une feuille de temps pour la semaine courante
    And je saisis "8" heures de travail
    And je sauvegarde la feuille de temps
    And je soumets la feuille de temps
    Then le statut de la feuille doit etre "Submitted"

  @approve_timesheet
  Scenario: Validation d'une feuille de temps par le manager
    Given je suis connecte en tant qu'admin
    When je navigue vers les feuilles de temps des employes
    And j'approuve la feuille de temps du premier employe
    Then le statut de la feuille doit etre "Approved"

  @full_timesheet_cycle
  Scenario: Cycle complet - Saisie et validation de feuille de temps
    Given je suis connecte en tant qu'employe
    When je navigue vers mes feuilles de temps
    And je cree une feuille de temps pour la semaine courante
    And je saisis "8" heures de travail
    And je sauvegarde la feuille de temps
    And je soumets la feuille de temps
    Then le statut de la feuille doit etre "Submitted"
    Given je suis connecte en tant qu'admin
    When je navigue vers les feuilles de temps des employes
    And j'approuve la feuille de temps du premier employe
    Then le statut de la feuille doit etre "Approved"