#!/usr/bin/env python3
"""
Build TRONC_CENTRAL_Yadulink_v2.docx from v1
Rebuilt version with truncation at Bloc 4B (BLOC 4 — RÈGLES SUR LES QUESTIONS)
"""
import zipfile
import shutil
import lxml.etree as etree
import re
import copy
import os

SRC = '/root/.claude/uploads/065cbdc2-3d76-4c0b-8d15-81ccc54bb9fb/17fd0a20-TRONC_CENTRAL_Yadulink_1.docx'
DST = '/home/user/Take20simpson/TRONC_CENTRAL_Yadulink_v2.docx'

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'

shutil.copy2(SRC, DST)

# Read all files from the docx
with zipfile.ZipFile(DST, 'r') as z:
    names = z.namelist()
    files = {n: z.read(n) for n in names}

# Parse document.xml
doc_xml = etree.fromstring(files['word/document.xml'])

# ─────────────────────────────────────────────────────────
# Helper functions
# ─────────────────────────────────────────────────────────
def para_text(p):
    return ''.join(t.text or '' for t in p.findall(f'.//{{{W}}}t'))

def get_para_elem(doc_xml, search_str):
    """Find first paragraph element containing search_str"""
    for p in doc_xml.findall(f'.//{{{W}}}p'):
        if search_str in para_text(p):
            return p
    return None

def set_para_text(p, new_text):
    """Replace text of a paragraph: consolidate into first run, clear others"""
    runs = p.findall(f'{{{W}}}r')
    if not runs:
        r = etree.SubElement(p, f'{{{W}}}r')
        t = etree.SubElement(r, f'{{{W}}}t')
        t.text = new_text
        t.set(XML_SPACE, 'preserve')
        return
    first_run = runs[0]
    t_elems = first_run.findall(f'{{{W}}}t')
    if t_elems:
        t_elems[0].text = new_text
        t_elems[0].set(XML_SPACE, 'preserve')
        for t in t_elems[1:]:
            first_run.remove(t)
    else:
        t = etree.SubElement(first_run, f'{{{W}}}t')
        t.text = new_text
        t.set(XML_SPACE, 'preserve')
    for r in runs[1:]:
        for t in r.findall(f'{{{W}}}t'):
            r.remove(t)

def make_paragraph_like(ref_para, text):
    """Create a new paragraph element with same style as ref_para, with given text"""
    new_p = etree.Element(f'{{{W}}}p')
    pPr = ref_para.find(f'{{{W}}}pPr')
    if pPr is not None:
        new_p.append(copy.deepcopy(pPr))
    runs = ref_para.findall(f'{{{W}}}r')
    rPr = None
    if runs:
        rPr = runs[0].find(f'{{{W}}}rPr')
    r = etree.SubElement(new_p, f'{{{W}}}r')
    if rPr is not None:
        r.append(copy.deepcopy(rPr))
    t = etree.SubElement(r, f'{{{W}}}t')
    t.text = text
    t.set(XML_SPACE, 'preserve')
    return new_p

def insert_paragraph_after(ref_para, new_para):
    """Insert new_para after ref_para in the XML tree"""
    parent = ref_para.getparent()
    idx = list(parent).index(ref_para)
    parent.insert(idx + 1, new_para)

# ─────────────────────────────────────────────────────────
# STEP 0: Truncate document at Bloc 4B (BLOC 4 — RÈGLES SUR LES QUESTIONS)
# Remove all paragraphs from para 703 onwards (i.e. from "BLOC 4 — RÈGLES SUR LES QUESTIONS")
# ─────────────────────────────────────────────────────────
body = doc_xml.find(f'.//{{{W}}}body')
all_paras = doc_xml.findall(f'.//{{{W}}}p')

# Find the truncation point: first paragraph with "BLOC 4 — RÈGLES SUR LES QUESTIONS"
truncate_para = None
for p in all_paras:
    txt = para_text(p)
    if 'BLOC 4' in txt and 'RÈGLES SUR LES QUESTIONS' in txt:
        truncate_para = p
        break

if truncate_para is None:
    # Fallback: find the paragraph right after last Bloc 4A content
    # Last Bloc 4A paragraph should be just before BLOC 4 — ...
    print("WARNING: Could not find 'BLOC 4 — RÈGLES SUR LES QUESTIONS', trying fallback...")
    for p in all_paras:
        txt = para_text(p)
        if 'SUJETS À ÉVITER' in txt and 'affinée par le testing' in txt:
            # The next sibling after this section
            pass

