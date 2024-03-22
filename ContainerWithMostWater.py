def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            currentArea = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, currentArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

def main():
    print(maxArea([5,7,6,5,8,9,3,4,8]))

if __name__ == "__main__":
    main()