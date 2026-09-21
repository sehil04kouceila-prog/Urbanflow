
import pygame
import sys
import random
from classes import Sommet#, Agent
import networkx as nx

# Initialisation de pygame
pygame.init()

# Taille de la fenêtre
WIDTH = 1200
HEIGHT = 750
RATIO= WIDTH/HEIGHT


LEFT_WIDTH = int(WIDTH * 0.70)
RIGHT_WIDTH = WIDTH - LEFT_WIDTH

left_panel = pygame.Rect(0, 0, LEFT_WIDTH, HEIGHT)
right_panel = pygame.Rect(LEFT_WIDTH, 0, RIGHT_WIDTH, HEIGHT)

marge=int(HEIGHT * 0.05)
x=marge
y=marge
langeur=int(HEIGHT -2*marge)
largeur=int(LEFT_WIDTH -2*marge)
#couleur=(248, 245, 235)
couleur = (230, 230, 230)

N=20
global n, dx, dy, mx, my

n = round((largeur * N) / langeur)

dx = (largeur - 2) / (n - 1)
dy = (langeur - 2) / (N - 1)

largeur_points = (n - 1) * dx
hauteur_points = (N - 1) * dy

mx = (largeur - largeur_points) / 2
my = (langeur - hauteur_points) / 2




###############################################################################################
def update_layout():
    global LEFT_WIDTH, RIGHT_WIDTH
    global left_panel, right_panel
    global marge, x, y, largeur, langeur
    global n, dx, dy, mx, my

    LEFT_WIDTH = int(WIDTH * 0.70)
    RIGHT_WIDTH = WIDTH - LEFT_WIDTH

    left_panel = pygame.Rect(0, 0, LEFT_WIDTH, HEIGHT)
    right_panel = pygame.Rect(LEFT_WIDTH, 0, RIGHT_WIDTH, HEIGHT)

    marge = int(HEIGHT * 0.05)

    x = marge
    y = marge
    largeur = LEFT_WIDTH - 2 * marge
    langeur = HEIGHT - 2 * marge

    n = round((largeur * N) / langeur)

    dx = (largeur - 2) / (n - 1)
    dy = (langeur - 2) / (N - 1)

    largeur_points = (n - 1) * dx
    hauteur_points = (N - 1) * dy

    mx = (largeur - largeur_points) / 2
    my = (langeur - hauteur_points) / 2
##################################################################################################################


def gen_points():
    points=[]
    for i in range(N):
        for j in range(n):
            px = x +mx+ j * dx
            py = y +my+ i * dy
            points.append((px, py))
    
    return points
   
def gen_sommets():
    points = gen_points()
    return [Sommet(px, py) for px, py in points]

sommets = gen_sommets()

def gen_graphe(sommets):
    G = nx.Graph()

    for i, s in enumerate(sommets):
        G.add_node(i, sommet=s, pos=(s.x, s.y))

    # grille complète
    for i in range(N):
        for j in range(n):
            a = i * n + j

            if j < n - 1:
                b = i * n + (j + 1)
                G.add_edge(a, b)

            if i < N - 1:
                b = (i + 1) * n + j
                G.add_edge(a, b)

    # arbre couvrant aléatoire
    T = nx.random_spanning_tree(G, seed=None)

    return T
G = gen_graphe(sommets)
#agent = Agent(0, sommets, G)
sommet_depart = random.choice(list(G.nodes()))









screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE) #cree la fenetre
pygame.display.set_caption ( " UrbanFlow Optimizer " ) # le titre
clock = pygame . time . Clock () # emporter le temps
dt = 0
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




        ###################
        if event.type == pygame.VIDEORESIZE:
            WIDTH = event.w
            HEIGHT = int(WIDTH / RATIO)

            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            update_layout()

            sommets = []
            points = gen_points()
            for px, py in points:
                sommets.append(Sommet(px, py))
        ###################





    screen . fill ((245 , 245 , 245) )
    pygame.draw.rect(screen, (255, 255, 255), left_panel)
    pygame.draw.rect(screen, (255, 255, 255), right_panel)
    #pygame.draw.line(screen, (210, 210, 210), (LEFT_WIDTH, 0), (LEFT_WIDTH, HEIGHT), 2)
    carre = pygame.Rect(x - marge // 2,y - marge // 2,largeur + 2 * marge // 2,langeur + 2 * marge // 2)
    pygame.draw.rect(screen, couleur, carre)
    points = gen_points()

    #for s in sommets:
       # pygame.draw.circle(screen, (0,0,0), (int(s.x), int(s.y)), 3)
    for a, b in G.edges():
        s1 = sommets[a]
        s2 = sommets[b]
        pygame.draw.line(screen, (250,250,250), (s1.x, s1.y), (s2.x, s2.y), 6)
        #dessiner_route(screen, s1, s2)

    



    pygame . display . flip ()
    clock . tick (60)

pygame . quit ()
sys . exit ()


