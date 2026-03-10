# language: fr
@search @filtrage
Fonctionnalite: Recherche et filtrage des employes
  En tant qu'administrateur RH
  Je veux pouvoir rechercher et filtrer les employes
  Afin de retrouver rapidement les informations desirees

  Contexte:
    Etant donne que je suis connecte en tant qu'admin
    Et que je navigue vers la liste des employes

  @search_by_name
  Scenario: Recherche d'un employe par son nom
    Lorsque je recherche l'employe par le nom "Linda"
    Alors seuls les employes contenant "Linda" dans leur nom doivent s'afficher

  @search_no_results
  Scenario: Recherche sans resultat correspondant
    Lorsque je recherche l'employe par le nom "ZZZ_Inexistant_XYZ"
    Alors aucun employe ne doit s'afficher dans la liste

  @filter_by_department
  Scenario: Filtrage des employes par departement
    Lorsque je filtre les employes par departement "IT"
    Alors seuls les employes du departement "IT" doivent apparaitre

  @search_and_filter
  Scenario: Combinaison recherche par nom et filtrage par departement
    Lorsque je recherche l'employe par le nom "Admin"
    Alors les resultats doivent correspondre au nom recherche
    Lorsque je reinitialise les filtres
    Et que je filtre les employes par departement "Engineering"
    Alors seuls les employes du departement "Engineering" doivent apparaitre
