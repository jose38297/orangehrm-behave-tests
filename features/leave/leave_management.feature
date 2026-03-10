# language: fr
@leave @conges
Fonctionnalite: Gestion des conges
  En tant qu'employe
  Je veux pouvoir poser des conges et suivre leur statut
  Afin que mon manager puisse approuver ou rejeter mes demandes

  @apply_leave
  Scenario: Soumission d'une demande de conge par un employe
    Etant donne que je suis connecte en tant qu'employe
    Lorsque je navigue vers la page de demande de conge
    Et que je selectionne un type de conge disponible
    Et que je definis la date de debut "2025-01-15"
    Et que je definis la date de fin "2025-01-16"
    Et que j'ajoute le commentaire "Conge personnel"
    Et que je clique sur Appliquer
    Alors la demande de conge doit avoir le statut "Pending Approval"

  @leave_status_pending
  Scenario: Verification du statut En attente apres soumission
    Etant donne que je suis connecte en tant qu'employe
    Lorsque je soumets une demande de conge du "2025-01-20" au "2025-01-21"
    Alors ma demande doit apparaitre dans la liste avec le statut "Pending Approval"

  @approve_leave
  Scenario: Approbation d'une demande de conge par un manager
    Etant donne que je suis connecte en tant qu'admin
    Lorsque je navigue vers la liste des conges
    Et que j'approuve la premiere demande de conge en attente
    Alors le statut de la demande doit etre "Approved"

  @full_leave_cycle
  Scenario: Cycle complet - Demande et approbation de conge
    Etant donne que je suis connecte en tant qu'employe
    Lorsque je soumets une demande de conge du "2025-02-10" au "2025-02-11"
    Alors ma demande doit apparaitre dans la liste avec le statut "Pending Approval"
    Etant donne que je suis connecte en tant qu'admin
    Lorsque je navigue vers la liste des conges
    Et que j'approuve la premiere demande de conge en attente
    Alors le statut de la demande doit etre "Approved"
