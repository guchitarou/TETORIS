import tkinter as tk
from tkinter import font
import random


from TetrisSquare import TetrisSquare
from TetrisBlock import TetrisBlock 
from TetrisField import TetrisField,HoldField
from TetrisCanvas import TetrisCanvas,TetrisCanvas2
from EventHandller import EventHandller
#from Music import Music

BLOCK_SIZE = 25  # ブロックの縦横サイズpx
BLOCK_SIZE2 = 15  # ブロックの縦横サイズpx
FIELD_WIDTH = 10  # フィールドの幅
FIELD_HEIGHT = 20  # フィールドの高さ
MOVE_LEFT = 0  # 左にブロックを移動することを示す定数
MOVE_RIGHT = 1  # 右にブロックを移動することを示す定数
MOVE_DOWN = 2  # 下にブロックを移動することを示す定数
MOVE_Rotate = 3  # 下にブロックを移動することを示す定数

class TetrisGame():

    def __init__(self, master):
        'テトリスのインスタンス作成'
      # ブロック管理リストを初期化
        self.field = TetrisField()
        self.field2 = HoldField()
        

        # 落下ブロックをセット
        self.block = None
        self.hold_number=None
        self.master=master
        # テトリス画面をセット
        self.canvas = TetrisCanvas(master, self.field)
        self.canvas2 = TetrisCanvas2(master, self.field2)

        # テトリス画面アップデート
        self.canvas.update(self.field, self.block)
        self.canvas2.update(self.field2, self.block)
        font3 = font.Font( size = 15)
        self.label6 = tk.Label(master, text="スコア", font=font3)
        self.label6.place(x = 300, y = 70)
        self.label8 = tk.Label(master, text="ストック", font=font3)
        self.label8.place(x = 304, y = 167)
        self.label7 = tk.Label(self.master, text="", font=font3)
        self.label7.place(x = 320, y = 90)
        self.set_score(0)

    def start(self, func):
        'テトリスを開始'
        self.set_score(0)
        self.hold_number=None
        self.block = None
        self.field = TetrisField()
        self.field2 = HoldField()
        self.canvas2.update(self.field2, self.block)
        self.end_func = func
        self.new_block()
    def set_hold_number(self,x):
        self.hold_number=x
    def get_hold_number(self):
        return self.hold_number
    
    def set_score(self,x):
        self.score=int(x)
        font3 = font.Font( size = 15)
        self.label7.destroy()
        self.label7 = tk.Label(self.master, text=str(x), font=font3)
        self.label7.place(x = 320, y = 90)
    def get_score(self):
        return self.score
    
    def new_block(self):
        'ブロックを新規追加'
        next_block_number=random.randint(1, 7)

        # 落下中のブロックインスタンスを作成
        self.block = TetrisBlock(next_block_number)

        if self.field.judge_game_over(self.block):
            self.end_func()

        # テトリス画面をアップデート
        self.canvas.update(self.field, self.block)
    def new_hold_block(self,next_block_number):

        # 落下中のブロックインスタンスを作成
        self.block = TetrisBlock(next_block_number)

        if self.field.judge_game_over(self.block):
            self.end_func()

        # テトリス画面をアップデート
        self.canvas.update(self.field, self.block)
        
    
    def hold_block(self):
        self.field.hold(self.block)
        next=self.get_hold_number()
        self.set_hold_number(self.block.get_my_number())
        h_block = TetrisBlock(self.block.get_my_number())
        self.canvas2.update(self.field2,h_block)
        if next==None:
            self.new_block()
        else:
            self.new_hold_block(next)
        
            
    def move_block(self, direction):
        # 画面をアップデート
        if self.field.judge_can_move(self.block, direction):
            self.block.move(direction)
            self.canvas.update(self.field, self.block)
        else:
            # ブロックが下方向に移動できなかった場合
            if direction == MOVE_DOWN:
                # ブロックを固定する
                self.field.fix_block(self.block)
                p=self.get_score()
                p=self.field.delete_line(int(p))
                self.set_score(p)
                self.new_block()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # アプリウィンドウの設定
        self.geometry("400x600")
        self.title("テトリス")

        # テトリス生成
        game = TetrisGame(self)
        # イベントハンドラー生成
        EventHandller(self, game)


if __name__ in '__main__':
    #Music()
    app = Application()
    app.mainloop()
    #Music().stop()
    