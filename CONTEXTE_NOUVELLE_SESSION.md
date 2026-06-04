# CONTEXTE COMPLET — Session Yadulink Tronc Central
*(À copier-coller en tête de la nouvelle conversation)*

---

## CE QU'ON FAIT

On travaille sur le document **"TRONC CENTRAL : STRATÉGIE DE SETTING AGENT IA"** pour le produit **Yadulink**.

L'objectif : produire un DOCX final propre, avec :
- Le contenu mis à jour (toutes les décisions prises)
- Des commentaires Word latéraux reproduisant les échanges Kevin / Matthias
- Zéro signal IA dans le texte (tirets, formules génériques, vocabulaire trop riche)

Le fichier de travail actuel : `TRONC_CENTRAL_Yadulink_v2.docx` (dans le repo GitHub `take20simpson/take20simpson`, branche `claude/zen-gates-sx1ZC`). Il contient les Blocs 1 à 4A déjà intégrés.

Le script de build est `build_v2.py` dans le même repo — il reconstruit le DOCX à partir du fichier original à chaque fois.

---

## ARCHITECTURE DU DOCUMENT (8 Blocs)

**Lexique** — Définitions des termes clés du système  
**Bloc 1** — Profils cibles (5 archétypes + CAS A / CAS B)  
**Bloc 2** — Signaux de sourcing (critères de sélection des prospects)  
**Bloc 3** — Premier message (Niveau 1, 2, 3 + timing d'envoi)  
**Bloc 4A** — Setting conversationnel (Niveau 3 ultra-personnalisé, exemples sectoriels)  
**Bloc 4B** — Suite du setting (blocs de conversation, gestion des refus)  
**Blocs 5-8** — Phases suivantes du setting (non encore annotés par Kevin)

---

## RÈGLES ABSOLUES DU DOCUMENT (à appliquer partout, sans exception)

### 1. Zéro tiret long (—)
Remplacer **tous** les `—` par une virgule `,` ou des parenthèses `(...)` selon le contexte.  
**Jamais** remplacer par un tiret court ` - `.  
Les tirets dans les mots composés (`ultra-personnalisé`, `sous-cas`) sont des traits d'union normaux — ne pas toucher.

### 2. Terminologie : "rondeur" pas "enrobage"
Le terme universel pour désigner la partie contextualisée/personnalisée après la question est **rondeur**.  
Remplacer **tous** les occurrences de "enrobage" par "rondeur" dans tout le document, y compris dans les définitions du Lexique.  
Si le Lexique a une définition de "enrobage", la remplacer par une définition de "rondeur".

### 3. Structure des messages Niveau 3
**[Question sur vision/approche] + parce que + [rondeur ancrée dans UN post ou UNE thématique spécifique]**  
Question d'abord, rondeur ensuite. Jamais l'inverse.

### 4. Zéro signal IA dans les exemples de messages
- Pas de `—` dans les exemples de conversations
- Pas de formules génériques ("Résultat ?", "Spoiler :", "La vérité c'est que...")
- Pas de vocabulaire trop riche ("catalyseur", "paradigme", "levier stratégique")
- Pas de "le truc qui m'a tué" ou expressions similaires

---

## DÉCISIONS PRISES BLOC PAR BLOC

### LEXIQUE
- Remplacer la définition "enrobage" par "rondeur"
- "Rondeur" = la partie du message qui ancre la question dans le contenu réel du prospect (un post, une thématique, une conviction détectée). Elle crée la crédibilité sans être lourde.

### BLOC 1
- CAS A = cas le plus fréquent (~70-80% des situations) — validé par Kevin
- CAS B = profil moins actif, moins exposé à la prospection
- Commentaire Word conservé : échange Kevin/Matthias/Kevin sur la fréquence du CAS A (avec sauts de ligne entre les interlocuteurs)

### BLOC 2
- **Archétype 5** : le niveau de méfiance élevé s'explique par le **volume de prospection reçu** (pas uniquement le statut). Un fondateur/builder reçoit des dizaines de messages/semaine — c'est cette exposition répétée qui génère le filtre.
- **Ancienneté** : distinction importante ajoutée — ancienneté **métier** ≠ ancienneté **LinkedIn**. Signal pertinent pour l'agent = l'ancienneté LinkedIn (exposition à la prospection), pas l'expérience professionnelle.
- Commentaires Word Kevin conservés (validations)

### BLOC 3
- Vérifier que la fenêtre d'envoi est bien "6 à 9 heures" (pas un autre format)
- Commentaire Kevin conservé : "Tu as raison, c'est exactement ce qui fait penser à une IA. C'est top 👍"

### BLOC 4A — Niveau 3 (LE CŒUR DU SYSTÈME)

**Template validé :**
```
[Question sur leur vision ou leur approche] + parce que [rondeur ancrée dans UN post ou UNE thématique spécifique de leur contenu]
```

**Deux variables clés à extraire du profil prospect :**

- **[TA THÈSE]** = la conviction forte que le prospect défend dans ses posts. Ce qu'il répète, ce qu'il contre-argumente, ce qu'il enseigne. Sa prise de position distinctive.
- **[LE FREIN PRINCIPAL]** = l'obstacle ou la croyance que le prospect identifie chez son audience. Ce contre quoi il se bat dans son contenu. La résistance qu'il essaie de lever.

**Règle "pas assez d'éléments" :**
- **Sous-cas A** — secteur identifiable (freelances, coachs, fondateurs...) : question ancrée dans la tension connue du secteur, sans prétendre avoir lu un post spécifique
- **Sous-cas B** — profil trop générique ou trop peu actif : question universelle sur l'acquisition ou la visibilité, formulée de façon ouverte
- Dans les deux cas : structure = [Question] + parce que [rondeur honnête sans surjouer la personnalisation]

**9 exemples sectoriels validés (structure : question d'abord, parce que + rondeur ensuite) :**

*Coach business (2 options) :*
- "C'est quoi ton approche quand un client arrive convaincu que son problème c'est le mindset, alors que toi tu vois clairement que c'est son offre qui est mal positionnée ? parce que j'ai été accompagné par quelqu'un qui m'a forcé à retravailler mon positionnement avant même de toucher à ma façon de penser, et ça a tout changé."
- "Comment tu fais tenir quelqu'un dans la durée quand les premiers résultats tardent ? parce que j'ai remarqué que dans tes posts tu parles beaucoup d'engagement sur le long terme, et je me demandais ce que ça donnait concrètement côté accompagnement."

*Freelance / Assistant virtuel (3 options) :*
- "C'est quoi ton approche quand un prospect te dit que tu es trop cher mais que tu sens qu'il a vraiment besoin de toi ? parce que dans tes posts tu parles souvent de comment te positionner, et je me demandais comment tu gérais cette tension-là."
- "Comment tu gères la période creuse entre deux missions ? parce que j'ai l'impression que dans ce que tu partages tu défends l'idée que l'acquisition ça doit être régulier, pas en mode panique."
- "C'est quoi le truc que tu aurais aimé savoir sur la prospection quand tu as démarré en freelance ? parce que en lisant tes posts j'ai l'impression que t'as traversé pas mal de phases avant de trouver ce qui marche."

*Fondateur SaaS (2 options) :*
- "C'est quoi le moment où tu as réalisé que ce que tu construisais n'était pas ce que tes utilisateurs voulaient vraiment ? parce que je suis le build in public d'un fondateur en ce moment, et ce qui est revenu c'est ce moment où il a réalisé que ses utilisateurs voulaient quelque chose de complètement différent de ce qu'il avait passé des mois à construire."  
  *(Note : "build in public" pas "building public". Référencer UN fondateur spécifique, pas "pas mal de fondateurs")*
- "Comment tu gères l'écart entre ce que tu veux construire et ce que le marché te demande de construire ? parce que dans tes posts tu sembles naviguer constamment entre vision long terme et feedback immédiat."

*Webdesigner (3 options — toutes validées parfaites) :*
- "C'est quoi ton approche quand un client veut quelque chose qui va à l'encontre de ce qui est bon pour lui ? parce que j'ai lu un de tes posts où tu parlais de devoir éduquer les clients, et je me demandais comment tu posais ça dans la pratique."
- "Comment tu justifies tes choix de design à un client qui ne comprend pas pourquoi ça vaut le prix ? parce que j'ai l'impression que dans ce que tu partages tu défends une vision très précise de la valeur du design, et ça m'a intrigué."
- "C'est quoi le moment dans un projet où tu sens que le client commence à faire confiance à ton jugement plutôt que d'imposer le sien ? parce que dans tes posts tu parles souvent de cette dynamique client-designer, et j'aimerais comprendre comment tu construis ça."

*Dirigeant d'agence / Corporate (2 options — niveau de précision = référence pour tous les autres) :*
- "C'est quoi votre approche quand une équipe résiste à un changement que vous savez nécessaire ? parce que j'ai suivi plusieurs de vos interventions et ce qui revient c'est cette tension entre ce que le management décide et ce que le terrain est prêt à absorber."
- "Comment vous gérez l'écart entre la stratégie que vous préconisez et les contraintes politiques internes de vos clients ? parce que j'ai l'impression que dans votre contenu vous défendez une vision assez directe, et je me demandais comment ça se traduisait dans les missions."

**Exemple ÉLIMINÉ** : fondateur e-commerce (supprimé sur décision de Matthias).

**Commentaire A/B testing** : note dans le document que ces exemples sont à tester niche par niche, et que les résultats doivent remonter à Kevin pour affiner le training data.

---

## PROCHAINE ÉTAPE : REVUE OMNISCIENTE BLOC PAR BLOC

Quand tu ouvres la nouvelle conversation, la mission est :

1. **Remplacer tous les "enrobage" par "rondeur"** dans tout le document (y compris la définition dans le Lexique)
2. **Relire chaque bloc dans son ensemble** — pas seulement les points de détail, mais la cohérence globale. Identifier :
   - Des éléments qui seraient mieux placés dans un autre bloc
   - Des redondances entre blocs
   - Des manques (quelque chose qu'on a dit en conversation mais qui n'est pas dans le document)
   - Des incohérences internes
3. **Proposer les modifications** à Matthias avant de toucher au document
4. **Générer le DOCX final** une fois tout validé

---

## FORMAT DES COMMENTAIRES WORD

Structure obligatoire pour les commentaires reproduisant des échanges :
- Un paragraphe par prise de parole (= saut de ligne entre les interlocuteurs dans Word)
- Format : `Prénom Nom : texte du message`
- Les emojis sont conservés tels quels
- Les commentaires de validation simple Kevin ("ok", "👍") sont conservés mais groupés avec l'échange qui précède

---

## RÈGLES TECHNIQUES (build_v2.py)

- Toujours reconstruire depuis le fichier original (`17fd0a20-TRONC_CENTRAL_Yadulink_1.docx`)
- Manipuler le DOCX via zipfile + lxml (pas python-docx) pour contrôle total du XML
- Quand on insère de nouveaux paragraphes : copier le `pPr` et `rPr` du paragraphe adjacent pour hériter du formatage
- Zéro `—` dans le document généré
- Les commentaires Word : structure multi-paragraphes (un `w:p` par ligne = saut de ligne visible dans Word)

---

## CE QUI RESTE À FAIRE

- [ ] Remplacer "enrobage" par "rondeur" dans tout le document + Lexique
- [ ] Revue omnisciente Bloc par Bloc (Lexique, Blocs 1 à 8)
- [ ] Les Blocs 5 à 8 n'ont pas encore été annotés par Kevin — les relire et identifier ce qui manque/ce qui est à améliorer
- [ ] Générer le DOCX v3 final une fois tout validé

---

*Dernière mise à jour : session du 4 juin 2026*
