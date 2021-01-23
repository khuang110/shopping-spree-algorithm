# Shopping spree algorithm
# By: Kyle Huang
# k = max weight carried for a person
# wt[] = weight of object
# val[] = P price
# n = n items
def shopping(k, wt, val, n):
    # Base case if not enough elements
    if n < 1 or k < 1:
        return

    w = max(wt)
    # init matrix for n elements X k
    v = [[0 for _ in range(k+1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for weight in range(k + 1):
            if wt[i - 1] > weight:
                v[i][weight] = v[i - 1][weight]
            else:
                v[i][weight] = max(v[i - 1][weight], v[i - 1][weight - wt[i - 1]] + val[i - 1])
    return v


def in_knapsack(v, w, n, wt):
    items = []
    for i in range(n, 1, -1):
        if v[i][w] != v[i - 1][w] and i > 0:
            items.append(i)
            i = i - 1
            w = w - wt[i]
        else:
            i = i - 1
    return items

# get file as list
def get_data():
    lines = []
    with open('shopping.txt') as infile:
        lines = [line.rstrip() for line in infile]
    return lines


def process_data(data):
    i = 0
    t = int(data[0])
    # init list of dict of length t
    test_cases = [{}]*t
    i = 1
    curr = 0
    # loop to fill each dict
    while i < len(data) and curr < t:
        n = int(data[i])
        p = []
        w = []
        m = []
        # range in data array for test case items
        for k in range(0+i+1, n+i+1):
            elem = data[k].split()
            p.append(int(elem[0]))
            w.append((int(elem[1])))
        # shift i over to index after n items
        i = i + n + 1
        f = int(data[i])
        # range in data array for weight carried by ith person
        for k in range(0+i+1, f+i+1):
            m.append(int(data[k]))
        i = i + f + 1
        # fill dictinary
        test_cases[curr] = {"N": n, "P": p, "W": w, "F": f, "M": m}
        curr += 1
    return test_cases

def output_to_file(case_num, total_price, mem_items):
    results = open("results.txt", "a")
    results.write("Test Case: %d\n" % (case_num))
    results.write("Total Price: %d\n" % (total_price))
    for member, item in enumerate(mem_items):
        results.write('{0}: {1}\n'.format(member+1, (' '.join(map(str, item)))))


def main():
    test_cases = process_data(get_data())

    # loop through T test cases
    for test_case in test_cases:
        # Max price of each family member
        total_price = 0
        items = [[]]
        case_num = 1
        # iterate over number of people in each family
        for mem in test_case["M"]:
            v = shopping(mem, test_case["W"], test_case["P"], test_case["N"])
            total_price = total_price + v[test_case["N"]][mem]
            items.append(in_knapsack(v, mem, test_case["N"], test_case["W"]))

        output_to_file(case_num, total_price, items[1:])
        case_num += 1


if __name__=="__main__":
    main()