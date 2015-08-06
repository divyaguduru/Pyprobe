CELLS = {
        ' _ | ||_|': 0,
        '     |  |': 1,
        ' _  _||_ ': 2,
        ' _  _| _|': 3,
        '   |_|  |': 4,
        ' _ |_  _|': 5,
        ' _ |_ |_|': 6,
        ' _   |  |': 7,
        ' _ |_||_|': 8,
        ' _ |_| _|': 9
}

def derive_account_number(input):
    cells = get_cells(input)
    cell_values = []
    
    for cell in cells:
        y = get_cell_value(cell)
        if y == '-1':
            cell_values.append('?')
        else:
            cell_values.append(get_cell_value(cell))
    
    return cell_values

def get_cells(input):
    cells = []
    lines = get_cell_lines(input)

    for offset in range(0, 26, 3):
        cell = lines[0][offset:offset+3]
        cell += lines[1][offset:offset+3]
        cell += lines[2][offset:offset+3]
        cells.append(cell)

    return cells

def get_cell_lines(input):
    lines = ["","",""]
    offset = 0

    for char in input:
        lines[offset] += char
        
        if len(lines[offset]) == 27:
            offset += 1
    
    return lines


def get_cell_value(cell):
    if cell in CELLS:
        return CELLS.get(cell)
    else:
        return '-1'


def check_sum_cal(account_number):
    sum_value = 0
    for i in range(len(account_number)):
        sum_value += (9-i)* account_number[i]
    if (sum_value % 11) == 0:
        return "valid"
    else:
        return "invalid"
    
def get_account_numbers_from_file(filename):
    
    account_numbers = []
    linecount = 0
    numberlines = ''
    str1=''
    
    with open(filename, 'r') as f:
        for line in f:
            linecount += 1
   
            if (linecount % 4) == 0:
                account_numbers=derive_account_number(numberlines)
                print(account_numbers)
                
            
                acc_num_Str=(''.join(str(e) for e in account_numbers))

                if '?' in account_numbers :
                        acc_num_Str=acc_num_Str+'   '+'ILL'
                        with open('write3.txt', 'a') as q:
                            q.write(acc_num_Str+'\n')
                else:
                    str1=check_sum_cal(account_numbers)
                    if(str1=='invalid'):
                        acc_num=(''.join(str(e) for e in account_numbers))
                        acc_num=acc_num+'   '+'ERR'

                        with open('write3.txt', 'a') as q:
                            q.write(acc_num+'\n')
                    else:
                        str2='OK'
                        with open('write3.txt', 'a') as q:
                            q.write(accnum+'\n')
                q.close()     
                numberlines =''
                account_numbers=[]       
                    
            else:
                numberlines += line.rstrip('\n')
    f.close()
    return 'no error'


