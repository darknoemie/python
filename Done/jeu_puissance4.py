# -*- coding:Utf-8 -*-
# python 2.7.3 Windows XP : OK
# python 2.7.2 Linux/Ubuntu : OK
from Tkinter import *
import sys
import tkMessageBox


class Initiation:
    def __init__(self):

        Initiation.jeu = 1  # le flag permet de controler le jeu (arrêt ou marche)

        self.lecture_options()
        Initiation.taille_carre = (
            Initiation.c
        )  ##je n'ai pu le mettre que dans __init__ :(   ~>> une initiation, pour eviter une erreur lors du 1er demarrage de la fenetre_options)

    def lecture_options(self):

        fichier_interface = open(
            "options-interface-DropBalls.txt", "a"
        )  # création d'un fichier,  si celui-ci n'existe pas...
        fichier_interface.close()

        fichier_interface = open("options-interface-DropBalls.txt", "r")
        if fichier_interface.readline() == "":
            fichier_interface.close()
            # création d'un nouveau fichier
            fichier_interface = open("options-interface-DropBalls.txt", "w")

            fichier_interface.write("50.0\n")
            fichier_interface.write("grey\n")
            fichier_interface.write("blue\n")
            fichier_interface.write("red\n")
            fichier_interface.write("Joueur 1\n")
            fichier_interface.write("Joueur 2\n")
            fichier_interface.write("0\n")

            fichier_interface.write(
                """\n\nCeci est le fichier Fourstones qui contient les options de l'interface. Elles sont modifiables dans le programme: Menu principal > Options OU directement ici (non-recommandé).
				
	Avertissement: Modifier les options peut empêcher le programme de fonctionner! 
	Dans ce cas, simplement détruire le fichier > options interface.txt < , un nouveau sera automatiquement créé.\n\nDans l'ordre de la liste:\n#taille d'un carré\n#couleur interface\n#couleur pièce Joueur1\n#couleur pièce Joueur2\n#nom du Joueur1\n#nom du Joueur2\n#demander pour quitter"""
            )
            fichier_interface.close()

        fichier_interface = open("options-interface-DropBalls.txt", "r")
        liste_option = fichier_interface.readlines()
        fichier_interface.close()

        try:
            Initiation.c = float(
                liste_option[0][0 : len(liste_option[0]) - 1]
            )  # taille des carrés
            Initiation.coul_1 = str(
                liste_option[1][0 : len(liste_option[1]) - 1]
            )  # on met str au cas où
            Initiation.coul_2 = str(liste_option[2][0 : len(liste_option[2]) - 1])
            Initiation.coul_3 = str(liste_option[3][0 : len(liste_option[3]) - 1])
            Initiation.joueur_1 = str(liste_option[4][0 : len(liste_option[4]) - 1])
            Initiation.joueur_2 = str(liste_option[5][0 : len(liste_option[5]) - 1])
            Initiation.var_quit = str(liste_option[6][0 : len(liste_option[6]) - 1])
            Initiation.marge = 5 * Initiation.c / 70  # marge de distance du bord

        except:
            print "\nIl y a une erreur dans le fichier: options interface.txt\nVeuillez le detruire afin que le programme puisse fonctionner correctement.\nNB: Meme en cours d'execution du programme, celui-ci creera un nouveau fichier."
            return None


