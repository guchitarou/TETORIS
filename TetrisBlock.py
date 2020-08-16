from TetrisSquare import TetrisSquare
BLOCK_SIZE = 25  # ブロックの縦横サイズpx
BLOCK_SIZE2 = 15  # ブロックの縦横サイズpx
FIELD_WIDTH = 10  # フィールドの幅
FIELD_HEIGHT = 20  # フィールドの高さ
MOVE_LEFT = 0  # 左にブロックを移動することを示す定数
MOVE_RIGHT = 1  # 右にブロックを移動することを示す定数
MOVE_DOWN = 2  # 下にブロックを移動することを示す定数
MOVE_Rotate = 3  # 下にブロックを移動することを示す定数

class TetrisBlock():
    def __init__(self,block_type):
        'テトリスのブロックを作成'
        self.squares = []
        # ブロックの形をランダムに決定
        self.set_my_number(block_type)
        # ブロックの形に応じて４つの正方形の座標と色を決定
        if block_type == 1:
            color = "red"
            cords = [
                [FIELD_WIDTH / 2, 1],
                [FIELD_WIDTH / 2, 0],
                [FIELD_WIDTH / 2, 2],
                [FIELD_WIDTH / 2, 3],
            ]
        elif block_type == 2:
            color = "blue"
            cords = [
                [FIELD_WIDTH / 2, 1],
                [FIELD_WIDTH / 2, 0],
                [FIELD_WIDTH / 2 - 1, 0],
                [FIELD_WIDTH / 2 - 1, 1],
            ]
        elif block_type == 3:
            color = "green"
            cords = [
                [FIELD_WIDTH / 2, 1],
                [FIELD_WIDTH / 2, 0],
                [FIELD_WIDTH / 2 - 1, 0],
                [FIELD_WIDTH / 2, 2],
            ]
        elif block_type == 4:
            color = "orange"
            cords = [
                [FIELD_WIDTH / 2 - 1, 1],
                [FIELD_WIDTH / 2 - 1, 0],
                [FIELD_WIDTH / 2, 0],
                [FIELD_WIDTH / 2 - 1, 2],
            ]
        elif block_type == 5:
            color = "purple"
            cords = [
                [FIELD_WIDTH / 2 , 1],
                [FIELD_WIDTH / 2, 0],
                [FIELD_WIDTH / 2 - 1, 1],
                [FIELD_WIDTH / 2 + 1, 1],
            ]
        elif block_type == 6:
            color = "cyan"
            cords = [
                [FIELD_WIDTH / 2 , 1],
                [FIELD_WIDTH / 2, 0],
                [FIELD_WIDTH / 2 - 1, 1],
                [FIELD_WIDTH / 2 - 1, 2],
            ]
        elif block_type == 7:
            color = "yellow"
            cords = [
                [FIELD_WIDTH / 2 , 1],
                [FIELD_WIDTH / 2, 0],
                [FIELD_WIDTH / 2 + 1, 1],
                [FIELD_WIDTH / 2 + 1, 2],
            ]
            
        # 決定した色と座標の正方形を作成してリストに追加
        for cord in cords:
            self.squares.append(TetrisSquare(cord[0], cord[1], color))
    
    def set_my_number(self,x):
        self.my_number=x
    def get_my_number(self):
        return self.my_number
      

    def get_squares(self):
        'フィールドを構成する正方形のリストを取得'

        return self.squares

    def get_square(self, x, y):
        '指定した座標の正方形を取得'

        return self.squares[y * self.width + x]

    
        
    def move(self, direction):
        # ブロックを構成する正方形を移動        
        if direction==MOVE_Rotate:
            i=0
            vx,vy=self.squares[0].get_cord()
            for square in self.squares:
                square.set_pxpy(vx,vy)
                x, y = square.get_Rotate_cord(i)
                square.set_cord(x, y)
                i=i+1
        else:
            for square in self.squares:
                x, y = square.get_moved_cord(direction)
                square.set_cord(x, y)