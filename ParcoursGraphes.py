def cherche_chemin(graphe, depart,arrivee):
    """
    recherche d'un chemin dans un graphe depuis un sommet de départ vers un sommet d'arrivée
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param depart: le sommet de départ pour le chemin recherché
    :param arrivee: le sommet d'arrivée pur le chemin recherché
    :return: la liste des sommets du graphe
    """
    if not(depart in graphe.keys()) or not(arrivee in graphe.keys()):
        return None
    pile = [(depart,[depart])]
    while len(pile) != 0:
        sommet,chemin = pile.pop()
        liste_nouveaux_sommets_voisins = [voisin for voisin in graphe[sommet] if not(voisin in chemin)]
        for voisin in liste_nouveaux_sommets_voisins:
            if voisin == arrivee:
                return chemin + [arrivee]
            pile.append((voisin,chemin + [voisin]))
    return None


def cherche_tous_chemins(graphe, depart,arrivee):
    """
    recherche tous les chemins dans un graphe depuis un sommet de départ vers un sommet d'arrivée
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param depart: le sommet de départ pour le chemin recherché
    :param arrivee: le sommet d'arrivée pur le chemin recherché
    :return: la liste des sommets du graphe
    >>> cherche_chemin({"A":("B","D","E"),"B":("A","C"),"C":("B","D"),"D":("A","C","E"),"E":("A","D","F","G"),"F":("E","G"),"G":("E","F","H"),"H":("G")},"A")
    ['A', 'B', 'D', 'E', 'C', 'F', 'G', 'H']
    """
    chemins = []
    if not(depart in graphe.keys()) or not(arrivee in graphe.keys()):
        return None
    pile = [(depart,[depart])]
    while len(pile) != 0:
        sommet,chemin = pile.pop()
        liste_nouveaux_sommets_voisins = [voisin for voisin in graphe[sommet] if not(voisin in chemin)]
        for voisin in liste_nouveaux_sommets_voisins:
            if voisin == arrivee:
                chemins.append(chemin + [arrivee])
            pile.append((voisin,chemin + [voisin]))
    return chemins

def cherche_chemin_plus_court(graphe, depart,arrivee):
    """
    recherche le chemin le plus court chemin dans un graphe depuis un sommet de départ vers un sommet d'arrivée
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param depart: le sommet de départ pour le chemin recherché
    :param arrivee: le sommet d'arrivée pur le chemin recherché
    :return: la liste des sommets du graphe
    """
    chemins = cherche_tous_chemins(graphe,depart,arrivee)
    if len(chemins) == 0:
        return None
    lg_chemin_min = len(chemins[0])
    chemin_min = chemins[0]
    for chemin in chemins:
        if len(chemin) < lg_chemin_min:
            lg_chemin_min = len(chemin)
            chemin_min = chemin.copy()
    return chemin_min

def cherche_cycles(graphe, sommet):
    """
    recherche tous les cycles de sommet sommet dans le graphe graphe
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param sommet: le sommet du cycle
    :return: la liste des cycles de sommet sommet du graphe graphe
    """
    cycles = []
    for autre_sommet in graphe.keys():
        if autre_sommet in graphe[sommet]:
            chemins = cherche_tous_chemins(graphe, sommet, autre_sommet)
            for chemin in chemins:
                cycles.append(chemin + [sommet])
            cycles.extend(chemins)
    return cycles


def cherche_tous_chemins(graphe, depart,arrivee):
    """
    recherche tous les chemins dans un graphe depuis un sommet de départ vers un sommet d'arrivée
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param depart: le sommet de départ pour le chemin recherché
    :param arrivee: le sommet d'arrivée pur le chemin recherché
    :return: la liste des sommets du graphe
    """
    chemins = []
    if not(depart in graphe.keys()) or not(arrivee in graphe.keys()):
        return None
    pile = [(depart,[depart])]
    chemin = []
    while len(pile) != 0:
        sommet,chemin = pile.pop()
        liste_nouveaux_sommets_voisins = [voisin for voisin in graphe[sommet] if not(voisin in chemin)]
        for voisin in liste_nouveaux_sommets_voisins:
            if voisin == arrivee:
                chemins.append(chemin + [arrivee])
            pile.append((voisin,chemin + [voisin]))
    return chemins


def parcours_en_largeur(graphe, sommet):
    """
    Parcours d'un graphe en largeur
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param sommet: le sommet de départ du graphe étudié
    :return: la liste des sommets du graphe
    >>> parcours_en_largeur({"A":("B","D","E"),"B":("A","C"),"C":("B","D"),"D":("A","C","E"),"E":("A","D","F","G"),"F":("E","G"),"G":("E","F","H"),"H":("G")},"A")
    ['A', 'B', 'D', 'E', 'C', 'F', 'G', 'H']
    """
    if not(sommet in graphe.keys()):
        return None
    F = [sommet]
    liste_sommets = []
    while len(F) != 0:
        S = F[0]
        for voisin in graphe[S]:
            if not(voisin in liste_sommets) and not(voisin in F):
                F.append(voisin)
        liste_sommets.append(F.pop(0))
    return liste_sommets


