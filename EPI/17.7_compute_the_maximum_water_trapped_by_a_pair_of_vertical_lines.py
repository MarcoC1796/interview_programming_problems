# Problem: An array of integers naturally defines a set of lines parallel to the Y-axis, starting from x=0.
#          The goal of this problem is to find the pair of lines that together "trap" the most water.
#          Write a prgram which takes as input an integer array and returns the pair of entries that trap the maximum
#          amount of water.

# EPI Judge: max_trapped_water.py
def get_max_trapped_water(heights):
    start = 0
    end = len(heights) - 1
    max_water = 0

    while start < end:
        h_start, h_end = heights[start], heights[end]
        curr_water = (end - start) * min(h_start, h_end)
        max_water = max(curr_water, max_water)

        if h_start > h_end:
            end -= 1
        else:
            start += 1

    return max_water

if __name__ == "__main__":
    heights = [52, 55, 40, 116, 66, 85, 105, 87, 15, 105, 46, 64, 17, 48, 122, 122, 33, 105, 106, 51, 130, 74, 84, 59, 84, 108, 52, 38, 88, 50, 132, 66, 32, 92, 52, 128, 87, 118, 37, 3, 9, 110, 41, 69, 47, 131, 106, 98, 87, 123, 42, 83, 86, 110, 120, 103, 115, 58, 37, 76, 74, 27, 46, 84, 106, 120, 106, 68, 37, 47, 70, 9, 70, 34, 134, 119, 82, 40, 81, 124, 51, 75, 86, 132, 116, 19, 92, 109, 132, 93, 6, 134, 21, 9, 82, 0, 94, 104, 102, 115, 81, 85, 95, 40, 124, 130, 39, 122, 45, 69, 130, 30, 15, 90, 52, 26, 121, 41, 132, 59, 22, 117, 99, 85, 79, 127, 32, 18, 47, 58, 10, 132, 135, 45, 50, 89, 86, 7, 40, 52, 31]
    print(get_max_trapped_water(heights))