removed_count = 0
if truncate_para is not None:
    # We need to find which element in the body (or its children) to start removing from
    # The paragraphs might be direct body children or nested in w:body
    # Get the parent of truncate_para
    trunc_parent = truncate_para.getparent()
    children_list = list(trunc_parent)
    trunc_idx = children_list.index(truncate_para)

    # Remove from trunc_idx to end (excluding the last sectPr which must stay)
    # Keep the last sectPr element
    last_child = children_list[-1]

    # Collect elements to remove
    to_remove = []
    for i in range(trunc_idx, len(children_list)):
        child = children_list[i]
        # Don't remove sectPr (section properties - last element in body)
        if child.tag == f'{{{W}}}sectPr':
            break
        to_remove.append(child)

    for elem in to_remove:
        trunc_parent.remove(elem)
        removed_count += 1

    print(f"Step 0 done: Truncated document. Removed {removed_count} elements from Bloc 4B onwards.")
else:
    print("Step 0 WARNING: Could not find truncation point!")

# ─────────────────────────────────────────────────────────
# STEP 1: Remove all comment-related elements from document body
# ─────────────────────────────────────────────────────────
for tag in ['commentRangeStart', 'commentRangeEnd', 'commentReference']:
    for el in doc_xml.findall(f'.//{{{W}}}{tag}'):
        parent = el.getparent()
        if parent is not None:
            parent.remove(el)

print("Step 1 done: Removed original comment elements from document.xml")

# ─────────────────────────────────────────────────────────
# STEP 2: Replace all em-dashes with ',' in text elements
# ─────────────────────────────────────────────────────────
count_em = 0
for t in doc_xml.findall(f'.//{{{W}}}t'):
    if t.text and '—' in t.text:
        t.text = t.text.replace('—', ',')
        count_em += 1

# Clean up any double commas
for t in doc_xml.findall(f'.//{{{W}}}t'):
    if t.text:
        t.text = t.text.replace(',,', ',')
        t.text = re.sub(r',\s+,', ',', t.text)

print(f"Step 2 done: Replaced em-dashes with ',' in {count_em} text elements")

# ─────────────────────────────────────────────────────────
# STEP 3: Text Change A — Archétype 5 méfiance paragraph
# ─────────────────────────────────────────────────────────
search_a = "Niveau de méfiance vis-à-vis de la prospection : Élevé à très élevé."
new_text_a = ("Niveau de méfiance vis-à-vis de la prospection : Élevé à très élevé. "
              "Ce niveau s'explique avant tout par le volume de prospection LinkedIn reçu - "
              "un fondateur ou un builder reçoit des dizaines de messages de prospection par semaine. "
              "C'est cette exposition répétée aux patterns qui génère le filtre, pas uniquement le statut "
              "ou l'ancienneté du profil.")

para_a = get_para_elem(doc_xml, search_a)
if para_a is not None:
    set_para_text(para_a, new_text_a.replace('—', ','))
    print("Step 3 done: Text change A applied (Archétype 5 méfiance)")
else:
    print("Step 3 WARNING: Paragraph for text change A not found")

# ─────────────────────────────────────────────────────────
# STEP 4: Text Change B — Add ancienneté note
# ─────────────────────────────────────────────────────────
anciennete_note = ("Note importante : ancienneté sur le métier  ≠  ancienneté sur LinkedIn. "
                   "Un freelance peut avoir 10 ans d'expérience métier et seulement 6 mois d'activité LinkedIn. "
                   "Le signal pertinent pour l'agent est l'ancienneté LinkedIn (exposition à la prospection), "
                   "pas l'ancienneté professionnelle.")

para_anciennete_insert = None
all_paras = doc_xml.findall(f'.//{{{W}}}p')
for i, p in enumerate(all_paras):
    txt = para_text(p)
    if '0 à 18 mois' in txt and 'exposée à la prospection' in txt:
        para_anciennete_insert = p
        break

if para_anciennete_insert is not None:
    new_note_para = make_paragraph_like(para_anciennete_insert, anciennete_note)
    insert_paragraph_after(para_anciennete_insert, new_note_para)
    print("Step 4 done: Text change B applied (ancienneté note)")