def parcours_en_profondeur(graphe, sommet):
    """
    Parcours d'un graphe en profondeur
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param sommet: le sommet de départ du graphe étudié
    :return: la liste des sommets du graphe
    >>> parcours_en_profondeur({"A":("B","D","E"),"B":("A","C"),"C":("B","D"),"D":("A","C","E"),"E":("A","D","F","G"),"F":("E","G"),"G":("E","F","H"),"H":("G")},"A")
    ['A', 'E', 'G', 'H', 'F', 'D', 'C', 'B']
    """
    if not(sommet in graphe.keys()):
        return None
    P = [sommet]
    liste_sommets = []
    while len(P) != 0:
        S = P.pop()
        liste_sommets.append(S)
        for voisin in graphe[S]:
            if not(voisin in liste_sommets) and not(voisin in P):
                P.append(voisin)
    return liste_sommets

def cherche_tous_cycles(graphe):
    """
    recherche tous les cycles dans le graphe graphe
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :return: la liste des cycles du graphe graphe
    """
    tous_cycles = []
    for sommet in graphe.keys():
        cycles = cherche_cycles(graphe, sommet)
        if cycles != []:
            tous_cycles.append(cycles)
    return tous_cycles


def cherche_tous_chemins_graphe_pondere(graphe, depart,arrivee):
    """
    recherche tous les chemins dans un graphe pondéré depuis un sommet de départ vers un sommet d'arrivée
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param depart: le sommet de départ pour le chemin recherché
    :param arrivee: le sommet d'arrivée pur le chemin recherché
    :return: la liste des sommets du graphe
    """
    chemins = []
    if not(depart in graphe.keys()) or not(arrivee in graphe.keys()):
        return None
    pile = [(depart,[depart])]
    chemin = []
    while len(pile) != 0:
        print(len(pile))
        sommet,chemin = pile.pop()
        if len(sommet) == 2:
            sommet = sommet[0]
        liste_nouveaux_sommets_voisins = []
        for voisin in graphe[sommet]:
            if len(voisin) == 2 and not (voisin in chemin):
                liste_nouveaux_sommets_voisins.append(voisin)
            if voisin[0] == arrivee:
                chemins.append(chemin + [voisin])
            pile.append((voisin,chemin + [voisin]))
    return chemins


def calcule_longueur_chemin(chemin,distances):
    """

    @param chemin:
    @param distances:
    @return:
    """
    sommet1 = chemin[0]
    longueur = 0
    for ind in range(1,len(chemin)):
        sommet2 = chemin[ind]
        trouve = False
        for distance in distances:
            if distance[0] == sommet1 and distance[1] == sommet2:
                longueur += distance[2]
                trouve = True
                break
        if not(trouve):
            return "Erreur"
        sommet1 = sommet2
    return longueur




def cherche_chemin_plus_court_graphe_pondere(graphe, distances, depart,arrivee):
    """
    recherche le chemin le plus court chemin dans un graphe pondéré depuis un sommet de départ vers un sommet d'arrivée
    :param graphe: une liste d'adajence du graphe étudié (un dictionnaire)
    :param depart: le sommet de départ pour le chemin recherché
    :param arrivee: le sommet d'arrivée pur le chemin recherché
    :return: la liste des sommets du graphe
    """
    chemins = cherche_tous_chemins(graphe,depart,arrivee)
    if len(chemins) == 0:
        return None
    lg_chemin_min = calcule_longueur_chemin(chemins[0],distances)
    chemin_min = chemins[0]
    for chemin in chemins:
        lg_chemin = calcule_longueur_chemin(chemin, distances)
        if lg_chemin < lg_chemin_min:
            lg_chemin_min = lg_chemin
            chemin_min = chemin.copy()
    return (lg_chemin_min,chemin_min)

def trouve_min(sommets,dist):
    """
    @param sommets:
    @return:
    """
    mini = float('inf')
    sommet = -1
    for s in sommets:
        if dist[s] < mini:
            mini = dist[s]
            sommet = s
    return sommet


def Dijkstra(graphe,depart,arrivee):
    """

    @param graphe:
    @param distances:
    @param depart:
    @param arrivee:
    @return:
    """
    dist = {}
    predecesseurs = {}
    for sommet in graphe.keys():
        dist[sommet] = float('inf')
    dist[depart] = 0
    sommets = list(graphe.keys())
    while len(sommets) != 0:
        s1 = trouve_min(sommets,dist)
        sommets.remove(s1)
        if s1 == -1:
            pass
        else:
            for voisin in graphe[s1]:
                if dist[voisin[0]] > dist[s1] + voisin[1]:
                    dist[voisin[0]] = dist[s1] + voisin[1]
                    predecesseurs[voisin[0]] = s1
    sommet = arrivee
    chemin_plus_court = []
    while sommet != depart:
        chemin_plus_court.insert(0,sommet)
        sommet = predecesseurs[sommet]
    chemin_plus_court.insert(0,depart)
    return (dist[arrivee],chemin_plus_court)
