# Problem 57:
#     Square Root Convergents
#
# Description:
#     It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#         sqrt{2} = 1 + 1/(2 + 1/(2 + 1/(2+...)))
#
#     By expanding this for the first four iterations, we get:
#         1 + 1/2                               =  3 /  2   = 1.5
#         1 + 1 / (2 + 1/2)                     =  7 /  5   = 1.4
#         1 + 1 / (2 + 1 / (2 + 1/2))           = 17 / 12   = 1.41666...
#         1 + 1 / (2 + 1 / (2 + 1 / (2 + 1/2))) = 41 / 29   = 1.41379...
#
#     The next three expansions are 99/70, 239/169, and 577/408,
#       but the eighth expansion, 1393/985,
#       is the first example where the number of digits in the numerator
#       exceeds the number of digits in the denominator.
#
#     In the first one-thousand expansions,
#       how many fractions contain a numerator with more digits than the denominator?

from math import ceil, floor, log10, sqrt


def main(n: int) -> int:
    """
    Returns the number of expansions of the convergent sqrt(2) sequence,
      within the first `n` (inclusive) iterations,
      where the numerator has more digits than the denominator.

    Args:
        n (int): Natural number

    Returns:
        (int):
            Number of expansions of the convergent sqrt(2) sequence
            having more digits in the numerator than the denominator.
    """
    assert type(n) == int and n > 0

    # Idea 1:
    #     Suppose we have the simplified form of the fraction for expansion `i`, for some natural number `i`.
    #     Let expansion e_i = n_i / d_i, where n_i and d_i are the numerator and denominator, respectively.
    #
    #     Then the fraction for the next expansion, e_{i+1}, can be derived as follows:
    #         e_{i+1} = 1 + 1 / (2 + ...)
    #                 = 1 + 1 / (1 + 1 + ...)
    #                 = 1 + 1 / (1 + e_i)
    #                 = 1 + 1 / (1 + n_i/d_i)
    #                 = 1 + 1 / ((n_i + d_i) / d_i)
    #                 = 1 + d_i / (n_i + d_i)
    #                 = (n_i + d_i) / (n_i + d_i) + d_i / (n_i + d_i)
    #                 = (n_i + 2*d_i) / (n_i + d_i)
    #     Thus, we can use the numerator and denominator of expansion `i` to determine those of expansion `i+1`.
    #
    #     We thus have the following recurrence for the expansions:
    #       * e_0 = 1
    #             = 1 / 1
    #               => n_i = d_i = 1
    #
    #       * e_{i+1} = (n_i + 2*d_i) / (n_i + d_i)
    #                 = n_{i+1} / d_{i+1}
    #                   => n_{i+1} = n_i + 2*d_i
    #                   => d_{i+1} = n_i + d_i
    #

    # Idea 2:
    #     Using the recurrence expressions from Idea #1,
    #       we can alternately express it in matrix form.
    #
    #     Suppose some expansion's fraction, e_i, can be represented as a vector:
    #         e_i = [ n_i ]
    #               [ d_i ]
    #     Then the transformation, or 'step', matrix be the following:
    #         S = [ 1  2 ]
    #             [ 1  1 ]
    #
    #     Now the recurrent process can be expressed as follows:
    #         e_{i+1} = S × e_i
    #     that is,
    #         [ n_{i+1} ] = [ 1  2 ] × [ n_i ]
    #         [ d_{i+1} ] = [ 1  1 ] × [ d_i ]
    #
    #     Further, the recurrence can be collapsed into a single formula:
    #         e_i = S^i × e_0
    #

    # Idea 3:
    #     The matrix expression for e_i is useful, but can be further improved.
    #
    #     First we find the eigenvalues and eigenvectors of S:
    #             S × v_i = λ_i × v_i, where...
    #                 i = 1 or 2,
    #                 λ_i is an eigenvalue of S
    #                 v_i is the nonzero eigenvector of S corresponding to λ_i
    #
    #         Solving for the eigenvalues first:
    #           => S × v = λ × v
    #           => S × v - λ × v = 0
    #           => (S - λ*I) × v = 0
    #                  * There is a nonzero solution v iff det(S-λ*I) = 0
    #           => | 1-λ   2  | = 0
    #              |  1   1-λ |
    #           => (1-λ)^2 - (2)(1) = 0
    #           => λ^2 - 2*λ + 1 - 2 = 0
    #           => λ^2 - 2*λ - 1 = 0
    #                  * Solve for λ using quadratic formula
    #
    #           => λ = (-b ± sqrt(b^2 - 4ac)) / 2a
    #           => λ = (-(-2) ± sqrt((-2)^2 - 4(1)(-1))) / 2(1)
    #           => λ = (2 ± sqrt(8)) / 2
    #           => λ = 1 ± sqrt(2)
    #
    #         Thus we have the following eigenvalues:
    #             λ1 = 1 - sqrt(2)
    #             λ2 = 1 + sqrt(2)
    #         Solving for the corresponding eigenvectors gives:
    #             v1 = [ -sqrt(2) ],     v2 = [ sqrt(2) ]
    #                  [    1     ]           [    1    ]
    #
    #     Now that we have the eigenvectors, we can decompose vector e_0 into a linear combination of those.
    #         Let `a` and `b` be some real numbers, so that we have:
    #             e_0 = [ n_0 ] = [ 1 ] = a * v1 + b * v2
    #                   [ d_0 ]   [ 1 ]
    #
    #         Solving for `a` and `b`:
    #              e_0 = a * v1 + b * v2
    #           => [ 1 ] = a * [ -sqrt(2) ] + b * [ sqrt(2) ]
    #              [ 1 ]       [    1     ]       [    1    ]
    #                  * Obtain a system of linear equations with variables `a` and `b`
    #
    #           => 1 = a * (-sqrt(2)) + b * sqrt(2),    and
    #              1 = a * (1)        + b * (1)
    #
    #           => 1 = sqrt(2) * (b-a),                 and
    #              1 = a + b
    #
    #           => sqrt(2) / 2 = b - a,                 and
    #              1           = a + b
    #                  * Combine by adding equations, to remove `a`
    #
    #           => 2*b = 1 + sqrt(2)/2
    #           => 2*b = (2 + sqrt(2))/2
    #           => b = (2 + sqrt(2))/4
    #                  * Using `b` to solve for `a`
    #           => a + b = 1
    #           => a = 1 - b
    #           => a = 1 - (2 + sqrt(2))/4
    #           => a = 4/4 - (2 + sqrt(2))/4
    #           => a = (2 - sqrt(2))/4
    #
    #         Thus we have:
    #             e_0 = a * v1 + b * v2
    #                 = (2-sqrt(2))/4 * [ -sqrt(2) ] + (2+sqrt(2))/4 * [ sqrt(2) ]
    #                                   [    1     ]                   [    1    ]
    #
    #     Plugging this back into the matrix expression:
    #          e_i = S^i × e_0
    #       => e_i = S^i × (a*v1 + b*v2)
    #       => e_i = S^i × a * v1 + S^i × b * v2
    #       => e_i = a * S^i × v1 + b * S^i × v2
    #       => e_i = a * λ1^i * v1 + b * λ2^i * v2
    #
    #     Expanding this into the vector components, we get individual formulae for the numerator and denominator:
    #         n_i = a * λ1^i * (-sqrt(2)) + b * λ2^i * sqrt(2)
    #         d_i = a * λ1^i              + b * λ2^i
    #
    #     However, note that the first part of the sum in both of these (involving λ1) is negligible.
    #         a           = (2 - sqrt(2)) / 4 =  0.146...
    #         a * sqrt(2)                     =  0.207...
    #         λ1          = 1 - sqrt(2)       = -0.414...
    #
    #     Thus we can simplify the formulae by omitting the first summand, and simply rounding the opposite summand:
    #         n_i = b * λ2^i * sqrt(2)
    #             = sqrt(2) * b * λ2^i
    #             = sqrt(2) * (2 + sqrt(2)) / 4 * λ2^i
    #             = (2*sqrt(2) + 2) / 4 * λ2^i
    #             = (1 + sqrt(2)) / 2 * λ2^i
    #
    #         d_i = b * λ2^i
    #             = (2 + sqrt(2)) / 4 * λ2^i
    #

    # Idea 4:
    #     Using the new exact formulae for each of n_i and d_i,
    #       we can determine the expansion `i` at which
    #       either term reaches some digit-count `c`.
    #
    #     Fix `c` as some desired count of digits.
    #     Now consider n_i, where `i` is the index of the first expansion at which n_i has at least `c` digits.
    #     We can solve for `i` with the following:
    #          n_i ≥ 10^(c-1)
    #       => log10( n_i ) ≥ c - 1
    #       => log10( (1+sqrt(2))/2 * λ2^i ) ≥ c - 1
    #       => log10( (1+sqrt(2))/2 ) + log10( λ2^i ) ≥ c - 1
    #       => log10( λ2^i ) ≥ c - 1 - log10((1+sqrt(2))/2)
    #       => i * log10(λ2) ≥ c - 1 - log10((1+sqrt(2))/2)
    #       => i * ln(λ2)/ln(10) ≥ c - 1 - log10((1+sqrt(2))/2)
    #       => i ≥ (ln(10)/ln(λ2)) * (c - 1 - log10((1+sqrt(2))/2))
    #     Thus the first expansion is when n_i has `c` digits is the ceiling of the right-hand expression.
    #
    #
    #     We can do the same for the denominator, d_i, which gives us:
    #       => i ≥ (ln(10)/ln(λ2)) * (c - 1 - log10((2+sqrt(2))/4))
    #

    # Idea 5:
    #     We know that it is possible for n_i to have one more digit than d_i, in some expansions.
    #     However, is it possible that it would have more than one digit in excess of d_i?
    #     No, as the ratio between n_i and d_i is sqrt(2), based on their formulae.
    #
    #     We briefly show here that this is not possible.
    #     Suppose, for some i, that d_i has c digits, then:
    #         10^(c-1) ≤ d_i < 10^c
    #     Suppose further that, for the same i, n_i has at least 2 more digits than d_i, then:
    #         10^(c+1) ≤ n_i
    #
    #     Combine to get the relationship between d_i and n_i:
    #          d_i < 10^c
    #       => 10 * d_i < 10^(c+1)
    #       => 10 * d_i < 10^(c+1) ≤ n_i
    #       => 10 * d_i < n_i
    #
    #     In order for n_i to have at least 2 more digits than d_i, it must be greater than 10 times d_i.
    #     Since we know this not to be true, as the ratio is actually sqrt(2),
    #       then we are sure that n_i only ever has at most 1 digit more than d_i.
    #

    # Idea 6:
    #     Based on Idea #5, we know that n_i can only have one more digit than d_i, if any.
    #     So for any fixed digit count `c`, we can determine i_n and i_d,
    #       the indices at which n_i and d_i first have `c` digits, respectively.
    #     Then the difference (i_d - i_n) is the number of expansions at which i_d has fewer digits than i_n.
    #

    b = (2 + sqrt(2)) / 4  # Same constant noted above as `b`
    e = 1 + sqrt(2)        # Eigenvalue noted above as `λ2`

    count = 0
    c_max = floor(log10(b) + log10(2)/2 + n*log10(e))  # Highest number of digits reached by n_i
    print('Max numbers of digits is {}'.format(c_max))
    for c in range(1, c_max+1):
        # Indices at which n_i and d_i each first have `c` digits
        # Maxed at n'th expansion, in case of overshooting
        i_n = min(ceil((c - 1 - log10(b) - log10(2)/2) / log10(e)), n)
        i_d = min(ceil((c - 1 - log10(b)) / log10(e)), 1000)
        count += i_d - i_n
    return count


if __name__ == '__main__':
    expansion_count = int(input('Enter a natural number: '))
    excess_digit_expansions = main(expansion_count)
    print('Number of expansions of sqrt(2) sequence having more numerator digits than denominator:')
    print('  {}'.format(excess_digit_expansions))
