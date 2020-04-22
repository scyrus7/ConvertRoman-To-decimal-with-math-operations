Implement a calculator that takes its input as a string, with numbers written as Roman Numerals, and outputs
the result as a decimal value. Your solution should obey the standard order of operations, and should support
+ , - , * , / and parentheses.

\
Test Cases
\
> I
\
1
\
> V
\
5
\
> X
\
10
\
> VI
\
6
\
> IV
\
4
\
> I + II
\
3
\
> I - II
\
-1
\
> I * II
\
2
\
> I / II
\
0.5
\
> I + II + III
\
6
\
> I - II - II
\
-4
\
> I * II * III
\
6
\
I / II / III
\
> 0.166
\
I + II * III
\
> 7
\
> I * II + III
\
5
\
> ( I + II ) * III
\
9
\
> I * ( II + III )
\
5
\