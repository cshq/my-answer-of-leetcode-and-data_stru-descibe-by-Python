# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:30:16 2019

@author: Administrator
"""
"""快乐数 Happy Number
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1"""
def isHappy(n):
    set_x=set()
    ha_sum=n
    while ha_sum!=1:
        num=0
        while ha_sum>=10:
            yu=ha_sum%10
            num=num+yu**2
            ha_sum=ha_sum//10
        num=num+ha_sum**2
        """求各个位数的平方和"""
        ha_sum=num
        if ha_sum in set_x:
            return False
        else:
            set_x.add(ha_sum)
    return True
    

print(isHappy(99231))