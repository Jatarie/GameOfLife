import random
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)


def GameOfLife():
    gens = 15
    n=100
    x = [[round(random.random()) for i in range(n)]for ii in range(n)]
    xx = [[0 for p in range(n)]for pp in range(n)]
    ind = list(set([(i, ii) for i in range(-1, 2)for ii in range(-1, 2) if (i, ii) != (0, 0)]))

    plt.matshow(x, cmap='Blues')
    plt.show()
    plt.ion()

    for i in range(gens):
        plt.close()
        plt.matshow(x, cmap='Blues')
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()
        plt.draw()
        plt.pause(.4)

        #adding in a 3x3 area around each pixel
        for a in range(len(x)):
            for b in range(len(x)):
                y = 0
                for num in range(8):
                    if (a+ind[num][0] < 0) or (b+ind[num][1] < 0):
                        continue
                    else:
                        try:
                            y+=x[a+ind[num][0]][b+ind[num][1]]
                        except IndexError:
                            pass

                #Game Rule Implementation
                if y < 2 and x[a][b] == 1:
                    xx[a][b] = 0
                elif (y == 2 or y==3) and x[a][b] == 1:
                    xx[a][b] = 1
                elif y > 3 and x[a][b] == 1:
                    xx[a][b] = 0
                elif (y == 3) and (x[a][b] == 0):
                    xx[a][b] = 1
                else:
                    pass
        #Assigning temp array to main array
        for numi in range(n):
            for numii in range(n):
                x[numi][numii] = xx[numi][numii]



GameOfLife()