#计算函数y(x)=-x ** 2 + 4 * x + 10的最大值
import numpy as np
import random
# 定义目标函数（待优化）
def y(x):
    return -x**2+4*x+10
# 初始化种群,选取一些可能的定义域内的x值组成列表x1，参数size为选取x值的数量，bounds为定义域
def initialize_population(size, bounds):
    x1=[]
    for _ in range(size):
        x1.append(random.uniform(bounds[0],bounds[1]))
    return x1
# 适应度评估,即计算自变量x1对应的y值，作为判断标准
def evaluate_population(x2):
    return [y(i) for i in x2]
# 选择（轮盘赌选择）
def select(population, y1):
    min_y1=min(y1)#取最小的适应度，即y值
    if min_y1<0:
        y1=[f-min_y1 for f in y1]  # 若为负，向上平移最小y值的绝对值使所有适应度非负,经过平移，后面只优化x
    total_y1=sum(y1)#计算所有y值的和
    probabilities=[i/total_y1 for i in y1]#将单个y值与所有y的和的比值作为其出现的概率，y越大越容易出现，更容易取到大的值
    selected=np.random.choice(population, size=len(population), p=probabilities)#在y1中选择出一组新的列表，较大的值比例提高
    return selected
# 交叉（单点交叉）
def crossover(parent1, parent2):
    child1=(parent1 + parent2) / 2
    child2=(parent1 + parent2) / 2
    return child1,child2
# 变异，在一定条件下重新选取部分x值
def mutate(x3, mutation_rate,bounds):
    if random.random()<mutation_rate:
        x3=random.uniform(bounds[0], bounds[1])
    return x3
# 遗传算法主函数
def function(bounds,x_size,generations,mutation_rate):
    # 初始化种群
    xx=initialize_population(x_size, bounds)
    for j in range(generations):
        # 评估种群适应度
        yy=evaluate_population(xx)
        # 选择
        selected_xx=select(xx,yy)
        # 生成新种群
        new_xx=[]
        final_xx=[]
        for i in range(0,len(selected_xx),2):
            parent1=selected_xx[i]
            parent2=selected_xx[i + 1]
            child1,child2=crossover(parent1,parent2)
            new_xx.append(mutate(child1,mutation_rate,bounds))
            new_xx.append(mutate(child2,mutation_rate,bounds))
        final_xx=new_xx
    # 返回最佳个体
    best_x=max(final_xx,key=y)
    return best_x
# 参数设置
bounds=[4, 10]
x_size=30
generations=50
mutation_rate=0.1
# 执行遗传算法
best_solution=function(bounds,x_size,generations,mutation_rate)
# 输出最佳解
best_solution_value=y(best_solution)
print(best_solution_value)







