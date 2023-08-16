def create_matrix(rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    num = 1

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = num
            num += 1

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def rotate_matrix(matrix, rotations):
    for _ in range(rotations):
        matrix = list(zip(*matrix[::-1]))
    return matrix


while True:
        user_input = input("input 1,2,3,4,5(End): ")
        if user_input == "5":
            break
        rotations = int(user_input)
        if rotations not in [1, 2, 3, 4]:
            print("입력번호 오류 1,2,3,4,5(End)로 입력하세 요")
            continue

        # 5*5  matrix생성한다. 
        matrix = create_matrix(5, 5)

        # matrix를 회전한다 
        rotated_matrix = rotate_matrix(matrix, rotations)

        #  rotated된  matrix를 출력한다. 
        print("Rotated matrix:")
        print_matrix(rotated_matrix)
        print()
    