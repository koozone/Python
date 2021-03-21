import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480								# 화면 가로 크기
screen_height = 640								# 화면 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Nado Game')			# 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load('D:/Work Folder/Private/Python/pygame_basic/background.png')

# 캐릭터 불러오기
character = pygame.image.load('D:/Work Folder/Private/Python/pygame_basic/character.png')
character_size = character.get_rect().size		# 캐릭터 크기 구해옴
character_width = character_size[0]				# 케릭터 가로 크기
character_height = character_size[1]			# 캐릭터 세로 크기
character_x_pos = (screen_width - character_width) / 2
character_y_pos = (screen_height - character_height)

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True									# 게임 진행중임
while running:
	for event in pygame.event.get():			# 어떤 이벤트가 발생했는가?
		if event.type == pygame.QUIT:			# 창이 닫히는 이벤트가 발생했는가?
			running = False						# 게임 진행중 아님

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				to_x -= 0.2
			elif event.key == pygame.K_RIGHT:
				to_x += 0.2
			elif event.key == pygame.K_UP:
				to_y -= 0.2
			elif event.key == pygame.K_DOWN:
				to_y += 0.2

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				to_x = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				to_y = 0

	character_x_pos += to_x			# 가로 위치
	character_y_pos += to_y			# 세로 위치

	# 가로 위치 경계 처리
	character_x_pos = max(character_x_pos, 0)
	character_x_pos = min(character_x_pos, (screen_width - character_width))
	# 세로 위치 경계 처리
	character_y_pos = max(character_y_pos, 0)
	character_y_pos = min(character_y_pos, (screen_height - character_height))

	screen.blit(background, (0, 0))				# 배경 그리기
	screen.blit(character, (character_x_pos, character_y_pos))

	pygame.display.update()						# 화면 다시 그리기

# pygame 종료
pygame.quit()