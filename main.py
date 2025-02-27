from time import sleep


class MemGen1:
    def __init__(self, *args):
        self.numbers_list = args
        self.list_len = len(self.numbers_list)
        self.pos_num = 0

    def get_next_num(self):
        res_num = self.numbers_list[self.pos_num]
        if self.pos_num < self.list_len -1:
            self.pos_num += 1
        else:
            self.pos_num = 0
        return print(res_num)

aboba = MemGen1(1,5,6,3,1,2,3,7,4,0)

for i in range(60):
    aboba.get_next_num()
    sleep(0.5)
