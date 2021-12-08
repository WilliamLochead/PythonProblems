# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


def count_carries(a, b):
    result = 0
    bigger = 0
    smaller = 0
    carry_on = 0

    if a > b:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a

    while bigger != 0:
        if bigger % 10 + smaller % 10 + carry_on > 9:
            result += 1
            carry_on = 1
        else:
            carry_on = 0

        bigger //= 10
        smaller //= 10

    return result


def count_consecutive_summers(n):
    total = 1

    for i in range(1, int(n / 2) + 1):
        for j in range(1, n):
            sum = (2 * i + j) * (j + 1) / 2
            if sum == n:
                # Found another sequence
                total += 1
                break

            if sum > n:
                break

    return total


def frequency_sort(elems):
    frequency_dict = dict()
    for elem in elems:
        if elem in frequency_dict:
            frequency_dict[elem] += 1

        else:
            frequency_dict[elem] = 1

    return sorted(elems, key=lambda elem: (-1 * frequency_dict[elem], elem))


def give_change(amount, coins):
    change = []

    index = 0
    while index < len(coins):
        while amount >= coins[index]:
            change.append(coins[index])
            amount -= coins[index]

        index += 1

    return change


def squares_intersect(s1, s2):
    if (s1[0] + s1[2] < s2[0]) or (s2[0] + s2[2] < s1[0]) or (
            s1[1] + s1[2] < s2[1]) or (s2[1] + s2[2] < s1[1]):
        return False
    else:
        return True


def safe_squares_rooks(n, rooks):
    safe_rows = n
    safe_columns = n

    for i in range(0, n):
        row_found = False
        column_found = False
        for rook in rooks:
            if rook[0] == i and rook[1] == i:
                if not row_found:
                    safe_rows -= 1
                    row_found = True
                if not column_found:
                    safe_columns -= 1
                    column_found = True

            elif rook[0] == i and not row_found:
                safe_rows -= 1
                row_found = True

            elif rook[1] == i and not column_found:
                safe_columns -= 1
                column_found = True

            if row_found and column_found:
                break  # both row and column found

    return safe_rows * safe_columns


def expand_intervals(intervals):
    result = []
    if len(intervals) == 0:
        return result

    tokens = intervals.split(",")
    for token in tokens:
        numbers = token.split("-")
        from_number = int(numbers[0])
        if len(numbers) == 2:
            to_number = int(numbers[1])
        else:
            to_number = from_number

        for i in range(from_number, to_number + 1):
            result.append(i)

    return result


def is_ascending(items):
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False

    return True


def riffle(items, out=True):
    res = []
    half = len(items) // 2
    for i in range(half):
        if out:
            res.append(items[i])
            res.append(items[half + i])
        else:
            res.append(items[half + i])
            res.append(items[i])
    return res
