We are going to learn two concepts:
1. Memoization
2. Tabulation

So let's start with the basics.
### Fibonacci Series:
Write an function `fib(n)` that takes in a number as an argument. The function should return the nth number of the Fibonacci sequence.

Let's look at the series:
```dart
n:     1,2,3,4,5,6,7,8
fib(n): 1,12,3,5,8,13,21 
```

#### Fib using Basic Recursion
Alright so let's look at the basic Fibonacci series. We are going to implement it in a basic recursive function:
```python
def fibonacci_recur(n):
	if n <= 2:
		return 1
	return fibonacci_recur(n-1) + fibonacci_recur(n-2)
```

The problem is that let's say if we want to call `fibonacci_recur(50)` you'll see that the program executes for a while. In fact we can even time the program and see how long it is taking to execute.

#### Let's draw our the Fibonacci Tree:

So when we see the tree for 7. This is what we get:
<img src = "https://i.postimg.cc/0Q4tvxfD/Screenshot-2024-07-06-at-3-45-09-PM.png"/>

So for all of the base cases we know that they are going to return 1.
<img src = "https://i.postimg.cc/qgVjtLW7/Screenshot-2024-07-06-at-3-48-32-PM.png"/>

 And remember:
 The time complexity of Fibonacci recursion is O( 2^n )

Let's look another basic algorithm. That really doesn't do anything but we want to calculate the number of calls and find out it's time complexity.
```python
def dib(n):
	if n <= 1:
		return
	dib(n-1)
	dib(n-1)
```

Now if we call `dib(5)` this is going to be the tree:
<img src = "https://i.postimg.cc/Dz8jM8Qn/Screenshot-2024-07-06-at-4-19-16-PM.png"/>

So the total number of levels = 4. Starting with 0 Level at the top. So now we know that the program's time complexity is again O( 2^n ).
But the space complexity of the above program is O(n)

Now if we look at `fib(50)` we have to make 2^50 calls which is a quadrillion. Clearly we need a better way. 

Now if we look back again at the tree for `fib(7)` we get the following:
<img src = "https://i.postimg.cc/KY6NpQvD/Screenshot-2024-07-06-at-4-33-20-PM.png"/>

We see that a lot of calculations are being repeated. So we don't need to do them twice, we'll have to device a way to store the calculation for instance `fib(5)` and store the value and get it from there for future calculations. This is called Dynamic Programming.

#### Fibonacci using Memoization
Since we want to store the values. The trick is to use Memoization. 

In order to implement Memoization we need a fast data structure preferably one with O(1) access time. So let's use Dictionary in python.

```python
# Memoization
# Using Dictionary, Keys will be arg to the fn, value will be the retun value
def fib(n, memo = {}):
	# First we check if the value is in the dict
	if n in memo:
		return memo[n]
	# This is the base case
	if n <= 2:
	return 1
	# Since we'll have to calculate at least once. We are going to store the value in our dict
	memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
	# Finally we return our value through dict
	return memo[n]
```

