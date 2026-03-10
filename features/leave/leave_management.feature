@leave @conges
Feature: Gestion des conges
  En tant qu'employe
  Je veux pouvoir poser des conges et suivre leur statut
  Afin que mon manager puisse approuver ou rejeter mes demandes

  @apply_leave
  Scenario: Soumission d'une demande de conge par un employe
    Given je suis connecte en tant qu'employe
    When je navigue vers la page de demande de conge
    And je selectionne un type de conge disponible
    And je definis la date de debut "2025-01-15"
    And je definis la date de fin "2025-01-16"
    And j'ajoute le commentaire "Conge personnel"
    And je clique sur Appliquer
    Then la demande de conge doit avoir le statut "Pending Approval"

  @leave_status_pending
  Scenario: Verification du statut En attente apres soumission
    Given je suis connecte en tant qu'employe
    When je soumets une demande de conge du "2025-01-20" au "2025-01-21"
    Then ma demande doit apparaitre dans la liste avec le statut "Pending Approval"

  @approve_leave
  Scenario: Approbation d'une demande de conge par un manager
    Given je suis connecte en tant qu'admin
    When je navigue vers la liste des conges
    And j'approuve la premiere demande de conge en attente
    Then le statut de la demande doit etre "Approved"

  @full_leave_cycle
  Scenario: Cycle complet - Demande et approbation de conge
    Given je suis connecte en tant qu'employe
    When je soumets une demande de conge du "2025-02-10" au "2025-02-11"
    Then ma demande doit apparaitre dans la liste avec le statut "Pending Approval"
    Given je suis connecte en tant qu'admin
    When je navigue vers la liste des conges
    And j'approuve la premiere demande de conge en attente
    Then le statut de la demande doit etre "Approved"