import random
import pygame
import sys
from button import button_class

#инициализация
pygame.init()

#размер экрана
width, height = 1280, 720

#фоны
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AkiNumber")
background_main = pygame.image.load("back_main.png")
background_rules = pygame.image.load("back_rules.png")
background_game1 = pygame.image.load("back_game1.png")
background_game2 = pygame.image.load("back_game2.png")
background_game3 = pygame.image.load("back_game3.png")
background_limbo = pygame.image.load("back_limbo.jpg")
background_final = pygame.image.load("back_final.png")
backgrounds = [background_game1, background_game2, background_game3]

#функция окна главного меню
def main_menu():
    #создание кнопок
    start_height = 240
    start_button = button_class(width / 2 - (400 / 2), start_height, 400, 100, "начать игру", "button.png","button_hover.png")
    rules_button = button_class(width / 2 - (400 / 2), start_height + 150, 400, 100, "правила", "button.png","button_hover.png")
    exit_button = button_class(width / 2 - (400 / 2), start_height + 300, 400, 100, "выйти", "button.png","button_hover.png")

    running = True
    while running:
        #вывод фон
        screen.fill((0, 0, 0))
        screen.blit(background_main, (0, 0))

        #вывод текста
        font = pygame.font.Font('Delta Block.ttf', 100)
        text_surface = font.render("AkiNumber", True, (250,250,250))
        text_rect = text_surface.get_rect(center=(width/2, 125))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                game()
            if event.type == pygame.USEREVENT and event.button == rules_button:
                rules()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for buttons in [start_button, rules_button, exit_button]:
                buttons.handle_event(event)

        for buttons in [start_button, rules_button, exit_button]:
            buttons.draw(screen)
            buttons.check_hover(pygame.mouse.get_pos())

        pygame.display.flip()

#функция окна правил
def rules():
    #создание кнопок
    back_button = button_class(width / 2 - (400 / 2), 240 + 300, 400, 100, "обратно", "button.png","button_hover.png")

    running = True
    while running:
        #вывод фона
        screen.fill((0, 0, 0))
        screen.blit(background_rules, (0, 0))

        #вывод текста
        font = pygame.font.Font('Delta Block.ttf', 70)
        font2 = pygame.font.Font('Delta Block.ttf', 40)
        text_surface = font.render("Правила просты:", True, (250, 250, 250))
        text_surface2 = font2.render("Вы загадываете число от 0 до 1000 (включительно)", True, (250, 250, 250))
        text_surface3 = font2.render("Программа постарается угадать ваше число", True, (250, 250, 250))
        text_surface4 = font2.render("Отвечайте на её вопросы только правду", True, (250, 250, 250))
        text_surface5 = font2.render("Если программа не угадает ваше число,", True, (250, 250, 250))
        text_surface6 = font2.render("то вы выиграли :)", True, (250, 250, 250))
        text_rect = text_surface.get_rect(center=(width / 2, 125))
        text_rect2 = text_surface2.get_rect(center=(width / 2, 215))
        text_rect3 = text_surface3.get_rect(center=(width / 2, 290))
        text_rect4 = text_surface4.get_rect(center=(width / 2, 365))
        text_rect5 = text_surface5.get_rect(center=(width / 2, 440))
        text_rect6 = text_surface6.get_rect(center=(width / 2, 490))
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface2, text_rect2)
        screen.blit(text_surface3, text_rect3)
        screen.blit(text_surface4, text_rect4)
        screen.blit(text_surface5, text_rect5)
        screen.blit(text_surface6, text_rect6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu()

            back_button.handle_event(event)

        back_button.draw(screen)
        back_button.check_hover(pygame.mouse.get_pos())

        pygame.display.flip()

#функция окна игры
def game():
    #(up > low, n for asked number, last for y/n, r for random background, question = question on display)
    low = 0
    up = 1000
    n = (up - low) // 2
    last = 0
    r = random.randrange(0, 3, 1)
    question = "Число больше, чем " + str(n) + "?"

    #создание кнопок
    yes_button = button_class(width / 2 - (400 / 2), 300, 400, 100, "да", "button.png","button_hover.png")
    no_button = button_class(width / 2 - (400 / 2), 450, 400, 100, "нет", "button.png", "button_hover.png")

    running = True
    while running:
        #вывод фона
        screen.fill((0, 0, 0))
        screen.blit(backgrounds[r], (0, 0))
        #вывод текста
        font = pygame.font.Font('Delta Block.ttf', 40)
        text_surface = font.render(question, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(width / 2, 110))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            #проверка на конец программы (up-low < 2)
            if (abs(up - (low - 1)) > 1) != 1:
                if (last == 1):
                    final (up)
                else:
                    final (low)

            if event.type == pygame.USEREVENT and event.button == yes_button:
                r = random.randrange(0, 3, 1)
                low = n + 1
                n = n + (abs((up - (low - 1))) // 2)
                last = 1
                question = "Число больше, чем " + str(n) + "?"

            if event.type == pygame.USEREVENT and event.button == no_button:
                r = random.randrange(0, 3, 1)
                up = n
                n = n - (abs((up - (low - 1))) // 2)
                last = 0
                question = "Число больше, чем " + str(n) + "?"

            for buttons in [yes_button, no_button]:
                buttons.handle_event(event)

        for buttons in [yes_button, no_button]:
            buttons.draw(screen)
            buttons.check_hover(pygame.mouse.get_pos())

        pygame.display.flip()

#функция окна ответа
def final(answer):
    ans = "Я думаю, что вы загадали число " + str(answer) + "!"

    #создание кнопок
    yes_button = button_class(width / 2 - (700 / 2), 250, 620, 100, "да, сыграть ещё раз!", "button.png", "button_hover.png")
    no_button = button_class(width / 2 - (700 / 2), 400, 620, 100, "нет...", "button.png", "button_hover.png")
    exit_button = button_class(width / 2 - (700 / 2), 550, 620, 100, "вернуться к меню", "button.png","button_hover.png")

    running = True
    while running:
        #вывод экрана
        screen.fill((0, 0, 0))
        screen.blit(background_final, (0, 0))
        #вывод текста
        font = pygame.font.Font('Delta Block.ttf', 35)
        text_surface = font.render(ans, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(width / 2, 110))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == yes_button:
                game()
            if event.type == pygame.USEREVENT and event.button == no_button:
                limbo()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                main_menu()

            for buttons in [yes_button, no_button, exit_button]:
                buttons.handle_event(event)

        for buttons in [yes_button, no_button, exit_button]:
            buttons.draw(screen)
            buttons.check_hover(pygame.mouse.get_pos())

        pygame.display.flip()

#функция окна, которое не должно быть открыто, но может
def limbo():
    #создание кнопок
    back_button = button_class(width / 2 - (700 / 2), 550, 620, 100, "вернуться к меню", "button.png","button_hover.png")

    running = True
    while running:
        #вывод экрана
        screen.fill((0, 0, 0))
        screen.blit(background_limbo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu()

            back_button.handle_event(event)

        back_button.draw(screen)
        back_button.check_hover(pygame.mouse.get_pos())

        pygame.display.flip()

#вызов функции главного меню, включение игры
main_menu()