else:
    print("Step 4 WARNING: Ancienneté insert paragraph not found")

# ─────────────────────────────────────────────────────────
# STEP 5: Text Change C — verify "6 à 9 heures" (no change needed)
# ─────────────────────────────────────────────────────────
for p in doc_xml.findall(f'.//{{{W}}}p'):
    txt = para_text(p)
    if '6 à 9 heures' in txt:
        print(f"Step 5: Found '6 à 9 heures' - format is correct, no change needed")
        break

# ─────────────────────────────────────────────────────────
# STEP 6: Text Change D — Replace Niveau 3 section in Bloc 4A
# ─────────────────────────────────────────────────────────
niveau3_para = None
all_paras = doc_xml.findall(f'.//{{{W}}}p')
for i, p in enumerate(all_paras):
    txt = para_text(p)
    if 'Niveau 3' in txt and 'challenge léger' in txt:
        niveau3_para = p
        niveau3_idx = i
        break

if niveau3_para is None:
    for i, p in enumerate(all_paras):
        txt = para_text(p)
        if 'Niveau 3' in txt and ('niveau supérieur' in txt or 'supérieur' in txt):
            niveau3_para = p
            niveau3_idx = i
            break

if niveau3_para is not None:
    n3_parent = niveau3_para.getparent()
    n3_parent_children = list(n3_parent)
    n3_in_parent_idx = n3_parent_children.index(niveau3_para)

    # Find paragraphs to remove: from n3 until LONGUEUR section
    paras_to_remove = []
    for idx in range(n3_in_parent_idx, len(n3_parent_children)):
        child = n3_parent_children[idx]
        child_txt = para_text(child) if child.tag == f'{{{W}}}p' else ''
        if idx > n3_in_parent_idx and ('LONGUEUR' in child_txt or 'TEST DE VALIDATION' in child_txt or 'Longueur' in child_txt):
            break
        paras_to_remove.append(child)

    for p in paras_to_remove:
        n3_parent.remove(p)

    new_niveau3_texts = [
        "Niveau 3 : Message ultra-personnalisé par insight profond",
        "",
        "Ce niveau représente le levier de différenciation le plus puissant du système. Un message Niveau 3 bien exécuté ne ressemble à aucun autre message de prospection - il prouve que l'agent a réellement lu et compris les posts du prospect.",
        "",
        "Structure du message Niveau 3 :",
        "",
        "[Question sur leur vision ou leur approche] + parce que [rondeur ancrée dans UN post ou UNE thématique spécifique de leur contenu]",
        "",
        "Extraction des deux variables clés :",
        "",
        "[TA THÈSE] = La conviction forte que le prospect défend dans ses posts. Ce qu'il répète, ce qu'il contre-argumente, ce qu'il enseigne. Sa prise de position distinctive.",
        "",
        "[LE FREIN PRINCIPAL] = L'obstacle ou la croyance que le prospect identifie chez son audience cible. Ce contre quoi il se bat dans son contenu. La résistance qu'il essaie de lever.",
        "",
        "Règle quand il n'y a pas assez d'éléments pour construire l'insight :",
        "",
        "Sous-cas A - Le secteur permet une tension identifiable (freelances, coachs, consultants, fondateurs, etc.) : utiliser une question ancrée dans la tension connue du secteur, sans prétendre avoir lu un post spécifique.",
        "",
        "Sous-cas B - Profil trop générique ou trop peu actif : utiliser une question universelle sur l'acquisition ou la visibilité, formulée de façon ouverte.",
        "",
        "Dans les deux cas, la structure reste : [Question] + parce que [rondeur honnête sans surjouer la personnalisation].",
    ]

    style_ref_para = paras_to_remove[0] if paras_to_remove else etree.Element(f'{{{W}}}p')

    insert_pos = n3_in_parent_idx
    for txt in reversed(new_niveau3_texts):
        if txt == "":
            empty_p = etree.Element(f'{{{W}}}p')
            if style_ref_para is not None:
                ref_pPr = style_ref_para.find(f'{{{W}}}pPr')
                if ref_pPr is not None:
                    empty_p.insert(0, copy.deepcopy(ref_pPr))
            n3_parent.insert(insert_pos, empty_p)
        else:
            new_p = make_paragraph_like(style_ref_para, txt)
            n3_parent.insert(insert_pos, new_p)

    print("Step 6 done: Niveau 3 section replaced")
