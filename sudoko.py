#!/usr/bin/python
import pprint
import Puzzle
import sys

#the serch method that carries out the backtracking
def search(sodoku):
    if sodoku.isComplete() == 'true':
        return sodoku
    else:
        #the following 6 lines were commented out to test without ac3 searching
       has_soulution = sodoku.ac3()
       if has_soulution == 'false':
           return ''
       if sodoku.isComplete() == 'true':
           return sodoku

       nextLevel = []
       nextLevel = sodoku.generate()                
       if nextLevel != []:
           for item in nextLevel:
               item.forwardChecking()
               result = search(item)
               if result:
                   return result
       else:
           return ''

def main():
    list_of_sodoku = []
    for i in range(10):
        list_of_sodoku.append(Puzzle.Puzzle('', ''))
    #set up the puzzles
    #Easy
    list_of_sodoku[0].list_of_rows[0] = [5, 2, -1, -1, 6, -1, 8, -1, 9]
    list_of_sodoku[0].list_of_rows[1] = [1, -1, -1, -1, -1, 5, -1, 2, -1]
    list_of_sodoku[0].list_of_rows[2] = [-1,-1,-1, -1, 9, -1, 5, -1, 3] 
    list_of_sodoku[0].list_of_rows[3] = [-1, -1, -1, 8, -1, -1, -1, 5, -1]  
    list_of_sodoku[0].list_of_rows[4] = [3, -1, 1, -1, -1, -1, 6, -1, 4]
    list_of_sodoku[0].list_of_rows[5] = [-1, 8, -1, -1, -1, 4, -1, -1, -1]  
    list_of_sodoku[0].list_of_rows[6] = [9, -1, 7, -1, 1, -1, -1, -1, -1]  
    list_of_sodoku[0].list_of_rows[7] = [-1, 1, -1, 7, -1, -1, -1, -1, 5]
    list_of_sodoku[0].list_of_rows[8] = [8, -1, 5, -1, 2, -1, -1, 4, 7]

    #medium - 74
    list_of_sodoku[1].list_of_rows[0] = [9, -1, -1, 3, -1, -1, -1, -1, -1]
    list_of_sodoku[1].list_of_rows[1] = [-1, -1, -1, -1, -1, -1, 7, -1, 6]
    list_of_sodoku[1].list_of_rows[2] = [-1, 1, -1, -1, -1, 7, 5, -1, -1]
    list_of_sodoku[1].list_of_rows[3] = [4, -1, -1, -1, -1, 3, -1, -1, 8]
    list_of_sodoku[1].list_of_rows[4] = [-1, 8, -1, -1, 7, -1, -1, 3, -1]
    list_of_sodoku[1].list_of_rows[5] = [6, -1, -1, 9, -1, -1, -1, -1, 2]
    list_of_sodoku[1].list_of_rows[6] = [-1, -1, 9, 5, -1, -1, -1, 2, -1]
    list_of_sodoku[1].list_of_rows[7] = [5, -1, 4, -1, -1, -1, -1, -1, -1]
    list_of_sodoku[1].list_of_rows[8] = [-1, -1, -1, -1, -1, 6, -1, -1, 1]

    #Hard
    list_of_sodoku[2].list_of_rows[0] = [-1, -1, 8, 5, -1, 2, -1, -1, -1]
    list_of_sodoku[2].list_of_rows[1] = [-1, 5, -1, -1, -1, -1, -1, 9, -1]
    list_of_sodoku[2].list_of_rows[2] = [-1, -1, -1, -1, 9, -1, -1, -1, 1]
    list_of_sodoku[2].list_of_rows[3] = [2, -1, -1, 4, -1, 6, -1, -1, 7]
    list_of_sodoku[2].list_of_rows[4] = [-1, -1, 5, -1, -1, -1, 3, -1, -1]
    list_of_sodoku[2].list_of_rows[5] = [6, -1, -1, 7, -1, 3, -1, -1, 9]
    list_of_sodoku[2].list_of_rows[6] = [8, -1, -1, -1, 2, -1, -1, -1, -1]
    list_of_sodoku[2].list_of_rows[7] = [-1, 4, -1, -1, -1, -1, -1, 7, -1]
    list_of_sodoku[2].list_of_rows[8] = [-1, -1, -1, 6, -1, 8, 4, -1, -1]

    #easy - 26
    list_of_sodoku[3].list_of_rows[0] = [-1, -1, -1, 2, 1, 5, -1, -1, -1]
    list_of_sodoku[3].list_of_rows[1] = [-1, 5, -1, -1, -1, -1, -1, 1, -1]
    list_of_sodoku[3].list_of_rows[2] = [-1, 8, 6, 7, -1, 3, 5, 4, -1]
    list_of_sodoku[3].list_of_rows[3] = [-1, 2, -1, -1, -1, -1, 6, 3, -1]
    list_of_sodoku[3].list_of_rows[4] = [-1, -1, -1, -1, 5, -1, -1, -1, -1]
    list_of_sodoku[3].list_of_rows[5] = [-1, 1, 3, -1, -1, -1, 7, 5, -1]
    list_of_sodoku[3].list_of_rows[6] = [-1, 3, 1, 6, -1, 2, 9, 7, -1]
    list_of_sodoku[3].list_of_rows[7] = [-1, 6, -1, -1, -1, -1, -1, 2, -1]
    list_of_sodoku[3].list_of_rows[8] = [-1, -1, -1, 9, 3, 4, -1, -1, -1]

    #medium - 35
    list_of_sodoku[4].list_of_rows[0] = [-1, 4, -1, 8, 3, -1, -1, -1, -1]
    list_of_sodoku[4].list_of_rows[1] = [-1, 5, -1, -1, -1, 9, 6, 1, 2]
    list_of_sodoku[4].list_of_rows[2] = [-1, 2, -1, -1, -1, -1, -1, -1, -1]
    list_of_sodoku[4].list_of_rows[3] = [-1, 6, -1, -1, -1, -1, -1, -1, 5]
    list_of_sodoku[4].list_of_rows[4] = [7, -1, -1, -1, 5, -1, -1, -1, 3]
    list_of_sodoku[4].list_of_rows[5] = [1, -1, -1, -1, -1, -1, -1, 8, -1]
    list_of_sodoku[4].list_of_rows[6] = [-1, -1, -1, -1, -1, -1, -1, 7, -1]
    list_of_sodoku[4].list_of_rows[7] = [5, 1, 3, 6, -1, -1, -1, 9, -1]
    list_of_sodoku[4].list_of_rows[8] = [-1, -1, -1, -1, 4, 8, -1, 3, -1]

    #hard - 126
    list_of_sodoku[5].list_of_rows[0] = [-1, -1, 5, 7, 2, -1, 1, 8, -1]
    list_of_sodoku[5].list_of_rows[1] = [3, -1, -1, -1, -1, -1, -1, -1, -1] 
    list_of_sodoku[5].list_of_rows[2] = [6, -1, -1, -1, -1, 1, -1, -1, 5]
    list_of_sodoku[5].list_of_rows[3] = [-1, -1, 2, -1, -1, -1, -1, -1, 8]
    list_of_sodoku[5].list_of_rows[4] = [9, -1, -1, -1, -1, -1, -1, -1, 2]
    list_of_sodoku[5].list_of_rows[5] = [1, -1, -1, -1, -1, -1, 4, -1, -1]
    list_of_sodoku[5].list_of_rows[6] = [7, -1, -1, 3, -1, -1, -1, -1, 1]
    list_of_sodoku[5].list_of_rows[7] = [-1, -1, -1, -1, -1, -1, -1, -1, 9] 
    list_of_sodoku[5].list_of_rows[8] = [-1, 4, 9, -1, 5, 7, 3, -1, -1]

    #medium - 68
    list_of_sodoku[6].list_of_rows[0] = [-1, -1, 1, -1, -1, 5, -1, 3, 9]
    list_of_sodoku[6].list_of_rows[1] = [-1, -1, -1, -1, -1, -1, -1, -1, 5] 
    list_of_sodoku[6].list_of_rows[2] = [5, -1, 8, -1, 1, -1, -1, -1, -1]
    list_of_sodoku[6].list_of_rows[3] = [-1, -1, -1, -1, 7, -1, -1, -1, 6]
    list_of_sodoku[6].list_of_rows[4] = [-1, -1, 5, 3, 2, 6, 9, -1, -1]
    list_of_sodoku[6].list_of_rows[5] = [1, -1, -1, -1, -1, 8, -1, -1, -1]
    list_of_sodoku[6].list_of_rows[6] = [-1, -1, -1, -1, 4, -1, 3, -1, 1]
    list_of_sodoku[6].list_of_rows[7] = [6, -1, -1, -1, -1, -1, -1, -1, -1] 
    list_of_sodoku[6].list_of_rows[8] = [4, 2, -1, 8, -1, -1, 5, -1, -1]

    #medium - 86
    list_of_sodoku[7].list_of_rows[0] = [4, -1, 6, -1, -1, -1, 8, -1, 7]
    list_of_sodoku[7].list_of_rows[1] = [-1, -1, -1, 3, -1, 5, -1, -1, -1] 
    list_of_sodoku[7].list_of_rows[2] = [1, -1, -1, -1, -1, -1, -1, -1, 9]
    list_of_sodoku[7].list_of_rows[3] = [-1, 3, -1, 7, -1, 6, -1, 4, -1]
    list_of_sodoku[7].list_of_rows[4] = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    list_of_sodoku[7].list_of_rows[5] = [-1, 9, -1, 1, -1, 8, -1, 6, -1]
    list_of_sodoku[7].list_of_rows[6] = [2, -1, -1, -1, -1, -1, -1, -1, 5]
    list_of_sodoku[7].list_of_rows[7] = [-1, -1, -1, 2, -1, 1, -1, -1, -1] 
    list_of_sodoku[7].list_of_rows[8] = [9, -1, 4, -1, -1, -1, 6, -1, 3]

    #hard - 120
    list_of_sodoku[8].list_of_rows[0] = [7, -1, 9, -1, -1, -1, 6, -1, 5]
    list_of_sodoku[8].list_of_rows[1] = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    list_of_sodoku[8].list_of_rows[2] = [1, -1, 6, 9, -1, 8, 7, -1, 2]
    list_of_sodoku[8].list_of_rows[3] = [-1, -1, -1, 7, -1, 1, -1, -1, -1]
    list_of_sodoku[8].list_of_rows[4] = [-1, 6, -1, -1, -1, -1, -1, 9, -1]
    list_of_sodoku[8].list_of_rows[5] = [-1, -1, -1, 3, -1, 5, -1, -1, -1]
    list_of_sodoku[8].list_of_rows[6] = [2, -1, 5, 1, -1, 4, 8, -1, 7]
    list_of_sodoku[8].list_of_rows[7] = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    list_of_sodoku[8].list_of_rows[8] = [8, -1, 3, -1, -1, -1, 2, -1, 1]

    #hard = 99
    list_of_sodoku[9].list_of_rows[0] = [3, 1, -1, -1, -1, -1, -1, 2, 8]
    list_of_sodoku[9].list_of_rows[1] = [-1, -1, 9, 5, -1, 6, 7, -1, -1]
    list_of_sodoku[9].list_of_rows[2] = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    list_of_sodoku[9].list_of_rows[3] = [-1, 5, -1, 6, -1, 7, -1, 8, -1]
    list_of_sodoku[9].list_of_rows[4] = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    list_of_sodoku[9].list_of_rows[5] = [-1, 4, -1, 1, -1, 8, -1, 3, -1]
    list_of_sodoku[9].list_of_rows[6] = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    list_of_sodoku[9].list_of_rows[7] = [-1, -1, 1, 7, -1, 2, 9, -1, -1]
    list_of_sodoku[9].list_of_rows[8] = [8, 6, -1, -1, -1, -1, -1, 7, 5]

    #itereate over the puzzles and report the solution
    for sodoku in list_of_sodoku:
        print ''
        sodoku.pprint()
        if sodoku.is_valid() == 'false':
           print 'puzzle is not valid, exiting...'
           sys.exit(1)
        else:
           print 'puzzle is correct'
        
        sodoku = search(sodoku)

        if sodoku.isComplete() == 'true':
           print 'Solution has been found: \n'

        sodoku.pprint()
        print ''

if __name__ == '__main__':
    main()
