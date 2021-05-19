import rasterclass
from pandas import DataFrame
import matplotlib.pyplot as plt

if __name__=='__main__':
    npgrid=rasterclass.readfile()
    fig1 = DataFrame(npgrid)
    heartmap1 = plt.pcolor(fig1)
    plt.colorbar(heartmap1)
    plt.title("Heights")
    ax = plt.gca()
    ax.xaxis.set_ticks_position('top')
    ax.invert_yaxis()
    plt.show()

    npgrid=rasterclass.AddRound(npgrid)
    slope=rasterclass.CacSlopAsp(npgrid)
    rasterclass.np.savetxt("slope.csv",slope,fmt = "%-4s")

    fig2 = DataFrame(slope)
    heartmap2 = plt.pcolor(fig2)
    plt.colorbar(heartmap2)
    plt.title("Gradients")
    ax = plt.gca()
    ax.xaxis.set_ticks_position('top')
    ax.invert_yaxis()
    plt.show()