else:
    print("Step 6 WARNING: Niveau 3 paragraph not found")

# ─────────────────────────────────────────────────────────
# STEP 7: Text Change E — Add 9 sectoral examples after Niveau 3 section
# ─────────────────────────────────────────────────────────
search_e = "sans surjouer la personnalisation"
para_e_ref = None
for p in doc_xml.findall(f'.//{{{W}}}p'):
    if search_e in para_text(p):
        para_e_ref = p
        break

examples_texts = [
    "Exemples par secteur (Niveau 3) :",
    "",
    "Coach business :",
    "Option A : \"C'est quoi ton approche quand un client arrive convaincu que son problème c'est le mindset, alors que toi tu vois clairement que c'est son offre qui est mal positionnée ? parce que j'ai été accompagné par quelqu'un qui m'a forcé à retravailler mon positionnement avant même de toucher à ma façon de penser, et ça a tout changé.\"",
    "",
    "Option B : \"Comment tu fais tenir quelqu'un dans la durée quand les premiers résultats tardent ? parce que j'ai remarqué que dans tes posts tu parles beaucoup d'engagement sur le long terme, et je me demandais ce que ça donnait concrètement côté accompagnement.\"",
    "",
    "Freelance / Assistant virtuel :",
    "Option A : \"C'est quoi ton approche quand un prospect te dit que tu es trop cher mais que tu sens qu'il a vraiment besoin de toi ? parce que dans tes posts tu parles souvent de comment te positionner, et je me demandais comment tu gérais cette tension-là.\"",
    "",
    "Option B : \"Comment tu gères la période creuse entre deux missions ? parce que j'ai l'impression que dans ce que tu partages tu défends l'idée que l'acquisition ça doit être régulier, pas en mode panique.\"",
    "",
    "Option C : \"C'est quoi le truc que tu aurais aimé savoir sur la prospection quand tu as démarré en freelance ? parce que en lisant tes posts j'ai l'impression que t'as traversé pas mal de phases avant de trouver ce qui marche.\"",
    "",
    "Fondateur SaaS :",
    "Option A : \"C'est quoi le moment où tu as réalisé que ce que tu construisais n'était pas ce que tes utilisateurs voulaient vraiment ? parce que je suis le build in public d'un fondateur en ce moment, et ce qui est revenu c'est ce moment où il a réalisé que ses utilisateurs voulaient quelque chose de complètement différent de ce qu'il avait passé des mois à construire.\"",
    "",
    "Option B : \"Comment tu gères l'écart entre ce que tu veux construire et ce que le marché te demande de construire ? parce que dans tes posts tu sembles naviguer constamment entre vision long terme et feedback immédiat.\"",
    "",
    "Webdesigner :",
    "Option A : \"C'est quoi ton approche quand un client veut quelque chose qui va à l'encontre de ce qui est bon pour lui ? parce que j'ai lu un de tes posts où tu parlais de devoir éduquer les clients, et je me demandais comment tu posais ça dans la pratique.\"",
    "",
    "Option B : \"Comment tu justifies tes choix de design à un client qui ne comprend pas pourquoi ça vaut le prix ? parce que j'ai l'impression que dans ce que tu partages tu défends une vision très précise de la valeur du design, et ça m'a intrigué.\"",
    "",
    "Option C : \"C'est quoi le moment dans un projet où tu sens que le client commence à faire confiance à ton jugement plutôt que d'imposer le sien ? parce que dans tes posts tu parles souvent de cette dynamique client-designer, et j'aimerais comprendre comment tu construis ça.\"",
    "",
    "Dirigeant d'agence / Corporate :",
    "Option A : \"C'est quoi votre approche quand une équipe résiste à un changement que vous savez nécessaire ? parce que j'ai suivi plusieurs de vos interventions et ce qui revient c'est cette tension entre ce que le management décide et ce que le terrain est prêt à absorber.\"",
    "",
    "Option B : \"Comment vous gérez l'écart entre la stratégie que vous préconisez et les contraintes politiques internes de vos clients ? parce que j'ai l'impression que dans votre contenu vous défendez une vision assez directe, et je me demandais comment ça se traduisait dans les missions.\"",
]

