
class BitString:
    version_sum = 0

    def __init__(self, s):
        self.string = s

    def pop(self, n):
        if n > len(self.string):
            raise Exception("Short end: {}. Version sum: {}".format(
                 self.string, BitString.version_sum))
        x = int(self.string[:n], 2)
        self.string = self.string[n:]
        return x

    def str_pop(self, n):
        if n > len(self.string):
            raise Exception("Short end: {}".format(self.string))
        x = self.string[:n]
        self.string = self.string[n:]
        return x

    def readpacket(self, length = None):
        if not self.string:
            return 0
        n = 0
        try:
            version = self.pop(3)
            BitString.version_sum += version
            id = self.pop(3)
            n += 6
            if id == 4:
                value = 0
                while self.pop(1) == 1:
                    value <<= 4
                    value += self.pop(4)
                    n += 4
                value <<= 4
                value += self.pop(4)
                n += 4
            else:
                mode = self.pop(1)
                match mode:
                    case 0:
                        length = self.pop(15)
                        sub_str = self.str_pop(length)
                        bs = BitString(sub_str)
                        ret_list = []
                        while bs.string:
                            ret_list.append(bs.readpacket())
                    case 1:
                        number = self.pop(11)
                        ret_list = []
                        for k in range(number):
                            ret_list.append(self.readpacket())
                if id == 0:
                    value = sum(ret_list)
                elif id == 1:
                    value = 1
                    for x in ret_list:
                        value *= x
                elif id == 2:
                    value = min(ret_list)
                elif id == 3:
                    value = max(ret_list)
                elif id == 5:
                    value = int(ret_list[0] > ret_list[1])
                elif id == 6:
                    value = int(ret_list[0] < ret_list[1])
                elif id == 7:
                    value = int(ret_list[0] == ret_list[1])
            return_value = {
                "version": version,
                "id": id,
                "value": value}
            return return_value["value"]

        except Exception:
            print("Kuken!")
            raise Exception("Nu är det slut")
            return 0



def main():
    with open("input.txt") as f:
        hexdata = f.readline().strip()
        f.close()
    bs = BitString(hex_to_binary(hexdata))
    while len(bs.string) > 7:
        try:
            result = bs.readpacket()
        except:
            break
    print("Part 1. Version sum: {}\nPart 2. Expression result: {}".format(BitString.version_sum, result))



def hex_to_binary(s):
    """recode hexdigit for hexdigit"""
    binstring = ""
    for c in s:
        binstring += "{:04b}".format(int(c, 16))
    return binstring


main()
