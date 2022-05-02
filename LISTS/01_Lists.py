
# T1Find idx of the largest element of list A
def findIndexOfLargestElementInList (A) :
    maxId = 0
    for i in range(1, len(A)):
        if A[i] > A[maxId]:
            maxId = i
    return maxId

# T2 Find 2nd largest element of the list A
def findSeconLargestListElement(A):
    # Less than 2 el in list.Return.
    if len(A) < 2: return None
    # Which one is bigger A[0] or A[1] ?
    if A[0] > A[1]:
        maxEl = A[0]
        secMax = A[1]
    else:
        maxEl = A[1]
        secMax = A[0]
    # Iterrate to find new maxEl and secMax el
    for i in range(2, len(A)):
        if A[i] > maxEl:
            secMax = maxEl
            maxEl = A[i]
        elif A[i] > secMax:
            secMax = A[i]
    return secMax

def findSeconLargestListElementV2(A):
    # Less than 2 el in list.Return.
    if len(A) < 2: return None
    # Which one is bigger A[0] or A[1] ?
    maxEl = max(A[0], A[1])
    secMax = min(A[0], A[1])
    # Iterrate to find new maxEl and secMax el
    for i in range(2, len(A)):
        if A[i] > maxEl:
            secMax = maxEl
            maxEl = A[i]
        elif A[i] > secMax:
            secMax = A[i]
    return secMax


# T3 Find largest even elemet of list A
def findLargestEvenElement(A):
    EvenElements = []
    for i in range (0, len(A)):
        if A[i] % 2 == 0:
            EvenElements.append(A[i])
    return max(EvenElements)

# T4
def IndexOfMaxEvenElemet(A):
    EvenElements = []
    EvenElementsIndices = []
    for i in range (0, len(A)):
        if A[i] % 2 == 0:
            EvenElements.append(A[i])
            EvenElementsIndices.append(i)
    idxOfLargestEventElement = findIndexOfLargestElementInList(EvenElements)
    return EvenElementsIndices[idxOfLargestEventElement]


# Testing TASK 1 
print("\nTask 1: Largest list element")
list1 = [2,20,19,3,8,7,1] # 1 (20)
list2 = [8,7,11,34,9,10,878,19] # 6 (879)
print(findIndexOfLargestElementInList(list1))
print(findIndexOfLargestElementInList(list2))


# Testing TASK 2
list1 = [18,19,3,8,21,7,32,60,61,1,58] # 0
list2 = [8,7,11,34,35,9,29,10] # 3
print("\nTask2 : Second max list element")
print(findSeconLargestListElement(list1))
print(findSeconLargestListElement(list2))
print("\n------ V2 ------")
print(findSeconLargestListElementV2(list1))
print(findSeconLargestListElementV2(list2))

# Test TASK 3
print("\nTask 3: Largest even element of list")
print(findLargestEvenElement(list1))
print(findLargestEvenElement(list2))

# Test TASK 3
print("\nTask 3: Largest even element of list")
print(IndexOfMaxEvenElemet(list1)) # 7
print(IndexOfMaxEvenElemet(list2)) # 3