if para_e_ref is not None:
    style_ref = para_e_ref
    prev_para = para_e_ref
    for txt in examples_texts:
        if txt == "":
            empty_p = etree.Element(f'{{{W}}}p')
            ref_pPr = style_ref.find(f'{{{W}}}pPr')
            if ref_pPr is not None:
                empty_p.insert(0, copy.deepcopy(ref_pPr))
            new_p = empty_p
        else:
            new_p = make_paragraph_like(style_ref, txt)
        insert_paragraph_after(prev_para, new_p)
        prev_para = new_p
    print("Step 7 done: Text change E applied (9 examples added)")
else:
    print("Step 7 WARNING: Reference paragraph for examples not found")

# ─────────────────────────────────────────────────────────
# STEP 8 (pre-comments): Replace "enrobage" with "rondeur" everywhere
# Applied AFTER all content insertions so new text is also covered
# ─────────────────────────────────────────────────────────
count_enrobage = 0
for t in doc_xml.findall(f'.//{{{W}}}t'):
    if t.text:
        original = t.text
        t.text = t.text.replace("l'enrobage", "la rondeur")
        t.text = t.text.replace("l’enrobage", "la rondeur")
        t.text = t.text.replace("Enrobage", "Rondeur")
        t.text = t.text.replace("enrobage", "rondeur")
        if t.text != original:
            count_enrobage += 1

print(f"Step 8 done: Replaced 'enrobage' with 'rondeur' in {count_enrobage} text elements")

# ─────────────────────────────────────────────────────────
# STEP 9: Build new comments.xml with 8 comments
# ─────────────────────────────────────────────────────────

COMMENTS_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
DATE = "2026-03-09T10:00:00Z"

def make_comment_xml(cid, author, lines):
    comment = etree.Element(f'{{{COMMENTS_NS}}}comment')
    comment.set(f'{{{COMMENTS_NS}}}id', str(cid))
    comment.set(f'{{{COMMENTS_NS}}}author', author)
    comment.set(f'{{{COMMENTS_NS}}}date', DATE)
    comment.set(f'{{{COMMENTS_NS}}}initials', author[0].upper())
    for line in lines:
        p = etree.SubElement(comment, f'{{{COMMENTS_NS}}}p')
        r = etree.SubElement(p, f'{{{COMMENTS_NS}}}r')
        t = etree.SubElement(r, f'{{{COMMENTS_NS}}}t')
        t.text = line
        t.set(XML_SPACE, 'preserve')
    return comment

comments_data = [
    (1, "Kevin Ouinsou", [
        "Kevin Ouinsou : Est-ce qu'on peut considérer que le Cas A est le cas le plus fréquent ?",
        "",
        "Matthias : Oui, clairement. Le Cas A représente environ 70-80% des situations. Les profils qui postent régulièrement mais qui n'ont pas encore de système d'acquisition structuré.",
        "",
        "Kevin Ouinsou : OK, ça aide à prioriser le training data 👍",
    ]),
    (2, "Matthias", [
        "Ajout : précision sur l'origine du niveau de méfiance élevé chez l'archétype 5. Ce n'est pas juste le statut, c'est le volume de prospection reçu qui crée le filtre.",
    ]),
    (3, "Matthias", [
        "Ajout : distinction ancienneté métier vs ancienneté LinkedIn. Signal pertinent = exposition à la prospection, pas l'expérience professionnelle.",
    ]),
    (4, "Kevin Ouinsou", [
        "Kevin Ouinsou : Tu as raison, c'est exactement ce qui fait penser à une IA.",
        "",
        "Kevin Ouinsou : C'est top 👍",
    ]),
    (5, "Matthias", [
        "Refonte complète du Niveau 3. C'est l'une des phases les plus importantes du système - un message bien exécuté ici change complètement la perception du prospect.",
        "",
        "Structure validée : [Question] + parce que [rondeur ancrée dans UN post spécifique].",
        "",
        "Les deux variables clés à extraire : [TA THÈSE] et [LE FREIN PRINCIPAL].",
    ]),
    (6, "Matthias", [
        "Règle importante quand le profil ne donne pas assez d'éléments pour construire l'insight. Deux sous-cas : secteur identifiable (tension connue) vs profil trop générique (question universelle).",
    ]),
    (7, "Matthias", [
        "9 exemples sectoriels validés. Structure systématique : question d'abord, rondeur ensuite avec 'parce que'.",
        "",
        "A tester en A/B par niche pour identifier les formulations qui convertissent le mieux - données à remonter à Kevin pour affiner le training data.",
    ]),
    (8, "Matthias", [
        "Règle appliquée sur tout le document : suppression de tous les tirets longs (,). Remplacés par ','. Signal fort d'IA à éliminer.",
    ]),
]

