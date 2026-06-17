---
name: commentaires-linkedin-punch
description: Génère des commentaires LinkedIn MÉMORABLES pour Matthias (visibilité sur gros comptes), qui allient un insight ultra-pertinent à de l'humour qui marque. Déclencher quand Matthias colle un post LinkedIn ET demande explicitement un registre drôle, percutant ou mémorable : "version punch", "commente avec humour", "fais-moi un truc marrant", "version mémorable", "fais-les rire", ou colle un post avec une instruction de ce type. Si Matthias colle juste un post sans demander ce registre, c'est le skill commentaires-linkedin classique qui s'applique. Produit toujours, sans demander confirmation, une question de fin + 6 options dans cet ordre exact (Humour fin / Storytelling / Humour barré / Solution ou Problem Aware / Clivant / Percutant), CHACUNE dans un bloc code séparé.
---

# Skill : Commentaires LinkedIn PUNCH (Mémorable) : Matthias

> Variante "punch" du skill commentaires LinkedIn. Découverte de Matthias après ~40
> commentaires en live : pousser l'humour fait deux choses, ça performe nettement mieux
> (les gens rebondissent, likent, commentent) ET ça casse mécaniquement la répétition des
> débuts de phrase, parce qu'une vanne ne peut pas être un template.
> Architecture à 6 options calibrée en live, avec DEUX slots humour distincts : un humour
> fin (option 1) et un humour barré second degré (option 3). 95% des règles de fond sont
> identiques au skill classique. Ce qui change : l'objectif, l'humour, et l'ordre des options.

---

## DÉTECTION

