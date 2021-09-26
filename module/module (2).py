import profile 


key = ['a', 'b', 'c', 'q']
print('q - это выход, a- это 1-я задача, b- это 2-я задача, с- 3-я задача')
profile.name = str(input('Введите ваше имя '))
print('Hello', profile.name)

while True:

    code=str(input())
    
    
    if code == 'q':
        break
    elif code not in key:
        print('Try again. Choose one from', key)
        continue
    elif code == 'c':
        lst = list(input('list = ').split( ))
        empty = []        
        res = []

        lst = [int(num) for num in lst]

        while lst:
            for num in lst:
                if num == min(lst):
                    lst.remove(num)
                    empty.append(num)
            

        for num in empty:
            if num not in lst:
                res.append(num)
        

        print(res)
        continue
    elif code == 'b':
        def get_unique(data, keys):
            result = []
            unique = []

            for _dict in data:
                values = [value for key, value in _dict.items() if key in keys]
                if values not in unique:
                    unique.append(values)
                    result.append(_dict)
                return result



            data = [
                {'Имя': 'Маша', 'Фамилия': 'Иванова', 'Возраст' : 27},
                {'Имя': 'Маша', 'Фамилия': 'Иванова', 'Возраст' : 28},
                {'Имя': 'Маша', 'Фамилия': 'Петрова', 'Возраст' : 27},
                {'Имя': 'Маша', 'Фамилия': 'Cидорова', 'Возраст' : 27}
            ]
            keys = ['Имя', 'Возраст']
    elif code == 'a':
            def wall_collect():
                wall = [ 
                    [1, 1, 1, 1],
                    [1, 2, 1, 1],
                    [1, 3, 1],
                ]
                return wall


    def get_dictance_matrix(wall):
                distance_matrix = dict()
                for wall_row in wall:
                    distance = 0

                for length in wall_row[:-1]:
                    distance += length
                    
                    if distance in distance_matrix:
                        distance_matrix[distance] += 1
                    else:
                        distance_matrix[distance] = 1

                        return distance_matrix


    def get_max_joints_distance(distance_matrix):
                max_joints = max(distance_matrix.values())
                for distance, joints_count in distance_matrix.items():
                    if joints_count == max_joints:
                        return distance


    if __name__ == "__main__":
                wall = wall_collect()
                distance_matrix = get_dictance_matrix(wall)
                distance = get_max_joints_distance(distance_matrix)
                print('Количество стыков =', distance)
    continue

    