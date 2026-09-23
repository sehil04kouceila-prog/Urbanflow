
import pygame
import math
import random
import networkx as nx


class Sommet:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.voisins = []


class Agent:

    def __init__(self, agent_id, sommet_depart, sommets, graphe, client):
        self.agent_id = agent_id
        self.sommet_actuel = sommet_depart
        self.sommet_cible = sommet_depart
        self.client = client

        self.x = sommets[sommet_depart].x
        self.y = sommets[sommet_depart].y

        self.vitesse = 80
        self.couleur = (50, 100, 220)
        self.rayon = 6

        self.chemin = []
        self.calculer_chemin(graphe)
    def calculer_chemin(self, graphe):
        self.chemin = nx.shortest_path(
            graphe,
            self.sommet_actuel,
            self.client.sommet_arrivee
        )
        

    def deplacer(self, dt, sommets, graphe):

        # S'il n'y a plus de sommet à parcourir
        if len(self.chemin) <= 1:
            return

        # Le prochain sommet est le deuxième élément du chemin
        self.sommet_cible = self.chemin[1]

        cible = sommets[self.sommet_cible]

        dx = cible.x - self.x
        dy = cible.y - self.y

        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:

            direction_x = dx / distance
            direction_y = dy / distance

            distance_parcourue = self.vitesse * dt

            if distance_parcourue >= distance:

                self.x = cible.x
                self.y = cible.y

                self.sommet_actuel = self.sommet_cible

                # On retire le sommet que l'on vient d'atteindre
                self.chemin.pop(0)

            else:

                self.x += direction_x * distance_parcourue
                self.y += direction_y * distance_parcourue

    def dessiner(self, screen):
        pygame.draw.circle(
            screen,
            self.couleur,
            (int(self.x), int(self.y)),
            self.rayon
        )


class Client:

    def __init__(self, sommet_arrivee):
        self.sommet_arrivee = sommet_arrivee
        self.agent_id = None

    def dessiner(self, screen, sommets, agents):
        sommet = sommets[self.sommet_arrivee]

        centre = (int(sommet.x), int(sommet.y))
        rayon = 8

        couleur_client = (220, 50, 50)

        # Couleur du livreur associé
        if self.agent_id is not None:
            couleur_agent = agents[self.agent_id].couleur
        else:
            couleur_agent = couleur_client

        # Cercle complet en rouge
        pygame.draw.circle(
            screen,
            couleur_client,
            centre,
            rayon
        )

        # Points pour dessiner la moitié gauche
        points = [centre]

        for angle in range(90, 271, 10):
            angle_rad = math.radians(angle)

            px = centre[0] + rayon * math.cos(angle_rad)
            py = centre[1] - rayon * math.sin(angle_rad)

            points.append((int(px), int(py)))

        # Moitié gauche avec la couleur du livreur
        pygame.draw.polygon(
            screen,
            couleur_agent,
            points
        )

        # Contour du client
        pygame.draw.circle(
            screen,
            (50, 50, 50),
            centre,
            rayon,
            1
        )

