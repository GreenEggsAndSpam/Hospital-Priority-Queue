'''
Author: Vrishank Kulkarni
KUID: 3115417
Date: 04/14/24
Lab: lab 08
Last modified: 2/25/24
Purpose: this program will create a cue for a hospital and when given a file it will output the number of patients and
the patients that need to be treated
'''

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, patient):
        self.heap.append(patient)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        top = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0)
        return top

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._sift_up(parent_index)

    def _heapify(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify(largest)
