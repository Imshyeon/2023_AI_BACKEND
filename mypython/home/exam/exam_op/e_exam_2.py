class Matrix:
    def __init__(self,matrix) -> None:
        super().__init__()
        self.__matrix = matrix
    def __add__(self, other):
        if isinstance(other, Matrix):
            tmp=[]
            for i in range(len(self.__matrix)):
                row=[]
                for j in range(len(self.__matrix[i])):
                    row.append(self.__matrix[i][j] + other.__matrix[i][j])
                tmp.append(row)
            return Matrix(tmp)
    def __repr__(self):
        return f'Matrix(rows={self.__matrix})'

if __name__ == '__main__':
    # [3]
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])
    result_addition = matrix1 + matrix2
    print("Result:")
    print(result_addition)  # 결과   ===> Matrix(rows=[[8, 10, 12], [14, 16, 18]])


    '''
class Matrix: # Matrix 클래스 재정의

    def __init__(self, matrix) -> None: # 클래스 생성자 재정의: matrix 인수를 인스턴스에 할당
        super().__init__()
        self.matrix = matrix # self.matrix에 matrix 할당

    def __add__(self, other): # 클래스 안에서 + 연산자 재정의
        if isinstance(other, Matrix): # 자신과 연산되는 다른 인스턴스 형태 검사
            rows = [] # 빈 리스트
            for i in range(len(self.matrix)): # matrix 행 순환 (0, 1)
                tmp = [] # 빈 리스트
                for j in range(len(self.matrix[i])): # matrix 열 순환 (0, 1, 2)
                    tmp.append(self.matrix[i][j] + other.matrix[i][j]) # 빈 리스트에 자신과, 연산되는 다른 인스턴스의 값을 저장
                rows.append(tmp) # rows에 j가 1회 순환하면 저장
            return Matrix(rows) # i 순환이 끝나면 Matrix(rows)로 self.maxtrix에 할당

    def __repr__(self): # 클래스 호출 시 표현될 문자열 재정의
        return f"Matrix(rows = {self.matrix})"

if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])
    result_addition = matrix1 + matrix2
    print("Result:")
    print(result_addition) # 결과 => Matrix(rows=[[8, 10, 12], [14, 16, 18]])
    
    '''