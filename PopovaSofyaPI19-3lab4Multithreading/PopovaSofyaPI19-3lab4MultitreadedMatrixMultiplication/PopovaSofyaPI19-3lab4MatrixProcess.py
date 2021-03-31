from multiprocessing import Process

def element(index):
    global matrix1, matrix2, matrix
    res = 0
    i, j = index
    N = len(matrix1[0])
    for k in range(N):
        res += matrix1[i][k] * matrix2[k][j]
    matrix[i][j] = res
    with open("matrix_process.txt", "a", encoding='utf-8') as f:
        if i == j == 0:
            f.write(str(res) + " ")
        elif j == 0:
            f.write("\n" + str(res) + " ")
        else:
            f.write(str(res) + " ")
    return matrix


with open('matrix1.txt', 'r') as f:
   matrix1 = [list(map(int, row.split())) for row in f.readlines()]

with open('matrix2.txt', 'r') as f:
   matrix2 = [list(map(int, row.split())) for row in f.readlines()]

matrix = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]

if __name__ == '__main__':

    try:

        procs = [] #список моих процессов

        number_of_proccesses = len(matrix1)*len(matrix2[0])
        print("Число процессов:", number_of_proccesses)  #число процессов - столько, сколько операций надо произвести

        indexes = []
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                indexes.append((i, j))

        for index in indexes:
            proc = Process(target=element, args=[index,]) #кол-во соответсвует числу потоков
            procs.append(proc)

        for proc in procs:
            proc.start()
            proc.join()
        
    except IndexError:
        print("Матрицы не могут быть перемножены, так как число столбцов первой матрицы не равно числу строк второй матрицы!")

    except ValueError:
        print("В матрице присутствуют не числовые элементы!")
