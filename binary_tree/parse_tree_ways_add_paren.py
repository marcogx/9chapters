# Given a string of numbers and operators,
# return all possible results from computing all the different possible ways
# to group numbers and operators. The valid operators are +, - and *.

# Input: "2*3-4*5"
#
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]


def parse_tree_ways_add_paren(input_str):
    if not input_str:
        return []
    ops = ('+', '-', '*')
    return helper(input_str, 0, len(input_str) - 1, ops)


def helper(input_str, start, end, ops):
    if start > end:
        return []

    res, has_ops = [], False
    for i in xrange(start, end + 1):
        if input_str[i] in ops:
            has_ops = True
            llist = helper(input_str, start, i - 1, ops)
            rlist = helper(input_str, i + 1, end, ops)
            for l in llist:
                for r in rlist:
                    res.append(compute(input_str[i], l, r))

    if not has_ops:
        res.append(int(input_str[start:end + 1]))
    return res


def compute(op, l, r):
    if op == '+':
        return l + r
    if op == '-':
        return l - r
    if op == '*':
        return l * r
