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
    return CELLS.get(cell)


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
    numberlines =''
    account_validator=''
    
    with open(filename, 'r') as f:
        for line in f:
            linecount += 1
           
            if (linecount % 4) == 0:
                account_numbers=derive_account_number(numberlines)
                print("x",account_numbers)
                account_validator=check_sum_cal(account_numbers)
                print("valid?",account_validator)
                              
            else:
                numberlines += line.rstrip('\n')
    f.close()      
    return account_validator
