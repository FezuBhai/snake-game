import pygame as pg
from pygame.locals import *
import random
#someone from class 11 name BHAI

if __name__=='__main__':
    pg.init()

    pg.mixer.init()
    
#color
    white = (255,255,255)
    black = (0,0,0)
    blue = (2, 213, 250)
    red = (255,0,0)
    skin = (181, 144, 107)
    pink = (243, 23, 73)
#game variable    
    width= 1500
    height = 700
    clock = pg.time.Clock()
    font = pg.font.SysFont(None,70)
    
    showBox=20
#function
    def s_score(text,color,x,y):
        s_text=font.render(text,True,color)
        screen.blit(s_text,[x,y])

    def make_box(box,box_list,box_size):
        for x,y in box_list:
            screen.blit(box,(x,y))


        
        
#handling files 
    
    
    


# main screen
    screen = pg.display.set_mode((width,height))
    pg.display.set_caption("kaif eats saif")
    

#loading image
    box = pg.image.load("box1.png")
    bg = pg.image.load('bg.png')
    bg =pg.transform.scale(bg,(width,height)).convert_alpha()
    mainbg = pg.image.load('mainbg.png')
    mainbg =pg.transform.scale(mainbg,(width,height)).convert_alpha()
    gameover = pg.image.load('gameover.png').convert_alpha()
    

    # food img is selected to be inside gameloop so that i can change it 

    def main_menu(box):
        # game variable
        
        button = pg.Rect(710,455,120,60)
        button2 = pg.Rect(980,450,70,25)
        
        index=0
        try:
            with open('high.txt',"r")as f:
                hiscore =f.read()
                
        except:
            hiscore = 0
        
        
        running = True
        while running :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False 
                if event.type == MOUSEBUTTONDOWN:
                    if button.collidepoint(event.pos):
                        running = False 

                        pg.mixer.music.load("main.mp3")
                        pg.mixer.music.play()
                        gameloop(box)
                    if button2.collidepoint(event.pos):
                        index += 1
                        if index < 7:
                            box = pg.image.load(f"box{index}.png").convert_alpha() 
                        else:
                            index = 0
                if event.type == KEYDOWN:
                    
                    if event.key == K_c :
                        index += 1
                        if index < 7:
                            box = pg.image.load(f"box{index}.png").convert_alpha() 
                        else:
                            index = 0
                            
                    if event.key == K_RETURN:
                        running = False 
                        pg.mixer.music.load("main.mp3")
                        pg.mixer.music.play()
                        gameloop(box)

            screen.blit(mainbg,(0,0))
           
            
            s_score(f"{hiscore}",pink,900,305)
            screen.blit(box,(995,420))
            pg.display.update()
            clock.tick(30)

    

    def gameloop(box):
        
        Bx = 0
        By = 70
        food = pg.image.load('saif.png').convert()
        
        vel_x =0
        vel_y = 0
        running = True
        game_over= False
        fps =30
        offset= 20
        food_x = random.randint(0,width-offset )
        food_y = random.randint(70,height-offset)
        score = 0
        button = pg.Rect(430,400,270,130)
        button2 = pg.Rect(740,400,245,130)
        try:
            with open('high.txt',"r")as f:
                hiscore =f.read()
        except:
            hiscore = 0
            
        box_list = []
        box_size =1
        
        
                

        while running == True:    
            if game_over== True:
                screen.blit(gameover,(250,100))
               

                s_score(f"{score} ",white,750,305)
                with open('high.txt',"w")as f:
                    f.write(str(hiscore))
                
                if event.type == MOUSEBUTTONDOWN:
                    if button.collidepoint(event.pos):
                        running= False

                        pg.mixer.music.load("main.mp3")
                        pg.mixer.music.play()
                        gameloop(box)
                    if button2.collidepoint(event.pos):
                        running= False

                        pg.mixer.music.load("home.mp3")
                        pg.mixer.music.play()
                        main_menu(box)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                        quit()
                    
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN:
                            running= False
                            pg.mixer.music.load("home.mp3")
                            pg.mixer.music.play()
                            main_menu(box)
                        if event.key == K_SPACE:
                            running= False 
                            pg.mixer.music.load("main.mp3")
                            pg.mixer.music.play()
                            gameloop(box)
            elif game_over == False:    
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                        quit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                        

                        elif event.key == K_a or event.key == K_LEFT :
                            vel_y =0
                            vel_x =-10
                            
                        

                        elif event.key == K_d or event.key == K_RIGHT:
                            vel_y =0
                            vel_x = 10
            

                        elif event.key == K_w or event.key == K_UP :
                            vel_x =0
                            vel_y = -10
                            

                        elif event.key == K_s or event.key == K_DOWN :
                            vel_x =0
                            vel_y =10
                        
                Bx += vel_x 
                By += vel_y 

                if abs(Bx-food_x)<15 and abs(By-food_y)<20:
                    score +=10 
                    box_size +=3
                    foodNo= random.randint(0,1)

                    if score > int(hiscore):
                         hiscore = score
                    
                    if foodNo ==1:
                         
                        food = pg.image.load('saif.png').convert()
                                    
                    else:
                        food = pg.image.load('kaif.png').convert()
                    food_x = random.randint(0,width-offset)
                    food_y = random.randint(70,height-offset) 
                    

                
                screen.blit(bg,(0,0))
                
                s_score(f"{score}",skin,250,12)
                s_score(f"{hiscore}",skin,1360,12)
                screen.blit(food,(food_x,food_y))
               
                head=[]
                head.append(Bx)
                head.append(By)
                box_list.append(head)


                if len(box_list) > box_size:
                    del box_list[0]

                if head in box_list[:-1] or Bx>width-offset or Bx<0 or By>height-offset or By<60:
                    game_over = True
                    pg.mixer.music.load("out.mp3")
                    pg.mixer.music.play()

                # if Bx>width or Bx<0 or By>height or By<60: 
                    # game_over = True
                    
                    
                    
                make_box(box,box_list,box_size)

                
           
            pg.display.update()
            clock.tick(fps)   


    pg.mixer.music.load("home.mp3")
    pg.mixer.music.play()
    main_menu(box)            