class Calcul(Initiation):
    def jeu_autorisation(self, event):
        if Panneau.jeu == 1:
            self.ajout_piece(event)
        else:
            self.msg_infos.configure(
                text="La partie est terminée. Aucune pièce ne peut plus être rajoutée.\nCliquez sur 'réinitialiser' pour commencer une nouvelle partie."
            )
            self.frame_infos.grid(row=1, column=1, rowspan=6, ipadx=5, ipady=5)
            self.update()
            self.frame_infos.after(1500, self.frame_infos.grid_forget())
            # print "Le jeu est stoppe. Aucune piece ne peut plus etre ajoutee dans cette partie"

    def piece_jeu(self, canvas, x, y, r, coul):
        self.oval1 = canvas.create_oval(x - r, x - r, x + r, x + r, fill=coul)
        try:
            if canvas == Panneau.can1:
                self.coord_arret_anim = (
                    Initiation.c * (6.5 - self.piece_col[self.col_selected])
                    + self.marge / 2
                )
                self.move()
        except:
            pass

    def move(self):
        "déplacement de la balle"
        anim_autorisation = 0
        self.y1 = self.y1 + Jeu.dy
        Panneau.can1.coords(
            self.oval1,
            self.x1 - self.r,
            self.y1 - self.r,
            self.x1 + self.r,
            self.y1 + self.r,
        )
        if self.y1 > self.coord_arret_anim:
            Panneau.can1.coords(
                self.oval1,
                self.x1 - self.r,
                self.coord_arret_anim - self.r,
                self.x1 + self.r,
                self.coord_arret_anim + self.r,
            )  # repositionnement de la pièce pour la recentrer
            Panneau.flag = 0  # arrêt de l'animation
            anim_autorisation = 1
        if Panneau.flag > 0:
            self.master.after(int(Initiation.c * 8 / 50), self.move)
        if (
            anim_autorisation == 1
        ):  # seulement déclecnchée si l'animation est entièrement terminée
            self.analyse_du_plateau()  # analyse du jeu

    def ajout_piece(self, event):
        self.col_selected = event.x / int(Initiation.c)

        if self.nombre_piece == 49:
            print "grille remplie"
            Panneau.jeu = 0  # autoriser le jeu
            return None  # a modifier pour mettre l'autorisation du jeu
        elif self.col_selected < 7:
            if (
                Panneau.piece_col[self.col_selected] < 7
            ):  # la colonne ne doit pas être remplie, cad pas plus de 7 pièces par colonne
                if Panneau.flag == 0:  # pour ne lancer qu'une seule boucle
                    Panneau.flag = 1
                    self.x1 = (
                        Initiation.c / 2
                        + self.col_selected * Initiation.c
                        + Initiation.marge / 2
                    )
                    self.y1 = 10
                    self.r = Initiation.c / 3
                    if Panneau.nombre_piece % 2 == 0:
                        coul = Initiation.coul_2
                        Panneau.msg_joueurs_1.config(font="Arial 8")
                        Panneau.msg_joueurs_3.config(font="Arial 12  bold")
                    else:
                        coul = Initiation.coul_3
                        Panneau.msg_joueurs_1.config(font="Arial 12 bold")
                        Panneau.msg_joueurs_3.config(font="Arial 8")

                    self.piece_jeu(Panneau.can1, self.x1, self.y1, self.r, coul)

                    coordonnees_piece = [
                        self.col_selected,
                        6 - Panneau.piece_col[self.col_selected],
                    ]
                    Panneau.__liste_pieces_placees__.append(
                        coordonnees_piece
                    )  # Ajout des coordonnées de la pièce placée
                    Panneau.nombre_piece += 1  # Nombre de pièces placées
                    Panneau.piece_col[
                        self.col_selected
                    ] += 1  # Nombre de pièces par colonne

                    Panneau.msg_piece.config(
                        text="Nombre de pièces: %s" % Panneau.nombre_piece
                    )

                    # self.analyse_du_plateau()  ##retirée car sinon elle se déclenche avant que la pièce ne soit tombée, gachant l'animation

            else:
                self.msg_infos.configure(
                    text="La colonne %s est remplie." % self.col_selected
                )
                self.frame_infos.grid(row=1, column=1, rowspan=6, ipadx=5, ipady=5)
                self.update()
                self.frame_infos.after(1000, self.frame_infos.grid_forget())
                # print "colonne", self.col_selected, "remplie"
        else:
            self.msg_infos.configure(text="Veuillez rester dans le plateau de jeu.")
            self.frame_infos.grid(row=1, column=1, rowspan=6, ipadx=5, ipady=5)
            self.update()
            self.frame_infos.after(1000, self.frame_infos.grid_forget())
            # print "Veuillez rester dans le plateau de jeu"

    def analyse_du_plateau(self):
        """On va analyser la disposition de toutes les pièces. Pour cela, on va logiquement ouvrir le fichier qui contient toutes
		les coordonnées des pièces placées. Il y a quatre disposition qui permettent une victoire:
		1. ligne de 4 horizontale (4 pieces ont la même coord X, et les coord Y se suivent)
		2. ligne de 4 verticale (4 pieces ont la même coord Y, et les coord X se suivent)
		3. ligne de 4 diagonale de gauche/haut à droite/bas (4 pieces ont les coord X et Y qui se suivent en augmentant)
		4. idem de droite/bas à gauche/haut (Les X augmentent et les Y diminuent en se suivant)."""

        """ Séparation des rouges et des bleus"""

        # BLEU #
        liste_x_bleu = (
            []
        )  # creation de 2 listes dans lesquelles se trouvent TOUS les x bleus
        liste_y_bleu = []  # TOUS les y bleus
        d = 0  # au debut, les bleus jouent
        while d < len(Panneau.__liste_pieces_placees__):
            coord_x_bleu = Panneau.__liste_pieces_placees__[d][0]
            coord_y_bleu = Panneau.__liste_pieces_placees__[d][1]

            liste_x_bleu.append(coord_x_bleu)  # rajout dans les listes
            liste_y_bleu.append(coord_y_bleu)

            d += 2  # logique puisqu'on joue une fois sur deux

        # ROUGE #
        liste_x_rouge = (
            []
        )  # creation de 2 listes dans lesquelles se trouvent TOUS les x rouges
        liste_y_rouge = []  # TOUS les y rouges
        f = 1  # on commence aux rouges
        while f < len(Panneau.__liste_pieces_placees__):
            coord_x_rouge = Panneau.__liste_pieces_placees__[f][0]
            coord_y_rouge = Panneau.__liste_pieces_placees__[f][1]

            liste_x_rouge.append(coord_x_rouge)  # rajout dans les listes
            liste_y_rouge.append(coord_y_rouge)

            f += 2  # logique puisqu'on joue une fois sur deux

        self.analyse_des_positions(
            liste_x_bleu, liste_y_bleu, liste_x_rouge, liste_y_rouge
        )  # je souhaite une nouvelle fonction pour mettre plus d'ordre dans le code :s (j'ai récupéré les meme noms de variables dans la fonction).

    def analyse_des_positions(
        self, liste_x_bleu, liste_y_bleu, liste_x_rouge, liste_y_rouge
    ):
        """ On va analyser la disposition des pieces, via les listes de coord x et y et un tri des listes..."""

        possibilites = ["0 1 2 3", "1 2 3 4", "2 3 4 5", "3 4 5 6"]

        ##################  BLEU  ##################
        liste_repartition_x_bleu = []
        liste_repartition_y_bleu = []
        for numb in range(12):
            repartition_x_bleu = liste_x_bleu.count(
                numb
            )  # on compte le nombre de fois que chaque nombre de 1 a 12 revient
            liste_repartition_x_bleu.append(repartition_x_bleu)
        for numb in range(12):
            repartition_y_bleu = liste_y_bleu.count(numb)
            liste_repartition_y_bleu.append(repartition_y_bleu)

        # comparaison des listes de coord avec les listes prédéfinies + Application des critères de victoires et arret du jeu en consequence.

        # VERTICALEMENT #
        for numb in range(12):
            if liste_repartition_x_bleu[numb] >= 4:

                # il faut ici retrouver les Y correspondant pour voir s'ils sont 'progressifs'
                #  > on va donc prendre les positions des X (qui ont des coordonnees identiques)  dans la liste de tous les x
                # ensuite, on regarde leur position dans cette liste.
                # après, on recopie cette position dans la liste de tous les Y
                # enfin, on regarde s'ils sont progressifs, d'abord en les triant puis en les comparant aux listes predefinies.

                liste_y_bleu_dixieme = []
                nn = 0
                while nn < len(liste_x_bleu):
                    if (
                        liste_x_bleu[nn] == numb
                    ):  ## je met en <str> car les elements de la liste sont <str>
                        liste_y_bleu_dixieme.append(
                            str(float(liste_y_bleu[nn]) / 10.0)
                        )  # creation d'une liste qui contient tous les correpondants (des X cible) en Y
                        # je divise par 10  pour eviter que 10 ou 11 ne se mettent en tete de liste lors du triage...
                    nn += 1

                liste_y_bleu_dixieme.sort()  # on les trie par ordre croissant et on va comparer a des liste predefinies pour voir si elles sont 'collées'
                liste_y_bleu_partic = []  ## je n'ai plus trouvé de nom :p
                nn = 0
                while nn < len(liste_y_bleu_dixieme):
                    liste_y_bleu_partic.append(
                        str(int(float(liste_y_bleu_dixieme[nn]) * 10.0))
                    )  # MDR, j'ai l'impression que ca ne ressemble a rien...et pourtant...       tout ca pour remultiplier par 10 :p
                    nn += 1

                liste_y_bleu_partic_str = " ".join(
                    liste_y_bleu_partic
                )  # on met la liste en chaîne de caract...(c'est plus facile lors des comparaisons...)

                u = 0
                while u < len(possibilites):  # et len(possibilites) vaut 9
                    suite_de_quatre = liste_y_bleu_partic_str.count(possibilites[u])

                    if suite_de_quatre > 0:
                        self.msg_infos.configure(
                            text="%s a gagné verticalement en X= %s et Y= %s"
                            % (self.joueur_1, numb, possibilites[u])
                        )
                        self.frame_infos.grid(
                            row=1, column=1, rowspan=6, ipadx=5, ipady=5
                        )
                        self.update()
                        self.frame_infos.after(2500, self.frame_infos.grid_forget())

                        Panneau.jeu = 0
                        return None

                    u += 1

        # HORIZONTALEMENT #
        for numb in range(12):
            if liste_repartition_y_bleu[numb] >= 4:

                liste_x_bleu_dixieme = []
                nn = 0
                while nn < len(liste_y_bleu):
                    if liste_y_bleu[nn] == numb:
                        liste_x_bleu_dixieme.append(str(float(liste_x_bleu[nn]) / 10.0))
                    nn += 1

                liste_x_bleu_dixieme.sort()
                liste_x_bleu_partic = []
                nn = 0
                while nn < len(liste_x_bleu_dixieme):
                    liste_x_bleu_partic.append(
                        str(int(float(liste_x_bleu_dixieme[nn]) * 10.0))
                    )
                    nn += 1

                liste_x_bleu_partic_str = " ".join(liste_x_bleu_partic)

                u = 0
                while u < len(possibilites):  # et len(possibilites) vaut 9 normallemnt
                    suite_de_quatre = liste_x_bleu_partic_str.count(possibilites[u])
                    if suite_de_quatre > 0:
                        self.msg_infos.configure(
                            text="%s a gagné horizontalement en Y= %s et X= %s"
                            % (self.joueur_1, numb, possibilites[u])
                        )
                        self.frame_infos.grid(
                            row=1, column=1, rowspan=6, ipadx=5, ipady=5
                        )
                        self.update()
                        self.frame_infos.after(2500, self.frame_infos.grid_forget())

                        Panneau.jeu = 0
                        return None
                    u += 1

        # DIAGONALE #
        """Procédure:
		- compter le nombre de pieces d'une couleur. S'il y a au moins 4 pieces d'une même couleur, on peut chercher des dispositions particulières
		- Dans la liste des X et Y d'une couleur, on va voir si tous les elements de la liste prédéfinie sont représentés.
		S'il y a une suite de 4 en X, et que les images en Y de ces 4 sont 'continues' alors il y a conmbinaison particuliere. """

        liste_controle = ["0", "0"]
        nombre_suite_4_x_bleu = []
        nombre_suite_4_y_bleu = []
        if (
            len(liste_x_bleu) >= 4
        ):  # nombre d'elemnts dans la liste des X bleus. Cad le nombre de pieces bleues qui ont été placées
            i = 0
            while i < len(possibilites):
                possibilites_indiv = possibilites[i]
                possibilites_indiv_liste = (
                    possibilites_indiv.split()
                )  # je decoupe chaque 'argument' de la liste 'possibilites' en liste eux-meme

                suite_quatre_x_bleu = []
                liste_suite_quatre_x = []
                nn = 0
                while nn < 4:
                    nombre_elements_suite = liste_x_bleu.count(
                        int(possibilites_indiv_liste[nn])
                    )  # de nouveau je ne sais pas comment l'appeler :p
                    liste_suite_quatre_x.append(nombre_elements_suite)
                    nn += 1

                if liste_suite_quatre_x[0] != 0:
                    if liste_suite_quatre_x[1] != 0:
                        if liste_suite_quatre_x[2] != 0:
                            if liste_suite_quatre_x[3] != 0:
                                rr = 0
                                while rr < len(possibilites_indiv_liste):
                                    suite_quatre_x_bleu.append(
                                        possibilites_indiv_liste[rr]
                                    )

                                    rr += 1
                                nombre_suite_4_x_bleu.append(suite_quatre_x_bleu)

                ## pour Y
                suite_quatre_y_bleu = []
                liste_suite_quatre_y = []
                zz = 0
                while zz < 4:
                    nombre_elements_suite = liste_y_bleu.count(
                        int(possibilites_indiv_liste[zz])
                    )  # de nouveau je ne sais pas comment l'appeler :p
                    liste_suite_quatre_y.append(nombre_elements_suite)

                    zz += 1

                if liste_suite_quatre_y[0] != 0:
                    if liste_suite_quatre_y[1] != 0:
                        if liste_suite_quatre_y[2] != 0:
                            if liste_suite_quatre_y[3] != 0:
                                tt = 0
                                while tt < len(possibilites_indiv_liste):
                                    suite_quatre_y_bleu.append(
                                        possibilites_indiv_liste[tt]
                                    )

                                    tt += 1
                                nombre_suite_4_y_bleu.append(suite_quatre_y_bleu)

                        # print 'nombre_suite_4_y_bleu', nombre_suite_4_y_bleu
                        # print 'len(nombre_suite_4_y_bleu)', len(nombre_suite_4_y_bleu)

                i += 1

                vvv = 0
                while vvv < len(nombre_suite_4_x_bleu):

                    ggg = 0
                    while ggg < len(nombre_suite_4_y_bleu):

                        a = 1
                        # if suite_quatre_x_bleu != []: ##test
                        if a == 1:
                            # print "Suite de 4 bleus en X=", nombre_suite_4_x_bleu [vvv]
                            place_x_bleu = []
                            uu = 0
                            while uu < len(
                                nombre_suite_4_x_bleu[vvv]
                            ):  ## c'est a coup sûr 4 :p

                                pp = 0
                                while pp < len(liste_x_bleu):  # pour tous les X placés,
                                    if (
                                        int(nombre_suite_4_x_bleu[vvv][uu])
                                        == liste_x_bleu[pp]
                                    ):  # on regarde lesquels sont identiques aux éléments de la liste des 4
                                        liste_temporaire = []
                                        # liste_temporaire.append(suite_quatre_x_bleu[uu])  # cela permettait de voir quelle colonne etait ciblée mais j'ai changé pour voir quel element de la liste de 4 etait ciblé
                                        liste_temporaire.append(uu)
                                        liste_temporaire.append(pp)
                                        place_x_bleu.append(
                                            liste_temporaire
                                        )  # et  on enregistre dans une liste, une autre liste qui contient la place de l'element dans la liste de 4 ainsi que sa place dans la suite des pieces placées. A la fin, la liste doit contenir 4 éléments minimum et plus si plusieurs pieces sont sur un même X;  ensuite, on fait de meme pour les Y: on cherche une suite de 4 minimum.
                                    pp += 1

                                uu += 1

                            liste_controle[0] = 1
                            # print "liste_x_bleu", liste_x_bleu
                            # print "la place des 4x 'suite' dans la liste des X bleus", place_x_bleu

                        if nombre_suite_4_y_bleu[ggg] != []:

                            place_y_bleu = []
                            uu = 0
                            while uu < len(
                                nombre_suite_4_y_bleu[ggg]
                            ):  ## c'est a coup sûr 4 :p
                                pp = 0
                                while pp < len(liste_y_bleu):
                                    if (
                                        int(nombre_suite_4_y_bleu[ggg][uu])
                                        == liste_y_bleu[pp]
                                    ):
                                        liste_temporaire = []
                                        liste_temporaire.append(uu)
                                        liste_temporaire.append(pp)
                                        place_y_bleu.append(liste_temporaire)
                                    pp += 1

                                uu += 1

                            liste_controle[1] = 1
                            # print "liste_y_bleu", liste_y_bleu
                            # print "la place des 4y 'suite' dans la liste des Y bleus", place_y_bleu

                        if liste_controle[0] == 1 and liste_controle[1] == 1:

                            liste_victoire_diago_1 = 0
                            kk = 0
                            while kk < len(place_x_bleu):

                                uu = 0
                                while uu < len(place_y_bleu):

                                    if place_x_bleu[kk] == place_y_bleu[uu]:
                                        liste_victoire_diago_1 += 1

                                    uu += 1

                                kk += 1

                            ddd = 0
                            while ddd < len(place_y_bleu):

                                element_1 = place_y_bleu[ddd][0]
                                place_y_bleu[ddd][0] = 3 - element_1

                                ddd += 1

                            liste_victoire_diago_2 = 0
                            kkk = 0
                            while kkk < len(place_x_bleu):

                                uuu = 0
                                while uuu < len(place_y_bleu):

                                    if place_x_bleu[kkk] == place_y_bleu[uuu]:
                                        liste_victoire_diago_2 += 1

                                    uuu += 1

                                kkk += 1

                            if liste_victoire_diago_1 == 4:
                                self.msg_infos.configure(
                                    text="%s a gagné en diagonale haut/gauche -> bas/droite."
                                    % (self.joueur_1)
                                )
                                self.frame_infos.grid(
                                    row=1, column=1, rowspan=6, ipadx=5, ipady=5
                                )
                                self.update()
                                self.frame_infos.after(
                                    2500, self.frame_infos.grid_forget()
                                )
                                # print "gagneeeee en diagonale haut/gauche -> bas/droite. \nAxe X:", suite_quatre_x_bleu, "et axe Y:", suite_quatre_y_bleu, "(marche pas!)"

                                Panneau.jeu = 0
                                return None

                            elif liste_victoire_diago_2 == 4:
                                self.msg_infos.configure(
                                    text="%s a gagné en diagonale bas/gauche -> haut/droite."
                                    % (self.joueur_1)
                                )
                                self.frame_infos.grid(
                                    row=1, column=1, rowspan=6, ipadx=5, ipady=5
                                )
                                self.update()
                                self.frame_infos.after(
                                    2500, self.frame_infos.grid_forget()
                                )
                                # print "gagneeeee en diagonale bas/gauche -> haut/droite. \nAxe X:", suite_quatre_x_bleu, "et axe Y:", suite_quatre_y_bleu, "(marche pas!)"

                                Panneau.jeu = 0
                                return None
                        ggg += 1

                    vvv += 1

        ##################  ROUGE  ##################
        liste_repartition_x_rouge = []
        liste_repartition_y_rouge = []
        for numb in range(12):
            repartition_x_rouge = liste_x_rouge.count(numb)
            liste_repartition_x_rouge.append(repartition_x_rouge)
        for numb in range(12):
            repartition_y_rouge = liste_y_rouge.count(numb)
            liste_repartition_y_rouge.append(repartition_y_rouge)

        # VERTICALEMENT #
        for numb in range(12):
            if liste_repartition_x_rouge[numb] >= 4:

                liste_y_rouge_dixieme = []
                nn = 0
                while nn < len(liste_x_rouge):
                    if liste_x_rouge[nn] == numb:
                        liste_y_rouge_dixieme.append(
                            str(float(liste_y_rouge[nn]) / 10.0)
                        )
                    nn += 1

                liste_y_rouge_dixieme.sort()
                liste_y_rouge_partic = []
                nn = 0
                while nn < len(liste_y_rouge_dixieme):
                    liste_y_rouge_partic.append(
                        str(int(float(liste_y_rouge_dixieme[nn]) * 10.0))
                    )  # MDR, j'ai l'impression que ca ne ressemble a rien...et pourtant...       tout ca pour remultiplier par 10 :p
                    nn += 1

                liste_y_rouge_partic_str = " ".join(
                    liste_y_rouge_partic
                )  # on met la liste en chaîne de caract...(c'est plus facile lors des comparaisons...)

                u = 0
                while u < len(possibilites):  # et len(possibilites) vaut 9 normallemnt
                    suite_de_quatre = liste_y_rouge_partic_str.count(possibilites[u])

                    if suite_de_quatre > 0:
                        self.msg_infos.configure(
                            text="%s a gagné verticalement en X= %s et Y= %s"
                            % (self.joueur_2, numb, possibilites[u])
                        )
                        self.frame_infos.grid(
                            row=1, column=1, rowspan=6, ipadx=5, ipady=5
                        )
                        self.update()
                        self.frame_infos.after(2500, self.frame_infos.grid_forget())
                        # print "Rouge a gagneeeeeee verticalement en X=", numb,"et Y=", possibilites[u]

                        Panneau.jeu = 0
                        return None

                    u += 1

        # HORIZONTALEMENT #
        for numb in range(12):
            if liste_repartition_y_rouge[numb] >= 4:

                liste_x_rouge_dixieme = []
                nn = 0
                while nn < len(liste_y_rouge):
                    if liste_y_rouge[nn] == numb:
                        liste_x_rouge_dixieme.append(
                            str(float(liste_x_rouge[nn]) / 10.0)
                        )
                    nn += 1

                liste_x_rouge_dixieme.sort()
                liste_x_rouge_partic = []
                nn = 0
                while nn < len(liste_x_rouge_dixieme):
                    liste_x_rouge_partic.append(
                        str(int(float(liste_x_rouge_dixieme[nn]) * 10.0))
                    )  # MDR, j'ai l'impression que ca ne ressemble a rien...et pourtant...       tout ca pour remultiplier par 10 :p
                    nn += 1

                liste_x_rouge_partic_str = " ".join(
                    liste_x_rouge_partic
                )  # on met la liste en chaîne de caract...(c'est plus facile lors des comparaisons...)

                u = 0
                while u < len(possibilites):  # et len(possibilites) vaut 9 normallemnt
                    suite_de_quatre = liste_x_rouge_partic_str.count(possibilites[u])

                    if suite_de_quatre > 0:
                        self.msg_infos.configure(
                            text="%s a gagné horizontalement en Y= %s et X= %s"
                            % (self.joueur_2, numb, possibilites[u])
                        )
                        self.frame_infos.grid(
                            row=1, column=1, rowspan=6, ipadx=5, ipady=5
                        )
                        self.update()
                        self.frame_infos.after(2500, self.frame_infos.grid_forget())
                        # print "rouge a gagneeeeeee horizontalement en Y=", numb,"et X=", possibilites[u]

                        Panneau.jeu = 0
                        return None
                    u += 1

        # DIAGONALE #

        liste_controle = ["0", "0"]
        nombre_suite_4_x_rouge = []
        nombre_suite_4_y_rouge = []
        if (
            len(liste_x_rouge) >= 4
        ):  # nombre d'elemnts dans la liste des X bleus. Cad le nombre de pieces bleues qui ont été placées
            i = 0
            while i < len(possibilites):
                possibilites_indiv = possibilites[i]
                possibilites_indiv_liste = (
                    possibilites_indiv.split()
                )  # je decoupe chaque 'argument' de la liste 'possibilites' en liste eux-meme

                suite_quatre_x_rouge = []
                liste_suite_quatre_x = []
                nn = 0
                while nn < 4:
                    nombre_elements_suite = liste_x_rouge.count(
                        int(possibilites_indiv_liste[nn])
                    )  # de nouveau je ne sais pas comment l'appeler :p
                    liste_suite_quatre_x.append(nombre_elements_suite)

                    nn += 1

                if liste_suite_quatre_x[0] != 0:
                    if liste_suite_quatre_x[1] != 0:
                        if liste_suite_quatre_x[2] != 0:
                            if liste_suite_quatre_x[3] != 0:
                                rr = 0
                                while rr < len(possibilites_indiv_liste):
                                    suite_quatre_x_rouge.append(
                                        possibilites_indiv_liste[rr]
                                    )

                                    rr += 1
                                nombre_suite_4_x_rouge.append(suite_quatre_x_rouge)

                ## pour Y
                suite_quatre_y_rouge = []
                liste_suite_quatre_y = []
                zz = 0
                while zz < 4:
                    nombre_elements_suite = liste_y_rouge.count(
                        int(possibilites_indiv_liste[zz])
                    )  # de nouveau je ne sais pas comment l'appeler :p
                    liste_suite_quatre_y.append(nombre_elements_suite)

                    zz += 1

                if liste_suite_quatre_y[0] != 0:
                    if liste_suite_quatre_y[1] != 0:
                        if liste_suite_quatre_y[2] != 0:
                            if liste_suite_quatre_y[3] != 0:
                                tt = 0
                                while tt < len(possibilites_indiv_liste):
                                    suite_quatre_y_rouge.append(
                                        possibilites_indiv_liste[tt]
                                    )

                                    tt += 1
                                nombre_suite_4_y_rouge.append(suite_quatre_y_rouge)

                i += 1

                vvv = 0
                while vvv < len(nombre_suite_4_x_rouge):

                    ggg = 0
                    while ggg < len(nombre_suite_4_y_rouge):

                        a = 1
                        # if suite_quatre_x_rouge!= []: ##test
                        if a == 1:

                            place_x_rouge = []
                            uu = 0
                            while uu < len(
                                nombre_suite_4_x_rouge[vvv]
                            ):  ## c'est a coup sûr 4 :p

                                pp = 0
                                while pp < len(
                                    liste_x_rouge
                                ):  # pour tous les X placés,
                                    if (
                                        int(nombre_suite_4_x_rouge[vvv][uu])
                                        == liste_x_rouge[pp]
                                    ):
                                        liste_temporaire = []
                                        # liste_temporaire.append(suite_quatre_x_bleu[uu])  # cela permettait de voir quelle colonne etait ciblée mais j'ai changé pour voir quel element de la liste de 4 etait ciblé
                                        liste_temporaire.append(uu)
                                        liste_temporaire.append(pp)
                                        place_x_rouge.append(liste_temporaire)
                                    pp += 1

                                uu += 1

                            liste_controle[0] = 1

                        if nombre_suite_4_y_rouge[ggg] != []:

                            place_y_rouge = []
                            uu = 0
                            while uu < len(
                                nombre_suite_4_y_rouge[ggg]
                            ):  ## c'est a coup sûr 4 :p
                                pp = 0
                                while pp < len(liste_y_rouge):
                                    if (
                                        int(nombre_suite_4_y_rouge[ggg][uu])
                                        == liste_y_rouge[pp]
                                    ):
                                        liste_temporaire = []
                                        liste_temporaire.append(uu)
                                        liste_temporaire.append(pp)
                                        place_y_rouge.append(liste_temporaire)
                                    pp += 1

                                uu += 1

                            liste_controle[1] = 1

                        if liste_controle[0] == 1 and liste_controle[1] == 1:

                            liste_victoire_diago_1 = 0
                            kk = 0
                            while kk < len(place_x_rouge):

                                uu = 0
                                while uu < len(place_y_rouge):

                                    if place_x_rouge[kk] == place_y_rouge[uu]:
                                        liste_victoire_diago_1 += 1

                                    uu += 1

                                kk += 1

                            ddd = 0
                            while ddd < len(place_y_rouge):

                                element_1 = place_y_rouge[ddd][0]
                                place_y_rouge[ddd][0] = 3 - element_1

                                ddd += 1

                            liste_victoire_diago_2 = 0
                            kkk = 0
                            while kkk < len(place_x_rouge):

                                uuu = 0
                                while uuu < len(place_y_rouge):

                                    if place_x_rouge[kkk] == place_y_rouge[uuu]:
                                        liste_victoire_diago_2 += 1

                                    uuu += 1

                                kkk += 1

                            if liste_victoire_diago_1 == 4:
                                self.msg_infos.configure(
                                    text="%s a gagné en diagonale haut/gauche -> bas/droite."
                                    % (self.joueur_2)
                                )
                                self.frame_infos.grid(
                                    row=1, column=1, rowspan=6, ipadx=5, ipady=5
                                )
                                self.update()
                                self.frame_infos.after(
                                    2500, self.frame_infos.grid_forget()
                                )
                                # print "gagneeeee en diagonale haut/gauche -> bas/droite. \nAxe X:", suite_quatre_x_bleu, "et axe Y:", suite_quatre_y_bleu, "(marche pas!)"

                                Panneau.jeu = 0
                                return None

                            elif liste_victoire_diago_2 == 4:
                                self.msg_infos.configure(
                                    text="%s a gagné en diagonale bas/gauche -> haut/droite."
                                    % (self.joueur_2)
                                )
                                self.frame_infos.grid(
                                    row=1, column=1, rowspan=6, ipadx=5, ipady=5
                                )
                                self.update()
                                self.frame_infos.after(
                                    2500, self.frame_infos.grid_forget()
                                )
                                # print "gagneeeee en diagonale bas/gauche -> haut/droite. \nAxe X:", suite_quatre_x_bleu, "et axe Y:", suite_quatre_y_bleu, "(marche pas!)"

                                Panneau.jeu = 0
                                return None
                        ggg += 1

                    vvv += 1

        ##########################################


