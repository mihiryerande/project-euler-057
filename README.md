# Project Euler

## Problem 57 - Square Root Convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

$$\sqrt{2} = 1 + \displaystyle\cfrac{1}{2 + \displaystyle\cfrac{1}{2 + \displaystyle\cfrac{1}{2 + \dots}}}$$

By expanding this for the first four iterations, we get:

$\qquad 1 + \displaystyle\cfrac{1}{2} = \displaystyle\cfrac{3}{2} = 1.5$

$\qquad 1 + \displaystyle\cfrac{1}{2 + \displaystyle\cfrac{1}{2}} = \displaystyle\cfrac{7}{5} = 1.4$

$\qquad 1 + \displaystyle\cfrac{1}{2 + \displaystyle\cfrac{1}{2 + \displaystyle\cfrac{1}{2}}} = \displaystyle\cfrac{17}{12} = 1.41666\dots$

$\qquad 1 + \displaystyle\cfrac{1}{2 + \displaystyle\cfrac{1}{2 + \displaystyle\cfrac{1}{2 + \displaystyle\cfrac{1}{2}}}} = \displaystyle\cfrac{41}{29} = 1.41379\dots$

The next three expansions are $\displaystyle\frac{99}{70}$,
$\displaystyle\frac{239}{169}$,
and $\displaystyle\frac{577}{408}$,
but the eighth expansion, $\displaystyle\frac{1393}{985}$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
