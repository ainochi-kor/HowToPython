#*****************************************************************************
# 슈팅게임,     resource 참조 : http://suanlab.com/youtube.html
#*****************************************************************************

import pygame, cv2
import numpy as np
import sys, time, random

padWidth = 640                                          # 게임화면 가로,세로 크기
padHeight = 480

MOVE_INTERVAL = 10                                      # 전투기 좌우 이동 크기(pixel수)
MAX_CRASH_NO = 3                                        # 게임 전투기 수

# 운석 이미지
rockImage = ['resources\\rock01.png','resources\\rock02.png', \
             'resources\\rock03.png','resources\\rock04.png', \
             'resources\\rock05.png','resources\\rock06.png', \
             'resources\\rock07.png','resources\\rock08.png', \
             'resources\\rock09.png','resources\\rock10.png']
# 사운드
explosionSound = ['.\\resources\\explosion01.wav','.\\resources\\explosion02.wav' \
                  ,'.\\resources\\explosion04.wav','.\\resources\\explosion04.wav']
#=============================================================================
# 점수 출력
#=============================================================================
def printHitScore(hitCount):
    font = pygame.font.Font('.\\resources\\NanumGothic.ttf',25)
    text = font.render('파괴한 운석수:' + str(hitCount), True, (0,0,255))
    gamePad.blit(text,(5,5)) 
 
def printMissedScore(missedCount):
    font = pygame.font.Font('.\\resources\\NanumGothic.ttf',25)
    text = font.render('놓친 운석수:' + str(missedCount), True, (255,0,0))
    gamePad.blit(text,(padWidth-170,5))

def printMessage(message) :    
    font = pygame.font.Font('.\\resources\\NanumGothic.ttf',50)
    text = font.render(message , True, (255,0,0))
    gamePad.blit(text,(int(padWidth/3),int(padHeight/2)))
 
#=============================================================================
# 게임 초기화
#=============================================================================
def initGame() :
    global gamePad, clock, background, fighter, missile, explosion, missileSound

    pygame.init()
    gamePad = pygame.display.set_mode((padWidth,padHeight))
    pygame.display.set_caption('Shooting')

    # 그림 관련 파일 설정
    fighter = pygame.image.load(".\\resources\\fighter.png")# 전투기 그림 설정
    missile = pygame.image.load(".\\resources\\missile.png")# 전투기 그림 설정
    explosion = pygame.image.load(".\\resources\\explosion.png")# 폭발 그림 설정

    # 사운드 관련 파일 설정
    '''
    #music.wav파일이 커서 resource 압축 파일에서 빠져 있음
    pygame.mixer.music.load('.\\resources\\music.wav')
    pygame.mixer.music.play(-1)
    '''
    missileSound = pygame.mixer.Sound('.\\resources\\missile.wav')
    clock = pygame.time.Clock()         
    
