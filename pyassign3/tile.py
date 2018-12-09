'''tile.py: 铺瓷砖

__author__ = "xhL"
__pkuid__  = "1800011791"
__email__  = "linxiaohan@pku.edu.cn"
'''


import turtle



def numberlist(m,n):
    '根据mn来建立一个编号列表'
    number_list=[]
    for i in range(m*n):
        number_list.append(i)
    return number_list



def coordinate(number_list,m,n):
    '把砖块的编号转化为砖块的行坐标和列坐标，都从0开始'
    coordinate=[]
    for i in number_list:
        coordinate.append([int(i)%n,int(i)//n])
    return coordinate



def number(coordinate,m,n):
    '把砖块的坐标转化为编号'
    number_list=[]
    for i in coordinate:
        number_list.append(i[1]*n+i[0])
    return number_list



def seriescoordinate(coordinate_one_of,a,b):
    '把某一个坐标扩充'
    list_1=[]
    list_2=[]
    for i in range(a):
        for j in range(b):
            list_1.append([coordinate_one_of[0]+i,coordinate_one_of[1]+j])
    for i in range(a):
        for j in range(b):
            list_2.append([coordinate_one_of[0]+j,coordinate_one_of[1]+i])
    return[list_1,list_2]



def isin(list_1,list_0):
    '判断一个列表中的元素是不是全部在另一个列表中'
    for i in list_1:
        if i not in list_0:
            return False
    return True



def maxmincoordinate(list_1):
    '找到一系列坐标里最大的一个和最小的一个'
    max_coordinate=list_1[0]
    min_coordinate=list_1[0]
    for j in range(len(list_1)):
        if list_1[j][0]+list_1[j][1]>max_coordinate[0]+max_coordinate[1]:
            max_coordinate=list_1[j]
        if list_1[j][0]+list_1[j][1]<min_coordinate[0]+min_coordinate[1]:
            min_coordinate=list_1[j]
    return [max_coordinate,min_coordinate]



def canfill(coordinate,m,n,a,b):
    '判断在一系列坐标下a*b的长方形能不能被填充，并且返回方案'
    boole_1=False
    boole_2=False
    parts=[]
    min_coordinate=maxmincoordinate(coordinate)[1]
    if a!=b:
        list_1=seriescoordinate(min_coordinate,a,b)[0]
        list_2=seriescoordinate(min_coordinate,a,b)[1]
        if isin(list_1,coordinate):
            parts.append(number(list_1,m,n))
            boole_1=True
        if isin(list_2,coordinate):
            parts.append(number(list_2,m,n))
            boole_1=True
        boole=boole_1 or boole_2
    else:
        list_1=seriescoordinate(min_coordinate,a,b)[0]
        list_2=seriescoordinate(min_coordinate,a,b)[1]
        if isin(list_1,coordinate):
            parts.append(number(list_1,m,n))
            boole_1=True
        boole=boole_1
    return[boole,parts]



def listremoval(list_total,list_numbers):
    '在一个列表中除去另一个列表中的所有值'
    list_final=[]
    for i in list_total:
        if i not in list_numbers:
            list_final.append(i)
    return list_final



def brick(solutions,m,n,a,b,x=0):
    '来铺墙壁啦!'
    if x==m*n/(a*b):
        return(solutions)
    else:
        solutions_1=[]
        for each_solution in solutions:
            number_list_total=numberlist(m,n)
            new_list=[]
            for i in each_solution:
                number_list_total=listremoval(number_list_total,i)
                new_list.append(i)
            boole=canfill(coordinate(number_list_total,m,n),m,n,a,b)[0]
            list_solution=canfill(coordinate(number_list_total,m,n),m,n,a,b)[1]
            for j in list_solution:
                new_list.append(j)
                solutions_1.append(new_list)
                new_list=[]
                for i in each_solution:
                    new_list.append(i)
        return(brick(solutions_1,m,n,a,b,x+1))



def nonegetaway(solutions):
    '去除掉solutions里的空列表'
    solutions_none=[]
    for i in solutions:
        each_solutions_none=[]
        for j in i:
            if j !=[]:
                each_solutions_none.append(j)
        solutions_none.append(each_solutions_none)
    return solutions_none



def tuplize(solutions):
    '把方案改写成tuple的形式'
    solution_tuple=[]
    for i in solutions:
        each_solution_tuple=[]
        for j in i:
            each_solution_tuple.append(tuple(j))
        solution_tuple.append(each_solution_tuple)
    return solution_tuple




def drawasquare(bob,left_corner,right_corner,color,size):
    '在知道左上角和右下角坐标的情况下画一个长方形'
    bob.color(color)
    bob.pensize(size)
    bob.penup()
    bob.goto(left_corner[0],left_corner[1])
    bob.pendown()
    bob.seth(0)
    bob.forward(right_corner[0]-left_corner[0])
    bob.seth(-90)
    bob.forward(-right_corner[1]+left_corner[1])
    bob.seth(-180)
    bob.forward(right_corner[0]-left_corner[0])
    bob.seth(90)
    bob.forward(-right_corner[1]+left_corner[1])



def turtles_see_you_again(solution,m,n,a,b,color,size):
    '小乌龟我们又见面了TAT'
    bg=turtle.Screen()
    bg.screensize(1500, 1500)
    bob=turtle.Turtle()
    list_0=[]
    for i in solution:
        list_1=coordinate(i,m,n)
        max_coordinate=maxmincoordinate(list_1)[0]
        min_coordinate=maxmincoordinate(list_1)[1]
        left_corner=[(min_coordinate[0])*50,-(min_coordinate[1])*50]
        right_corner=[(max_coordinate[0]+1)*50,-(max_coordinate[1]+1)*50]
        drawasquare(bob,left_corner,right_corner,color,size)



def main():
    """main module
    """
    m=int(input('请输入墙壁的长: '))
    n=int(input('请输入墙壁的宽: '))
    a=int(input('请输入瓷砖的长: '))
    b=int(input('请输入瓷砖的宽: '))
    if (m*n)%(a*b)!=0:
        print('不能铺满')
    else:
        list_answer=(brick([[[]]],m,n,a,b))
        if list_answer==[]:
            print('不能铺满')
        else:
            list_answer_1=nonegetaway(list_answer)
            list_answer_2=tuplize(list_answer_1)
            number=1
            for solution in list_answer_2:
                print(str(number)+': ',end='')
                print(solution)
                number+=1
            t=int(input('请选择一种进行可视化: '))
            turtles_see_you_again(list_answer_1[t-1],m,n,a,b,'blue',5)
            list_all=[]
            for i in range(m*n):
                list_all.append([i])
            turtles_see_you_again(list_all,m,n,a,b,'black',1)

    

if __name__ == '__main__':
    main()

