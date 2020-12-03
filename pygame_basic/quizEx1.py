"""
하늘에서 떨어지는 똥 피하기 게임을 만드시오
[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐, X 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS 는 30으로 고정'
[게임 이미지]

1. 배경 : 640 * 480(세로 * 가로) - background.png
2. 캐리기터 : 70 * 70 - character.png
3. 똥 : 70 * 70 -enemy.png
"""
import random
import pygame
#####################################################################
# 기본 초기화 부분
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption(" Quiz Game")

#FPS

clock = pygame.time.Clock()
######################################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 이동 속도,  폰트 등)

# 배경 만들기
background = pygame.image.load("C:\\Users\\hany0\\OneDrive\\바탕 화면\\pythonWorkspace\\python20201123\\python20201123\\pygame_basic\\background.png")

# 캐릭터 만들기
character = pygame.image.load("C:\\Users\\hany0\\OneDrive\\바탕 화면\\pythonWorkspace\\python20201123\\python20201123\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width /2)
character_y_pos = screen_height - character_height

# 이동 위치
to_x = 0
character_speed = 10


# 똥 만들기
ddong = pygame.image.load("C:\\Users\\hany0\\OneDrive\\바탕 화면\\pythonWorkspace\\python20201123\\python20201123\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 10

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) 
   
# 2. 이벤트 처리(키보드, 마우스 등)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

# 3. 게임 케릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed 

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)



 # 4. 충돌처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌 했습니다.")
        running = False

 # 5. 화면에 그리기

    screen.blit(background,(0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    pygame.display.update() # 게임 화면 다시 그리기!


pygame.quit()


