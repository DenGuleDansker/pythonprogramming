print("--------------------------------------------------------------------")
print("Opgave 1")
print("double_row")
def double_row(row):
    row_result = []
    col = 0
    while col < len(row):
        row_result.append(row[col] * 2)
        col += 1
    return row_result

def matrix_double(m):
    row = 0
    doublelst = []
    while row < len(m):
        doublelst.append(double_row(m[row]))  
        row += 1
    return doublelst

print(matrix_double([[1, 4, 6], [2, 5, 6]]))

print("--------------------------------------------------------------------")
print("Opgave 2")
print("matrix_cum_min_of")
def matrix_cum_min_of(m):
    row = 0
    cumlist = []
    while row < len(m):
        cumlist.append(matrix_cum_col(m[row]))  
        row += 1
    return cumlist

def matrix_cum_col(row):
    sum = 0
    row_result = []
    col = 0
    while col < len(row):
        sum += row[col]
        row_result.append(sum)
        col += 1
    return row_result

matrice = [[1,2,45], [2,4], [2,5,6]]
print(len(matrice))
print(matrix_cum_min_of([[1,2,3], [1,2,3]]))

print("--------------------------------------------------------------------")
print("Opgave 3")
print("matrix_substract_vector")
def matrix_substract_vector(m, v):
    row = 0
    substractlst = []
    while row < len(m):
        substractlst.append(substract_col(m[row], v))
        row += 1
    return substractlst

def substract_col(row, v):
    sum = 0
    col = 0
    subtractlst = []
    while col < len(row):
        sum = row[col] - v[0]
        subtractlst.append(sum)
        col += 1
    return subtractlst

print(matrix_substract_vector([[1,2,3],[4,5,6]],[3]))

