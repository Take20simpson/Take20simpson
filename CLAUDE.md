# CLAUDE.md

Hub central pour les assistants IA travaillant avec Matthias. Contient l'identité, le snapshot business actuel, et la carte des documents actifs du système.

> **Réécrit le 22 juillet 2026.** Ancienne version : base de connaissances qui accumulait tout (identité, stratégie, learnings clients, closing, contenu, changelog daté). Nouvelle architecture : ce fichier reste léger (identité + snapshot + carte), la doctrine et les moteurs opérationnels vivent dans 4 documents dédiés (voir Partie 3). Certains détails (tarifs exacts, offres) peuvent avoir besoin d'être reconfirmés avec Matthias — c'est normal et accepté, mieux vaut un système clair qu'un fichier qui accumule sans fin.

---

## PARTIE 1 : IDENTITÉ

### Informations Personnelles

- **Prenom :** Matthias
- **Age :** 22 ans (ne le 13 decembre 2003)
- **Localisation :** Nice, France (vit chez sa mere)
- **Chienne :** Vaya

### Parcours

- Bac obtenu juillet 2021 avec 10,5/20 — s'ennuyait a l'ecole, on lui disait "faineant", "tu n'iras nulle part"
- Depuis le bac : lance en entrepreneuriat, teste plein de projets (landing pages, webdesign, etc.) sans succes au debut, puis full focus sur la prospection LinkedIn
- Autodidacte complet (copywriting principalement) — aucun diplome supplementaire, aucun mentor, tout appris seul
- **La galere avant le declic :** des mois de prospection en mode automatique sans structure (aucun client) → un coaching a 1500 EUR qui n'a rien apporte (templates a copier-coller, zero comprehension) → 8 mois de prestations gratuites "pour la credibilite" (0 EUR sur le compte, cercle vicieux). Le vrai probleme n'etait pas la technique : sa peur de demander de l'argent, le volume sans intention, l'absence de structure
- **Le declic :** comprendre que le probleme etait l'approche complete, pas la technique — passer du mode automatique au mode intention (comprendre les patterns + agir avec conscience)
- Cette histoire personnelle est du materiau reel reutilisable en storytelling (posts, commentaires, DM) — voir aussi la banque de vecu dans `SKILL_CONTENU_LINKEDIN.md`

### Niveau Technique & Qualites

