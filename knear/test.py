import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D




def paint_3d1():
    fig = plt.figure(5) #创建窗口
    ax = fig.add_subplot(1,1,1, projection='3d')
    x,y = np.mgrid[-2:2:20j,-2:2:20j]
    z=x*np.exp(-x**2-y**2)   #获取z轴数据

    ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)  #绘制三维图表面
    ax.set_xlabel('x-name')     #x轴名称
    ax.set_ylabel('y-name')     #y轴名称
    ax.set_zlabel('z-name')

    plt.show()


def paint_zzt():
    price = [39.5, 39.9, 45.4, 38.9, 33.34]
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.barh(range(5),price,align='center',color='black',alpha=0.5)
    plt.xlabel('price')
    plt.yticks(range(5),['Amazon','Dangdang','BooksChina','Jingdong','Tianmao'])
    plt.xlim([32,47])
    plt.title('Book Price Comparsion')
    for x,y in enumerate(price):
        plt.text(y+0.1,x,'%s' %y,va='center')
    plt.show()


def paint_3d2():
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    u = np.linspace(-1,1, 100)
    x,y = np.meshgrid(u,u)
    z = x * x + y*y
    ax.plot_surface(x,y,z ,rstride=4,cstride=4,cmap=plt.cm.coolwarm)
    plt.show()


def paint_count():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    u = np.linspace(-1,1, 100)
    x, y = np.meshgrid(u, u)
    z = x **2 + y**2
    ax.contourf(x,y,z)
    plt.show()


paint_3d2()
