import time

class Combiner:
    def __init__(self, volume, fuel_consumption, engine_power):
        self.volume = volume
        self.fuel_consumption = fuel_consumption
        self.engine_power = engine_power

def insertion_sort_by_volume(combiners):
    print("Insertion sort by volume")
    comparisons = 0
    changes = 0
    for index in range(1, len(combiners)):
      value = combiners[index].volume
      i = index - 1
      while i >= 0:
          if value < combiners[i].volume:
              comparisons = comparisons + 1
              combiners[i+1].volume = combiners[i].volume
              combiners[i].volume = value
              i = i - 1
              changes = changes + 1
          else:
              break
    changes = changes + 1

    for i in range(len(combiners)):
        print("Volume " + str(combiners[i].volume), "Fuel " + str(combiners[i].fuel_consumption),
              "Power " + str(combiners[i].engine_power))
    print ("Comparisons: " + str(comparisons))
    print ("Changes: " + str(changes))

def merge_sort_by_power(combiners):

    comparisons = 0
    changes = 0
    if len(combiners) > 1:
       middle = len(combiners)//2
       left = combiners[:middle]
       right = combiners[middle:]

       merge_sort_by_power(left)
       merge_sort_by_power(right)

       i = 0
       j = 0
       k = 0

       while i < len(left) and j < len(right):
           comparisons = comparisons + 1
           if left[i].engine_power < right[j].engine_power:
               combiners[k] = left[i]
               i = i+1
               changes = changes + 1
           else:
               combiners[k] = right[j]
               j = j+1
               changes = changes + 1
           k = k+1

       while i < len(left):
           combiners[k] = left[i]
           i = i+1
           k = k+1
           changes = changes + 1

       while j < len(right):
           combiners[k] = right[j]
           j = j+1
           k = k+1
           changes = changes + 1

c1 = Combiner(15, 8, 50)
c2 = Combiner(25, 5, 1000)
c3 = Combiner(4, 3, 200)
c4 = Combiner(1, 7, 32)
c5 = Combiner(9, 3, 47)
c6 = Combiner(100, 3, 623)
combiners = [c1, c2, c3, c4, c5, c6]

insertion_sort_by_volume(combiners)
start = time.perf_counter()
print("Time: " + str(time.perf_counter() - start))

merge_sort_by_power(combiners)
print ("Merge sort in descended order")
print("Combiners sorted by engine power:")
for i in range(len(combiners)):
    print ("Volume " + str(combiners[i].volume),"Fuel " +  str(combiners[i].fuel_consumption), "Power " + str(combiners[i].engine_power))
start = time.perf_counter()
print("Time: " + str(time.perf_counter() - start))

