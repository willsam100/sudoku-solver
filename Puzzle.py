import copy

class Puzzle():
    def __init__(self, rows, dic_forward):
        self.dic_forward_checking = {} 
        self.list_of_rows = []
        if rows == '':
            row = []
            for i in range(9):
                 row.append('')
            self.list_of_rows = row
            for row in range(9):
                 for column in range(9):
                    self.dic_forward_checking[(str(row) + str(column))] = range(1,10)
        else:
            self.list_of_rows = rows
            self.dic_forward_checking = dic_forward

    #retrives the 3x3 box, number is between 1 and 9 starting top left
    def getBox(self, x):
        row = []
        #a bit of math to work out how to retrive the correct cells
        if x <= 3:
            for splice in self.list_of_rows[:3]:
                tmp = splice[(x*3)-3:(x*3)]
                row.extend(tmp)
        elif x <= 6:
            x = x - 6
            for splice in self.list_of_rows[3:6]:
                tmp = splice[(x*3)-3:(x*3)]
                row.extend(tmp)
        elif x <= 9:
            x = x - 9
            for splice in self.list_of_rows[6:9]:
                tmp = splice[(x*3)-3:(x*3)]
                row.extend(tmp)
        return row

    #allows for spaces to be in the puzzle
    def is_valid(self):
        valid_puzzle = 'true'
        #check each row first
        for row in self.list_of_rows:
            seen_numbers = []
            for i in row:
                if i >= 1:
                    if i in seen_numbers or i > 9:
                        valid_puzzle = 'false'
                        return valid_puzzle
                    else:
                        seen_numbers.append(i)
        #then each column
        for col in range(9):
            seen_numbers = []
            for row in self.list_of_rows:
                if row[col] >= 1:
                    if row[col] in seen_numbers:
                        valid_puzzle = 'false'
                        return valid_puzzle
                    else:
                        seen_numbers.append(row[col])
        #and each box
        for i in range(1,10):
            seen_numbers = []
            box = self.getBox(i)
            for i in box:
                if i >= 1:
                    if i in seen_numbers:
                        valid_puzzle = 'false'
                        break;
                    else:
                        seen_numbers.append(i)
        return valid_puzzle

    #to check if the puzzle has been filled up and backtracking needs to begin
    def is_filled(self):
        result = 'true'
        for row in self.list_of_rows:
            for i in row:
                if i <= 1:
                    result = 'false'
                    return valid_puzzle
        return result
    
    #to find the complete soultion
    def isComplete(self):
        isCompleted = 'true'
        for row in self.list_of_rows:
            if -1 in row:
                 isCompleted = 'false'
                 break;
        if isCompleted == 'true':
            isCompleted = self.is_valid()
        return isCompleted

    #fills in one free cell with each possibilty from the domain.
    def generate(self):
        for row in range(9):
            for digit in range(9):
                if self.list_of_rows[row][digit] == -1:
                    newPuzzles = []
                    key = str(row) + str(digit)
                    for i in self.dic_forward_checking[key]:
                        tmp = Puzzle(self.list_of_rows, self.dic_forward_checking)
                        tmp.list_of_rows[row][digit] = i
                        if tmp.is_valid() == 'true':
                            newPuzzles.append(copy.deepcopy(tmp))
                    return newPuzzles
        return []
    
    def forwardChecking(self):
        for key in self.dic_forward_checking.keys():
            if len(self.dic_forward_checking[key]) == 1:
                (row, col) = int(key[0]), int(key[1])
                self.list_of_rows[row][col] = self.dic_forward_checking[key]

    def ac3(self):
        #must first cheeck the details are up to date (this is also invovled with generaateing the domains for new puzzle)
        keys_to_delete = []
        for key in self.dic_forward_checking:
            (row, column) = (int(key[0]), int(key[1]))
            if self.list_of_rows[row][column] >= 1:
                keys_to_delete.append(key)
        
        for item in keys_to_delete:
             del self.dic_forward_checking[item]
        #keep track if we placed in some numbers
        keys_to_delete = []

        for key in self.dic_forward_checking.keys():
            (row, column) = (int(key[0]), int(key[1]))
            valid_nums = self.dic_forward_checking[key]

            #to reomve the numbrs that are in row
            for iterator in range(9):
                t = self.list_of_rows[row][iterator] 
                if t >= 1:
                    if len(valid_nums) > 1:
                        item_to_remove = self.list_of_rows[row][iterator]
                        if item_to_remove in valid_nums:
                            valid_nums.remove(item_to_remove)


            if len(valid_nums) > 1:
                #to reomve the numbrs that are in column
                for iterator in range(9):
                    if self.list_of_rows[iterator][column] >= 1:
                        item_to_remove = self.list_of_rows[iterator][column]
                        if item_to_remove in valid_nums:
                            valid_nums.remove(item_to_remove)


            if len(valid_nums) > 1:
                #to reomve the numbers that are in the same box
                box_to_get = 1
                if row >= 3 and row <= 5:
                    box_to_get = 4
                elif row >= 6:
                    box_to_get = 7

                if column >= 3 and column <= 5:
                    box_to_get += 1
                elif column >= 6:
                    box_to_get += 2

                box = self.getBox(box_to_get)
                for digit in box:
                    if digit >= 1 and digit in valid_nums:
                        valid_nums.remove(digit)
            
            if len(valid_nums) == 1:
                self.list_of_rows[row][column] = valid_nums[0]
                keys_to_delete.append(key)

            if len(valid_nums) == 0:
                return 'false'

            self.dic_forward_checking[key] = valid_nums

        for item in keys_to_delete:
            del self.dic_forward_checking[item]

        #these two lines were moved for the variable to variable assignment for ac3 checking
        if keys_to_delete != []:
            self.ac3()
        return 'true'

    #a prnting method to make the puzles look nice :)
    def pprint(self):
        for row in self.list_of_rows:
            tmp = []
            for r in row:
                if r == -1:
                    tmp.append(' ')
                else:
                    tmp.append(r)
            one = "%01s %01s %01s" % (tmp[0], tmp[1], tmp[2])
            two = "%01s %01s %01s" % (tmp[3], tmp[4], tmp[5])
            three = "%01s %01s %01s" % (tmp[6], tmp[7], tmp[8])
            print one, two, three
