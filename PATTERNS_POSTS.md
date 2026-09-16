# PATTERNS POSTS — Banque de patterns performance (Matthias)

> Pôle 3, document dédié — créé le 16 septembre 2026. Rattaché à `SKILL_CONTENU_LINKEDIN.md` Module 1, qui reste la référence pour la mécanique de génération (catalogue d'angles PA/SA/PR/PB, pipeline 8 accroches/3 approches, règles Ton & Voix — rien de tout ça ne change). Ce document remplace uniquement la partie "qu'est-ce qui marche et pourquoi" + le tracking : l'ancienne section "Patterns de performance" de `SKILL_CONTENU_LINKEDIN.md` et le tracking `JOURNAL.md` (Journal Contenu) pour les posts sont désactivés à partir de cette date (voir note dans ces deux documents).
>
> **Table rase volontaire, décision explicite de Matthias le 16 septembre 2026.** Rien de l'ancien corpus (57 posts + 19 vidéos analysés le 22 juillet 2026) n'est repris ici, même si cette donnée était réelle et chiffrée — Matthias ne voulait pas polluer la nouvelle itération avec des patterns calés sur un contexte différent (ancien ICP, avant les posts de visibilité demandés par Yann Perono). Cette ancienne analyse reste consultable dans l'historique git de `SKILL_CONTENU_LINKEDIN.md` si jamais besoin, mais n'est plus une source active. Ce document démarre vide et se construit uniquement à partir de ce que Matthias colle activement à partir de maintenant.
>
> **Contexte stratégie (16 septembre 2026) :** Yann Perono n'a pas encore donné de doctrine de contenu précise. Sa seule consigne à ce jour : faire des posts à visibilité. Les patterns capturés ici sont donc lus dans ce cadre — visibilité (reach, engagement) — pas encore optimisés pour un objectif de conversion précis tant que Yann n'a pas affiné. Si/quand Yann donne une doctrine de contenu plus précise, elle va dans `STRATEGIE_YANN.md` (jamais ici) et ce document s'y articule.

---

## Ce que ce document EST et n'est PAS

- **Ce n'est pas un journal.** Pas d'entrée systématique pour chaque post publié, pas de log exhaustif. Un post qui n'apprend rien de nouveau (confirme un pattern déjà solidement établi, sans nuance) n'a pas besoin d'entrée.
- **Ce n'est pas un catalogue de sujets/angles.** Ça reste le rôle du catalogue PA/SA/PR/PB dans `SKILL_CONTENU_LINKEDIN.md`. Ici, on ne classe pas les posts par thème — on classe les MÉCANISMES qui expliquent une performance, indépendamment du sujet.
- **C'est une banque de patterns, alimentée uniquement par des posts que Matthias apporte lui-même**, avec un verdict et si possible des stats réelles. Claude ne va jamais chercher de posts tout seul (pas de fouille rétroactive dans `ARCHIVE_CONTENU.md` ou `JOURNAL.md` sans que Matthias les ramène explicitement ici).
- **L'objectif est le POURQUOI, jamais le QUOI seul.** Un sujet qui a marché n'est pas un pattern. Le mécanisme qui explique que ce sujet ait marché (et qui pourrait donc se reproduire sur un autre sujet) est un pattern.

## Comment ça marche

1. Matthias colle un post (déjà publié) avec :
   - **Le verdict** : "ça a marché", "ça n'a pas marché alors que je pensais que oui", "flop, mais je veux comprendre pourquoi précisément", ou "surprise, ça a marché alors que je m'y attendais pas".
   - **Les stats réelles si disponibles** (impressions, réactions, commentaires) — pas obligatoire pour démarrer l'analyse, mais nécessaire pour faire monter un pattern au statut "confirmé".
2. Claude analyse le mécanisme, pas le sujet : qu'est-ce qui, structurellement, explique ce résultat — et est-ce que ce même ressort tiendrait sur un sujet complètement différent ? Si Claude n'est pas sûr du mécanisme, il le dit et propose une hypothèse plutôt que d'inventer une certitude.
3. L'entrée va dans une des sections ci-dessous. Jamais un résumé neutre sans verdict.
4. **Un nouveau post qui confirme un pattern déjà noté n'ouvre pas une nouvelle entrée** : sa preuve s'ajoute à la liste de preuves du pattern existant, ce qui le fait passer d'hypothèse à confirmé (voir statuts plus bas).
5. **Un post qui contredit un pattern déjà noté** est signalé comme tension explicite (section dédiée plus bas) — jamais deux patterns contradictoires qui coexistent silencieusement dans les listes principales (même discipline anti-pollution que `CLAUDE.md` Partie 4).
6. Réflexe de capture immédiat, dans le même tour de conversation où Matthias colle le post : mise à jour de ce document, puis commit + push sur la branche de session en cours, puis vérification/synchronisation de la branche par défaut (voir `CLAUDE.md` Partie 4).

**Statuts d'un pattern :**
- **Hypothèse** — 1 seule preuve. Utilisable en réflexion, jamais présenté à Matthias comme une certitude.
- **Confirmé** — 2 preuves ou plus, cohérentes entre elles.
- **En tension** — des preuves qui se contredisent sur le même mécanisme apparent (voir section dédiée).

---

## Patterns confirmés (ce qui marche, avec preuve)

*(vide — se remplit au fur et à mesure que Matthias colle des posts qui ont marché, avec au moins 2 preuves cohérentes pour passer d'hypothèse à confirmé)*

Format d'une entrée :
```
### [Nom du pattern]
Statut : Hypothèse / Confirmé
Mécanisme : [le POURQUOI en 1-3 phrases — qu'est-ce qui, structurellement, produit ce résultat]
Preuves :
- [Date] — [description courte du post], [stats si dispo]
```

---

## Patterns invalidés / pièges (ce qui n'a pas marché malgré l'attente, avec preuve)

*(vide — se remplit quand Matthias colle un post qu'il pensait bon et qui a flop, avec l'analyse de ce qui a raté)*

Format d'une entrée :
```
### [Ce qui semblait une bonne idée]
Statut : Hypothèse / Confirmé
Pourquoi ça semblait devoir marcher : [l'intuition de départ, pour ne pas la reproduire sans savoir pourquoi elle a paru bonne]
Mécanisme réel de l'échec : [le POURQUOI précis]
Preuves :
- [Date] — [description courte du post], [stats si dispo]
```

---

## Tensions non résolues

*(vide — cas où deux posts se contredisent sur le même mécanisme apparent, à statuer avec Matthias plutôt qu'à trancher seul)*

---

## Historique

**16 septembre 2026 — Création du document.** Matthias tranche : on repart de zéro sur l'analyse de performance des posts, sans reprendre l'ancien corpus (57 posts + 19 vidéos, section "Patterns de performance" de `SKILL_CONTENU_LINKEDIN.md`) pour ne pas polluer la nouvelle itération avec un contexte différent (ancien ICP, avant les posts de visibilité Yann Perono). Le tracking automatique via `JOURNAL.md` (Journal Contenu) est retiré pour les posts — conséquence assumée : plus de garde-fou automatique anti-répétition de thématique/angle d'une session à l'autre, à surveiller au feeling ou en le signalant explicitement à Claude si Matthias veut éviter une redite précise. Le catalogue d'angles (PA/SA/PR/PB), le pipeline de génération (8 accroches/3 approches) et les règles Ton & Voix de `SKILL_CONTENU_LINKEDIN.md` restent inchangés et actifs.
