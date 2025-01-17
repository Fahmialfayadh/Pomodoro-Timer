import pygame
import sys
from button import Button
import winsound

pygame.init()

# aplikasi settings
WIDTH, HEIGHT = 900, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Timer")

CLOCK = pygame.time.Clock()

# Assets
BACKDROP = pygame.image.load("assets/backgrounde.jpg")
WHITE_BUTTON = pygame.image.load("assets/button.png")

# Fonts
FONT = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 120)  # Font utama untuk timer
SMALL_FONT = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 60)  # Font untuk "Waktu Habis!"

# Buttons
START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH / 2, HEIGHT / 2 + 100), 170, 60, "START", 
                           pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#ff2c2c", "#9ab034")
POMODORO_BUTTON = Button(None, (WIDTH / 2 - 150, HEIGHT / 2 - 140), 120, 30, "Pomodoro", 
                         pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#ff2c2c")
SHORT_BREAK_BUTTON = Button(None, (WIDTH / 2, HEIGHT / 2 - 140), 120, 30, "Short Break", 
                            pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#ff2c2c")
LONG_BREAK_BUTTON = Button(None, (WIDTH / 2 + 150, HEIGHT / 2 - 140), 120, 30, "Long Break", 
                           pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#FFFFFF", "#ff2c2c")

# Timer durations
POMODORO_LENGTH = 1500  
SHORT_BREAK_LENGTH = 300  
LONG_BREAK_LENGTH = 900 

# Initial settings
current_seconds = POMODORO_LENGTH
active_timer_length = POMODORO_LENGTH  
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False
timer_expired = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                if started:
                    started = False
                else:
                    started = True
                    timer_expired = False
            if POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                active_timer_length = POMODORO_LENGTH
                current_seconds = POMODORO_LENGTH
                started = False
                timer_expired = False
            if SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                active_timer_length = SHORT_BREAK_LENGTH
                current_seconds = SHORT_BREAK_LENGTH
                started = False
                timer_expired = False
            if LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                active_timer_length = LONG_BREAK_LENGTH
                current_seconds = LONG_BREAK_LENGTH
                started = False
                timer_expired = False

            # Update start/stop button text
            if started:
                START_STOP_BUTTON.text_input = "STOP"
                START_STOP_BUTTON.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20).render(
                    START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
            else:
                START_STOP_BUTTON.text_input = "START"
                START_STOP_BUTTON.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20).render(
                    START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)

        if event.type == pygame.USEREVENT and started:
            current_seconds -= 1
            if current_seconds <= 0:
                current_seconds = 0
                started = False
                timer_expired = True
                winsound.Beep(1000, 1000)  # SUARA beeep
                print("Waktu Habis!") 

                # Reset timer
                current_seconds = active_timer_length

    # Drawing background and buttons
    SCREEN.fill("#ba4949")
    SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH / 2, HEIGHT / 2)))

    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.change_color(pygame.mouse.get_pos())
    POMODORO_BUTTON.update(SCREEN)
    POMODORO_BUTTON.change_color(pygame.mouse.get_pos())
    SHORT_BREAK_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
    LONG_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos())

    # Timer display
    if timer_expired:
        timer_text = SMALL_FONT.render("HABIS DEK!!!", True, "white")
        timer_text_rect = timer_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    else:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
        timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
        timer_text_rect = timer_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 25))
    SCREEN.blit(timer_text, timer_text_rect)

    pygame.display.update()
