BLOCK_SIZE = 25  # ブロックの縦横サイズpx
BLOCK_SIZE2 = 15  # ブロックの縦横サイズpx
FIELD_WIDTH = 10  # フィールドの幅
FIELD_HEIGHT = 20  # フィールドの高さ
MOVE_LEFT = 0  # 左にブロックを移動することを示す定数
MOVE_RIGHT = 1  # 右にブロックを移動することを示す定数
MOVE_DOWN = 2  # 下にブロックを移動することを示す定数
MOVE_Rotate = 3  # 下にブロックを移動することを示す定数
class TetrisSquare():
    def __init__(self, x=0, y=0, color="black"):
        '１つの正方形を作成'
        self.x = x
        self.y = y
        self.color = color

    def set_cord(self, x, y):
        '正方形の座標を設定'
        self.x = x
        self.y = y
    
    def set_pxpy(self, x, y):
        '正方形の座標を設定'
        self.px = x
        self.py = y

    def get_cord(self):
        '正方形の座標を取得'
        return int(self.x), int(self.y)
    
    def get_pxpy(self):
        '正方形の座標を取得'
        return int(self.px), int(self.py)

    def set_color(self, color):
        '正方形の色を設定'
        self.color = color

    def get_color(self):
        '正方形の色を取得'
        return self.color
    def get_Rotate_cord(self,nb):
        if(nb==0):
            x,y=self.get_cord()
            return x,y
        else:
            px,py=self.get_pxpy()
            x,y=self.get_cord()
            vx=x-px
            vy=y-py
            x=px-vy
            y=py+vx
            return x,y
    def get_moved_cord(self, direction):
        '移動後の正方形の座標を取得'

        # 移動前の正方形の座標を取得
        x, y = self.get_cord()

        # 移動方向を考慮して移動後の座標を計算
        if direction == MOVE_LEFT:
            return x - 1, y
        elif direction == MOVE_RIGHT:
            return x + 1, y
        elif direction == MOVE_DOWN:
            return x, y + 1
        else:
            return x, y