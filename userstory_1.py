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


def get_account_numbers_from_file(filename):
    
    account_numbers = []
    linecount = 0
    numberlines =''
    
    with open(filename, 'r') as f:
        for line in f:
            linecount += 1
           
            if (linecount % 4) == 0:
                account_numbers=(derive_account_number(numberlines))
                print("x",account_numbers)
                acc_num_str=(''.join(str(e) for e in account_numbers))
                with open("write.txt", 'a') as q:
                    q.write(acc_num_str+'\n')
                q.close()
                numberlines = ''
                linecount=0
                
            else:
                numberlines += line.rstrip('\n')
    f.close()        
    return "noerr"
