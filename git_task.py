import pygame
import random

# Definim constante pentru a evita "numerele magice" (magic numbers) în cod
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE

def generate_random_color_grid():
    """
    Generează o matrice 10x10 ce conține culori RGB generate aleatoriu.
    Fiecare element din matrice reprezintă o culoare sub formă de tuplu (R, G, B).
    """
    grid = []
    for _ in range(GRID_SIZE):
        row = []
        for _ in range(GRID_SIZE):
            # Generăm valori aleatorii între 0 și 255 pentru roșu, verde și albastru
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            row.append((red, green, blue))
        grid.append(row)
    return grid

def main():
    # Inițializăm modulul pygame
    pygame.init()

    # Creăm fereastra aplicației
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Procedural Color Grid (Regenerare la 5 secunde)")

    # Generăm prima grilă de culori
    color_grid = generate_random_color_grid()
    
    is_running = True
    
    # Salvăm momentul (în milisecunde) în care am generat ultima dată grila
    last_update_time = pygame.time.get_ticks()

    # Bucla principală a programului
    while is_running:
        # 1. Gestionarea evenimentelor (ex: închiderea ferestrei)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                
        # 2. Logica de regenerare automată la fiecare 5 secunde (5000 milisecunde)
        current_time = pygame.time.get_ticks()
        if current_time - last_update_time >= 5000:
            color_grid = generate_random_color_grid()
            last_update_time = current_time  # Resetăm cronometrul

        # 3. Desenarea elementelor pe ecran
        screen.fill((0, 0, 0)) # Setăm fundalul negru

        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                color = color_grid[y][x]
                rect_x = x * CELL_SIZE
                rect_y = y * CELL_SIZE
                
                # Desenăm fiecare pătrat în parte
                pygame.draw.rect(screen, color, (rect_x, rect_y, CELL_SIZE, CELL_SIZE))

        # Actualizăm ecranul pentru a afișa noile desene
        pygame.display.flip()

        # O mică pauză pentru a nu suprasolicita procesorul (rulează la aprox. 30-40 FPS)
        pygame.time.delay(30)

    # Închidem pygame curat la ieșirea din buclă
    pygame.quit()

# Punctul de intrare în program
if __name__ == "__main__":
    main()