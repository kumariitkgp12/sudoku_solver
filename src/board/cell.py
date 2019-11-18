# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:44:24 2019

@author: sahitya kumar
"""


'''
The most Atomic element of a Sudoku board is a cell 
A cell has two co-ordinates (x,y) 
The basic hiearchy is like this 
---- A Sudoku board consists of Blocks 
---- A block is made of cells
'''
class cell:
    
    def __init__(self, x, y):
        self.__rowId = x
        self.__colId = y
        self.__solved = False
        self.__value = None
        
    
    def isSolved(self):
        return (self.__solved)
    
    def getValue(self):
        return self.__value
    

        