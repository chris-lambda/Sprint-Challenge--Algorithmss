Add your answers to the Algorithms exercises here.
Exercise I:
a) 
A while loop is ran n becomes less than a n^3 
In the loop, a is updated to equal a + n^2
Time complexity: O(2)
Reasoning: a will always be upddated to a greater value after two run of the loop because after first iteration a is equal to n^2 and after the second iteration a is equal to n^4 which is greater than n^3

b)
4 nesting for loops 
first loop is running O(n)
second loop is running O(n-1)
third loop is running O(n-2)
fourth loop is running O(n + 7)
Time complexity: O(n^4)
Reasoning: though the loops are being slighly adjusted as n gets signinficantly larger those slight adjustments start meaning less and less and the closest notation would still be n^4

c)
bunnieEars is passed in a number and recursively calling itself decrementing bunnies by 1 till it reaches 0, adding 2 for every bunny.
Time Complexity: O(n)

Exercise II:
I would start off by halfing the _n_ stories 
Checking if it breaks at that middle value

If it breaks at the middle value check the lower half number
If it doesnt check the higher half
Storing the middle in a variable _m_
And the edge number(the previous middle number) as _e_

so if we have 12 as _n_ stories and we check 6
If it breaks at 6 check the next half which would be 3
If it  doesn't break at 6 check the upper half which would be 9

Repeate until _m_ value is equal to or less than _e_
_e_ is your _f_ value

Time complexity would be O(log n) 
becuase worst case senario you would check half the floors 
which would be log n