#=============================================================================
# 게임 실행 및 이벤트 처리
#=============================================================================
def runGame():
    global gamePad, clock, backgound, fighter, missile, explosion, \
           missileSound, explosionSound, padWidth, padHeight

    # 전투기 크기 정보 추출
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    # 전투기 취치 설정
    x = padWidth * 0.5                              # x,y: 전투기 가로, 새로 위치
    y = padHeight * 0.9                             #       초기위치는 화면 중앙 아래쪽
    fighterXPos = 0                                 # 전투기 가로 위치 이동량

    # 미사일 위치 리스트 초기화    
    missilePos = []                                 # 발사된(화면에 보여질) 미사일들 위치 (x,y)

    # 운석 생성
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]

    rockX = random.randrange(0,padWidth-rockWidth)
    rockY = 0
    rockSpeed = 1

    # 점수 및 관련 변수 초기화
    isShot = False                                  # 운석 충돌 여부
    shotCount = 0                                   # 운석을 맞춘 횟수
    rockMissed = 0                                  # 운석을 높친 횟수
    crashCount = 0

    cap = cv2.VideoCapture(0)                       # 웹캠 객체 생성
    #========================================================================
    # 게임 무한루프 시작 부분
    #========================================================================
    while True :
        ret, frame = cap.read()                     # 웹캠에서 영상 캡춰
                                                    # pygame Surface 포맷으로 변경
        bg_color=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        background = np.rot90(bg_color)
        background = pygame.surfarray.make_surface(background)  # 배경이미지 생성
        #-------------------------------------------
        # [1] 게임 화면에 배경 그림 그리기
        #-------------------------------------------
        gamePad.blit(background,(0,0))              

        #-------------------------------------------
        # [2] 사용자 입력 처리 - 종료/전투기이동/미사일발사
        #-------------------------------------------
        for event in pygame.event.get():
                # 종료
            if event.type in [pygame.QUIT] :         
                pygame.quit()                       # (2-1) 게임 종료 
                break                               #       무한루프 종료
                # 좌/우로 전투기 위치 이동
            elif event.type in [pygame.KEYDOWN]:    # (2-2) 키보드 아래로 눌러졌을때
                if event.key == pygame.K_LEFT:      #       왼쪽 화살표  
                    fighterXPos -= MOVE_INTERVAL    #       전투기 위치 이동량 왼쪽(-)으로 변경
                elif event.key == pygame.K_RIGHT:   #       오른쪽 화살표
                    fighterXPos += MOVE_INTERVAL

                elif event.key == pygame.K_SPACE:   # (2-3) 스페이스바 - 미사일 발사
                    missileSound.play()             # 미사일 사운드 재생
                    missileX = x + fighterWidth/2   # 미사일 위치 - 전투기 가로 위치에 연동되게
                    missileY = y - fighterHeight    #               전투기 앞머리(상단) 위치
                    missilePos.append([missileX, missileY])

            elif event.type in [pygame.MOUSEBUTTONDOWN] :   # 마우스 클릭 - 미사일 발사
                missileSound.play()                 # 미사일 사운드 재생
                missileX = x + fighterWidth/2       # 미사일 위치 - 전투기 가로 위치에 연동되게
                missileY = y - fighterHeight        #               전투기 앞머리(상단) 위치
                missilePos.append([missileX, missileY])
                
            elif event.type in [pygame.KEYUP]:         
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:         
                    fighterXPos = 0


        #-------------------------------------------
        # [3] 전투기 위치 조정 및 그리기
        #-------------------------------------------
        x += fighterXPos                            # 키보드 값에 따라 전투기 위치좌표 재계산
        if x < 0 :                                  # 화면 왼쪽 바깥으로 안나가게
            x = 0
        elif x > (padWidth - fighterWidth) :        # 화면 오른쪽 바깥으로 벗어나지 않게
            x = padWidth - fighterWidth

        gamePad.blit(fighter,(int(x),int(y)))       # 전투기 위치 그리기
        
        #-------------------------------------------
        # [4] 전투기와 운석 충돌 체크
        #-------------------------------------------
                                                    # 운석 우측끝이 전투기 전투기 왼쪽보다 크고
                                                    # 운석 좌측이 전투기 우측보다 작고
        if x <= rockX + rockWidth  and x+fighterWidth >= rockX  and \
            y <= (rockY + rockHeight) :             # 운석 아래쪽이 전투기 위쪽보다 크면 충돌
            gamePad.blit(explosion,(rockX,rockY))
                                                    # 파괴 사운드
            destroySound = pygame.mixer.Sound(random.choice(explosionSound))
            destroySound.play()

            crashCount += 1                         # 파괴된 전투기 수 증가
            rockX = 10000                           # 이 if분이 속 실행 되지 않게
                                                    # 배경화면 색깔 변화 후 그리기
            bg_gray=cv2.cvtColor(bg_color,cv2.COLOR_RGB2GRAY)
            background = np.rot90(bg_gray)
            background = pygame.surfarray.make_surface(background)
            gamePad.blit(background,(0,0))
            printMessage("전투기 파괴 !!!")          # 메세지 출력
            
        #-------------------------------------------
        # [5] 전체 미사일에 대하여 세로상의 좌표 재계산/그리기
        #-------------------------------------------
        if len(missilePos) > 0:
            
            for i, bulletPos in enumerate(missilePos): # bullet[0]:x좌표,bullet[1]:y좌표
                bulletPos[1] -= 10                     # 위쪽으로 10 Pixel 이동
                missilePos[i][1] = bulletPos[1]

                # 미사일이 운석을 맟춘 경우
                if bulletPos[1] < rockY :
                    if rockX <= bulletPos[0] <= rockX + rockWidth :
                        missilePos.remove(bulletPos)    # 미사일 리스트에서 해당 미사일 제거
                        isShot = True
                        shotCount += 1
                        
                if bulletPos[1] < 0 and len(missilePos) > 0:
                    missilePos.remove(bulletPos)
                    
        # 전체 미사일 그리기
        if len(missilePos) > 0:
            for bulletX, bulletY in missilePos:
                gamePad.blit(missile,(int(bulletX),int(bulletY)))             # 미사일 그리기
                
        #-------------------------------------------
        # [6] 새로운 운석 그리기 - 운석이 바닥에 닿거나, 미사일에 파괴될 때
        #-------------------------------------------
        rockY += rockSpeed                          # 운석 세로 위치 조정

        if rockY > padHeight or isShot:             # 이전 운석이 바닥에 닿거나
            # 폭발 그리기
            if isShot:
                gamePad.blit(explosion,(rockX,rockY))
                                                    # 폭발 사운드 설정/재생
                destroySound = pygame.mixer.Sound(random.choice(explosionSound))
                destroySound.play()
                isShot = False

                rockSpeed += 1
                rockSpeed = min(rockSpeed, 9)       # 최대 속도를 9로 제한
            else :
                rockMissed += 1
                
            # 새로운 운석 생성
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0,padWidth-rockWidth)
            rockY = 0  

        gamePad.blit(rock,(rockX,rockY))                 # 운석 그리기

        #-------------------------------------------
        # [7] 점수 출력
        #-------------------------------------------
        printHitScore(shotCount)
        printMissedScore(rockMissed)

        if crashCount >= MAX_CRASH_NO :
            printMessage("게임오버 !!!")
        
        #-------------------------------------------
        # [8] 화면 다시 그림
        #-------------------------------------------
        pygame.display.update()                         # 게임 화면 업데이              
        clock.tick(60)                                  # FPS(Frame Per Second) 설정
                                                        # 게임실행 속도에 영향 예:5 -> 느림
    #------------------------ 무한 루프 끝 --------------------------------------------------
    cap.release()

initGame()
runGame()
