# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:05:40 2019

@author: Administrator
"""
"""
 盛最多水的容器 Container With Most Water
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。



图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

 

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49"""

"""solution :Doubule Pointer"""
def MaxArea(height):
    left=0
    right=len(height)-1
    max_area=0
    while left!=right:
        if height[left]<height[right]:
            area=height[left]*(right-left)
            max_area=max(max_area,area)
            left+=1
        else:
            area=height[right]*(right-left)
            max_area=max(max_area,area)
            right-=1
    return max_area
print(MaxArea([1,8,6,2,5,4,8,3,7]))

        