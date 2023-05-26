import random
import time

class SortingAlgorithm:
    @staticmethod
    def merge_sort_iterative(arr):
        if len(arr) <= 1:
            return arr

        def merge(left, right):
            merged = []
            left_index = right_index = 0

            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1

            merged.extend(left[left_index:])
            merged.extend(right[right_index:])
            return merged

        merged_arr = [[num] for num in arr]

        while len(merged_arr) > 1:
            next_level = []
            for i in range(0, len(merged_arr), 2):
                if i + 1 < len(merged_arr):
                    merged = merge(merged_arr[i], merged_arr[i + 1])
                else:
                    merged = merged_arr[i]
                next_level.append(merged)
            merged_arr = next_level

        return merged_arr[0]

    @staticmethod
    def merge_sort_recursive(arr):
        if len(arr) <= 1:
            return arr

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left

            if left[0] < right[0]:
                return [left[0]] + merge(left[1:], right)
            return [right[0]] + merge(left, right[1:])

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = SortingAlgorithm.merge_sort_recursive(left)
        right = SortingAlgorithm.merge_sort_recursive(right)

        return merge(left, right)

    @staticmethod
    def quick_sort_iterative(arr):
        if len(arr) <= 1:
            return arr

        stack = [(0, len(arr) - 1)]

        while stack:
            start, end = stack.pop()
            pivot_index = SortingAlgorithm.partition(arr, start, end)

            if pivot_index - 1 > start:
                stack.append((start, pivot_index - 1))
            if pivot_index + 1 < end:
                stack.append((pivot_index + 1, end))

        return arr

    @staticmethod
    def quick_sort_recursive(arr):
        if len(arr) <= 1:
            return arr

        pivot_index = SortingAlgorithm.partition(arr, 0, len(arr) - 1)
        left = SortingAlgorithm.quick_sort_recursive(arr[:pivot_index])
        right = SortingAlgorithm.quick_sort_recursive(arr[pivot_index + 1:])

        return left + [arr[pivot_index]] + right

    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


class TestSortingAlgorithms:
    @staticmethod
    def generate_random_array(size):
        return [random.randint(1, 1000) for _ in range(size)]

    @staticmethod
