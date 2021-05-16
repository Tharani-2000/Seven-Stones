from setup import *
from intro import *
from database import *
from purchase import *
from characters import *
from runner import *
from sevenstones import *

alltimehighscore = 0

def update_score(score, highscore):
    updatecoins(score)
    if int(highscore) > int(alltimehighscore):
        updatehighscore(int(highscore))


def quit_game(score, highscore):
    update_score(score, highscore)
    pygame.quit()
    sys.exit(0)


def main():
    global alltimehighscore
    alltimehighscore = gethighscore()
    score_font = pygame.font.Font('04B_19.ttf', 25)
    font = pygame.font.Font('04B_19.ttf', 15)
    high_score = 0

    global ball_list
    start = False
    pygame.mixer.music.play(-1)

    create_runner_time = pygame.USEREVENT
    pygame.time.set_timer(create_runner_time, 10000)

    cycle = pygame.USEREVENT
    pygame.time.set_timer(cycle, 250)
    index = 0

    direction_arr = ['left', 'right', 'left', 'left', 'right', 'right', 'left', 'right', 'right', 'left', 'left']
    runs = [createRunner(random.choice(direction_arr), window)]
    ball_image_posx = 200

    score = getcoins()

    COOLDOWN = 2
    cool = 0
    hit = False
    purchase_bool = False
    ball_image = checkballimage()

    lives = 7

    color_list = [red(window), blue(window), green(window), black(window), yellow(window), grey(window), orange(window)]

    while True:
        if high_score < 50:
            FPS = 60
        elif high_score < 100:
            FPS = 80
        elif high_score < 200:
            FPS = 100
        else:
            FPS = 120

        clock.tick(FPS)

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():

            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
                quit_game(score, high_score)

            if event.type == pygame.KEYDOWN:
                start = True

            if keys[pygame.K_LEFT]:
                ball_image_posx = (ball_image_posx - 15) % 400

            if keys[pygame.K_RIGHT]:
                ball_image_posx = (ball_image_posx + 15) % 400

            if keys[pygame.K_SPACE]:
                if cool == 0:
                    temp = Ball(window, ball_image_posx, ball_image)
                    ball_list.append(temp)
                if cool >= COOLDOWN:
                    cool = 0
                else:
                    cool += 1

            if hit:

                if event.type == create_runner_time and len(runs) < 1:
                    runs.append(createRunner(random.choice(direction_arr), window))

                if event.type == cycle:
                    index = (index + 1) % 3

        window.blit(background, (0, 0))

        if start and hit and not purchase_bool and lives > 0:
            if len(ball_list) > 10:
                ball_list = ball_list[10:]

            for color in color_list:
                color.display()
            high_score += 0.01
            for run in runs:
                run.image_selection(index)
                run.move()
                x = run.rectangle.centerx

                for color in color_list:
                    if run.collision(color.rect) and run.stone is False:
                        run.stone = True
                        run.colors = color
                        color_list.remove(color)

                if x < 0 or x > 400:
                    if run.stone:
                        lives -= 1
                    runs.remove(run)
                for j in ball_list:
                    ball = j
                    if ball.collide(run.rectangle):
                        score += 10
                        try:
                            if run.stone:
                                color_list.append(run.colors)
                                run.colors.visible = True
                            runs.remove(run)
                            ball_list.remove(ball)
                        except:
                            pass

            for j in ball_list:
                ball = j
                ball.move()

            if len(runs) > 2:
                runs = runs[2:]
            window.blit(ball_image, (ball_image_posx, 580))


        elif start and not purchase_bool:
            goli_surface = pygame.image.load(os.path.join('images', 'goli.jpeg')).convert_alpha()
            goli_surface = pygame.transform.scale(goli_surface, (100, 120))
            goli_rect = goli_surface.get_rect(center=(200, 360))

            window.blit(goli_surface, goli_rect)

            for ball in ball_list:
                ball.move()

                if ball.collide(goli_rect):
                    hit = True
                    ball_list.remove(ball)
            window.blit(ball_image, (ball_image_posx, 580))


        elif not purchase_bool:
            window.blit(start_screen, (0, 0))

        mouse = pygame.mouse.get_pos()
        if button2("Mute Music", mouse[0], mouse[1], 250, 0, 150, 30, (43, 3, 132), (60, 0, 190), 10):
            pygame.mixer.music.pause()
        if button2("Play Music", mouse[0], mouse[1], 250, 40, 150, 30, (43, 3, 132), (60, 0, 190), 10):
            pygame.mixer.music.unpause()

        if button2("Store", mouse[0], mouse[1], 250, 80, 150, 30, (43, 3, 132), (60, 0, 190), 10) or purchase_bool:
            purchase_bool, score = purchase(window, score, background)
            ball_image = checkballimage()


        if lives == 0:

            window.blit(background, (0, 0))

            if high_score > alltimehighscore:
                image = pygame.image.load(os.path.join('images', 'new-high-score.png')).convert_alpha()
                image = pygame.transform.scale(image, (120, 120))
                window.blit(image, (140, 170))

            score_surface1 = score_font.render("Your Score", True, (0, 0, 0))
            score_rect1 = score_surface1.get_rect(center=(200, 290))
            window.blit(score_surface1, score_rect1)
            score_surface2 = score_font.render(str(int(score)), True, (0, 0, 0))
            score_rect2 = score_surface2.get_rect(center=(185, 330))
            window.blit(score_surface2, score_rect2)

            mouse = pygame.mouse.get_pos()
            if button2("Restart", mouse[0], mouse[1], 75, 400, 100, 50, (43, 3, 132), (60, 0, 190), 15):
                ball_image_posx = 200

                COOLDOWN = 2
                cool = 0
                hit = False
                lives = 7
                index = 0
                start = False
                color_list = [red(window), blue(window), green(window), black(window), yellow(window), grey(window),
                              orange(window)]


                update_score(score, high_score)

            if button2("QUIT", mouse[0], mouse[1], 200, 400, 100, 50, (255, 0, 0), (255, 77, 77), 15):
                quit_game(score, high_score)

        # coins
        score_surface = score_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(75, 20))
        window.blit(score_surface, score_rect)

        score_surface = font.render(('COINS'), True, (0, 0, 0))
        score_rect = score_surface.get_rect(center=(20, 20))
        window.blit(score_surface, score_rect)

        # highcore
        curr_score_surface = score_font.render(str(alltimehighscore), True, (255, 255, 255))
        curr_score_rect = curr_score_surface.get_rect(center=(75, 60))
        window.blit(curr_score_surface, curr_score_rect)

        score_surface = font.render(('HIGH'), True, (0, 0, 0))
        score_rect = score_surface.get_rect(center=(25, 50))
        window.blit(score_surface, score_rect)

        score_surface = font.render(('SCORE'), True, (0, 0, 0))
        score_rect = score_surface.get_rect(center=(25, 65))
        window.blit(score_surface, score_rect)

        # curr_score high_score
        score_surface = score_font.render(str(int(high_score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(75, 100))
        window.blit(score_surface, score_rect)

        score_surface = font.render(('CURRENT'), True, (0, 0, 0))
        score_rect = score_surface.get_rect(center=(29, 90))
        window.blit(score_surface, score_rect)

        score_surface = font.render(('SCORE'), True, (0, 0, 0))
        score_rect = score_surface.get_rect(center=(25, 105))
        window.blit(score_surface, score_rect)

        pygame.display.update()


intro(window, poweredby, clock)
main()
