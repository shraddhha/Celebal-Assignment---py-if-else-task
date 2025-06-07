if __name__ == '__main__':
    n = int(input())  # Number of elements in tuple
    elements = tuple(map(int, input().split()))  # Create tuple from input
    print(hash(elements))
