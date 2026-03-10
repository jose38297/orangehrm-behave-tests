# language: fr
@employee @crud
Fonctionnalite: Gestion complete d'un employe (CRUD)
  En tant qu'administrateur RH
  Je veux pouvoir creer, modifier et supprimer un employe
  Afin de gerer correctement les informations du personnel

  Contexte:
    Etant donne que je suis connecte en tant qu'admin

  @create
  Scenario: Creation d'un nouvel employe avec informations de base
    Lorsque je navigue vers la page d'ajout d'employe
    Et que je saisis le prenom "John" et le nom "TestAuto"
    Et que je sauvegarde l'employe
    Alors l'employe "John TestAuto" doit apparaitre dans la liste des employes

  @create_with_photo
  Scenario: Creation d'un employe avec photo de profil
    Lorsque je navigue vers la page d'ajout d'employe
    Et que je saisis le prenom "Jane" et le nom "PhotoTest"
    Et que j'upload une photo de profil
    Et que je sauvegarde l'employe
    Alors l'employe "Jane PhotoTest" doit apparaitre dans la liste des employes

  @update
  Scenario: Modification des informations personnelles d'un employe existant
    Lorsque je recherche l'employe "John TestAuto" dans la liste
    Et que je clique sur modifier pour le premier resultat
    Et que je mets a jour le prenom avec "Johnny"
    Et que je sauvegarde les modifications
    Alors les informations mises a jour doivent etre visibles dans le profil

  @delete
  Scenario: Suppression d'un employe de la liste
    Lorsque je recherche l'employe "Johnny TestAuto" dans la liste
    Et que je supprime le premier employe trouve
    Alors l'employe ne doit plus apparaitre dans la liste

  @full_cycle
  Scenario: Cycle de vie complet - Creation, Modification et Suppression
    Lorsque je navigue vers la page d'ajout d'employe
    Et que je saisis le prenom "Cycle" et le nom "Complet"
    Et que je sauvegarde l'employe
    Alors l'employe "Cycle Complet" doit apparaitre dans la liste des employes
    Lorsque je recherche l'employe "Cycle Complet" dans la liste
    Et que je clique sur modifier pour le premier resultat
    Et que je mets a jour le prenom avec "CycleModifie"
    Et que je sauvegarde les modifications
    Lorsque je recherche l'employe "CycleModifie Complet" dans la liste
    Et que je supprime le premier employe trouve
    Alors l'employe ne doit plus apparaitre dans la liste
