from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap


iris = datasets.load_iris()

#print(iris.data[0:15])


def paint3D():
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    print(X)
    fig = plt.figure(5)
    ax=fig.add_subplot(1,1,1,projection='3d')     #绘制三维图

    x,y=np.mgrid[-2:2:20j,-2:2:20j]  #获取x轴数据，y轴数据
    z=x*np.exp(-x**2-y**2)   #获取z轴数据

    ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)  #绘制三维图表面
    ax.set_xlabel('x-name')     #x轴名称
    ax.set_ylabel('y-name')     #y轴名称
    ax.set_zlabel('z-name')     #z轴名称

    plt.show()

def paintEdg(iris):
    x = iris.data[:,:2]
    y = iris.target
    x_min, x_max = x[:,0].min() - 0.5, x[:,0].max() + 0.5
    y_min, y_max = y[:,0].min() - 0.5, y[:,0].max() + 0.5
    cmap_light = ListedColormap(['#AAAAFF','#AAFFAA','#FFAAAA'])
    h = .02
    xx,yy = np.meshgrid(np.arange(x_min, x_max, h), np.array(y_min, y_max,h))
    knn = KNeighborsClassifier()
    knn.fit(x,y)
    #Z = knn.predict(np.c_[xx.])



def trainKNN(iris):
    x = iris.data
    y = iris.target
    i = np.random.permutation(len(iris.data))

    x_train = x[i[:-10]]
    y_train = y[i[:-10]]
    x_test = x[i[10:]]
    y_test = y[i[10:]]

    knn = KNeighborsClassifier()
    knn.fit(x_train, y_train)

    t = knn.predict(x_test)

    result = t == y_test


    print(t)
    print(y_test)


def paint_3d(iris):
    x = iris.data[:,0]
    y = iris.data[:,1]
    x_reduced = PCA(n_components=3).fit_transform(iris.data)
    species1 = iris.target
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_title('Iris by PCA', size = 14)
    ax.scatter(x_reduced[:,0], x_reduced[:,1],x_reduced[:,2],c=species1)
    ax.set_xlabel('First')
    ax.set_ylabel('Second')
    ax.set_zlabel('Third')
    ax.w_xaxis.set_ticklabels(())
    ax.w_yaxis.set_ticklabels(())
    ax.w_zaxis.set_ticklabels(())
    plt.show()



def paintX_Y(species):
    x = iris.data[:,0]
    y = iris.data[:,1]
    species = iris.target
    x_min, x_max = x.min() - 0.5, x.max() + 0.5
    y_min, y_max = y.min() - .5, y.max() + .5

    plt.figure()
    plt.title('Iris DataSet')
    plt.scatter(x, y, c=species)
    plt.xlabel('Length')
    plt.ylabel('Width')
    plt.xlim(x_min,x_max)
    plt.ylim(y_min,y_max)
    plt.xticks(())
    plt.yticks(())
plt.show()


paint3D()