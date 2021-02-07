
def predict_personal_names(matrix):

    fio = []
    
    try:      
        p = [matrix[0][0][0], matrix[1][0][0], matrix[2][0][0]]
    except:
        le = len(matrix)
        # если 1 слово или больше 3-х слов
        if le == 1:
            if len(matrix[0]) == 2:
                if matrix[0][0][0] == 'imya':
                    fio.append('')
                    fio.append(matrix[0][1])
                    fio.append('')
                    fio1 = fio[0]
                    fio2 = fio[1]
                    fio3 = fio[2]
                    return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
                if matrix[0][0][0] == 'otchestvo':
                    fio.append('')
                    fio.append('')
                    fio.append(matrix[0][1])
                    fio1 = fio[0]
                    fio2 = fio[1]
                    fio3 = fio[2]
                    return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
                if matrix[0][0][0] == 'familiya':
                    fio.append(matrix[0][1])
                    fio.append('')
                    fio.append('')
                    fio1 = fio[0]
                    fio2 = fio[1]
                    fio3 = fio[2]
                    return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
                if matrix[0][0][0] == '0':
                    fio.append(matrix[0][1])
                    fio.append('')
                    fio.append('')
                    fio1 = fio[0]
                    fio2 = fio[1]
                    fio3 = fio[2]
                    return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
                
            else:
                fio1 = matrix[0]
                fio2 = ''
                fio3 = ''
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
                
        if le == 2:
            if matrix[0][0][0] + matrix[1][0][0] == 'imyaotchestvo':
                fio.append('')
                fio.append(matrix[0][1])
                fio.append(matrix[1][1])
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == 'otchestvoimya':
                fio.append('')
                fio.append(matrix[1][1])
                fio.append(matrix[0][1])
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == 'imyafamiliya':
                fio.append(matrix[1][1])
                fio.append(matrix[0][1])
                fio.append('')
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == 'familiyaimya':
                fio.append(matrix[0][1])
                fio.append(matrix[1][1])
                fio.append('')
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == 'otchestvofamiliya':
                fio.append(matrix[1][1])
                fio.append('')
                fio.append(matrix[0][1])
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == 'familiyaotchestvo':
                fio.append(matrix[0][1])
                fio.append('')
                fio.append(matrix[1][1])
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == 'imya0':
                fio.append(matrix[1][1])
                fio.append(matrix[0][1])
                fio.append('')
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == '0imya':
                fio.append(matrix[0][1])
                fio.append(matrix[1][1])
                fio.append('')
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == 'familiya0':
                fio.append(matrix[0][1])
                fio.append(matrix[1][1])
                fio.append('')
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == '0familiya':
                fio.append(matrix[1][1])
                fio.append(matrix[0][1])
                fio.append('')
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == 'otchestvo0':
                fio.append('')
                fio.append(matrix[1][1])
                fio.append(matrix[0][1])
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == '0otchestvo':
                fio.append('')
                fio.append(matrix[0][1])
                fio.append(matrix[1][1])
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            if matrix[0][0][0] + matrix[1][0][0] == '00':
                fio.append(matrix[0][1])
                fio.append(matrix[1][1])
                fio.append('')
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

            if matrix[0][0][0] + matrix[1][0][0] in ['familiyafamiliya', 'imyaimya', 'otchestvootchestvo']:
                fio.append(matrix[0][1])
                fio.append(matrix[1][1])
                fio.append('')
                fio1 = fio[0]
                fio2 = fio[1]
                fio3 = fio[2]
                return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
            

    try:

        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'imyaimyaotchestvo':
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'imya'
                matrix[1][0][0] = 'familiya'
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'imya'
                matrix[0][0][0] = 'familiya'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'imyaotchestvoimya':
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'imya'
                matrix[2][0][0] = 'familiya'
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'imya'
                matrix[0][0][0] = 'familiya'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'otchestvoimyaimya':
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'imya'
                matrix[2][0][0] = 'familiya'
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'imya'
                matrix[1][0][0] = 'familiya'
        #
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'familiyafamiliyaotchestvo':
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'familiya'
                matrix[1][0][0] = 'imya'
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'familiya'
                matrix[0][0][0] = 'imya'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'familiyaotchestvofamiliya':
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'familiya'
                matrix[2][0][0] = 'imya'
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'familiya'
                matrix[0][0][0] = 'imya'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'otchestvofamiliyafamiliya':
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'familiya'
                matrix[2][0][0] = 'imya'
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'familiya'
                matrix[1][0][0] = 'imya'

        #
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'otchestvootchestvoimya':
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'otchestvo'
                matrix[1][0][0] = 'familiya'
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'otchestvo'
                matrix[0][0][0] = 'familiya'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'otchestvoimyaotchestvo':
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'otchestvo'
                matrix[2][0][0] = 'familiya'
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'otchestvo'
                matrix[0][0][0] = 'familiya'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'imyaotchestvootchestvo':
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'otchestvo'
                matrix[2][0][0] = 'familiya'
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'otchestvo'
                matrix[1][0][0] = 'familiya'
        #
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'otchestvootchestvofamiliya':
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'otchestvo'
                matrix[1][0][0] = 'imya'
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'otchestvo'
                matrix[0][0][0] = 'imya'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'otchestvofamiliyaotchestvo':
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'otchestvo'
                matrix[2][0][0] = 'imya'
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'otchestvo'
                matrix[0][0][0] = 'imya'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'familiyaotchestvootchestvo':
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'otchestvo'
                matrix[2][0][0] = 'imya'
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'otchestvo'
                matrix[1][0][0] = 'imya'
        #
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'familiyafamiliyaimya':
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'familiya'
                matrix[1][0][0] = 'otchestvo'
            if max(matrix[0][0][1], matrix[1][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'familiya'
                matrix[0][0][0] = 'otchestvo'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'familiyaimyafamiliya':
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[0][0][1]:
                matrix[0][0][0] = 'familiya'
                matrix[2][0][0] = 'otchestvo'
            if max(matrix[0][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'familiya'
                matrix[0][0][0] = 'otchestvo'
        if matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'imyafamiliyafamiliya':
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[1][0][1]:
                matrix[1][0][0] = 'familiya'
                matrix[2][0][0] = 'otchestvo'
            if max(matrix[1][0][1], matrix[2][0][1]) == matrix[2][0][1]:
                matrix[2][0][0] = 'familiya'
                matrix[1][0][0] = 'otchestvo'
                
        p = [matrix[0][0][0], matrix[1][0][0], matrix[2][0][0]]

        if all(x in 'familiyaimyaotchestvo' for x in p):
            matrix.sort()
            for k in matrix:
                fio.append(k[1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  '0imyaotchestvo':
            for k in matrix:
                fio.append(k[1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'familiya0otchestvo':
            for k in matrix:
                fio.append(k[1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'familiyaimya0':
            for k in matrix:
                fio.append(k[1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  '0familiyaimya':
            fio.append(matrix[1][1])
            fio.append(matrix[2][1])
            fio.append(matrix[0][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  '0imyafamiliya':
            fio.append(matrix[2][1])
            fio.append(matrix[1][1])
            fio.append(matrix[0][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  '0otchestvoimya':
            fio.append(matrix[0][1])
            fio.append(matrix[2][1])
            fio.append(matrix[1][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  '0otchestvofamiliya':
            fio.append(matrix[2][1])
            fio.append(matrix[0][1])
            fio.append(matrix[1][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'otchestvo0familiya':
            fio.append(matrix[2][1])
            fio.append(matrix[1][1])
            fio.append(matrix[0][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'imya0familiya':
            fio.append(matrix[2][1])
            fio.append(matrix[0][1])
            fio.append(matrix[1][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'imyaotchestvo0':
            fio.append(matrix[2][1])
            fio.append(matrix[0][1])
            fio.append(matrix[1][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'otchestvoimya0':
            fio.append(matrix[2][1])
            fio.append(matrix[1][1])
            fio.append(matrix[0][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'otchestvofamiliya0':
            fio.append(matrix[1][1])
            fio.append(matrix[2][1])
            fio.append(matrix[0][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  'familiya00':
            fio.append(matrix[0][1])
            fio.append(matrix[1][1])
            fio.append(matrix[2][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  '0imya0':
            fio.append(matrix[0][1])
            fio.append(matrix[1][1])
            fio.append(matrix[2][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  '00otchestvo':
            fio.append(matrix[0][1])
            fio.append(matrix[1][1])
            fio.append(matrix[2][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        elif matrix[0][0][0] + matrix[1][0][0] + matrix[2][0][0] ==  '000':
            fio.append(matrix[0][1])
            fio.append(matrix[1][1])
            fio.append(matrix[2][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}

        else:
            fio.append(matrix[0][1])
            fio.append(matrix[1][1])
            fio.append(matrix[2][1])
            fio1 = fio[0]
            fio2 = fio[1]
            fio3 = fio[2]
            return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}
    except:
        fio.append(matrix[0][1])
        fio.append(matrix[1][1])
        fio.append(matrix[2][1])
        fio1 = fio[0]
        fio2 = fio[1]
        fio3 = fio[2]
        return {'Фамилия': fio1, 'Имя': fio2, 'Отчество': fio3}