class Panneau(Frame, Calcul, Initiation):
    def __init__(self, boss=None):
        Frame.__init__(self)

        self.lecture_options()

        Panneau.can1 = Canvas(
            self,
            width=Initiation.c * 7 + Initiation.marge,
            height=Initiation.c * 7 + Initiation.marge,
            bg=Initiation.coul_1,
        )
        Panneau.can1.bind("<Button-1>", self.jeu_autorisation)
        Panneau.can1.grid(row=1, column=1, rowspan=6, padx=5, pady=5)

        bouton_reinit = Button(
            self,
            text="Réinitialiser",
            relief="ridge",
            font="Arial 10",
            command=self.reinitialiser,
        )
        bouton_reinit.grid(row=1, column=2)

        Panneau.msg_piece = Label(self, text="Nombre de pièces: 0")
        Panneau.msg_piece.grid(row=2, column=2)

        Panneau.msg_joueurs_1 = Label(
            self, text=self.joueur_1, font="Arial 12 bold"
        )  # je met le texte plus gros parce que c'est lui qui commence
        Panneau.msg_joueurs_1.grid(row=3, column=2)
        if (
            self.coul_2 == "yellow"
        ):  ## parce que le jaune est trop vif donc je l'adouci un peu pour qu'il soit lisible
            Panneau.msg_joueurs_1["fg"] = "#efdf00"
        else:
            Panneau.msg_joueurs_1["fg"] = self.coul_2
        self.msg_joueurs_2 = Label(self, text="contre")
        self.msg_joueurs_2.grid(row=4, column=2)
        Panneau.msg_joueurs_3 = Label(self, text=self.joueur_2, fg=self.coul_3)
        Panneau.msg_joueurs_3.grid(row=5, column=2)

        self.msg_codeur = Label(self, text="Codé par THE_VIP", font="arial 7")
        self.msg_codeur.grid(row=7, column=1, pady=5)
        self.bou2 = Button(
            self, text="Quitter", relief="ridge", command=quitter
        )  # je lance la fonction quitter qui permettra d'ouvrir la fenetre menu
        self.bou2.grid(row=7, column=2, pady=5)

        self.frame_infos = Frame(self, bg="light blue", relief="raised", borderwidth=3)
        self.msg_infos = Label(self.frame_infos, bg="light blue")
        self.msg_infos.grid()

        self.frame_infos.grid_forget()

        Jeu.dy = Initiation.c / 5  # 'pas' du déplacement
        self.flag = 0

        self.init_jeu()

    def init_jeu(self):

        Panneau.can1.delete(ALL)

        #  ------------ réinitialisation des fichiers  --------------#
        Panneau.__liste_pieces_placees__ = []
        Panneau.jeu = 1  # autoriser le jeu
        Panneau.flag = 0  # une piece peut être jouée
        Panneau.nombre_piece = 0

        # initialisation d'un dictionnaire des pièces placées par colonne
        Panneau.piece_col = {}
        for numb in range(7):
            self.piece_col[numb] = 0
        # --------------------------------------------------------------- #

        self.plateau(Panneau.can1, Initiation.c, Initiation.coul_1)
        Panneau.msg_joueurs_1.config(font="Arial 12 bold")
        Panneau.msg_joueurs_3.config(font="Arial 8")

        Panneau.msg_piece.configure(text="Nombre de pièces: %s" % Panneau.nombre_piece)

    def plateau(self, canvas, c, coul):
        y = 0
        while y < 7:
            x = 0
            self.dessin_des_rond(canvas, x * c, y * c, c)
            y += 1

    def dessin_des_rond(self, canvas, x, y, c):
        e = 0
        while e < 7:
            canvas.create_oval(
                x + Initiation.marge, y + Initiation.marge, x + c, y + c, fill="white"
            )
            x += c
            e += 1

    def ask_menu_principal(self):
        if Panneau.nombre_piece > 0 and Panneau.jeu == 1:
            if tkMessageBox.askokcancel(
                "Attention",
                "Voulez-vous réellement quitter l'interface de jeu?\nToutes les données du jeu seront perdues!",
            ):
                self.master.destroy()
                MenuPrincipal()
        else:
            self.master.destroy()
            MenuPrincipal()

    def reinitialiser(self):
        if (
            Panneau.nombre_piece > 0 and Panneau.jeu == 1
        ):  # si aucune pièce n'est placée ET le jeu est 'activé'
            if tkMessageBox.askokcancel(
                "Attention",
                "Attention, vous êtes sur le point de réinitialiser le jeu !\nToutes les données seront perdues!",
            ):
                pass
        elif Panneau.jeu == 0:
            pass
        else:
            return None

        self.init_jeu()
        self.msg_infos.configure(text="Réinitialisation effectuée.")
        self.frame_infos.grid(row=1, column=1, rowspan=6, ipadx=5, ipady=5)
        self.update()
        self.frame_infos.after(1000, self.frame_infos.grid_forget())
        # print "------------------------------------------\nreinitialisation effectuee\n"


