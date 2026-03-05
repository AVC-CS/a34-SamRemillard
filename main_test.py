import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # June 10.10, July 11.20, August 13.20 -> avg 11.50
    regex_test([r'June.*July.*August.*11\.50'], lines)


@pytest.mark.T2
def test_main_2():
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Jan 10, Feb 20, Mar 30 -> avg 20.00
    regex_test([r'Jan.*Feb.*Mar.*20\.00'], lines)


@pytest.mark.T3
def test_main_3():
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Mar 50, Apr 60, June 70 -> avg 60.00
    regex_test([r'Mar.*Apr.*June.*60\.00'], lines)


@pytest.mark.T4
def test_main_4():
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    # Sep 5.5, Oct 8.5, Nov 12.0 -> avg 8.67
    regex_test([r'Sep.*Oct.*Nov.*8\.67'], lines)
