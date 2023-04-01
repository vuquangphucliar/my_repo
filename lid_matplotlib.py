import pandas
import matplotlib.pyplot as plt 
import os
import numpy

def Graph():
    '''Pie_chart'''
    plt.subplot(2,2,1)
    x = numpy.array([19,17,33,31])
    label = "One Two Three Four".split()
    myexplode = [0.2,0,0,0]
    color = ['b','m','k','c']
    plt.pie(x,labels=label,explode=myexplode)
    # plt.pie(x,labels=label,startangle=180, shadow= True,colors=color)
    # plt.legend()
    plt.title('Pie_chart')


    '''Scatter'''
    plt.subplot(2,2,2)
    x = numpy.random.randint(200,size=30)
    y = numpy.random.randint(200,size=30)
    size = numpy.random.randint(100,size=30)

    plt.scatter(x,y,color='blue',alpha=0.5,s=size)
    
    plt.xlabel('X-axis',fontdict={'color':'blue','family':'serif','size':15})  #label for the X-sxis
    plt.ylabel('Y-axis',fontdict={'color':'green','family':'serif','size':15}) #label for the Y-sxis
    plt.title('This char is mine !',fontdict={'color':'darkred','family':'serif','size':17},loc='center')
    plt.grid(axis='both',linestyle='-',linewidth=0.7,color='pink') # đường Lưới

    plt.colorbar()
    # plt.show()
    plt.title('Scatter')

    '''Bar'''
    plt.subplot(2,2,3)
    y= numpy.random.randint(100,size=6)
    x = numpy.array("A B C D E F".split(' '))
    
    plt.bar(x,y,color='hotpink',width=0.6) # the figure lies vertical
    # plt.barh(x,y,color='hotpink') # the figure lies horizontal
    # plt.show()

    plt.title('Bar')
    plt.suptitle('My result ! ',fontdict={'color':'blue','size':17})
    plt.subplot(2,2,4)


    '''Graph from file data'''
    link = "C:/Users/my pc/Documents/File_Python/đatacsv.csv" # dùng biến để tí chèn link
    colum_name = ['Population','Profit']
    data = pandas.read_csv(link,names=colum_name)
    
    data.plot(kind='line',x='Population',y='Profit',linestyle='solid',color='hotpink',linewidth=3)
    # data.plot(kind='line',x='Population',y='Profit',ls='--',c='black',lw='3')
    # data.plot(kind='line',x='Population',y='Profit',ls='dotted',c='red',lw='2')
    # plt.show()
    plt.title('Graph')
    plt.show()
Graph()
