def to_binaer(num):
    result = ""
    while (num >= 1):
        result += str(num % 2)
        num = num // 2
    return result


def main():
    ip = input("ip: ")  # 255.255.255.255
    ips = ip.split('.')
    final = ""
    for binary in ips:
        result = to_binaer(int(binary))
        current = len(result)
        ziel = 0
        if (current < 8):
            target = 8
            ziel = target - current
        res = ""
        for i in range(ziel):
            res += "0"  # res = res + "0"
        result += res
        result = result[::-1]
        final += result
    print(final)


main()