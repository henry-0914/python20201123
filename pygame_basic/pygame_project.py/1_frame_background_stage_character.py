import os
import pygame
#####################################################################
# 기본 초기화 부분
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("pangpang Game")

#FPS

clock = pygame.time.Clock()
######################################################################

# 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 이동 속도,  폰트 등)
current_path = 

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) 
   
# 2. 이벤트 처리(키보드, 마우스 등)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

# 3. 게임 케릭터 위치 정의
   


 # 4. 충돌처리를 위한 rect 정보 업데이트

    

 # 5. 화면에 그리기

    


    pygame.display.update() # 게임 화면 다시 그리기!


pygame.quit()

