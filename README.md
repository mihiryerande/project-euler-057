# Project Euler

## Problem 57 - Square Root Convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

<img src="https://render.githubusercontent.com/render/math?math=\sqrt{2} = 1 %2b \frac{1}{2 %2b \frac{1}{2 %2b \frac{1}{2 %2b \dots}}}">

By expanding this for the first four iterations, we get:

<img src="https://render.githubusercontent.com/render/math?math=1 %2b \frac{1}{2} = \frac{3}{2} = 1.5">

<img src="https://render.githubusercontent.com/render/math?math=1 %2b \frac{1}{2 %2b \frac{1}{2}} = \frac{7}{5} = 1.4">

<img src="https://render.githubusercontent.com/render/math?math=1 %2b \frac{1}{2 %2b \frac{1}{2 %2b \frac{1}{2}}} = \frac{17}{12} = 1.41666\dots">

<img src="https://render.githubusercontent.com/render/math?math=1 %2b \frac{1}{2 %2b \frac{1}{2 %2b \frac{1}{2 %2b \frac{1}{2}}}} = \frac{41}{29} = 1.41379\dots">

The next three expansions are <img src="https://render.githubusercontent.com/render/math?math=\frac{99}{70}">, <img src="https://render.githubusercontent.com/render/math?math=\frac{239}{169}">, and <img src="https://render.githubusercontent.com/render/math?math=\frac{577}{408}">, but the eighth expansion, <img src="https://render.githubusercontent.com/render/math?math=\frac{1393}{985}">, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