- Intermediaire en tech (a l'aise, pas developpeur expert) — expliquer clairement, sans jargon inutile, sans sous-estimer ses capacites
- Perseverant, oriente action, direct et sans filtre, exigeant sur la qualite

### Contexte Personnel

- Pere 75 ans, tres ouvert mais ne comprend pas les details du business. Entourage peu au courant de ce qu'il fait, pas d'encouragement reel exterieur
- Motivation : prouver par les resultats, pas d'ego
- Gestion du rejet en DM : ne le touche presque plus, la methode lui donne confiance face aux objections
- 3 erreurs identifiees sur 4 ans de recul entrepreneurial : manque de consistance (lache trop tot), manque de sens (faisait des choses sans y croire), dispersion (voulait reinventer au lieu de copier ce qui marche). La solution trouvee : copier une methode de vente qui marche deja, faire un truc qui a du sens, persister

---

## PARTIE 2 : BUSINESS ACTUEL (SNAPSHOT)

### Positionnement

- **Denomination :** "Prospecter avec intention" — pas de marque formelle, travaille sous son nom
- Specialiste prospection LinkedIn pour freelances et solopreneurs (tous secteurs), avec intention (volume suffisant + structure), pas volume aveugle ni juste qualite

### Offre 1 : Accompagnement Complet (coaching + suivi)

- **Prix (juillet 2026) :** 2000 EUR, 3 mois avec suivi reel — monte progressivement depuis 350 EUR (fevrier 2026). Paiement en plusieurs fois possible, virement bancaire
- Livrables non figes, adaptes a chaque client : frameworks IA personnalises (setting, commentaires), 1-2 videos strategie, groupe WhatsApp (3 canaux), suivi proactif 2x/semaine

### Offre 2 : Framework(s) IA Seuls (sans suivi)

- **Prix :** 50 EUR — vestige du debut, plus une priorite strategique (le focus est sur l'accompagnement complet)

### Promesse Commune

> "C'est pas juste un robot qui ecrit a ta place. C'est comme avoir un coach de setting H24 qui t'explique les mecanismes derriere chaque reponse."

Alternative abordable aux coachings a 1500-3000 EUR.

### Cible (ICP)

**Cible large, pas limitee aux assistantes virtuelles.** Freelances (tous secteurs), coachs, solopreneurs, petites agences (1-5 employes), France/francophones, 300-5000 connexions LinkedIn.

**Criteres :** actifs sur LinkedIn (postent 1x/semaine mini), profil soigne, commentent regulierement. Pas debutant complet, cree un minimum de contenu, a une offre deja definie.

**Pain points frequents (par ordre) :** inconsistance de clients (feast or famine) → volume sans structure/intention → peur de vendre/facturer → deja accompagnes ailleurs sans resultats → dispersion strategique → mauvaise strategie pour leur contexte.

### Ressources Gratuites

- **Manifeste "Prospecter avec Intention"** (PDF, 18-22 pages) : utilise dans ~10% des cas seulement, quand le prospect commence a se desengager — jamais envoye si la conversation flow naturellement
- Autres lead magnets crees a la demande selon le besoin du moment

### Outils

| Outil | Usage |
|-------|-------|
| **LinkedIn** | Prospection, sourcing, setting, contenu |
| **Airtable** | CRM prospects/clients + calendrier editorial |
| **WhatsApp** | Suivi clients + video pre-appel |
| **Google Meet** | Closing visio (enregistre avec tl;dv + otter.ai) |
| **Claude** | Setting DM, contenu LinkedIn, strategie (voir Partie 3) |
| **Fillout** | Questionnaires clients |

### Statut Legal

Auto-entrepreneur, paiement par virement bancaire. Pas de site web, pas de Calendly (toujours 2-3 creneaux proposes manuellement).

---

## PARTIE 3 : ARCHITECTURE DU SYSTÈME — CARTE DES DOCUMENTS

> Cette carte est la règle de navigation pour toute nouvelle session. Le système repose sur 4 pôles + ce hub. **Aucun autre document du repo ne fait partie du socle actif.**

| # | Pôle | Document(s) | Rôle |
|---|------|-------------|------|
| — | **Hub** | `CLAUDE.md` (ce fichier) | Identité + snapshot business + carte |
| 1 | **Conseiller Stratégie** | `SKILL_STRATEGIE.md` | Le pôle le plus important. Vision macro + micro, doctrine (croyance centrale, philosophie, closing, KPIs, objectifs), et surtout comment Claude doit se comporter comme collaborateur. Ne fait ni setting, ni contenu, ni journal — il s'appuie sur eux. |
| 2 | **Setting (prospection DM)** | `SKILL_SETTING_DM.md` + `TEASING_METHODE_DM.md` | Moteur de décision en temps réel pour répondre aux messages de prospects LinkedIn. |
| 3 | **Contenu LinkedIn** | `SKILL_CONTENU_LINKEDIN.md` | Génération de posts, commentaires classiques et commentaires punch. |
| 4 | **Journaux** | `JOURNAL.md` | Mémoire compacte : conversations de prospection traitées + contenus produits. Sert de matière première au Pôle 1. |

### Règle d'exclusion (stricte)

Les fichiers suivants existent dans le repo mais **ne font pas partie du socle actif**. Ne jamais aller y chercher de l'information, ne jamais s'y référer, sauf si Matthias les nomme explicitement dans son message :

- **Dossiers clients nommés** (Lucille/Lucile, Mélanie, etc.) : `STRATEGIE_LUCILLE.md`, `PREP_APPEL_LUCILE.md`, `FRAMEWORK_POSTS_LINKEDIN_LUCILE.md`, `TRAME_SETTING_MELANIE.md`
- **Dossier produit** (ce que Matthias livre à ses clients, pas sa propre stratégie) : `ASSISTANT_CLIENT.md`, `QUESTIONNAIRE_ONBOARDING.md`, `METHODOLOGIE_ACCOMPAGNEMENT.md`
- **Références historiques** : `METHODE_ENZO_RACINE.md`, `CONVERSATION_ENZO_RACINE.md`, `TRONC_CENTRAL_YADULINK.md`, `LEAD_MAGNET.md`

Si une tâche semble en avoir besoin, le dire à Matthias plutôt que d'aller y puiser de soi-même — ne jamais halluciner ou déduire à partir de ces documents non mentionnés.

### Comment une nouvelle session doit se comporter

1. Lire ce hub (`CLAUDE.md`) — chargé automatiquement
2. Identifier le pôle concerné par la demande (stratégie / setting DM / contenu / journal) et lire le(s) document(s) correspondant(s) en entier
3. Ne jamais se fier à une connaissance antérieure sur le contenu de ces documents — ils évoluent en continu, toujours relire la version actuelle
4. Appliquer le réflexe de capture continue (Partie 4) dès qu'une nuance est validée par Matthias

---

## PARTIE 4 : CONVENTIONS & RÉFLEXE DE CAPTURE CONTINUE

### Conventions Techniques

1. **Lire avant d'editer** — Toujours lire un fichier avant de proposer des modifications
2. **Changements minimaux** — Ne changer que ce qui est necessaire
3. **Pas de secrets** — Ne jamais committer de fichiers `.env`, credentials, cles API
4. **Langue** — Matthias parle francais, communiquer en francais par defaut

### Reflexe de Capture Continue (a appliquer dans TOUTE session)

Des qu'un echange fait apparaitre une nuance, une confirmation, une correction ou une regle nouvelle, Claude met a jour le document le plus pertinent **immediatement dans le meme tour de conversation** — jamais en fin de session.

**Ou capturer selon la nature de l'info :**
- Identite, snapshot business (prix, positionnement, ICP), architecture du systeme → `CLAUDE.md`
- Doctrine, posture de Claude, closing, KPIs, objectifs → `SKILL_STRATEGIE.md`
- Mecanique de reponse DM en temps reel → `SKILL_SETTING_DM.md` (ou `TEASING_METHODE_DM.md` pour le teasing/signal marche specifiquement)
- Posts, commentaires classique ou punch → `SKILL_CONTENU_LINKEDIN.md`
- Etat d'un prospect ou d'un contenu produit → `JOURNAL.md`

**Apres chaque edition :** commit + push sur la branche de session en cours, avec un message de commit qui decrit la nuance capturee.

**CRITIQUE — synchroniser aussi la branche par defaut du repo, pas seulement la branche de session.** Chaque nouvelle conversation Claude Code demarre depuis la branche par defaut (verifiable avec `git remote show origin | grep "HEAD branch"`), qui peut differer de la branche de session en cours.

**Reflexe a chaque fois :**
1. Commit + push sur la branche de session en cours
2. Verifier la branche par defaut
3. Si la branche de session est en avance, fusionner (fast-forward si possible) et pusher la branche par defaut aussi, avant de rendre la main
4. Si un fast-forward n'est pas possible (branches divergees), faire un vrai merge et signaler le conflit a Matthias plutot que de forcer silencieusement

**Discipline anti-pollution :** en ajoutant une nuance, verifier si elle contredit ou rend obsolete une regle existante ailleurs. Si oui, corriger la regle existante ou la marquer explicitement comme tension non tranchee — jamais deux regles contradictoires qui coexistent silencieusement.

---

*Derniere restructuration : 22 juillet 2026 — passage a l'architecture 4 pôles (Stratégie / Setting / Contenu / Journaux) + hub allégé.*