class MenuPrincipal(Initiation, Panneau):
    def __init__(self, boss=None):
        self.fenetre_menu = Tk()
        self.fenetre_menu.title(".:: DropBalls ::.")
        self.fenetre_menu.protocol(
            "WM_DELETE_WINDOW", quitter
        )  # héhé, ca controle la fermeture de la fenetre  via le X en haut a droite...
        self.fenetre_menu.resizable(width=False, height=False)

        self.msg1 = Label(
            self.fenetre_menu,
            text="\nBienvenue dans DropBalls! \n",
            font="arial 12 bold",
        )
        self.msg1.grid(column=1, row=1, columnspan=2)

        self.msg2 = Label(
            self.fenetre_menu,
            text="Vérifiez le nom des deux joueurs puis cliquez sur Jouer! :\n",
        )
        self.msg2.grid(column=1, row=2, columnspan=2)

        self.msg3 = Label(
            self.fenetre_menu,
            text=Initiation.joueur_1,
            font="arial 12",
            fg=Initiation.coul_2,
        )
        self.msg3.grid(column=1, row=3, columnspan=2)

        self.msg4 = Label(self.fenetre_menu, text="contre")
        self.msg4.grid(column=1, row=4, columnspan=2)

        self.msg5 = Label(
            self.fenetre_menu,
            text=Initiation.joueur_2,
            font="arial 12",
            fg=Initiation.coul_3,
        )
        self.msg5.grid(column=1, row=5, columnspan=2)

        self.msg7 = Label(self.fenetre_menu, text="")
        self.msg7.grid(column=1, row=6)

        self.bouton_jouer = Button(
            self.fenetre_menu,
            text="Jouer!",
            font="arial 16 italic",
            padx=30,
            pady=10,
            relief="groove",
            borderwidth=4,
            command=self.ask_jeu,
        )
        self.bouton_jouer.grid(column=1, row=7, columnspan=2)

        self.msg6 = Label(self.fenetre_menu, text="")
        self.msg6.grid(column=1, row=8)

        self.bouton_aide = Button(
            self.fenetre_menu, text="  Aide  ", relief="groove", command=self.aide
        )
        self.bouton_aide.grid(row=9, column=1, sticky="w", padx=7, pady=1)

        self.bouton_version = Button(
            self.fenetre_menu, text="Version", relief="groove", command=self.version
        )
        self.bouton_version.grid(row=10, column=1, sticky="w", padx=7, pady=1)

        self.bouton_interface = Button(
            self.fenetre_menu, text="Options", relief="groove", command=self.option
        )
        self.bouton_interface.grid(row=11, column=1, sticky="w", padx=7, pady=1)

        self.bouton_quit = Button(
            self.fenetre_menu, text="Quitter", relief="groove", command=quitter
        )
        self.bouton_quit.grid(column=1, row=12, columnspan=2, pady=5)

        self.fenetre_menu.mainloop()

    def aide(self):
        try:
            self.fenetre_version.destroy()
        except:
            pass

        try:
            self.fenetre_aide.destroy()
        except:
            pass

        try:
            self.fenetre_option.destroy()
        except:
            pass

        self.fenetre_aide = Toplevel()
        self.fenetre_aide.title("Aide - DropBalls")
        self.fenetre_aide.resizable(width=False, height=False)

        message1 = Label(
            self.fenetre_aide, text="Instructions de jeu:", font="arial 16"
        )
        message1.pack()

        message1bis = Label(
            self.fenetre_aide, text="Le jeu se joue à deux, au tour par tour."
        )
        message1bis.pack()
        message2 = Label(
            self.fenetre_aide, text="\nBut du jeu:", font="arial 12 underline"
        )
        message2.pack()
        message3 = Label(
            self.fenetre_aide,
            text="	Le but de jeu est simple: placer 4 pièces d' une même couleur côte à côte.\
		\nVous pouvez aligner 4 pièces à l'horizontale, à la verticale, ou encore en diagonale.",
        )
        message3.pack()
        message4 = Label(
            self.fenetre_aide, text="\nComment jouer ?", font="arial 12 underline"
        )
        message4.pack()
        message5 = Label(
            self.fenetre_aide,
            text="	Cliquez sur la colonne dans laquelle vous désirer placer une pièce; les pièces\
		\nvont tomber verticalement dans la grille et s'empiler les unes sur les autres.\n\n",
        )
        message5.pack()

        bouton_quit = Button(
            self.fenetre_aide,
            text="Quitter",
            relief="ridge",
            command=self.fenetre_aide.destroy,
        )
        bouton_quit.pack(side="bottom", pady=5)

    def version(self):
        try:
            self.fenetre_version.destroy()
        except:
            pass

        try:
            self.fenetre_aide.destroy()
        except:
            pass

        try:
            self.fenetre_option.destroy()
        except:
            pass

        self.fenetre_version = Toplevel()
        self.fenetre_version.title("Version - DropBalls")
        self.fenetre_version.resizable(width=False, height=False)

        message0 = Label(
            self.fenetre_version,
            text="DropBalls: Informations - Version",
            font="arial 16",
        )
        message0.grid(column=0, row=0, columnspan=2, pady=5, padx=10)
        message1 = Label(self.fenetre_version, text="\n - Codeur: THE_VIP")
        message1.grid(column=1, row=1, sticky=W)
        message2 = Label(self.fenetre_version, text=" - Version: 1.0 (22/08/06)")
        message2.grid(column=1, row=2, sticky=W)
        message3 = Label(self.fenetre_version, text=" - Release: 22/08/06\n\n")
        message3.grid(column=1, row=3, sticky=W)
        message4 = Label(
            self.fenetre_version,
            text=" - Pour tout contact, bug ou suggestion:	the_vip@skynet.be",
        )
        message4.grid(column=1, row=4, sticky=W)
        message5 = Label(self.fenetre_version, text="", font="arial 11")
        message5.grid(column=1, row=5, columnspan=2)

        bouton_quit = Button(
            self.fenetre_version,
            text="Quitter",
            relief="ridge",
            command=self.fenetre_version.destroy,
        )
        bouton_quit.grid(column=1, row=6, columnspan=2, pady=5)

    def option(
        self,
    ):  ## Bien que non-disponible via la barre de menu, je souhaite garder les 3 fenetres ensembles
        try:
            self.fenetre_version.destroy()
        except:
            pass

        try:
            self.fenetre_aide.destroy()
        except:
            pass

        try:
            self.fenetre_option.destroy()
        except:
            pass

        self.lecture_options()

        self.fenetre_option = Toplevel()
        self.fenetre_option.title("Options - DropBalls")
        self.fenetre_option.resizable(width=False, height=False)

        self.message0 = Label(
            self.fenetre_option, text="DropBalls: Options", font="arial 16"
        )
        self.message0.grid(column=1, row=0, columnspan=5, pady=5, padx=10)

        self.message0bis = Label(self.fenetre_option, text=" - Joueur 1:")
        self.message0bis.grid(column=1, row=1, sticky=W)
        self.entry1 = Entry(self.fenetre_option, width=10)
        self.entry1.insert(0, Initiation.joueur_1)
        self.entry1.bind("<KeyRelease>", self.event_key)
        self.entry1.grid(column=2, row=1, sticky=W, padx=3)

        self.message0bisbis = Label(self.fenetre_option, text=" - Joueur 2:")
        self.message0bisbis.grid(column=1, row=2, sticky=W)
        self.entry2 = Entry(self.fenetre_option, width=10)
        self.entry2.insert(0, Initiation.joueur_2)
        self.entry2.bind("<KeyRelease>", self.event_key)
        self.entry2.grid(column=2, row=2, sticky=W, padx=3)

        self.message1 = Label(self.fenetre_option, text=" - Taille des carrés:")
        self.message1.grid(column=1, row=3, sticky=W)

        self.scale_1 = Scale(
            self.fenetre_option,
            length=250,
            orient=HORIZONTAL,
            troughcolor="grey",
            sliderlength=20,
            showvalue=1,
            from_=30,
            to=80,
            tickinterval=50,
            command=self.scale_value,
        )
        self.scale_1.set(int(self.c))
        self.scale_1.grid(column=2, columnspan=3, row=3, sticky=W, padx=3)

        self.message2 = Label(self.fenetre_option, text=" - Couleur du damier:")
        self.message2.grid(column=1, row=4, sticky=W)
        self.myvar = StringVar()
        self.myvar.set(self.coul_1)
        self.r1 = Radiobutton(
            self.fenetre_option,
            text="Bleu foncé",
            variable=self.myvar,
            value="dark blue",
            command=self.apercu,
        )
        self.r2 = Radiobutton(
            self.fenetre_option,
            text="Bleu clair",
            variable=self.myvar,
            value="#4169e1",
            command=self.apercu,
        )
        self.r3 = Radiobutton(
            self.fenetre_option,
            text="Brun clair",
            variable=self.myvar,
            value="#cd853f",
            command=self.apercu,
        )
        if (
            self.myvar.get() == "dark blue"
        ):  ## pas trouvé l'option pour récupérer la valeur d'un radiobutton :((
            self.r1.select()
        elif self.myvar.get() == "#4169e1":
            self.r2.select()
        else:
            self.r3.select()
        self.r1.grid(column=2, row=4, sticky=W, padx=3)
        self.r2.grid(column=3, row=4, sticky=W, padx=3)
        self.r3.grid(column=4, row=4, sticky=W, padx=3)

        self.message3 = Label(self.fenetre_option, text=" - Couleur des pièces:")
        self.message3.grid(column=1, row=5, sticky=W)
        self.message3bis = Label(self.fenetre_option, text="	Joueur 1:")
        self.message3bis.grid(column=1, row=6, sticky=W)
        self.myvar2 = StringVar()
        self.myvar2.set(self.coul_2)
        self.r1bis = Radiobutton(
            self.fenetre_option,
            text="Jaune",
            variable=self.myvar2,
            value="yellow",
            command=self.apercu,
        )
        self.r2bis = Radiobutton(
            self.fenetre_option,
            text="Orange",
            variable=self.myvar2,
            value="#ffa500",
            command=self.apercu,
        )
        self.r3bis = Radiobutton(
            self.fenetre_option,
            text="Vert",
            variable=self.myvar2,
            value="#00ff00",
            command=self.apercu,
        )
        if (
            self.myvar2.get() == "yellow"
        ):  ## pas trouvé l'option pour récupérer la valeur d'un radiobutton :((
            self.r1bis.select()
        elif self.myvar2.get() == "#ffa500":
            self.r2bis.select()
        else:
            self.r3bis.select()
        self.r1bis.grid(column=2, row=6, sticky=W, padx=3)
        self.r2bis.grid(column=3, row=6, sticky=W, padx=3)
        self.r3bis.grid(column=4, row=6, sticky=W, padx=3)

        self.message3bisbis = Label(self.fenetre_option, text="	Joueur 2:")
        self.message3bisbis.grid(column=1, row=7, sticky=W)
        self.myvar3 = StringVar()
        self.myvar3.set(self.coul_3)
        self.r1bisbis = Radiobutton(
            self.fenetre_option,
            text="Rouge",
            variable=self.myvar3,
            value="red",
            command=self.apercu,
        )
        self.r2bisbis = Radiobutton(
            self.fenetre_option,
            text="Violet",
            variable=self.myvar3,
            value="#c71585",
            command=self.apercu,
        )
        self.r3bisbis = Radiobutton(
            self.fenetre_option,
            text="Cyan sombre",
            variable=self.myvar3,
            value="#008b8b",
            command=self.apercu,
        )
        if (
            self.myvar3.get() == "red"
        ):  ## pas trouvé l'option pour récupérer la valeur d'un radiobutton :((
            self.r1bisbis.select()
        elif self.myvar3.get() == "#008b8b":
            self.r2bisbis.select()
        else:
            self.r3bisbis.select()
        self.r1bisbis.grid(column=2, row=7, sticky=W, padx=3)
        self.r2bisbis.grid(column=3, row=7, sticky=W, padx=3)
        self.r3bisbis.grid(column=4, row=7, sticky=W, padx=3)

        self.message4 = Label(self.fenetre_option, text="\n\n - Apercu:")
        self.message4.grid(column=1, row=9, sticky=W)

        self.canvas_apercu = Canvas(
            self.fenetre_option,
            width=self.c * 3,
            height=self.c * 3,
            bg=Initiation.coul_1,
        )
        self.canvas_apercu.grid(column=2, row=10, columnspan=2)

        self.message5 = Label(
            self.fenetre_option,
            text="%s\n\ncontre\n\n%s" % (self.joueur_1, self.joueur_2),
        )
        self.message5.grid(column=4, row=10, sticky=W, padx=10)

        self.var = IntVar()
        self.checkbutton = Checkbutton(
            self.fenetre_option,
            text="Ne pas demander pour quitter",
            font="arial 7",
            variable=self.var,
        )
        if Initiation.var_quit == "1":
            self.checkbutton.select()
        self.checkbutton.grid(column=1, columnspan=2, row=11, pady=5, sticky=W, padx=5)

        self.bouton_enreg = Button(
            self.fenetre_option,
            text="Paramètres par défaut",
            relief="groove",
            font="arial 7",
            command=self.options_reinit,
        )
        self.bouton_enreg.grid(column=1, columnspan=2, row=12, pady=5, sticky=W, padx=5)

        self.bouton_quit = Button(
            self.fenetre_option,
            text="Annuler",
            relief="ridge",
            command=self.fenetre_option.destroy,
        )
        self.bouton_quit.grid(column=1, row=13, pady=5)
        self.bouton_enreg = Button(
            self.fenetre_option,
            text="Enregistrer",
            relief="ridge",
            command=self.enregistrer,
        )
        self.bouton_enreg.grid(column=3, row=13, pady=5)

        self.apercu()

    def scale_value(self, x):
        self.taille_carre = float(x)
        self.apercu()

    def event_key(self, event):
        self.apercu()

    def apercu(self):

        self.coul_1 = self.myvar.get()
        self.coul_2 = self.myvar2.get()
        self.coul_3 = self.myvar3.get()
        self.var_quit = (
            self.var.get()
        )  # pas besoin dans l'aperçu, mais ca structure le code

        try:
            self.joueur_1 = str(self.entry1.get())
            self.joueur_2 = str(self.entry2.get())
        except:
            pass
            print "\n\n---------------------\nIl y a une erreur dans votre saisie de nom de joueur.\nVerifiez que vous n'avez pas entre de caracteres speciaux.\n\nExcepte les accents (aigus, graves et circonflexes) ainsi que le _ (underscore), Tkinter ne prend en charge les caracteres speciaux."

        self.message5.configure(
            text="%s\n\ncontre\n\n%s" % (self.joueur_1, self.joueur_2)
        )

        self.canvas_apercu.delete(ALL)
        self.canvas_apercu.config(
            width=self.taille_carre * 3, height=self.taille_carre * 3, bg=self.coul_1
        )

        self.plateau(self.canvas_apercu, self.taille_carre, self.coul_1)

        x = self.taille_carre / 2 + 0 * self.taille_carre
        y = self.taille_carre / 2 + 0 * self.taille_carre
        self.piece_jeu(
            self.canvas_apercu,
            x + Initiation.marge / 2,
            y + Initiation.marge / 2,
            self.taille_carre / 3,
            self.coul_2,
        )

        x = self.taille_carre / 2 + 1 * self.taille_carre
        y = self.taille_carre / 2 + 2 * self.taille_carre
        self.piece_jeu(
            self.canvas_apercu,
            x + Initiation.marge / 2,
            y + Initiation.marge / 2,
            self.taille_carre / 3,
            self.coul_3,
        )

    def enregistrer(self):
        self.apercu()  # pour être sûr que la fonction a été appellée et que les variables ont été 'capturées'

        self.fenetre_option.destroy()

        if self.joueur_1 == "":
            self.joueur_1 = "Joueur 1"
        elif self.joueur_2 == "":
            self.joueur_2 = "Joueur 2"
        elif self.joueur_1 == self.joueur_2:
            self.joueur_1 = str(self.joueur_1 + " 1")
            self.joueur_2 = str(self.joueur_2 + " 2")

        self.msg3.config(text=self.joueur_1, fg=self.coul_2)
        self.msg5.config(text=self.joueur_2, fg=self.coul_3)

        fichier_interface = open("options-interface-DropBalls.txt", "w")

        fichier_interface.write(str(self.taille_carre))
        fichier_interface.write("\n")
        fichier_interface.write(str(self.coul_1))
        fichier_interface.write("\n")
        fichier_interface.write(str(self.coul_2))
        fichier_interface.write("\n")
        fichier_interface.write(str(self.coul_3))
        fichier_interface.write("\n")
        fichier_interface.write(str(self.joueur_1))
        fichier_interface.write("\n")
        fichier_interface.write(str(self.joueur_2))
        fichier_interface.write("\n")
        fichier_interface.write(str(self.var_quit))
        fichier_interface.write("\n")

        fichier_interface.write(
            """\n\nCeci est le fichier Fourstones qui contient les options de l'interface. Elles sont modifiables dans le programme: Menu principal > Options OU directement ici (non-recommandé).
			
Avertissement: Modifier les options peut empêcher le programme de fonctionner! 
Dans ce cas, simplement détruire le fichier > options interface.txt < , un nouveau sera automatiquement créé.\n\nDans l'ordre de la liste:\n#taille d'un carré\n#couleur interface\n#couleur pièce Joueur1\n#couleur pièce Joueur2\n#nom du Joueur1\n#nom du Joueur2\n#demander pour quitter"""
        )

        fichier_interface.close()

        self.lecture_options()

    def options_reinit(self):
        self.entry1.delete(0, END)
        self.entry1.insert(0, "Joueur 1")
        self.entry2.delete(0, END)
        self.entry2.insert(0, "Joueur 2")
        self.scale_1.set(50)
        self.r1.select()
        self.r1bis.select()
        self.r1bisbis.select()
        self.checkbutton.deselect()
        self.message5.configure(text="Joueur 1\n\ncontre\n\nJoueur 2")

        self.apercu()

    def ask_jeu(self):
        self.fenetre_menu.destroy()
        Jeu().mainloop()


