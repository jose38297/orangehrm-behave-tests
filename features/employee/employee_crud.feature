@employee @crud
Feature: Gestion complete d'un employe (CRUD)
  En tant qu'administrateur RH
  Je veux pouvoir creer, modifier et supprimer un employe
  Afin de gerer correctement les informations du personnel

  Background:
    Given je suis connecte en tant qu'admin

  @create
  Scenario: Creation d'un nouvel employe avec informations de base
    When je navigue vers la page d'ajout d'employe
    And je saisis le prenom "John" et le nom "TestAuto"
    And je sauvegarde l'employe
    Then l'employe "John TestAuto" doit apparaitre dans la liste des employes

  @create_with_photo
  Scenario: Creation d'un employe avec photo de profil
    When je navigue vers la page d'ajout d'employe
    And je saisis le prenom "Jane" et le nom "PhotoTest"
    And j'upload une photo de profil
    And je sauvegarde l'employe
    Then l'employe "Jane PhotoTest" doit apparaitre dans la liste des employes

  @update
  Scenario: Modification des informations personnelles d'un employe existant
    When je recherche l'employe "John TestAuto" dans la liste
    And je clique sur modifier pour le premier resultat
    And je mets a jour le prenom avec "Johnny"
    And je sauvegarde les modifications
    Then les informations mises a jour doivent etre visibles dans le profil

  @delete
  Scenario: Suppression d'un employe de la liste
    When je recherche l'employe "Johnny TestAuto" dans la liste
    And je supprime le premier employe trouve
    Then l'employe ne doit plus apparaitre dans la liste

  @full_cycle
  Scenario: Cycle de vie complet - Creation Modification et Suppression
    When je navigue vers la page d'ajout d'employe
    And je saisis le prenom "Cycle" et le nom "Complet"
    And je sauvegarde l'employe
    Then l'employe "Cycle Complet" doit apparaitre dans la liste des employes
    When je recherche l'employe "Cycle Complet" dans la liste
    And je clique sur modifier pour le premier resultat
    And je mets a jour le prenom avec "CycleModifie"
    And je sauvegarde les modifications
    When je recherche l'employe "CycleModifie Complet" dans la liste
    And je supprime le premier employe trouve
    Then l'employe ne doit plus apparaitre dans la liste