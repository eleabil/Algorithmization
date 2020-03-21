def paint(K, T, L):
    start = max(L)
    end = sum(L)
    while start < end:
        mid = start + (end - start)//2
        required_painters = getPainters(L, mid)
        # check if we have enough painters to paint the left half
        # find optimum in the left half. mid is included
        # because we may not get anything better
        if required_painters <= K:
            end = mid
        # find optimum in right half here
        else:
            start = mid + 1

    # print("Required: " + str(required_painters))
    return end * T

def getPainters(L, max_for_one_painter):
    currently_painted = 0
    painters = 1
    for i in range(len(L)):
        currently_painted += L[i]
        if currently_painted > max_for_one_painter:
            currently_painted = L[i]
            painters += 1
    return painters

if __name__ == '__main__':

  K = 10
  T = 5
  L = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]

  print("Painters: " + str(K))
  print("Time: " + str(T))
  print("Shields: " + str(L))
  print("Result: " + str(paint(K, T, L)))