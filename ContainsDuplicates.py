def containsDupe(items):
    visited = set()

    for item in items:
        if item in visited:
            return True
        visited.add(item)
    
    return False

def main():
    num_array_with_dupe = [1,2,3,4,5,6,7,1]
    num_array = [1,2,3,4,5,6,7]
    item_array = ['cat', 'dog', 4, '7', 'dog']

    print(containsDupe(num_array_with_dupe))
    print(containsDupe(num_array))
    print(containsDupe(item_array))

if __name__ == "__main__":
    main()