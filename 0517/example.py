import pygame

pygame.init()

screen_surf = pygame.display.set_mode((640,480)) #1280,720 화면사이즈 조절 sulface는 rect를 가짐

ship_img=pygame.image.load('images/ship.bmp')
alien_img=pygame.image.load('images/alien.bmp')

# ship_rect=pygame.rect.Rect(0,0,100,100) #rect의 위치 지정
ship_rect=ship_img.get_rect() #다른방식으로 + getrect에 넣고
ship_rect.midbottom = screen_surf.get_rect().midbottom #bottom 가운데로 맞춰라
alien_rect=pygame.rect.Rect(200,200,200,200)
bullet_rect = None
bullets = []

# bullet_rect = pygame.rect.Rect(0,0,5,30) #총알만들기
# bullet_rect.midbottom = ship_rect.midtop #총알 위치 지정


clock = pygame.time.Clock()

left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False


while True: #종료되지 않게 루프문 돌때마다 새로 그림
    # Process player inputs. 이벤트코드
    for event in pygame.event.get(): #한번에 담아뒀다가 하나씩 나옴
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #스페이스바 누를때 총알발사
                bullet_rect = pygame.rect.Rect(0,0,5,30) #총알 리스트 만들고 붙여넣기
                bullet_rect.midbottom = ship_rect.midtop
                bullets.append(bullet_rect)

            if event.key == pygame.K_RIGHT:    
                # ship_rect.x = ship_rect.x +5
                # alien_rect.x = alien_rect.x +7
                right_pressed = True
            elif event.key == pygame.K_LEFT:
                # ship_rect.x = ship_rect.x -10
                # alien_rect.x = alien_rect.x -20
                left_pressed = True
            elif event.key == pygame.K_UP:
                # ship_rect.y = ship_rect.y -10
                # alien_rect.y = alien_rect.y -20
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                # ship_rect.y = ship_rect.y +10
                # alien_rect.y = alien_rect.y +20
                down_pressed = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                  right_pressed = False    
            elif event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False

            
            


    # Do logical updates here. #루프문 돌때마다 새로 그림(보이는 화면이 두개 필요)
    # ... 업데이트 코드
    if right_pressed:
        ship_rect.x = ship_rect.x +1
        alien_rect.x = alien_rect.x +2

    if left_pressed:
        ship_rect.x = ship_rect.x -1
        alien_rect.x = alien_rect.x -2

    if up_pressed:
        ship_rect.y = ship_rect.y -1
        alien_rect.y = alien_rect.y -2

    if down_pressed:
        ship_rect.y = ship_rect.y +1
        alien_rect.y = alien_rect.y +2

    for bullet in bullets:  #총알 움직임
        bullet.y = bullet.y -5

    # bullet_rect.y = bullet_rect.y -5 #총알 쏘기(움직임) 

    screen_surf.fill("white")  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    screen_surf.blit(ship_img, ship_rect)
    screen_surf.blit(alien_img, alien_rect)
    if bullets: #총알그림
        for bullet in bullets:
            pygame.draw.rect(screen_surf, 'purple', bullet)

    # pygame.draw.rect(screen_surf, 'purple', bullet_rect) #총알 화면에 보이게
    pygame.display.flip()  # Refresh on-screen display 처음화면 보여주다가 두번째 화면 호출전환
    clock.tick(60)         # wait until next frame (at 60 FPS) 초당 60번 화면돌려줌