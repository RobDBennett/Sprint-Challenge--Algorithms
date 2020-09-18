#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
I believe that while loops are largely O(n). O(1) doesn't matter on input, but 
for loops definitely increase as n increases. For a large value of n, this loop would need to run several times for a to catch up. 
Its not terribly ineffecient, but it will get slower the large n gets.

b)
I believe that nested for loops yield a O(n^2). If there were more nested loops, the ^2 would go up per loop.
Because the function needs to run a number of times times a number of times, the cost to solve the function increases in a polynomial fashion. As n becomes larger, both for loops will have to run an order of magnitude larger.

c)
Fibonacci functions are usually O(2^n). This one is a little tricky since its not returning:
return bunnyEars(bunnies-2) + bunnyEars(bunnies-1)
Adding a constant value rather than a second recursion feels like it would simplify the run time, but ultimately I believe that this is still an exponetially growing run time based on the value of n.

## Exercise II

This problem feels very much like a binary search or agnostic binary search. We don't want to test this on every floor because of the cost of eggs/time. So, given n number of floors, and f is the safe floor, we would start in the middle of n and drop an egg.
If the egg survives, then we can presume that all floors lower than k are also safe, so we disregard the 'left' side of the building (in this case the bottom half). If it shatters, then we know that all floors higher than this are also not safe, so we disregard the right half (top). We then go to the middle of the remaining floors and repeat the process. 
Each time we drop an egg, we are eliminating half of the remaining floors, as the egg either shatters or bounces and eventually find the safest maximum floor to drop an egg from.

The code would look something like this:
def egg_drop(array, low, high)
low = first floor
high = top floor
middle = (low + high) // 2
if array[middle] == broken egg:
return egg_drop(array, low, mid - 1)
else:
return egg_drop(array, mid + 1, high)


The runtime complexity of this one should be O(log n). O(n) would be us checking an egg on every floor, and O(1) would be us checking an egg once. This feels like a middle ground, where you are certainly not checking each floor, but rather eliminating half of each remaining total of floors each egg you test. Since the total number of floors (n) will increase the run time the higher it goes, its not constant, but also doesn't increase in a linear fashion.

