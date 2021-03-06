"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of SEQUENCES OF SUB-SEQUENCES.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Kathi Munoz.
"""  # done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the other functions to test them. """
    run_test_largest_number()
    run_test_largest_negative_number()
    run_test_first_is_elsewhere_too()


def run_test_largest_number():
    """ Tests the    largest_number    function. """
    # ------------------------------------------------------------------
    # done: 2. Implement this TEST function.
    #   It TESTS the  largest_number  function defined below.
    #   Include at least ** 1 ** ADDITIONAL test beyond those we wrote.
    # ------------------------------------------------------------------
    print()
    print('-------------------------------------')
    print('Testing the   LARGEST_NUMBER   function:')
    print('-------------------------------------')


    # Test 1:
    expected = 13
    answer = largest_number([(3, 1, 4),
                             (13, 10, 11, 7, 10),
                             [1, 2, 3, 4]])
    print('Expected and actual are:', expected, answer)

    # Test 2:
    expected = -1111111111111111
    answer = largest_number(([], [-1111111111111111], []))
    print('Expected and actual are:', expected, answer)

    # Test 3:
    expected = None
    answer = largest_number(([], [], []))
    print('Expected and actual are:', expected, answer)

    # TO DO 2 (continued): Add your ADDITIONAL test(s) here:
    seq_seq = [(1, 2, 3), (7, 8, 9), (10, 3, 4)]
    expected = 10
    actual = largest_number(seq_seq)
    print('Expected and actual are:', expected, actual)


def largest_number(seq_seq):
    """
    Returns the largest number in the subsequences of the given
    sequence of sequences.  Returns None if there are NO numbers
    in the subsequences.

    For example, if the given argument is:
        [(3, 1, 4),
         (13, 10, 11, 7, 10),
         [1, 2, 3, 4]]
    then this function returns 13.

    As another example, if the given argument is:
      ([], [-1111111111111111], [])
    then this function returns -1111111111111111.

    As yet another example, if the given argument is:
      ([], [], [])
    then this function returns None.

    Preconditions:
      :type seq_seq: (list, tuple)
    and the given argument is a sequence of sequences,
    where each subsequence contains only numbers.
    """
    # ------------------------------------------------------------------
    # done: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    # ------------------------------------------------------------------
    largest_num = None
    for m in range(len(seq_seq)):
        if len(seq_seq[m])>0:
            largest_num = seq_seq[m][0]
    if largest_num is None:
        return None

    for k in range(len(seq_seq)):
        sublist = seq_seq[k]
        for j in range(len(sublist)):
            if sublist[j] > largest_num:
                largest_num = sublist[j]
    return largest_num

def run_test_largest_negative_number():
    """ Tests the    largest_negative_number    function. """
    # ------------------------------------------------------------------
    # done: 4. Implement this TEST function.
    #   It TESTS the  largest_negative_number  function defined below.
    #
    #   Include enough tests to give you confidence that your solution
    #   to this challenging problem is indeed correct.
    # ------------------------------------------------------------------
    print()
    print('-------------------------------------------------')
    print('Testing the   LARGEST_NEGATIVE_NUMBER   function:')
    print('-------------------------------------------------')

    # test 1
    seq_seq = [(0, -5), (10, -11)]
    expected = -11
    actual = largest_negative_number(seq_seq)
    print('Test 1 expected and actual are:', expected, actual)

    # test 2
    seq_seq = [[], [-5]]
    expected = -5
    actual = largest_negative_number(seq_seq)
    print('Test 2 expected and actual are:', expected, actual)

    # test 3
    seq_seq = [(1, 2, 3)]
    expected = None
    actual = largest_negative_number(seq_seq)
    print('Test 3 expected and actual are:', expected, actual)