comments_root = etree.Element(f'{{{COMMENTS_NS}}}comments')
for cid, author, lines in comments_data:
    comments_root.append(make_comment_xml(cid, author, lines))

# ─────────────────────────────────────────────────────────
# STEP 10: Attach comments to paragraphs in document.xml
# ─────────────────────────────────────────────────────────

def attach_comment(doc_xml, search_str, cid, exact=True):
    """Find paragraph containing search_str and add comment markers"""
    target_para = None
    for p in doc_xml.findall(f'.//{{{W}}}p'):
        txt = para_text(p)
        if exact:
            if search_str in txt:
                target_para = p
                break
        else:
            if search_str.lower() in txt.lower():
                target_para = p
                break

    if target_para is None:
        print(f"  WARNING: Could not find paragraph for comment {cid} (search: '{search_str[:60]}')")
        return False

    crs = etree.Element(f'{{{W}}}commentRangeStart')
    crs.set(f'{{{W}}}id', str(cid))
    target_para.insert(0, crs)

    cre = etree.Element(f'{{{W}}}commentRangeEnd')
    cre.set(f'{{{W}}}id', str(cid))
    target_para.append(cre)

    r_ref = etree.SubElement(target_para, f'{{{W}}}r')
    rpr = etree.SubElement(r_ref, f'{{{W}}}rPr')
    rtag = etree.SubElement(rpr, f'{{{W}}}rStyle')
    rtag.set(f'{{{W}}}val', 'CommentReference')
    cr = etree.SubElement(r_ref, f'{{{W}}}commentReference')
    cr.set(f'{{{W}}}id', str(cid))

    print(f"  Comment {cid} attached to paragraph: '{para_text(target_para)[:80]}'")
    return True

print("\nStep 10: Attaching comments to paragraphs...")

attach_comment(doc_xml, "CAS A", 1)
attach_comment(doc_xml, "Ce niveau s'explique avant tout par le volume de prospection LinkedIn reçu", 2)
attach_comment(doc_xml, "Note importante : ancienneté sur le métier", 3)
attached_4 = attach_comment(doc_xml, "part croissante des commentaires LinkedIn est générée avec de l'IA", 4)
if not attached_4:
    attach_comment(doc_xml, "commentaires est générée avec de l'IA", 4)
attach_comment(doc_xml, "Ce niveau représente le levier de différenciation le plus puissant", 5)
attach_comment(doc_xml, "Règle quand il n'y a pas assez d'éléments pour construire l'insight", 6)
attach_comment(doc_xml, "Exemples par secteur (Niveau 3)", 7)
attach_comment(doc_xml, "VOCABULAIRE DU BLOC 4A", 8)

# ─────────────────────────────────────────────────────────
# STEP 11: Write back to docx
# ─────────────────────────────────────────────────────────

files['word/document.xml'] = etree.tostring(
    doc_xml,
    xml_declaration=True,
    encoding='UTF-8',
    standalone=True
)

files['word/comments.xml'] = etree.tostring(
    comments_root,
    xml_declaration=True,
    encoding='UTF-8',
    standalone=True
)

with zipfile.ZipFile(DST, 'w', zipfile.ZIP_DEFLATED) as z:
    for name, data in files.items():
        z.writestr(name, data)

# ─────────────────────────────────────────────────────────
# STEP 12: Verify
# ─────────────────────────────────────────────────────────
size = os.path.getsize(DST)
print(f"\nDone! File saved: {DST}")
print(f"File size: {size:,} bytes ({size/1024:.1f} KB)")
print(f"Paragraphs removed from Bloc 4B onwards: {removed_count}")

# Verify no em-dashes or enrobage remain
with zipfile.ZipFile(DST, 'r') as z:
    doc_bytes = z.read('word/document.xml')
doc_str = doc_bytes.decode('utf-8')

em_count = doc_str.count('—')
enrobage_count = doc_str.count('enrobage') + doc_str.count('Enrobage')
print(f"\nVerification:")
print(f"  Em-dashes (—) remaining: {em_count}")
print(f"  'enrobage' remaining: {enrobage_count}")
print(f"  File size OK (>150KB): {size > 150*1024}")
