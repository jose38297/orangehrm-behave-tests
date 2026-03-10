@search @filtrage
Feature: Recherche et filtrage des employes
  En tant qu'administrateur RH
  Je veux pouvoir rechercher et filtrer les employes
  Afin de retrouver rapidement les informations desirees

  Background:
    Given je suis connecte en tant qu'admin
    And je navigue vers la liste des employes

  @search_by_name
  Scenario: Recherche d'un employe par son nom
    When je recherche l'employe par le nom "Linda"
    Then seuls les employes contenant "Linda" dans leur nom doivent s'afficher

  @search_no_results
  Scenario: Recherche sans resultat correspondant
    When je recherche l'employe par le nom "ZZZ_Inexistant_XYZ"
    Then aucun employe ne doit s'afficher dans la liste

  @filter_by_department
  Scenario: Filtrage des employes par departement
    When je filtre les employes par departement "IT"
    Then seuls les employes du departement "IT" doivent apparaitre

  @search_and_filter
  Scenario: Combinaison recherche par nom et filtrage par departement
    When je recherche l'employe par le nom "Admin"
    Then les resultats doivent correspondre au nom recherche
    When je reinitialise les filtres
    And je filtre les employes par departement "Engineering"
    Then seuls les employes du departement "Engineering" doivent apparaitre