def largest_negative_number(seq_seq):
    """
    Returns the largest NEGATIVE number in the given sequence of
    sequences of numbers.  Returns None if there are no negative numbers
    in the sequence of sequences.

    For example, if the given argument is:
        [(30, -5, 8, -20),
         (100, -2.6, 88, -40, -5),
         (400, 500)
        ]
    then this function returns -2.6.

    As another example, if the given argument is:
      [(200, 2, 20), (500, 400)]
    then this function returns None.

    Preconditions:
      :type seq_seq: (list, tuple)
    and the given argument is a sequence of sequences,
    where each subsequence contains only numbers.
    """
    # ------------------------------------------------------------------
    # done: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # CHALLENGE: Try to solve this problem with no additional sequences
    #   being constructed (so the SPACE allowed is limited to the
    #   give sequence of sequences plus any non-list variables you want).
    # ------------------------------------------------------------------
    # large_neg_num = None
    # for j in range(len(seq_seq)):
    #     if len(seq_seq[j]) > 0:
    #         if seq_seq[j][j] < 0:
    #             large_neg_num = seq_seq[j][j]
    # if large_neg_num is None:
    #     return None
    # for k in range(len(seq_seq)):
    #     sublist = seq_seq[k]
    #     for m in range(len(sublist)):
    #         if sublist[m] < 0:
    large_neg_num = None
    for j in range(len(seq_seq)):
        sublist = seq_seq[j]
        for k in range(len(sublist)):
            if sublist[k] < 0:
                large_neg_num = sublist[k]
                break
        if large_neg_num is not None:
            break
    if large_neg_num is None:
        return None
    for n in range(len(seq_seq)):
        sublist1 = seq_seq[n]
        for o in range(len(sublist1)):
            if sublist1[o] < large_neg_num:
                large_neg_num = sublist1[o]
    return large_neg_num


def run_test_first_is_elsewhere_too():
    """ Tests the    first_is_elsewhere_too    function. """
    # ------------------------------------------------------------------
    # We have supplied tests for you. No additional tests are required,
    # although you are welcome to supply more tests if you choose.
    # ------------------------------------------------------------------
    print()
    print('-------------------------------------')
    print('Testing the   FIRST_IS_ELSEWHERE_TOO   function:')
    print('-------------------------------------')

    # FYI: The notation below constructs what is called a DICTIONARY.
    #      It is like a list, but the indices can be any immutable
    #      objects (here, True or False), not just 0, 1, 2, ... as in lists.
    message = {True: 'Your code PASSED this test.\n',
               False: 'Your code FAILED this test.\n'}
    no_failures = True

    # Test 1:
    expected = True
    answer = first_is_elsewhere_too([(3, 1, 4),
                                     (13, 10, 11, 7, 10),
                                     [11, 12, 3, 10]])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 2:
    expected = False
    answer = first_is_elsewhere_too([(3, 1, 4),
                                     (13, 10, 11, 7, 10),
                                     [11, 2, 13, 14]])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 3:
    expected = False
    answer = first_is_elsewhere_too([[], [1, 2], [1, 2]])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 4:
    expected = True
    answer = first_is_elsewhere_too([('a', 9),
                                     (13, 10, 11, 7, 'a'),
                                     [11, 12, 3, 10]])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])  # Test 1:
    no_failures = no_failures and (answer == expected)

    # Test 5:
    expected = False
    answer = first_is_elsewhere_too([('a', 9),
                                     (13, 10, 11, 7, 'aa'),
                                     [11, 12, 3, 10]])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 6:
    expected = False
    answer = first_is_elsewhere_too([('a', 'a', 'b', 'b', 'a', 'b')])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 7:
    expected = False
    answer = first_is_elsewhere_too([()])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 8:
    expected = True
    answer = first_is_elsewhere_too([('a'), (), (), (), ('a')])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 9:
    expected = True
    answer = first_is_elsewhere_too([('a'), (), (), (), ('a'), ()])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 10:
    expected = False
    answer = first_is_elsewhere_too([('a'), (), (), (), ('b'), ()])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 11:
    expected = True
    answer = first_is_elsewhere_too(['hello', 'goodbye'])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 12:
    expected = False
    answer = first_is_elsewhere_too(['hello', 'xxxxxxxxxxx'])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 13:
    expected = False
    answer = first_is_elsewhere_too(['1234567890',
                                     'one two three',
                                     'i am free',
                                     'four five six',
                                     'get my sticks',
                                     'seven eight nine',
                                     'i am fine'])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 14:
    expected = True
    answer = first_is_elsewhere_too([(1000 * 'a') + 'b' + (500 * 'a'),
                                     (800 * 'c') + 'd' + 1200 * 'c',
                                     'b'])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 15:
    expected = True
    answer = first_is_elsewhere_too([(1000 * 'a') + 'b' + (500 * 'a'),
                                     (800 * 'c') + 'd' + 1200 * 'c',
                                     (700 * 'eee') + 'b' + (90 * 'd'),
                                     (800 * 'c') + 'd' + 1200 * 'c'])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 16:
    expected = True
    answer = first_is_elsewhere_too([(1000 * 'b') + 'acd' + (500 * 'f'),
                                     (800 * '1') + '234a',
                                     'eeee'])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 17:
    expected = True
    answer = first_is_elsewhere_too([(1000 * 'b') + 'acd' + (500 * 'f'),
                                     'a' + (800 * '1') + '234',
                                     '123'])
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 18:
    test1 = [(1000 * 'b') + 'acd' + (500 * 'f'),
             (800 * '1') + '234',
             '123']
    for k in range(95):
        test1.append(k * chr(k))
    test2 = []
    for k in range(30):
        test2.append(k * chr(k))

    expected = True
    answer = first_is_elsewhere_too(test1 + ['a'] + test2)
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 19 (continues test 18):
    expected = False
    answer = first_is_elsewhere_too(test1 + test2)
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    # Test 20 (continues test 18):
    expected = True
    a_inside = (100 * 'b') + 'a' + (100 * 'b')
    answer = first_is_elsewhere_too(test1 + [a_inside] + test2)
    print('Expected and actual are:', expected, answer)
    print(message[answer == expected])
    no_failures = no_failures and (answer == expected)

    if no_failures:
        print('*** Your code PASSED all')
    else:
        print('!!! Your code FAILED some')
    print('    of the tests for first_is_elsewhere_too')


