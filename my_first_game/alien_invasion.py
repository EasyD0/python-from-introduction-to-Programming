import sys
import pygame
from settings import Settings

class AlienInvasion:
    """管理资源和行为的类"""
    
    def __init__(self):
        pygame.init()
        
        self.settings=Settings() #self.settings是Settings类型的

        self.screen=pygame.display.set_mod((self.settings.screen_width,self.settings.screen_height))
           #设置显示窗口大小,self.settings.screen_width,self.settings.screen_height) 是一个元组
        pygame.display.set_caption('Alien Invasion')   #设置窗口的标题(caption)

        self.bg_color=self.settings.bg_color #建立一个bg_color数据成员来保存背景颜色


    def run_game(self):
        """游戏的主循环"""

        while True:
            """监视鼠标和键盘的事件"""
            for event in pygame.event.get():   
                #pygame.event.get()将返回一个list,包含从上次调用结束 到 这次调用时刻 的时间段内
                #所有的键盘和鼠标事件

                if event.type == pygame.QUIT:   
                    #单击关闭窗口就是pygame.QUIT事件,若关闭,则调用sys.exit退出
                    sys.exit
            
            self.screen.fill(self.bg_color) #每次绘制前重新填充背景色

            pygame.display.flip()
            #该函数让最近绘制的屏幕可见,每次while循环的时候都会重新绘制,擦除之前的屏幕
            #while循环每执行一次,该指令将刷新屏幕一次

if __name__=='__main__':
    ai = AlienInvasion()   #创造游戏实例
    ai.run_game()   #运行该实例