Trigger : Matthias colle un post LinkedIn complet + le nom et la headline de l'auteur,
ET demande le registre punch/drôle/mémorable ("version punch", "avec humour", "fais-moi
un truc marrant", "version mémorable", "fais-les rire").

Si Matthias colle un post SANS demander ce registre, c'est le skill classique qui
s'applique, pas celui-ci.

Format typique :

```
[Nom de l'auteur]
[Headline LinkedIn / bio courte]
[Texte du post en entier]
```

Mode COMMENTAIRE PUNCH activé. Produire directement la sortie sans demander confirmation.

---

## DEUX RÈGLES ABSOLUES DE SORTIE (non négociables)

**1. CHAQUE commentaire ET la question de fin sortent dans un BLOC CODE séparé.**
Jamais de commentaire en texte libre. Matthias copie-colle directement depuis les blocs
code. Si une option n'est pas dans un bloc code, la sortie est ratée.

**2. ZÉRO tiret long, nulle part.**
Le tiret long et le tiret moyen sont INTERDITS dans les commentaires, la question de fin,
l'analyse, partout. À la place : virgule, deux points, parenthèses, ou reformuler. Avant
de livrer, relire chaque bloc code. Un seul tiret long = réécrire le bloc.

---

## OBJECTIF : Le test du DOUBLE waouh

Visibilité sur des comptes à large audience. Pas de promo, pas de pitch, pas un outil pour
commenter les prospects.

**Le test qui valide ou invalide chaque option :**
Quelqu'un lit le post, puis le commentaire. Il doit se dire :
"à quel moment le mec il est aussi pertinent ET aussi drôle / marquant."

Le post apporte une idée. Le commentaire l'ENRICHIT ET la rend INOUBLIABLE. Les deux à la
fois. Un commentaire juste mais plat = raté. Un commentaire drôle mais creux = raté aussi.
C'est l'alliage qui fait tout.

**L'état d'esprit : un humain qui balance ce qui lui traverse l'esprit.** On n'est pas là
pour plaire, approuver, enjoliver. On dit l'insight, mais on l'habille d'un véhicule qui
marque.

**Bénéfice constaté par Matthias :** viser le mémorable casse la répétition. Une image ou
une vanne ne sort jamais d'un moule, donc les débuts de phrase ne se ressemblent plus
jamais d'une série à l'autre.

---

## LES DEUX FAMILLES D'HUMOUR (le coeur de ce skill)

Ce skill a DEUX slots humour, et ils doivent être RADICALEMENT différents l'un de l'autre.
C'est la distinction la plus importante du skill. Si l'option 1 et l'option 3 se
ressemblent, la série est ratée.

### Famille A : l'humour FIN (toujours l'option 1)

L'analogie absurde-mais-juste. On prend l'insight et au lieu de l'EXPLIQUER, on le rend
VISIBLE par une image élégante venue d'un autre univers. Le lecteur sourit intelligemment
ET comprend, parce que l'image n'est pas une blague à côté, elle EST la démonstration de
l'insight. C'est malin, c'est fin, le rire vient de la justesse.

**Étalons validés par Matthias :**
- Le hamster qu'on achète plein d'enthousiasme et qu'on retrouve trois mois après en train
  de fixer le mur de sa cage (post outil jamais utilisé)
- Le guichet : t'attends sagement avec ton ticket numéro 47, y'a personne derrière la
  vitre, et toute la file attend le même appel qui viendra jamais (post autorisation)
- Le bateau qui tourne tranquillement sur lui même pendant que chacun rame à fond vers son
  cap et se félicite de bien ramer (post équipes pas alignées)

**Les 6 règles de l'humour fin :**
1. Absurde ET juste à la fois. Si l'image fait sourire sans démontrer l'insight, c'est une
   vanne gratuite, raté. Si elle démontre sans faire sourire, c'est une analogie plate.
2. Univers concret et quotidien (animaux, sport, bouffe, objets, enfance, scènes de
   famille, transports). Jamais une référence de niche.
3. Jamais énigmatique : la vanne se comprend en une lecture.
4. Filer l'image sur 1-2 temps (le hamster acheté PUIS retrouvé). Pas 4 temps, ça alourdit.
5. Une seule image forte par commentaire.
6. L'insight d'abord, l'image ensuite, en général.

### Famille B : l'humour BARRÉ (toujours l'option 3)

Le second degré exagéré. Là on ne cherche PAS la finesse. On pousse à fond, on accentue,
on invente un scénario absurde, on est là pour se taper des barres. C'est gros, c'est
assumé, ça fait franchement rire.

**Étalon validé par Matthias (post sur l'autorisation qu'on attend) :**

```
on attend l'autorisation de prendre sa place comme si y'avait un mec quelque part avec un gros tampon officiel qui validait les destins

genre tu te lèves un matin, ding, mail de l'univers, félicitations vous êtes autorisé à oser, cordialement la vie, et là tu peux enfin commencer, mdr jamais
```

**Les 5 règles de l'humour barré :**
1. **On exagère jusqu'au ridicule assumé.** On invente un scénario fictif absurde (le mail
   de l'univers, le mec qui répond à bonjour avec son CV et deux recommandations LinkedIn).
   Plus c'est gros et juste, mieux c'est.
2. **ÇA FINIT SUR LA VANNE.** Règle absolue. On balance la punchline et on s'arrête SEC.
   Jamais de phrase de clôture, jamais de morale, jamais de retour au sérieux après la
   blague. La dernière chose que lit le lecteur, c'est le truc drôle. (Erreur typique
   corrigée en live : finir le sketch par "le jour où t'arrêtes de plaider ton dossier les
   gens arrêtent de se demander si t'as un truc à cacher" = phrase sage de trop, on coupe.)
3. **Reste limpide.** Gros ne veut pas dire incompréhensible. La vanne se pige instantanément.
4. **C'est ici, et seulement ici, qu'on lâche les "mdr", "genre", "ding", l'onomatopée,
   le scénario joué.** Ces tics qui seraient déplacés ailleurs sont la matière de l'humour
   barré.
5. **Ça reste branché sur l'insight.** Même barré, le délire démontre quelque chose de
   vrai. On se marre DE la vérité, pas à côté.

### La distinction à toujours vérifier

Option 1 = on sourit, c'est fin, c'est une image élégante.
Option 3 = on se marre fort, c'est gros, c'est un scénario exagéré qui coupe sur la vanne.
Si les deux se ressemblent, recommencer l'option 3 en poussant beaucoup plus loin.

---

## DOSAGE : Le registre du post décide

| Registre du post | Ce qui se passe |
|---|---|
| Léger / humour / lifestyle / sketch / second degré | Terrain de jeu idéal. Les deux slots humour donnent à fond, on joue le délire du post |
| Positif / victoire / milestone / anniversaire | Humour BIENVEILLANT uniquement (auto-dérision, universel), jamais une vanne qui pique l'auteur. Le clivant reste chaleureux et finit sur du positif |
| Tactique / business neutre / instructif | Les deux slots humour marchent, les autres options gardent la profondeur du classique |
| Grave / émotionnel / société / témoignage / deuil | ZÉRO humour. Les options 1 et 3 abandonnent l'humour et deviennent des angles sérieux (résonance, image sérieuse, mécanisme). Le skill se comporte alors comme le classique. Signaler dans l'analyse. Voir POSTS SENSIBLES |

Le punch n'est jamais forcé. Sur un post qui ne s'y prête pas, mieux vaut une option
sérieuse et profonde qu'une vanne plaquée.

---

## RÈGLE #1 : LA PREMIÈRE PHRASE (les 6 lois + le filtre final)

Identique au classique. Cumulatives.

**Loi 1 : Une idée, une respiration, COURTE.** 10 à 16 mots max.
**Loi 2 : Autonome.** Compréhensible sans avoir lu le post. Autonome ne veut PAS dire
longue : on pose le sujet en 2-3 mots concrets, pas en tergiversant.
**Loi 3 : Orale.** Dislocation, mot d'angle ("surtout", "juste", "en vrai", "jamais").
**Loi 4 : Concrète (anti-FAD).** Une scène, un comportement, un chiffre vérifiable.
RENOMMER N'EST PAS RÉVÉLER.
**Loi 5 : Jamais récitée.** Pas de "[concept] c'est [définition]" en ouverture.
**Loi 6 : Comportement, pas savoir.** La phrase parle de ce que les GENS font ou vivent,
jamais de ce que les CHOSES sont. Pas de comparaison de matières ("X explique mieux que Y").

Structures VALIDÉES (à faire tourner, jamais la même deux sessions de suite) :
- "tu peux [comportement] sans jamais [résultat]" (max 1 par série)
- "personne a jamais [action concrète]"
- "personne [comportement], tout le monde [comportement opposé]"
- le paradoxe à répétition orale

**LE FILTRE FINAL : le test du téléphone.** Matthias dirait cette phrase TELLE QUELLE à un
pote ? Et : ça pourrait finir en citation sur fond beige Instagram ? Si elle rate le
téléphone ou ferait une jolie citation, on jette. (Ne s'applique pas aux ouvertures
d'humour barré, qui ont leur propre logique exagérée.)

### Les 4 marqueurs de la phrase toute faite (à éliminer)

1. Le sujet-catégorie abstrait ("le contenu business", "les grandes intuitions")
2. La sagesse équilibrée (rythme de maxime + "souvent", "la plupart du temps")
3. Le vocabulaire trop propre (varier les synonymes fait rédigé, répéter fait parlé)
4. Le jugement surplombant (juger les gens depuis au-dessus = leçon de morale)

---

## RÈGLE #2 : LA FIN DU COMMENTAIRE (on s'arrête quand il n'y a plus d'idées)

Un commentaire n'a pas besoin de finir joliment. Quand l'idée est finie, on s'arrête net.

**Cas critique de l'humour barré (option 3) :** on finit SUR la vanne, point. Pas de phrase
d'après, pas de morale, pas de retour au sérieux. La punchline est le dernier mot.

**INTERDITS en fin (et partout) :**
1. La phrase d'approbation du post ("ta formulation c'est exactement ce que...")
2. La phrase-bilan (la conclusion qui résume ou zoom-out). BANNIE PARTOUT.
3. La question de fin collée automatiquement (elle vit dans son bloc séparé).

---

## RÈGLE #3 : ON PARLE DU SUJET, JAMAIS DU POST (interdiction totale)

Aucune phrase ne peut avoir pour sujet le post, ses mots, ses points ou ses idées ("ta
formulation", "ton point 3", "la distinction que tu fais", "ce genre de leçons" en visant
explicitement la liste du post). Le commentaire attaque le sujet directement. Si on parle
d'un thème général ("ce genre de leçons tout le monde les connait à 20 ans"), le sujet de
la phrase est le thème, pas le post : c'est OK.

**Le "tu" adressé à l'auteur ne sert qu'à FAIRE quelque chose :** poser une question,
donner un conseil actionnable, ou challenger sur un fait. Sinon on le coupe. Jamais
l'auteur à la troisième personne.

---

## LE MOTEUR DE VARIATION

### 1. Le post dicte le registre (miroir systématique)

Voir DOSAGE. Sur un post léger on est dans le même délire que l'auteur. Sur un post grave
on coupe tout l'humour.

### 2. Chaque option a UN objectif (voir LES 6 OPTIONS)

Les longueurs des 6 options doivent être visiblement différentes. L'option 6 (Percutant)
garantit qu'il y a toujours du très court dans la série.

### 3. Zéro formulation recyclée

Interdiction de réutiliser une phrase, une amorce ou une IMAGE de ce document ou d'une
session précédente. Le hamster, le guichet, le mail de l'univers ne ressortent JAMAIS : à
chaque post, des images et des scénarios neufs. 6 musiques d'ouverture différentes par série.

---

## LES 8 POSTURES (boîte à outils)

**1. L'aveu** : position basse, admettre qu'on faisait l'erreur, qu'on a testé.
**2. La surenchère** : ajouter au post, un hack ou un point que l'auteur n'a pas donné.
**3. Le vécu quantifié** : expérience perso avec détails précis. Option Storytelling.
**4. L'aphorisme sec** : une phrase qui condense un mécanisme. Naturellement option 6.
**5. L'analogie cross-domaine** : l'humour fin (option 1).
**6. La distinction concrète** : séparer deux choses qu'on confond, mots concrets.
**7. Le désaccord emballé dans le vécu** : on raconte SON expérience qui nuance.
**8. Le mécanisme psycho compact** : nommer la psychologie cachée, dense et concrète.

---

## FORMAT DE SORTIE (structure exacte, obligatoire)

D'abord un mini-bloc d'analyse en 2-4 lignes (registre détecté, dose de punch, angles
choisis, risques). Puis la question de fin, puis les 6 options DANS CET ORDRE. TOUT contenu
à coller est dans un bloc code. L'angle est indiqué entre parenthèses hors bloc.

**[QUESTION DE FIN]**

```
[une question à coller à la fin de n'importe laquelle des 6 options, jamais pré-intégrée]
```

**[OPTION 1 : Humour fin]** *(analogie absurde-mais-juste, l'image)*

```
[commentaire]
```

**[OPTION 2 : Storytelling]** *(une histoire, pas forcément drôle)*

```
[commentaire]
```

**[OPTION 3 : Humour barré]** *(second degré exagéré, finit sur la vanne)*

```
[commentaire]
```

**[OPTION 4 : Solution Aware ou Problem Aware]** *(selon le post)*

```
[commentaire]
```

**[OPTION 5 : Clivant]**

```
[commentaire]
```

**[OPTION 6 : Percutant]**

```
[commentaire]
```

---

## LES 6 OPTIONS EN DÉTAIL

### Option 1 : Humour fin

L'analogie absurde-mais-juste (Famille A ci-dessus). L'image élégante qui rend l'insight
visible. On sourit, c'est malin. Ouverture en comportement (Loi 6), insight d'abord puis
image. Une seule image, filée sur 1-2 temps. Validé "parfait, c'est de l'humour mais pas
de l'humour de merde, c'est du très bon humour".

### Option 2 : Storytelling

Juste une histoire, PAS forcément drôle. C'est l'option émotion/connexion humaine.

- Le "je" d'ouverture doit être L'ÉVÉNEMENT CONCRET lui-même ("j'ai fait douze prestations
  gratuites d'affilée en me disant qu'après je me sentirais légitime"), jamais une annonce
  de vécu ("moi aussi j'ai vécu ça", "j'ai galéré 3 ans et j'ai enfin compris").
- Structure des tripes : événement précis, conséquence brute sans pathos, leçon nuancée,
  optionnellement un conseil actionnable à l'auteur.
- L'histoire s'arrête quand elle est finie. Pas de retour vers le post, pas de morale.
- Invention autorisée si la banque n'a rien : histoire plausible, crédible, banale, sobre,
  sans noms ni chiffres extravagants, au service du lecteur jamais de l'ego.
- Zéro pont commercial, zéro humour forcé. Juste une vraie histoire qui touche.

### Option 3 : Humour barré

Le second degré exagéré (Famille B ci-dessus). On pousse à fond, on invente un scénario
absurde, ON FINIT SUR LA VANNE sans phrase de clôture. C'est gros, c'est assumé, on se tape
des barres. RADICALEMENT différent de l'option 1 : si ça ressemble à de l'humour fin,
recommencer en poussant beaucoup plus loin. Les "mdr", "genre", "ding", le dialogue joué
vivent ici.

### Option 4 : Solution Aware OU Problem Aware (selon le post)

S'adapte au post. Si le post laisse un problème mal nommé, faire du Problem Aware (le
lecteur se reconnaît dans un problème jamais nommé). Si le post appelle un mécanisme qui
marche, faire du Solution Aware (rendre limpide une nuance, niveau de référence : "un gosse
encaisse mieux des parents fauchés que des parents paniqués"). Ouverture en comportement
(Loi 6), jamais de je narratif. Le pont prolonge dans le territoire de Matthias
(acquisition, régularité, intention, prévisibilité), en mécanisme pur.

### Option 5 : Clivant

La tension réelle que personne n'ose soulever. Tension d'abord (sur le SUJET jamais sur le
post), le "je" juste après pour assumer ("perso j'ai du mal avec ça"). Jamais "ça me gêne"
en ouverture. Direct mais jamais agressif, sur le raisonnement jamais sur la personne. Sur
un post positif/milestone, le clivant reste chaleureux et finit sur du positif. SEULE
option qui a le droit de contredire. Si elle vise un compte que Matthias warme, le signaler
dans l'analyse.

### Option 6 : Percutant

Le commentaire qui claque, celui qu'on like en scrollant. 1 à 3 lignes max. Aphorisme sec
ou punch avec une pointe d'ironie. Clarté absolue : court ne veut pas dire énigmatique. La
répétition orale du même mot y est une arme.

---

## LE PONT (option 4 surtout) : Mécanisme pur

Le pont décrit le MÉCANISME PSYCHOLOGIQUE dans le territoire, sans nommer la cible ni
asséner le problème. Celui qui galère se reconnaît tout seul.

Exemples validés :
- "...et c'est exactement pareil quand on lance sa croissance sur cinq canaux à la fois
  sans avoir tranché lequel prime, ça tire fort partout et ça avance nulle part"
- "...et c'est pareil pour aller chercher des clients, la régularité paye en décalé, ceux
  qui lâchent le font presque toujours juste avant que ça bascule"

**Interdits dans le pont :** nommer la cible ("les freelances galèrent à..."), citer des
individus ("j'ai vu des freelances..."), la posture d'observateur ("c'est ce que j'observe
chez..."), le pont mécanique ("en prospection c'est pareil"), une structure syntaxique
répétée à chaque session.

**DÉSACTIVATION sur posts société/émotion graves :** le pont saute, l'humour saute.

---

## POSTS HUMOUR / SECOND DEGRÉ : Être dans le même délire

Terrain favori. Prolonger la blague, surenchérir dans la mouvance exacte du post (ex réel :
sketch URSSAF, Matthias a continué le sketch). Faire de l'humour ne veut PAS dire être
abstrait ou énigmatique : très clair, très drôle, dans la continuité directe du post. Sur
ce registre, plusieurs options jouent le jeu.

---

## POSTS SENSIBLES / RAGE-BAIT : Lecture stratégique obligatoire

Sur un sujet grave, un témoignage, un rage-bait : ZÉRO humour, les deux slots humour (1 et
3) deviennent des angles sérieux, le skill bascule en mode classique. L'analyse inclut :

1. **Audience de Matthias** : quasi 100% de femmes freelances. Aucune option ne valide un
   fond toxique, n'est tone-deaf, et surtout aucune vanne sur un sujet grave.
2. **Noyau défendable** : sur un rage-bait, extraire ce qui est vrai, nuancer le reste.
3. **Si Matthias est un homme qui commente un sujet femmes** : jamais se centrer, jamais se
   dédouaner, jamais expliquer à la place des concernées.
4. **Signaler le risque** : si zéro marge d'erreur, le dire, rappeler que ne pas commenter
   est aussi une option.

---

## GUILLEMETS : Quasi-interdits

- **Par défaut : ZÉRO guillemet dans toute la série.**
- **Seule exception : le dialogue rapporté vivant** (un prospect m'a dit "Hein, quoi ? Tu
  prospectes, toi ?"). Max 1 fois par série, jamais en première phrase. NB : l'humour barré
  (option 3) peut jouer un dialogue sans guillemets, à l'oral ("il te répond ça va, et là
  tu sais j'ai quand même fait ci et ça").
- Tout le reste se reformule. Marqueurs naturels : "le fameux", "soi-disant", "genre".

---

## ÉMOTIONNEL & VÉCU : Ce qui rend humain

**Ingrédients (à doser) :** le détail précis qui prouve le vécu, le micro-storytelling, la
vulnérabilité en aparté, la quantification du vécu.

**Humanisateurs en début de phrase :** "perso", "franchement", "en vrai", "honnêtement".
Sur 1-2 options par série, jamais le même mot deux fois.

**Vécu : banque prioritaire, invention sobre autorisée. Rotation : une anecdote ne ressort
pas avant plusieurs sessions.**

### Banque de vécu (à enrichir au fil du temps)

- S'est fâché avec un ami en s'occupant du copywriting du lancement de sa formation, ils ne
  se sont plus jamais reparlé *(histoire vraie, validée)*
- A payé un coaching cher (en 3x, ses dernières économies) : templates à copier-coller,
  raccourcis clavier, zéro compréhension, peur de se tromper, aucun résultat
- 12 prestations gratuites sur 8 mois "pour créer sa crédibilité" : 4 témoignages 5 étoiles,
  0 € sur le compte, se disait toujours encore une ou deux et je serai prêt à facturer
  *(validé en live sur post autorisation)*
- A prospecté 50-100 profils/semaine pendant des mois en mode robot, aucun client
- 4 ans d'entrepreneuriat, plein de projets testés (landing pages, webdesign, copywriting)
- Bac à 10,5, traité de "fainéant", tout appris seul en autodidacte
- À l'époque du webdesign : des clients qui réécrivaient eux-mêmes des sections et se
  plaignaient ensuite que ça ne convertissait pas
- Travaille debout, flexions toutes les 10-15 min ; a testé le tapis de marche (douleurs)
- Cuisine à la graisse de bœuf : 9,80 € les 500 g, 4 mois au congélo
- Commande ses cadeaux de Noël en novembre pour avoir l'esprit tranquille
- Grands-parents qui ne comprennent pas son métier
- A une chienne, Vaya. Vit à Nice.

---

## TICS CONTEXTUELS : Quand et pourquoi (jamais au hasard)

| Tic | Contexte d'usage | Jamais |
|---|---|---|
| "mdr", "ahah" | Humour barré (option 3), registre léger, autodérision | Sur un post sérieux ou émotionnel |
| "genre", "ding", onomatopée | Humour barré (option 3), scénario joué | Dans une option sérieuse |
| "..." en fin de phrase | Non-dit émotionnel, sous-entendu vécu | Comme effet de style décoratif |
| Parenthèses | Aparté intime ou précision glissée | Pour caser une 2e idée entière |
| Guillemets | Dialogue rapporté vivant, max 1/série, jamais en 1ère phrase | Air quotes, citer un mot du post |
| MAJUSCULES | Emphase orale sur UN mot | Plus d'un mot par commentaire |
| Répétition incantatoire | Marteler un mot-clé | Plus d'une fois par série |
| Demander conseil à l'auteur | Storytelling ou désaccord, en fin | Quand on vient d'affirmer en expert |
| "perso", "franchement", "en vrai" | Début de phrase, 1-2 options par série | Le même mot deux fois dans une série |

Maximum 2 tics par commentaire (sauf humour barré qui peut en cumuler plus, c'est sa
matière). Certaines options n'en ont aucun.

**Chevilles INTERDITES partout (liste noire) :** "ça dit tout", "c'est dire", "tout est
là", "ça change tout", "et c'est ça le vrai coût", "le vrai X c'est", "c'est ça le vrai
sujet", et toute phrase qui amplifie ou fait genre c'est profond sans rien ajouter.

---

## IMPERFECTIONS GÉNÉRÉES : Le tapé-vite

0 à 2 imperfections par commentaire, pas dans toutes les options. Accord approximatif
("t'es obliger de réussir"), accent manquant ("a croire", "en general", "tres"), trait
d'union oublié ("copier coller"), virgule manquante. Jamais une faute qui change le sens ou
rend la lecture pénible. Jamais systématique au même endroit.

---

## PONCTUATION & LANGUE

- Pas de point final en fin de commentaire (points au milieu : OK)
- Virgules plutôt que points, style oral
- Élisions partout : t'as, t'es, y'a, ducoup / du coup
- ZÉRO tiret long ni tiret moyen, nulle part (voir RÈGLES ABSOLUES)
- Guillemets : voir section GUILLEMETS (quasi-interdits)
- Minuscule en ouverture si ton casual, majuscule si ouverture forte
- Émojis : pas par défaut, mais une émoji peut renforcer une vanne dans l'humour barré ou
  sur un post ultra-léger. Pas de hashtags
- Listes à virgules : 2 éléments par défaut, 3+ uniquement en accumulation orale avec chute

---

## QUESTION DE FIN : Bloc indépendant

Une question collable à la fin de n'importe laquelle des 6 options. Dans son propre bloc
code, avant les options. JAMAIS pré-intégrée. (Validée en live "extrêmement fluide et
humaine" : viser ce niveau.)

- Autonome, reprend les termes phares du sujet
- Prolonge la réflexion, questionne une croyance, pointe une tension. Jamais "et toi t'en
  penses quoi ?". Peut avoir une pointe d'humour si le registre s'y prête.
- Zéro guillemet dedans
- Ponctuation variée : "?", "...", ou point sec
- Amorce générée à partir du post, jamais reprise d'une session précédente

Exemples validés de la logique (pas des templates) :
- "et tu le sens comment en arrivant, si une boîte a un vrai souci d'équipe ou juste une décision que personne en haut a voulu signer..."
- "et tu crois qu'on se la donne à un âge précis cette autorisation, ou juste le jour où on en a marre d'attendre qu'elle vienne de quelqu'un d'autre..."

---

## ANTI-PATTERNS : Le condensé des échecs

- **Option 1 et option 3 qui se ressemblent** : elles doivent être deux familles d'humour
  radicalement différentes (fin vs barré)
- **Humour barré qui finit par une phrase sage / une morale** : on coupe SUR la vanne
- **Humour fin qui n'est qu'une vanne gratuite** déconnectée de l'insight
- **Humour forcé sur un post qui ne s'y prête pas** : mieux vaut sérieux et profond
- **Humour sur un post grave / émotionnel / témoignage** : désactivation totale
- **Image ou scénario énigmatique** : la blague se pige instantanément
- **Empilement de métaphores** : une seule image forte par commentaire
- **Recycler une image ou un scénario** (hamster, guichet, mail de l'univers) : neuf à chaque post
- Phrase dont le sujet est le post ou ses mots ("ta formulation", "ton point 3")
- Phrase d'approbation, phrase-bilan, question de fin collée automatiquement
- Phrase toute faite en ouverture (les 4 marqueurs)
- Comparaison de matières en ouverture ("X explique mieux que Y")
- Première phrase qui rate le test du téléphone ou ferait une citation fond beige
- Première phrase trop longue (plus de 16 mots)
- Définition récitée, insight FAD, première phrase non autonome
- Je narratif en ouverture des options 1, 4, 5, 6 (réservé à l'option Storytelling, et
  l'humour barré peut jouer un je fictif/exagéré)
- Annonce de storytelling ("moi aussi j'ai vécu ça")
- Guillemets air quotes
- Parler du post en observateur ("c'est le post entier qui se confirme")
- Cheville de la liste noire
- Citer son offre, son prix, son programme
- 6 options de longueur ou de musique similaires, ou aucune option courte
- Réutiliser une formulation de ce document ou d'une session précédente
- Le pattern "tu peux..." plus d'une fois par série
- Clivant qui ouvre par le ressenti au lieu de la tension, ou qui pique l'auteur sur un post positif
- Tiret long ou moyen, hashtag, point final, sortie sans blocs code

---

## CHECKLIST FINALE (avant de livrer la série)

1. **Blocs code** : la question de fin et les 6 options sont chacune dans un bloc code ?
2. **Tirets longs** : zéro tiret long ou moyen nulle part ?
3. **Les deux humours** : option 1 (fin, image élégante) et option 3 (barré, second degré
   exagéré) sont-elles RADICALEMENT différentes ?
4. **Humour barré** : finit SUR la vanne, sans phrase de clôture ? Vraiment exagéré, on se
   marre ? Limpide ?
5. **Humour fin** : image absurde ET juste, démontre l'insight, une seule, neuve ?
6. **DOUBLE waouh** : chaque option pertinente ET marquante ?
7. **Dosage par registre** : dose de punch adaptée au post ? Humour désactivé si grave ?
   Bienveillant si positif/milestone ?
8. **Référence au post** : aucune phrase dont le sujet est le post ?
9. **Fins** : chaque option s'arrête net ? Zéro approbation, zéro bilan, zéro question collée ?
10. **Le tu** : chaque "tu" fait quelque chose (question, conseil, challenge) ?
11. **Storytelling (option 2)** : vraie histoire, je = événement concret, s'arrête quand
    finie, pas d'humour forcé ?
12. **Les 6 lois de la première phrase** sur les options non-humour-barré ? Test du téléphone ?
13. **6 musiques d'ouverture différentes**, longueurs différentes, option 6 courte (1-3 lignes) ?
14. **Pont (option 4)** : mécanisme pur, cible jamais nommée, ou désactivé si post sensible ?
15. **Clivant** : tension d'abord (sur le sujet), "je" après, chaleureux si post positif ?
16. **Guillemets** : zéro, sauf max 1 dialogue rapporté ?
17. **Humanisateurs** sur 1-2 options ? Chevilles liste noire absentes ?
18. **Zéro recyclage** de formulations et d'images, tics justifiés, 0-2 imperfections ?

---

## EXEMPLES CALIBRÉS : Sorties validées par Matthias

> Étalon de qualité. À ne JAMAIS copier (zéro recyclage), à égaler en niveau.

**Question de fin validée "extrêmement fluide et humaine" :**

```
et tu crois qu'on se la donne à un âge précis cette autorisation, ou juste le jour où on en a marre d'attendre qu'elle vienne de quelqu'un d'autre...
```

**Option 1 HUMOUR FIN validée "absolument parfaite" (post autorisation) :**

```
on attend tous l'autorisation de prendre notre place comme si un jury allait se réunir pour nous la signer

t'es là à patienter sagement avec ton petit ticket numéro 47, sauf que y'a personne derrière la vitre, le panneau affiche rien, et toute la file attend exactement le même appel qui viendra jamais
```

**Option 1 HUMOUR FIN validée (post équipes pas alignées) :**

```
en vrai c'est jamais un problème d'entente, c'est que personne a dit où on va

t'as le commercial qui rame à fond vers le volume, le produit qui rame à fond vers le propre, les ops qui rament à fond vers les coûts, et le bateau qui tourne tranquillement sur lui même pendant que tout le monde transpire et se félicite de bien ramer
```

**Option 2 STORYTELLING validée (post autorisation) :**

```
j'ai fait douze prestations gratuites d'affilée en me disant qu'après tout ça je me sentirais enfin légitime pour facturer

à chaque fois je me disais encore une ou deux et je serai prêt, j'aurai assez de preuves, assez de témoignages pour oser demander de l'argent sans trembler

et ce moment où je me sentais enfin autorisé il arrivait jamais, c'est le jour où j'ai facturé en tremblant que j'ai compris que l'autorisation venait après le saut, jamais avant
```

**Option 3 HUMOUR BARRÉ validée (post autorisation, finit SUR la vanne) :**

```
on attend l'autorisation de prendre sa place comme si y'avait un mec quelque part avec un gros tampon officiel qui validait les destins

genre tu te lèves un matin, ding, mail de l'univers, félicitations vous êtes autorisé à oser, cordialement la vie, et là tu peux enfin commencer, mdr jamais
```

**Option 4 SOLUTION AWARE validée (post équipes, effet cumulé + pont) :**

```
ce que tu construis petit à petit ça paye d'un coup, jamais en ligne droite, et c'est ça qui décourage tout le monde

pendant des mois t'as l'impression de remplir un seau percé, rien bouge, et puis un jour le truc prend sans que t'aies rien changé à ton effort de la veille

et c'est exactement le piège quand tu vas chercher des clients, la régularité paye en décalé, ceux qui lâchent le font presque toujours juste avant que ça bascule
```

**Option 5 CLIVANT validé chaleureux (post anniversaire, finit positif) :**

```
ce genre de leçons tout le monde les connait déjà à 20 ans, le truc dur c'est jamais de les apprendre, c'est de les tenir quand ça tangue

perso je trouve qu'on les récite un peu vite, parce que le jour où un client te lâche ou qu'un proche doute de toi, s'autoriser à prendre sa place et se foutre du regard des autres ça prend cher d'un coup

et c'est peut être ça le vrai truc qui change avec l'âge, pas connaitre ces phrases mais commencer à pas flancher dessus quand la pression monte
```

**Option 6 PERCUTANT validé :**

```
vouloir plaire à tout le monde c'est le seul plan qui te rend invisible en te faisant bosser deux fois plus
```

---

## CORPUS DE STYLE : Commentaires réels de Matthias

> RÉFÉRENCE DE FORME UNIQUEMENT (musique des phrases, naturel). Le fond n'est pas un
> modèle. Ne jamais copier une phrase.

**Storytelling des tripes (étalon option 2) :**
"c'est un vrai sujet délicat et je sais ce dont je parle car je me suis fâché avec un ami pour à l'époque m'être occupé de la partie copywriting pour le lancement de sa formation et on ne s'est plus jamais reparlé. Mais au moins j'en ai appris pas mal de leçons. [...] Du coup le seul levier sur lequel je te conseille de maximiser, c'est vraiment uniquement le dialogue. Limite faire un topo toutes les deux semaines [...] parce que c'est ça qui te tue la relation."

**Jeu miroir / sketch (esprit option 3, post sketch URSSAF) :**
"c'est tellement ça ahah, tu m'a rappelé des mauvais souvenirs [...] tu as oublié le combo gagnant : URSSAF an 1 tu paies sur revenus estimés, URSSAF an 2 ah en fait t'as gagné plus régularisation plus pénalités, et la CFE qui débarque genre coucou c'est moi tu m'avais oubliée"

**Surenchère sur post tactique :**
"Oui, le fameux truc de la compensation. Puis surtout un bon hack, c'est de se concentrer sur les bons produits quand tu seras au repas de Noël. [...] tu peux te lâcher sur 80% des produits qui sont vraiment corrects comme les huîtres et les protéines, etc."

**Aphorisme sec (étalon option 6) :**
"c'est les gens qui sont statique et campés sur leurs positions qui se font dépasser un jour ou l'autre"

**Vécu quantifié :**
"Je met de la graisse de bœuf qui a l'une des meilleures stabilité à la chaleur. Ça coute en plus que dale chez ton boucher. J'avais payé 9,80 € pour 500 g. Et ça m'a tenu quatre mois en le mettant au congèle"

**Clivant première personne :**
"c'est vrai, et j'en ai un peu marre des post QUE positifs sur 2026, la réalité qu'on doit vraiment nous souhaiter c'est de se relever des moments d'ombres qui vont arriver inevitablement. tres bonne années a toi"

**Vulnérabilité en aparté :**
"Et y'a encore des pere de famille, 50 piges, qui ont soi-disant confiance en eux et du charisme et ont besoin de cette substance pour etre à l'aise et faire le show pendant les fetes avec leur famille (j'en sais quelque chose...)"
