
# test2 = [[3, 0, 0, 0, 0, 0, 0, 0, 0],
#           [5, 2, 0, 0, 0, 0, 0, 0, 0],
#           [0, 8, 7, 0, 0, 0, 0, 3, 1],
#           [0, 0, 3, 0, 1, 0, 0, 8, 0],
#           [9, 0, 0, 8, 6, 3, 0, 0, 5],
#           [0, 5, 0, 0, 9, 0, 6, 0, 0],
#           [1, 3, 0, 0, 0, 0, 2, 5, 0],
#           [0, 0, 0, 0, 0, 0, 0, 7, 4],
#           [0, 0, 5, 2, 0, 6, 3, 0, 0]]
#
# test3 = [[1, 2, 3, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def solve_matrix(array):
    """
    Takes matrix as argument, returns solved matrix if solved, False if not.
    :param array: array of arrays
    :return: solved array of arrays if solved, False if not.
    """
    def solver(matrix):
        """
        This subfunction solves the matrix. Return True if solved, False if not. During the process changes the
        mutable array.
        :param matrix: array of arrays
        :return: True if solved, else False.
        """
        cell = find_empty_cell(matrix)
        # if blank cell exists:
        if cell:
            line, column = cell[0], cell[1]
        else:
            # if there is no blank cells - matrix solved
            return True

        for i in range(1, 10):
            if check_if_valid(matrix, line, column, i):
                # print(matrix)
                matrix[line][column] = i
                if solver(matrix):
                    return True

                matrix[line][column] = 0

        return False

    def check_final_state(matrix):
        """
        Final check if matrix is solved right, just in case, left it bc this function has been already written,
        may be deleted.
        :param matrix: array of arrays
        :return: True or False
        """
        for line in matrix:
            sum = 0
            for num in line:
                sum += num
            if sum != 45:
                # print("Сумма строк не равна, координаты:", line)
                return False

        for i in range(0, len(matrix)):
            sum = 0
            for j in range(0, len(matrix)):
                sum += matrix[i][j]
            if sum != 45:
                # print("Сумма столбцов не равна, координаты:", i, j)
                return False

        return True

    def find_empty_cell(matrix):
        """
        This subfunctions finds empty cells in matrix.
        :param matrix: array of arrays
        :return: i,j coordinates if empty cell exists, False if not.
        """
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    return i, j
        return False

    # copying incoming argument in mutable obj
    matrix_to_solve = array

    if solver(matrix_to_solve):
        # check one more final time if everything is ok
        if check_final_state(matrix_to_solve):
            return matrix_to_solve
        else:
            return False
    else:
        return False


# print(solve_matrix(test2))

def check_if_valid(matrix, line, column, num):
    """
    This function checks if there is no issue with current matrix and current number in matrix.
    :param matrix: array of arrays
    :param line: int
    :param column: int
    :param num: int
    :return: True if num is fitting, else False.
    """
    # print(matrix, line, column, num)
    # horizontal check
    if num in matrix[line]:
        return False

    # vertical check
    for i in range(0, len(matrix)):
        if matrix[i][column] == num:
            return False

    # box check
    pos = (line, column)
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if matrix[i][j] == num and (i, j) != pos:
                return False

    return True


def validate_form(matrix):
    """
    This function checks if all elements are integers and if matrix is 9x9 size.
    :param matrix: takes matrix as argument.
    :return: True if all elements are int and size is 9x9, else False.
    """
    # check if all elem are int and 0<int<10
    for col in matrix:
        for elem in col:
            try:
                int(elem)
            except Exception as e:
                # print('int  error')
                return False
            if int(elem) > 9 or int(elem) < 0:
                # print('<0 and >9 error')
                return False

    # check if matrix is 9x9 size
    for col in matrix:
        if len(col) != 9:
            # print('size error')
            return False

    return True


def check_sudoku_rules(matrix):
    """
    This function takes incoming transported matrix and checks every integer in it except 0 if there is sudoku
    rules violations.
    :param matrix: array of arrays
    :return: True or false
    """
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):
            # skip when there is 0
            if matrix[line][column] != 0:
                num = matrix[line][column]
                # make the current num in matrix 0 so we can use check_if_valid() without rewritings
                matrix[line][column] = 0
                if not check_if_valid(matrix, line, column, num):
                    # print('sudoku rules error')
                    return False
                # turn the num back
                matrix[line][column] = num
    return True


def turn_matrix(matrix):
    """
    This function transporting a matrix, plus transforms str to int.
    :param matrix: takes matrix as argument.
    :return: transported matrix in list format, where each element is int.
    """
    transported_array = [list(i) for i in zip(*matrix)]
    transported_array = [[int(j) for j in i] for i in transported_array]
    return transported_array


def return_session(request):
    """
    Small function that returns session_key, if session does not exists - creates it.
    :param request:
    :return: session_key
    """
    if request.session.exists(request.session.session_key):
        return request.session.session_key
    else:
        request.session.create()
        return request.session.session_key


