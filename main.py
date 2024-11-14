import pygame
#Sử dụng hàm sleep()
import time 
import math
pygame.init()

screen = pygame.display.set_mode((500,600))
GREY = (150,150,150) #set màu cho màn hình
running = True
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
total_secs = 0
total = 0
Start = False
# Khởi tạo font chữ
font = pygame.font.SysFont('sans', 50)
font1 = pygame.font.SysFont('sans', 100)
#Tạo chữ để điền vào ô
b1= font.render('+',True, BLACK)
b2= font.render('-',True, BLACK)
b3= font.render('Min',True, BLACK)
b4= font.render('Sec',True, BLACK)
b5= font.render('Start',True, BLACK)
b6= font.render('Reset',True, BLACK)
#Khởi tạo giá trị ban đầu
mins = 0
secs = 0
while running:
	screen.fill(GREY) # tạo màu cho màn hình
	#Lấy tạo độ của chuột
	mouse_x,mouse_y = pygame.mouse.get_pos()
	#tạo 1 ô vuông trắng với toạ độ sau hình vẽ với (2 số đầu là khoảng cách bắt đầu vẽ 2 số sau là khoảng cách vẽ)
	pygame.draw.rect(screen, WHITE, (100,50,50,50)) # ô 1
	pygame.draw.rect(screen, WHITE, (200,50,50,50)) # ô 2
	pygame.draw.rect(screen, WHITE, (300,50,150,50)) # ô 3
	pygame.draw.rect(screen, WHITE, (100,200,50,50)) # ô 4
	pygame.draw.rect(screen, WHITE, (200,200,50,50)) # ô 5
	pygame.draw.rect(screen, WHITE, (300,200,150,50)) # ô 6
	pygame.draw.rect(screen, WHITE, (60,530,380,30)) # ô 7

	pygame.draw.rect(screen, BLACK, (50,520,400,50)) 
	pygame.draw.rect(screen, WHITE, (60,530,380,30))
	#Vẽ +
	screen.blit(b1,(110,45))
	screen .blit(b1,(210,45))
	#Vẽ -
	screen.blit(b2,(115,190))
	screen.blit(b2,(215,190))
	#Vẽ start
	screen.blit(b5,(310,45))
	#Vẽ Reset
	screen.blit(b6,(310,195))
	#Vẽ đồng hồ
	pygame.draw.circle(screen,BLACK,(250,375),100)
	pygame.draw.circle(screen,WHITE,(250,375),98)
	pygame.draw.circle(screen,BLACK,(250,375),5)


	for event in pygame.event.get(): #tạo tương tác đối với chương trình

		if event.type == pygame.QUIT: #Tương tác với nút x tắt chương trình

			running = False #Chuyển thành False để tắt
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				#Xác định toạ độ dấu cộng
				if (100 <mouse_x<150) and (50<mouse_y<100):
					total_secs += 60
					total = total_secs
				if (200 < mouse_x < 250) and (50 < mouse_y < 100):
					total_secs += 1
					total = total_secs
				#Xác định tạo đô dấu trừ
				if (100<mouse_x<150) and (200<mouse_y<250):
					total_secs -= 60
					total = total_secs
				if (200<mouse_x<250) and (200<mouse_y<250):
					total_secs -= 1
					total = total_secs
				#Xác định nút Start
				if (300<mouse_x<450) and (50<mouse_y<100):
					total = total_secs
					Start = True
				#Xác định nút Reset
				if (300<mouse_x<450) and (200<mouse_y<250):
					total_secs = 0
					total = total_secs
	#Vẽ lệnh cho nút start
	if Start:
		if total_secs > 0:
			total_secs -= 1
			time.sleep(1)
		else:
			Start = False
	#Vẽ thời gian hiện tại
	mins = total_secs//60
	secs = total_secs-(mins * 60)
	text_time = font1.render(str(mins) + " : " + str(secs),True,RED)
	screen.blit(text_time,(100,100))
	#Vẽ kim giây chạy 
	# xc = 250 + rsina
	x_secs = 250 + 90*math.sin(6*secs*math.pi/180)
	# yc = 400 - rcosa
	y_secs = 375 - 90*math.cos(6*secs*math.pi/180)
	pygame.draw.line(screen,BLACK,(250,375), (int(x_secs),int(y_secs)))
	#Vẽ kim phút
	x_mins = 250 + 50*math.sin(6*mins*math.pi/180)
	# yc = 400 - rcosa
	y_mins = 375 - 50*math.cos(6*mins*math.pi/180)
	pygame.draw.line(screen,BLACK,(250,375), (int(x_mins),int(y_mins)))
	#Vẽ hình chữ nhật đỏ để giảm dần theo thời gian
	if total!=0:
		pygame.draw.rect(screen,RED,(60,530,int(380*(total_secs/total)),30))
	pygame.display.flip() #hàm để khiến màn hình hiện màu

pygame.quit() #Thoát chương trình giảm dung lượng bộ nhớ