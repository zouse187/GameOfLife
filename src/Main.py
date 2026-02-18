class Button:
    def __init__(self, x, y, w, h, hover=True, button_color=(55, 55, 55), text="Button", text_color=(255, 255, 255), hover_effect=1):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.hover_rect = pygame.Rect(x-hover_effect, y-hover_effect, w+hover_effect*2, h+hover_effect*2)
        self.hover = hover
        self.button_color = button_color
        self.text = text
        self.text_color = text_color
        self.button_font = pygame.font.SysFont(None, round((w+h)//4))
        self.hover_color = tuple(min(x + 95, 255) for x in self.button_color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.button_color, self.rect, border_radius=7)
        if self.hover == True:
            mx, my = pygame.mouse.get_pos()
            if self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h:
                pygame.draw.rect(screen, self.hover_color, self.hover_rect, border_radius=7)

        text = self.button_font.render(self.text, True, self.text_color)
        screen.blit(text, (self.rect.x + (self.rect.width - text.get_width()) // 2,
                           self.rect.y + (self.rect.height - text.get_height()) // 2))
        
    def is_clicked(self):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h:
                return True
            else:
                return False
        

class Slider:
    def __init__(self, x, y, w, h, min_val, max_val, start_val, color=(200,200,200)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.min_val = min_val
        self.max_val = max_val
        self.value = start_val
        self.handle_x = x + (start_val - min_val) / (max_val - min_val) * w
        self.color = color
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, (100,100,100), self.rect)
        pygame.draw.circle(screen, self.color, (int(self.handle_x), self.rect.centery), 10)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            if abs(event.pos[0] - self.handle_x) < 15 and abs(event.pos[1] - self.rect.centery) < 15:
                self.dragging = True
            if self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h:
                self.handle_x = max(self.rect.x, min(event.pos[0], self.rect.x + self.rect.width))
                t = (self.handle_x - self.rect.x) / self.rect.width
                self.value = self.min_val + t * (self.max_val - self.min_val)

        if event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False

        if event.type == pygame.MOUSEMOTION and self.dragging:
            self.handle_x = max(self.rect.x, min(event.pos[0], self.rect.x + self.rect.width))
            t = (self.handle_x - self.rect.x) / self.rect.width
            self.value = self.min_val + t * (self.max_val - self.min_val)

import pygame
import random

# Zeichnet ein Raster
def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, (40, 40,40), (x, 0), (x, height))

    for y in range(0, height, cell_size):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (width, y))

# Entscheidet random für jede Zelle ob sie lebendig oder tot ist
def random_dead_or_alive():
    for x in range(cols):
        for y in range(rows):
            if grid[x][y] == 1:
                pygame.draw.rect(screen, (cell_color_r, cell_color_g, cell_color_b), (x * cell_size, y * cell_size, cell_size, cell_size))

# Bestätigungsfenster, was nochmal fragt ob man sich sicher ist
def draw_confirm_window():
    # Hintergrundbox
    pygame.draw.rect(screen, (30, 30, 30), (width//2 - 200, height//2 - 100, 400, 200))
    pygame.draw.rect(screen, (200, 200, 200), (width//2 - 200, height//2 - 100, 400, 200), 3)

    # Text
    text = font.render("Spiel wirklich beenden?", True, (255, 255, 255))
    screen.blit(text, (width//2 - text.get_width()//2, height//2 - 60))

    # Buttons
    yes_button.draw(screen)
    no_button.draw(screen)

def draw_value(slider, x, y):
    value = str(int(slider.value))
    if slider == slider_spawn_rate:
        value = str(round(slider.value, 2))
    text = font.render(value, True, (255,255,255))
    screen.blit(text, (x, y))
    pygame.draw.rect(screen, (200, 200, 200), (x-7, y-5, text.get_width() + 15, 35), 1)

# Einstellungsfenster
def draw_settings_window():
    # Hintergrundbox
    pygame.draw.rect(screen, (30, 30, 30), (width//2 - 225, height//2 - 250, 450, 500))
    pygame.draw.rect(screen, (200, 200, 200), (width//2 - 225, height//2 - 250, 450, 500), 3)

    labels = [
        ("Zellgröße", -200),
        ("Spawn-Rate", -150),
        ("Rot", 0),
        ("Grün", 50),
        ("Blau", 100),
        ("Zeit (ms)", 190)
    ]

    # Labels werden gezeichent
    for text, offset in labels:
        t = font.render(text, True, (255,255,255))
        screen.blit(t, (width//2 - t.get_width()//2 - 35, height//2 + offset - 25))

    # Slider werden gezeichnet
    slider_cell_size.draw(screen)
    slider_spawn_rate.draw(screen)
    slider_r.draw(screen)
    slider_g.draw(screen)
    slider_b.draw(screen)
    slider_time.draw(screen)

    # Values neben den Sliders werden gezeichent
    draw_value(slider_cell_size, width//2 + 150, height//2 - 203)
    draw_value(slider_spawn_rate, width//2 + 150, height//2 - 153)
    draw_value(slider_r, width//2 + 150, height//2 - 3)
    draw_value(slider_g, width//2 + 150, height//2 + 47)
    draw_value(slider_b, width//2 + 150, height//2 + 97)
    draw_value(slider_time, width//2 + 150, height//2 + 187)

    # Reset-Button
    reset_button.draw(screen)

# Generiert die nächste Generation
def new_gen():
    new_grid = [[0 for _ in range(rows)] for _ in range(cols)]

    for x in range(cols):
        for y in range(rows):
            alive_neighbors = 0

            # Alle 8 Nachbarn prüfen
            for nx in (-1, 0, 1):
                for ny in (-1, 0, 1):
                    if nx == 0 and ny == 0:
                        continue
                    if 0 <= x + nx < cols and 0 <= y + ny < rows:
                        alive_neighbors += grid[x + nx][y + ny]

            # Regeln von Conway
            if grid[x][y] == 1:
                if alive_neighbors in (2, 3):
                    new_grid[x][y] = 1
                elif alive_neighbors < 2:
                    new_grid[x][y] = 0
                elif alive_neighbors > 3:
                    new_grid[x][y] = 0
            else:
                if alive_neighbors == 3:
                    new_grid[x][y] = 1

    return new_grid

pygame.init()

# Variablen
window = pygame.display
info = pygame.display.Info()
width, height = info.current_w, info.current_h
cell_size = 10
cell_color_r = 255
cell_color_g = 255
cell_color_b = 255
spawn_rate = 0.09
time = 100
cols = width // cell_size
rows= height // cell_size
grid = [[1 if random.random() <= spawn_rate else 0 for _ in range(rows)] for _ in range(cols)]
font = pygame.font.SysFont(None, 40)
show_confirm = False
show_settings = False
paused = False
space_paused = False
update_event = pygame.USEREVENT + 1

# Pending-Werte (werden erst nach Reset aktiv)
pending_cell_size = cell_size
pending_spawn_rate = spawn_rate

# Buttons
yes_button = Button(width//2 - 150, height//2 + 10, 120, 50, text="Ja", button_color=(255, 0, 0))
no_button = Button(width//2 + 30, height//2 + 10, 120, 50, text="Nein")
reset_button = Button(width//2 - 110, height//2 - 110, 150, 40, text="Reset", button_color=(255, 150, 0))

# Slider
slider_cell_size = Slider(width//2 - 185, height//2 - 195, 300, 10, 5, 50, cell_size)
slider_spawn_rate = Slider(width//2 - 185, height//2 - 145, 300, 10, 0.0, 1.0, spawn_rate)

slider_r = Slider(width//2 - 185, height//2 + 5 , 300, 10, 0, 255, cell_color_r, (255,0,0))
slider_g = Slider(width//2 - 185, height//2 + 55, 300, 10, 0, 255, cell_color_g, (0,255,0))
slider_b = Slider(width//2 - 185, height//2 + 105, 300, 10, 0, 255, cell_color_b, (0,0,255))

slider_time = Slider(width//2 - 185, height//2 + 195, 300, 10, 10, 2000, time)

# Initialisiert Fenster
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
window.set_caption("Game of Life")

# Timer
pygame.time.set_timer(update_event, time)

# Game-Loop
running = True
while running:
    for event in pygame.event.get():
        # Wenn das Fenster geschlossen wird, wird das Spiel beendet
        if event.type == pygame.QUIT:
            running = False
        # Event für Escape-Taste
        if not show_settings and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            # Toggle: Man kann mit Escape-Taste confirm Fenster öffnen und schließen
            show_confirm = not show_confirm
            paused = True
            if not show_confirm and not space_paused:
                paused = False

        # Wenn Bestätigungsfenster angezeigt wird
        if show_confirm:
            # Wenn der 'Ja' Button gedrückt wurde
            if yes_button.is_clicked():
                running = False
            # Wenn der 'Nein' Button gedrückt wurde
            if no_button.is_clicked():
                show_confirm = False

        # Wenn Einstellungsfenster angezeigt wird
        if show_settings:
            # Wenn der Reset-Button gedrückt wird
            if reset_button.is_clicked():
                # Werte zu den Werten der Slider anpassen
                cell_size = pending_cell_size
                spawn_rate = pending_spawn_rate

                # cols und rows neu berechnen, weil sich die cell_size geändert hat
                cols = width // cell_size
                rows = height // cell_size

                # Neues grid erstellen
                grid = [[1 if random.random() <= spawn_rate else 0 for _ in range(rows)] for _ in range(cols)]

        # Event für E-Taste
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and not show_confirm:
            show_settings = True
            paused = True
        
        # Damit man die Einstellungen mit Escape schließen kann
        if show_settings and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            show_settings = False
            # Wenn man mit Leertaste pausiert hat bleibt es pausiert, wenn man die Einstellungen schließt
            if not space_paused:
                paused = False

        # Mit Leertaste Simulation pausieren
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not show_confirm and not show_settings:
            paused = not paused
            space_paused = not space_paused

        # Mit R-Taste die Simulation reseten
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and not show_confirm and not show_settings:
            grid = [[1 if random.random() <= spawn_rate else 0 for _ in range(rows)] for _ in range(cols)]

        # Mit Pfeiltaste nach rechts Generationen durchgehen
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and paused and not show_confirm and not show_settings:
            grid = new_gen()

        # Was passiert wenn der Timer einsetzt
        if event.type == update_event and not paused:
            grid = new_gen()

    screen.fill((0, 0, 0))
    draw_grid()
    random_dead_or_alive()
    if show_confirm:
        draw_confirm_window()

    if show_settings:
        draw_settings_window()

        slider_cell_size.update(event)
        slider_spawn_rate.update(event)
        slider_r.update(event)
        slider_g.update(event)
        slider_b.update(event)
        slider_time.update(event)

        # Live-Werte
        cell_color_r = int(slider_r.value)
        cell_color_g = int(slider_g.value)
        cell_color_b = int(slider_b.value)

        time = int(slider_time.value)
        pygame.time.set_timer(update_event, time)

        # Pending-Werte (erst nach Reset aktiv)
        pending_cell_size = int(slider_cell_size.value)
        pending_spawn_rate = slider_spawn_rate.value

    if paused:
        pause_text = font.render("PAUSE", True, (255, 255, 255))
        screen.blit(pause_text, (20, 20))

    window.flip() # Aktualisieren

pygame.quit()