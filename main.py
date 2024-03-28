import pygame
import random

# Инициализация pygame
pygame.init()

# Основные параметры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Заголовок и иконка
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("images/icon.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения мишени и настройка размеров
target_img = pygame.image.load("images/target.png")
target_width = 80
target_height = 80

# Начальное положение мишени и уменьшенная скорость
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = random.choice([-0.4, -0.2, 0.2, 0.4])  # Уменьшенная скорость
target_speed_y = random.choice([-0.4, -0.2, 0.2, 0.4])  # Уменьшенная скорость

# Начальное количество очков
score = 0

# Шрифт для отображения счета
score_font = pygame.font.SysFont("comicsansms", 32)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Главный цикл игры
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Увеличиваем счет при попадании и сброс положения мишени
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Перемещение мишени
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка столкновений с краями экрана
    if target_x <= 0 or target_x + target_width >= SCREEN_WIDTH:
        target_speed_x *= -1
    if target_y <= 0 or target_y + target_height >= SCREEN_HEIGHT:
        target_speed_y *= -1

    # Отрисовка мишени
    screen.blit(target_img, (target_x, target_y))

    # Вывод счета
    score_text = score_font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.update()

pygame.quit()