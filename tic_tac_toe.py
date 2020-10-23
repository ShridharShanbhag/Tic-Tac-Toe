import pygame
pygame.init()
win=pygame.display.set_mode((600,700))
pygame.display.set_caption("TIC TAC TOE")
run=True
(a,w,a11,a12,a13,a21,a22,a23,a31,a32,a33)=(180,30,' ',' ',' ',' ',' ',' ',' ',' ',' ')
class coin:
    def __init__(self,face1,face2):
        self.face1=face1
        self.face2=face2
    def switch(self):
        self.face1,self.face2=self.face2,self.face1
op=coin('x','o')
ximg=pygame.image.load('x.png')
oimg=pygame.image.load('o.png')
go=True
while run:
    for event in pygame.event.get():
        pos,mx,my=None,0,0
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            if 0<mx<a and 0<my<a and a11==' ' and go:
                a11=op.face1
                op.switch()
            elif (a+w<mx<2*a+w) and (0<my<a) and a12==' ' and go:
                a12=op.face1
                op.switch()
            elif (2*a+2*w<mx<3*a+2*w) and (0<my<a) and a13==' ' and go:
                a13=op.face1
                op.switch()
            elif (0<mx<a)and(a+w<my<2*a+w) and a21==' ' and go:
                a21=op.face1
                op.switch()
            elif (a+w<mx<2*a+w) and (a+w<my<2*a+w) and a22==' ' and go:
                a22=op.face1
                op.switch()
            elif (2*a+2*w<mx<3*a+2*w) and (a+w< my<2*a+w) and a23==' ' and go:
                a23=op.face1
                op.switch()
            elif (0<mx<a) and (2*a+2*w<my<3*a+2*w) and a31==' ' and go:
                a31=op.face1
                op.switch()
            elif (a+w<mx<2*a+w) and (2*a+2*w<my<2*a+w,3*a+2*w) and a32==' ' and go:
                a32=op.face1
                op.switch()
            elif (2*a+2*w <mx< 3*a+2*w) and (2*a+2*w<my<3*a+2*w) and a33==' ' and go:
                a33=op.face1
                op.switch()
    win.fill((255,255,255))
    if a11=='x':
        win.blit(ximg,(0,0))
    elif a11=='o':
        win.blit(oimg,(0,0))
    if a12=='x':
        win.blit(ximg,(a+w,0))
    elif a12=='o':
        win.blit(oimg,(a+w,0))
    if a13=='x':
        win.blit(ximg,(2*a+2*w,0))
    elif a13=='o':
        win.blit(oimg,(2*a+2*w,0))
    if a21=='x':
        win.blit(ximg,(0,a+w))
    elif a21=='o':
        win.blit(oimg,(0,a+w))
    if a22=='x':
        win.blit(ximg,(a+w,a+w))
    elif a22=='o':
        win.blit(oimg,(a+w,a+w))
    if a23=='x':
        win.blit(ximg,(2*(a+w),a+w))
    elif a23=='o':
        win.blit(oimg,(2*(a+w),a+w))
    if a31=='x':
        win.blit(ximg,(0,2*(a+w)))
    elif a31=='o':
        win.blit(oimg,(0,2*(a+w)))
    if a32=='x':
        win.blit(ximg,(a+w,2*(a+w)))
    elif a32=='o':
        win.blit(oimg,(a+w,2*(a+w)))
    if a33=='x':
        win.blit(ximg,(2*(a+w),2*(a+w)))
    elif a33=='o':
        win.blit(oimg,(2*(a+w),2*(a+w)))
    result=''
    if a11==a12==a13=='x':
        result='X has won the game'
        go=False
    elif a11==a22==a33=='x':
        result='X has won the game'
        go=False
    elif a31==a22==a13=='x':
        result='X has won the game'
        go=False
    elif a11==a21==a31=='x':
        result='X has won the game'
        go=False
    elif a21==a22==a23=='x':
        result='X has won the game'
        go=False
    elif a31==a32==a33=='x':
        result='X has won the game'
        go=False
    elif a12==a22==a32=='x':
        result='X has won the game'
        go=False
    elif a13==a23==a33=='x':
        result='X has won the game'
        go=False
    elif a11==a12==a13=='o':
        result='O has won the game'
        go=False
    elif a31==a22==a13=='o':
        result='O has won the game'
        go=False
    elif a11==a22==a33=='o':
        result='O has won the game'
        go=False
    elif a11==a21==a31=='o':
        result='O has won the game'
        go=False
    elif a21==a22==a23=='o':
        result='O has won the game'
        go=False
    elif a31==a32==a33=='o':
        result='O has won the game'
        go=False
    elif a12==a22==a32=='o':
        result='O has won the game'
        go=False
    elif a13==a23==a33=='o':
        result='O has won the game'
        go=False
    elif (a11 !=' ') and (a12 !=' ') and (a13 !=' ') and (a21 !=' ') and (a22 !=' ') and (a23 !=' ') and (a31 !=' ') and (a32 !=' ') and (a33 !=' '):
        result='Draw'
    font = pygame.font.SysFont('Sans', 32)
    text = font.render(result, True, (255,0,0), (255,255,255))
    textRect = text.get_rect()
    textRect.center = (300, 650)
    win.blit(text,textRect)
    pygame.draw.rect(win,(0,0,0),(a,0,w,600))
    pygame.draw.rect(win,(0,0,0),(2*a+w,0,w,600))
    pygame.draw.rect(win,(0,0,0),(0,a,600,w))
    pygame.draw.rect(win,(0,0,0),(0,2*a+w,600,w))
    pygame.draw.rect(win,(0,0,0),(0,600,600,1))
    pygame.display.update()
pygame.quit()