class MenuBar(Frame, Panneau, Initiation, MenuPrincipal):
    def __init__(self, boss=None):
        Frame.__init__(self)

        self.BoutonMenu1 = Menubutton(self, text="Menu")
        self.BoutonMenu1.pack(side=LEFT)

        self.menu1 = Menu(self.BoutonMenu1, tearoff=0)
        self.menu1.add_command(label="Menu principal", command=self.ask_menu_principal)

        self.BoutonMenu1.configure(menu=self.menu1)

        self.BoutonMenu2 = Menubutton(self, text="Informations")
        self.BoutonMenu2.pack(side=LEFT)

        self.menu2 = Menu(self.BoutonMenu2, tearoff=0)
        self.menu2.add_command(label="Aide", command=self.aide)
        self.menu2.add_command(label="Version", command=self.version)

        self.BoutonMenu2.configure(menu=self.menu2)

        # self.frame1 = Frame()
        # self.frame1.pack()

        # self.menu1 = Menu(self.frame1)
        # self.sous_menu1 = Menu(self.menu1, tearoff=0)
        # self.menu1.add_cascade(label=" Menu ", menu = self.sous_menu1)
        # self.sous_menu1.add_command(label = "Menu principal")#, command = self.ask_menu_principal)

        # self.sous_menu2 = Menu(self.menu1, tearoff=0)
        # self.menu1.add_cascade(label=" Informations ", menu = self.sous_menu2)
        # self.sous_menu2.add_command(label = "Aide")#, command = self.aide)
        # self.sous_menu2.add_command(label = "Version")#, command = self.version)

        # self.frame1.config(menu = self.menu1)


class Jeu(Frame):
    def __init__(self, boss=None):
        Frame.__init__(self)
        self.master.title(".:: DropBalls ::.")
        self.master.protocol("WM_DELETE_WINDOW", quitter)
        self.master.resizable(width=False, height=False)

        self.barre_menu = MenuBar(self)
        self.barre_menu.grid(row=1, column=1, sticky=W)

        self.interface = Panneau(self)
        self.interface.grid(row=2, column=1)


def quitter():
    if Initiation.var_quit == "0":
        if tkMessageBox.askokcancel("Quitter", "Voulez-vous réellement quitter?"):
            sys.exit()
    else:
        sys.exit()


if __name__ == "__main__":
    Initiation()
    MenuPrincipal()
