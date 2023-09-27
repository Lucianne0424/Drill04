from pico2d import *

TUK_WIDTH, TUK_HEUGHT = 1280, 720
open_canvas(TUK_WIDTH, TUK_HEUGHT)
tuk_ground = load_image('TUK_GROUND.png')

img = load_image('sheet.png')

def handle_events():
    global running, dirX, dirY

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1


Size  = 150
def printImg():
    global lastDir
    if dirX > 0:
        # 자연스럽게 이미지 출력을 하기 위해 마지막 프레임만 y좌표 값 보정. 바텀값이 어떤 프레임은 머리에서 시작하고 어떤 프레임은 날개에서 시작하는 바람에 높낮이가 달라졌다.
        if frame == 3:
            img.clip_draw(rightMove[frame][0], rightMove[frame][1], rightMove[frame][2], rightMove[frame][3], x, y - 40, Size, Size)
        else:
            img.clip_draw(rightMove[frame][0], rightMove[frame][1], rightMove[frame][2], rightMove[frame][3], x, y, Size, Size)
        lastDir = 0
    elif dirX < 0:
        if frame == 3:
            img.clip_draw(leftMove[frame][0], leftMove[frame][1], leftMove[frame][2], leftMove[frame][3], x, y - 40, Size, Size)
        else:
             img.clip_draw(leftMove[frame][0], leftMove[frame][1], leftMove[frame][2], leftMove[frame][3], x, y, Size, Size)
        lastDir = 1
    elif dirY > 0:
        img.clip_draw(topMove[frame][0], topMove[frame][1], topMove[frame][2], topMove[frame][3], x, y, Size, Size)
        lastDir = 2
    elif dirY < 0:
        if frame == 3:
            img.clip_draw(bottomMove[frame][0], bottomMove[frame][1], bottomMove[frame][2], bottomMove[frame][3], x, y - 25, Size, Size)
        else:
            img.clip_draw(bottomMove[frame][0],bottomMove[frame][1],bottomMove[frame][2],bottomMove[frame][3], x, y, Size, Size)
        lastDir = 3

    elif lastDir == 0:
        if frame == 3:
            img.clip_draw(rightMove[frame][0], rightMove[frame][1], rightMove[frame][2], rightMove[frame][3], x, y - 40, Size, Size)
        else:
            img.clip_draw(rightMove[frame][0], rightMove[frame][1], rightMove[frame][2], rightMove[frame][3], x, y, Size, Size)
    elif lastDir == 1:
        if frame == 3:
            img.clip_draw(leftMove[frame][0], leftMove[frame][1], leftMove[frame][2], leftMove[frame][3], x, y - 40, Size, Size)
        else:
             img.clip_draw(leftMove[frame][0], leftMove[frame][1], leftMove[frame][2], leftMove[frame][3], x, y, Size, Size)
    elif lastDir == 2:
        img.clip_draw(topMove[frame][0], topMove[frame][1], topMove[frame][2], topMove[frame][3], x, y, Size, Size)
    elif lastDir == 3:
        if frame == 3:
            img.clip_draw(bottomMove[frame][0], bottomMove[frame][1], bottomMove[frame][2], bottomMove[frame][3], x, y - 25, Size, Size)
        else:
            img.clip_draw(bottomMove[frame][0], bottomMove[frame][1], bottomMove[frame][2], bottomMove[frame][3], x, y, Size, Size)
def moveCher():
    global  x, y
    x += dirX * 20
    y += dirY * 20
    if x >= TUK_WIDTH - 50 or x <= 0 + 50:
        x -= dirX * 20
    if y >= TUK_HEUGHT - 50 or y <= 0 + 50:
        y -= dirY * 20

running = True
dirX, dirY = 0,0
frame = 1
x, y = TUK_WIDTH // 2, TUK_HEUGHT // 2
lastDir = 0

# 산술 연산은 프레임의 시작 위치 및 프레임의 폭 or 넓이를 계산하기 위해 사용
imgSize = 375
bottomMove = (
    (  0, imgSize - 82,  96 -   0, 82 - 3),
    (164 - 10, imgSize - 78, 227 - 164 + 20, 78 - 0),
    (294, imgSize - 80, 391 - 294, 80 - 1),
    (422, imgSize - 72, 519 - 422, 72 - 15),
)
leftMove = (
    (  0, imgSize - 163,  96 -   0, 163 - 91),
    (148, imgSize - 167, 243 - 148, 167 - 84),
    (295, imgSize - 161, 391 - 295, 161 - 89),
    (422, imgSize - 173, 519 - 422, 173 - 103)
)
rightMove = (
    (  0, imgSize - 259,  95 -   0, 259 - 187),
    (148, imgSize - 263, 243 - 148, 263 - 180),
    (294, imgSize - 257, 390 - 294, 257 - 185),
    (422, imgSize - 269, 519 - 422, 269 - 199)
)
topMove = (
    (  0, imgSize - 375,  96 -   0, 375 - 283),
    (163 - 10, imgSize - 368, 228 - 163 + 20, 368 - 277),
    (294, imgSize - 372, 391 - 294, 372 - 281),
    (422, imgSize - 360, 518 - 422, 360 - 284)
)
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEUGHT // 2)

    printImg()
    moveCher()

    update_canvas()
    handle_events()

    frame = (frame + 1) % 4
    delay(0.1)
