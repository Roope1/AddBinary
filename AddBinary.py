# By translating the binary into integers and then doing the maths
def add_binary(a: str, b:str) -> str:
    a = "0b"+a
    b = "0b"+b

    res = int(a,2) + int(b,2)
    return str(bin(res))[2:]


# Without translating to integers
def add_binary_no_int(a: str, b: str) -> str:
    
    # make the strings equal sizes
    def compare_length(a: str, b: str) -> int:
        l_a = len(a)
        l_b = len(b)

        if l_a == l_b: return 0

        return 1 if l_a < l_b else -1


    diff = compare_length(a, b)
    while(diff != 0):
        diff = compare_length(a, b)
        if diff < 0: b = '0' + b
        if diff > 0: a = '0' + a

    
    result = ""
    carryin = 0
    for bit in zip(a[::-1], b[::-1]):
        x = int(bit[0]) + int(bit[1]) + carryin
        if x == 0:
            result = '0' + result
            carryin = 0
        elif x == 1:
            result = '1' + result
            carryin = 0
        elif x == 2:
            result = '0' + result
            carryin = 1
        elif x == 3:
            result = '1' + result
            carryin = 1

    if carryin == 1:
        result = '1' + result

    return result


def test_functions():
    assert add_binary("1", "1") == "10"
    assert add_binary("10", "1") == "11"
    assert add_binary("10", "11") == "101"
    assert add_binary("10101010", "11001100") == "101110110"

    assert add_binary_no_int("1", "1") == "10"
    assert add_binary_no_int("10", "1") == "11"
    assert add_binary_no_int("10", "11") == "101"
    assert add_binary_no_int("10101010", "11001100") == "101110110"


if __name__ == "__main__":
    test_functions()
    print("All tests passed")