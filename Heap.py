#!/usr/bin/env python3

#
# Heap.py - an heap-based implementation of a priority queue in Python3
# Copyright (C) Yavor Stoychev 2012 <stoychev.yavor@gmail.com>
# 
# Heap is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Heap is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

#Input Format Example Follows
#######################
#12
#1
#8
#D
#4
#68
#1
#32
#2
#D
#######################
#End of Input Format
#
#Notes
#######################
# This program requires Python 3.0 or later
# The first number from the input sets the heap size.
# "D" means dequeue.
# Any calls to push when the heap is full are ignored.
# Any calls to pop when the heap is empty are ignored.
# Lower value means higher priority.
#
#
from array import array
class heap:
  def __init__(self, length):
		self.max_length = length					#set maximum length
		self.data = array('i', (-1,) * 1)			#create internal array	

	def push(self, item):
		if len(self.data) - 1 == self.max_length:		#do not add elements if the heap is full
			return False

		self.data.append(item) 						#put item at the end
		self.HeapifyUp(len(self.data) - 1)

	def print(self):
		s = str(self.data)
		patterns = [",", "array('i' [-1", "])"]
		for pattern in patterns:
			s = s.replace(pattern, "")
		print(">" + s)
			
	def pop(self):
		n = len(self.data) - 1
		if  n == 0:				
			return False

		first = self.data[1]
		self.data[1] = self.data[n] 		#replace root
		self.data.pop(n)					#remove item
		self.HeapifyDown()
		return first


	def HeapifyUp(self, i):
		if i > 1:
			j = i//2
			if self.data[i] < self.data[j]:
				tmp = self.data[i]
				self.data[i] = self.data[j]
				self.data[j] = tmp
				self.HeapifyUp(j)

	def HeapifyDown(self, i=1):
		n  = len(self.data) - 1
		if 2*i > n:
			return
		elif 2*i < n:
			left = 2*i
			right = 2*i + 1
			j = left if self.data[left] < self.data[right] else right
		elif 2*i == n:
			j = 2*i
		if self.data[j] < self.data[i]:
			tmp = self.data[i]
			self.data[i] = self.data[j]
			self.data[j] = tmp
			self.HeapifyDown(j)

if __name__ == "__main__":
	h = heap(int(input()))
	while 1:
		try:
			item = input()
		except EOFError:
			break
		if item == "D":
			h.pop()
		else:
			h.push(int(item))
		h.print()
