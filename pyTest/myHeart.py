import random
from math import sin,cos,pi,log

from tkinter import *

CANVAS_WIDTH = 640      # 画布宽
CANVAS_HEIGHT = 480     # 画布高
CANVAS_CENTER_X = CANVAS_WIDTH/2    # 画布中心位置
CANVAS_CENTER_Y = CANVAS_HEIGHT/2   # 画布中心位置

# 放大比例
IMAGE_ENLIARGE = 11         # 内层心的放大比例

HEART_COLOR = "#FF7171"     # 心的颜色

# (x²+y²-1)³+x²y³ = 0 心形线
# x²z³+9y²z³/80=(x²+9y²/4+z²-1)³ 心形三维曲面
# x²+y² = (2x²+2y²-x)² 心形线
# 参数方程
# x=a(2cost-cos2t)
# y=a(2sint-sin2t)


def heart_function(t, shrink_ratio=IMAGE_ENLIARGE):
    """
    生成器
    :param t: 随机生成数，范围在 0-2*pi
    :param shrink_ratio: 方法比例
    :return: 坐标
    """
    # 爱心基础函数（根据随机数，和基础函数公式得到x和y的值）
    x = 16*(sin(t)**3)
    y = -(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t))

    # 放大
    x *= shrink_ratio
    y *= shrink_ratio

    # 移到画布中央
    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y

    return int(x),int(y)


def scatter_inside(x, y, beta=0.15):
    """
    ❤扩散
    :param x:
    :param y:
    :param beta: 强度
    :return: 新坐标
    """
    ratio_x = -beta * log(random.random(), 10)      # 0到1的随机数的自然对数
    ratio_y = -beta * log(random.random(), 10)

    if ratio_y > 0.1:
        ratio_y -= (ratio_y * 10 % 10)*0.1

    dx = ratio_x * (x-CANVAS_CENTER_X)
    dy = ratio_y * (x-CANVAS_CENTER_Y)

    return x-dx, y-dy


def shrink(x,y,ratio):
    """
    抖动
    :param x:
    :param y:
    :param ratio: 比例
    :return: 新坐标
    """

    force = -1/(((x-CANVAS_CENTER_X)**2+(y-CANVAS_CENTER_Y)**2)**0.6)
    dx = ratio*force*(x-CANVAS_CENTER_X)
    dy = ratio*force*(y-CANVAS_CENTER_Y)

    return x-dx, y-dy


def curve(p):
    """
    自定义曲线函数，调整跳动周期
    :param p:
    :return: 正弦
    """
    return 2*(4*sin(4*p))/(2*pi)

class Heart:
    """
    心类
    """
    def __init__(self, generate_frame=20):
        self._points = set()  # 原始爱心坐标集合
        self._edge_diffusion_points = set()     # 边缘扩散效果点坐标集合
        self._center_diffusion_points = set()   # 中心扩散 效果点坐标集合
        self.all_points = {}        # 每帧动态点坐标

        self.random_halo = 1000
        self.generate_frame = generate_frame

        self.build(2000)

        for frame in range(generate_frame):
            self.calc(frame)


    def build(self, number):
        for i in range(number):
            t = random.uniform(0, 2 * pi)  # 随机不到的地方造成爱心有缺口
            x, y = heart_function(t)
            self._points.add((x, y))

        # 爱心内扩散
        for _x, _y in list(self._points):
            for _ in range(10):
                x, y = scatter_inside(_x, _y, 0.35)
                self._edge_diffusion_points.add((x, y))

        # 爱心内再次扩散
        point_list = list(self._points)

        for i in range(4000):
            x, y = random.choice(point_list)        # 返回point_list中的随机项
            x, y = scatter_inside(x, y, 0.15)
            if x and y:
                self._center_diffusion_points.add((x, y))


    @staticmethod
    def calc_position(x, y, ratio):
        # 调整缩放比例
        force = 1 / (((x-CANVAS_CENTER_X)**2+(y-CANVAS_CENTER_Y)**2)**0.520) # 魔方函数
        dx = ratio * force * (x-CANVAS_CENTER_X)+random.randint(-1, 1)
        dy = ratio * force * (y-CANVAS_CENTER_Y)+random.randint(-1, 1)

        return x-dx, y-dy


    def calc(self, generate_frame):
        ratio = 10*curve(generate_frame/10*pi)  # 圆滑的周期的缩放比例
        halo_radius = int(4+6*(1+curve(generate_frame/10*pi)))
        halo_number = int(3000+4000*abs(curve(generate_frame/10*pi)**2))

        all_points = []

        # 光环
        heart_halo_point = set()    # 光环的点坐标集合

        for i in range(halo_number):
            t = random.uniform(0, 2*pi)  # 随机不到的地方造成爱心有缺口
            x, y = heart_function(t, shrink_ratio=11.6)  # 魔方参数
            x, y = shrink(x, y, halo_radius)
            if(x, y) not in heart_halo_point:
                # 处理新的点
                heart_halo_point.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_points.append((x, y, size))

        # 轮廓
        for x, y in self._points:
            x,y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        # 内容，这里有问题了
        for x, y in self._edge_diffusion_points:
            x, y = self.calc_position(x,y,ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        for x,y in self._center_diffusion_points:
            x,y = self.calc_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        self.all_points[generate_frame] = all_points

    def render(self, render_canvas, render_frame):
        for x, y, size in self.all_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x+size, y+size, width=0, fill=HEART_COLOR)      # 建立矩形



def draw(main:Tk,render_cavas:Canvas,render_heart:Heart,render_frame=0):
    render_cavas.delete('all')
    render_heart.render(render_cavas, render_frame)
    main.after(160, draw, main, render_cavas, render_heart, render_frame+1)



if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, bg="black", height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    canvas.pack()
    heart = Heart()
    draw(root, canvas, heart)
    root.mainloop()
