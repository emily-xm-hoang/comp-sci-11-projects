import pygame
import sys
import math
import random
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('python_game/assets/beepbox.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 507
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("dreamcatchers")
huge_font = pygame.font.Font("python_game/assets/font.ttf", 60)
hud_font = pygame.font.Font("python_game/assets/font.ttf", 40)
med_font = pygame.font.Font("python_game/assets/font.ttf", 30)
small_font = pygame.font.Font("python_game/assets/font.ttf", 20)
tiny_font = pygame.font.Font("python_game/assets/font.ttf", 15)
bg_image = pygame.image.load('python_game/assets/bg.png').convert()
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

boy_img = pygame.image.load("python_game/assets/1.png").convert_alpha()
girl_img = pygame.image.load("python_game/assets/2.png").convert_alpha()
all_sprites = pygame.sprite.Group()

class boy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("python_game/assets/1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (95, 200))
        self.rect  = self.image.get_rect(topleft=(x, y))
        self.speed = 12

class girl(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("python_game/assets/2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (122, 195))
        self.rect  = self.image.get_rect(topleft=(x, y))
        self.speed = 12

class feather(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("python_game/assets/feather.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 40))
        random_x = random.randint(0, 860) 
        self.rect = self.image.get_rect(topleft=(random_x, -30)) 
        self.speed = random.randint(5, 8)

    def update(self):
        self.rect.y += self.speed
        
        if self.rect.y > 507:
            self.kill()

flock = pygame.sprite.Group()

class star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("python_game/assets/star.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        random_x = random.randint(0, 860) 
        self.rect = self.image.get_rect(topleft=(random_x, -30)) 
        self.speed = random.randint(5, 8)

    def update(self):
        self.rect.y += self.speed
        
        if self.rect.y > 507:
            self.kill()
galaxy = pygame.sprite.Group()

class ghost(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("python_game/assets/boo.png").convert_alpha()
        random_size = random.randint(50, 120)
        self.image = pygame.transform.scale(self.image, (random_size, random_size))
        random_x = random.randint(0, 860) 
        self.rect = self.image.get_rect(topleft=(random_x, -30)) 
        self.speed = random.randint(10, 15)

    def update(self):
        self.rect.y += self.speed
        
        if self.rect.y > 507:
            self.kill()
booby_trap = pygame.sprite.Group()

running = True
game_state = "main_menu"
mode = "normal"
state = "waiting"
state_count = 0
feather_counter = 0
ghost_counter = 0
galaxy_counter = 0
boy = boy(305, 193)
girl = girl(490, 198)
score = 0
lives = 5
arrow_x = 330
text_offset_y = 0      
text_direction = 1    
text_timer = 0
keys = pygame.key.get_pressed()

while running:
    FPS = 30
    clock = pygame.time.Clock()
    clock.tick(FPS)
    text_timer += 1
    if text_timer >= 15:
        text_timer = 0
        text_direction *= -1
    text_offset_y += text_direction * 0.5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_state == "main_menu":
            game_state = "character_selection"
            
        if game_state == "character_selection":
            if arrow_x == 330:
                    character = "boy"
                    boy.rect.topleft = (305, 193) 
            if arrow_x == 530:
                character = "girl"
                girl.rect.topleft = (490, 198)  

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    arrow_x = 330
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    arrow_x = 530 

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game_state = "main_menu"
            score = 0
            lives = 5
            flock.empty()
            booby_trap.empty()
            galaxy.empty()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if game_state == "character_selection":
                if arrow_x == 330:
                    character = "boy"
                    boy.rect.topleft = (398, 193) 
                if arrow_x == 530:
                    character = "girl"
                    girl.rect.topleft = (398, 198)  
                game_state = "playing"

    if game_state == "game_over":
        screen.blit(bg_image, (0, 0))
        animated_y = 70 + text_offset_y
        fast_y = 70 + (text_offset_y * 2)
        shadow_text = hud_font.render("game over", True, (161, 165, 212))
        score_text = hud_font.render("game over", True, (255, 255, 255))
        screen.blit(shadow_text, (345 + 5, animated_y + 5))
        screen.blit(score_text, (345, animated_y ))

        start_shadow = small_font.render("press [esc] to restart >>", True, (161, 165, 212))
        start_text = small_font.render("press [esc] to restart >>", True, (255, 255, 255))
        screen.blit(start_shadow, (315 + 3, animated_y + 50 + 3))
        screen.blit(start_text, (315, animated_y + 50))
        
    if game_state == "playing":
        feather_counter += 1
        ghost_counter += 1
        galaxy_counter += 1
        state_count += 1
        if state == "waiting":
            mode = "normal"
            if state_count >= 600:
                state_count = 0
                state = "active"
                mode = random.choice(["lucid", "nightmare"])
                if mode == "lucid":
                    booby_trap.empty()
                elif mode == "nightmare":
                    flock.empty()
        elif state == "active":
            if state_count >= 300:
                state_count = 0
                state = "waiting"
                mode = "normal"

        if feather_counter >= 18:
            feather_counter = 0
            if mode == "lucid":
                for _ in range(5):
                    flock.add(feather())
            elif mode == "normal":
                flock.add(feather())

        if ghost_counter >= 45:
            ghost_counter = 0
            if mode == "nightmare":
                for _ in range(6):
                    booby_trap.add(ghost())
            elif mode == "normal":
                booby_trap.add(ghost())

        if galaxy_counter >= 300:
            galaxy_counter = 0
            if mode == "lucid":
                for _ in range(6):
                    galaxy.add(star())
            elif mode == "normal":
                galaxy.add(star())

        animated_y = 10 + text_offset_y
        flock.update() 
        booby_trap.update()
        galaxy.update()
        screen.blit(bg_image, (0, 0))
        if character == "boy":
            sprite = boy
        else:
            sprite = girl
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: 
            sprite.rect.x -= sprite.speed
        if keys[pygame.K_d]: 
            sprite.rect.x += sprite.speed
        screen.blit(sprite.image, sprite.rect)
        flock.draw(screen) 
        booby_trap.draw(screen)
        galaxy.draw(screen)
        score_lives_shadow = med_font.render("Score: {}\nLives: {}".format(score, lives), True, (161, 165, 212))
        score_text = med_font.render("Score: {}\nLives: {}".format(score, lives), True, (255, 255, 255))
        screen.blit(score_lives_shadow, (10 + 5, animated_y + 5))
        screen.blit(score_text, (10, animated_y))

        if sprite.rect.x < 0:
            sprite.rect.x = 0
            
        if sprite.rect.x > 780:
            if sprite == boy and sprite.rect.x > 805:
                sprite.rect.x = 805
            elif sprite == girl:
                sprite.rect.x = 780

        death = pygame.sprite.spritecollide(sprite, booby_trap, True)
        if death:
            lives -= 1
            if lives == 0:
                game_state = "game_over"
        immunity = pygame.sprite.spritecollide(sprite, galaxy, True)
        if immunity:
            lives += 1

        if character == "boy":
            basket = pygame.Rect(sprite.rect.x + 20, sprite.rect.y + 130, 95, 10)
        else: 
            basket = pygame.Rect(sprite.rect.x + 30, sprite.rect.y + 120, 95, 10)

        for bird in flock:
            if basket.colliderect(bird.rect):
                score += 1
                bird.kill()

        if mode == "lucid":
            lucid_shadow = hud_font.render("lucid dreaming", True, (161, 165, 212))
            lucid_text = hud_font.render("lucid dreaming", True, (255, 255, 255))
            screen.blit(lucid_shadow, (305 + 5, animated_y + 5 + 50))
            screen.blit(lucid_text, (305, animated_y + 50))

        if mode == "nightmare":
            nightmare_shadow = hud_font.render("nightmare", True, (161, 165, 212))
            nightmare_text = hud_font.render("nightmare", True, (255, 255, 255))
            screen.blit(nightmare_shadow, (335 + 5, animated_y + 5 + 50))
            screen.blit(nightmare_text, (335, animated_y + 50))

    if game_state == "character_selection":
        current_time = pygame.time.get_ticks()
        animated_y = 70 + text_offset_y
        fast_y = 75 + (text_offset_y * 3.5)
        screen.blit(bg_image, (0, 0))

        selection_shadow = hud_font.render("pick a character", True, (161, 165, 212))
        selection_text = hud_font.render("pick a character", True, (255, 255, 255))
        screen.blit(selection_shadow, (295 + 5, animated_y + 5))
        screen.blit(selection_text, (295, animated_y))

        enter_shadow = tiny_font.render("press [enter] to confirm", True, (161, 165, 212))
        enter_text = tiny_font.render("press [enter] to confirm", True, (255, 255, 255))
        screen.blit(enter_shadow, (365 + 3, animated_y + 50 + 3))
        screen.blit(enter_text, (365, animated_y + 50))

        screen.blit(boy.image, boy.rect)
        screen.blit(girl.image, girl.rect)

        def arrow(x):
            arrow_shadow = huge_font.render("v", True, (255, 255, 255))
            arrow_text = huge_font.render("v", True, (61, 65, 112))
            screen.blit(arrow_shadow, (x + 5, fast_y + 5 + 35))
            screen.blit(arrow_text, (x, fast_y + 35))
        arrow(arrow_x)

    if game_state == "main_menu":
        screen.blit(bg_image, (0, 0))
        animated_y = 70 + text_offset_y
        fast_y = 70 + (text_offset_y * 2)
        shadow_text = hud_font.render("dreamcatchers", True, (161, 165, 212))
        score_text = hud_font.render("dreamcatchers", True, (255, 255, 255))
        screen.blit(shadow_text, (305 + 5, animated_y + 5))
        screen.blit(score_text, (305, animated_y ))

        start_shadow = tiny_font.render("press [space bar] to start >>", True, (161, 165, 212))
        start_text = tiny_font.render("press [space bar] to start >>", True, (255, 255, 255))
        screen.blit(start_shadow, (345 + 3, animated_y + 50 + 3))
        screen.blit(start_text, (345, animated_y + 50))

        creator_shadow = tiny_font.render("created by: emily hoang", True, (161, 165, 212))
        creator = tiny_font.render("created by: emily hoang", True, (255, 255, 255))
        screen.blit(creator_shadow, (5 + 3, animated_y - 55 + 3))
        screen.blit(creator, (5, animated_y - 55))
        music_shadow = tiny_font.render("music also by me", True, (161, 165, 212))
        music = tiny_font.render("music also by me", True, (255, 255, 255))
        screen.blit(music_shadow, (5 + 3, animated_y - 35 + 3))
        screen.blit(music, (5, animated_y - 35))
        
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()
sys.exit()