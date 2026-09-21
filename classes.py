import pygame
import math
import random

class Sommet:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.voisins = []

'''
class agent:
    def __init__(self, sommet_depart, sommets, graphe):
        self.sommet_actuel= sommet_depart
        self.sommet_cible=sommet_depart
        self.x = sommets[sommet_depart].x
        self.y = sommets[sommet_depart].y
        self.vitesse = 80
        self.couleur = (50, 100, 220)
        self.rayon = 6
        self.choisir_prochain_sommet(graphe)
    def choisir_prochain_sommet(self, graphe):
        voisins = list(graphe.neighbors(self.sommet_actuel))
        if voisins:
            self.sommet_cible = random.choice(voisins)

    def deplacer(self, dt, sommets, graphe):
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
                self.choisir_prochain_sommet(graphe)
            else:
                self.x += direction_x * distance_parcourue
                self.y += direction_y * distance_parcourue
    def dessiner(self, screen):
        pygame.draw.circle(
            screen,self.couleur,(int(self.x), int(self.y)),self.rayon )
            '''