def first_is_elsewhere_too(seq_seq):
    """
    Given a sequence of subsequences:
      -- Returns True if any element of the first (initial) subsequence
           appears in any of the other subsequences.
      -- Returns False otherwise.

    For example, if the given argument is:
        [(3, 1, 4),
         (13, 10, 11, 7, 10),
         [11, 12, 3, 10]]
    then this function returns True because 3 appears
    in the first subsequence and also in the third subsequence.

    As another example, if the given argument is:
        [(3, 1, 4),
         (13, 10, 11, 7, 10),
         [11, 2, 13, 14]]
    then this function returns False because 3 does not appear in
    any subsequence except the first, 1 does not appear in any
    subsequence except the first, and 4 does not appear in any
    subsequence except the first.

    As yet another example, if the given argument is:
      ([], [1, 2], [1, 2])
    then this function returns False since no element of the first
    subsequence appears elsewhere.

    Preconditions:
      :type seq_seq: (list, tuple)
    and the given argument is a sequence of sequences.
    """
    # ------------------------------------------------------------------
    # done: 6. Implement and test this function.
    #          Some tests are already written for you (above).
    #
    # IMPLEMENTATION RESTRICTION:
    #   ** You may NOT use anything but comparison (==) in judging
    #      membership.  In particular, you may NOT use:
    #        -- the IN operator
    #              (example:  7 in [9, 6, 7, 9] returns True)
    #        -- the COUNT method
    #              (example:  [9, 6, 7, 9].count(9) returns 2)
    #        -- the INDEX method
    #              (example:  [9, 6, 7, 9, 6, 1].index(6) returns 1)
    #   in this problem, as doing so would defeat the goal of providing
    #   practice at loops within loops (within loops within ...)
    # ------------------------------------------------------------------

    for k in range(1, len(seq_seq)):
        sublist = seq_seq[0]
        sublist1 = seq_seq[k]
        for m in range(len(sublist)):
            num_to_look_for = sublist[m]
            for n in range(len(sublist1)):
                if sublist1[n] == num_to_look_for:
                    return True
    return False





# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
