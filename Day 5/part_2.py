from collections import namedtuple


class Computer:
    ThreeParam = namedtuple('ThreeParam', 'p1 p2 p3', defaults=(0,)*3)
    TwoParam = namedtuple('TwoParam', 'p1 p2', defaults=(0,)*2)
    OneParam = namedtuple('OneParam', 'p1', defaults=(0,))

    def __init__(self, code_seq):
        self.code_seq = code_seq
        self.inst_point = 0
        self.last_output = None
        self.last_input = None
        self.last_op_code = None

    def set_input(self, new_input):
        self.last_input = new_input

    def process_code_sequence(self):
        try:
            while self.inst_point < len(self.code_seq):
                self.get_op_code()
                if self.last_op_code == 1:
                    self.exec_op_1()
                elif self.last_op_code == 2:
                    self.exec_op_2()
                elif self.last_op_code == 3:
                    self.exec_op_3()
                elif self.last_op_code == 4:
                    self.exec_op_4()
                elif self.last_op_code == 5:
                    self.exec_op_5()
                elif self.last_op_code == 6:
                    self.exec_op_6()
                elif self.last_op_code == 7:
                    self.exec_op_7()
                elif self.last_op_code == 8:
                    self.exec_op_8()
                else:
                    return self.last_output
        except IndexError:
            print("IndexError in {i}".format(i=self.inst_point))

    def get_op_code(self):
        if len(str(self.code_seq[self.inst_point])) != 1:
            self.last_op_code = int(str(self.code_seq[self.inst_point])[-2:])
        else:
            self.last_op_code = self.code_seq[self.inst_point]

    def exec_op_1(self):
        mode = self.get_mode()
        i1 = self.code_seq[self.code_seq[self.inst_point + 1]
                           ] if mode.p1 == 0 else self.code_seq[self.inst_point + 1]
        i2 = self.code_seq[self.code_seq[self.inst_point + 2]
                           ] if mode.p2 == 0 else self.code_seq[self.inst_point + 2]
        i3 = self.code_seq[self.inst_point + 3]
        self.code_seq[i3] = i1 + i2
        self.inst_point += 4

    def exec_op_2(self):
        mode = self.get_mode()
        i1 = self.code_seq[self.code_seq[self.inst_point + 1]
                           ] if mode.p1 == 0 else self.code_seq[self.inst_point + 1]
        i2 = self.code_seq[self.code_seq[self.inst_point + 2]
                           ] if mode.p2 == 0 else self.code_seq[self.inst_point + 2]
        i3 = self.code_seq[self.inst_point + 3]
        self.code_seq[i3] = i1 * i2
        self.inst_point += 4

    def exec_op_3(self):
        mode = self.get_mode()
        i1 = self.code_seq[self.inst_point + 1
                           ] if mode.p1 == 0 else self.code_seq[self.inst_point + 1]
        self.code_seq[i1] = self.last_input
        self.inst_point += 2

    def exec_op_4(self):
        mode = self.get_mode()
        i1 = self.code_seq[self.code_seq[self.inst_point + 1]
                           ] if mode.p1 == 0 else self.code_seq[self.inst_point + 1]
        self.last_output = i1
        self.inst_point += 2

    def exec_op_5(self):
        mode = self.get_mode()
        i1 = self.code_seq[self.code_seq[self.inst_point + 1]
                           ] if mode.p1 == 0 else self.code_seq[self.inst_point + 1]
        i2 = self.code_seq[self.code_seq[self.inst_point + 2]
                           ] if mode.p2 == 0 else self.code_seq[self.inst_point + 2]
        if i1 != 0:
            self.inst_point = i2
        else:
            self.inst_point += 3

    def exec_op_6(self):
        mode = self.get_mode()
        i1 = self.code_seq[self.code_seq[self.inst_point + 1]
                           ] if mode.p1 == 0 else self.code_seq[self.inst_point + 1]
        i2 = self.code_seq[self.code_seq[self.inst_point + 2]
                           ] if mode.p2 == 0 else self.code_seq[self.inst_point + 2]
        if i1 == 0:
            self.inst_point = i2
        else:
            self.inst_point += 3

    def exec_op_7(self):
        mode = self.get_mode()
        i1 = self.code_seq[self.code_seq[self.inst_point + 1]
                           ] if mode.p1 == 0 else self.code_seq[self.inst_point + 1]
        i2 = self.code_seq[self.code_seq[self.inst_point + 2]
                           ] if mode.p2 == 0 else self.code_seq[self.inst_point + 2]
        i3 = self.code_seq[self.inst_point + 3]
        self.code_seq[i3] = 1 if i1 < i2 else 0
        self.inst_point += 4

    def exec_op_8(self):
        mode = self.get_mode()
        i1 = self.code_seq[self.code_seq[self.inst_point + 1]
                           ] if mode.p1 == 0 else self.code_seq[self.inst_point + 1]
        i2 = self.code_seq[self.code_seq[self.inst_point + 2]
                           ] if mode.p2 == 0 else self.code_seq[self.inst_point + 2]
        i3 = self.code_seq[self.inst_point + 3]
        self.code_seq[i3] = 1 if i1 == i2 else 0
        self.inst_point += 4

    def get_mode(self):
        op_code = int(str(self.code_seq[self.inst_point])[-2:])
        op_params = str(self.code_seq[self.inst_point])[:-2][::-1]
        if 1 == op_code or 2 == op_code or 7 == op_code or 8 == op_code:
            fields = tuple(int(d) for d in op_params)
            return self.ThreeParam(*fields) if 0 < len(op_params) else self.ThreeParam()
        elif 3 == op_code or 4 == op_code:
            return self.OneParam(op_params[0]) if 0 < len(op_params) else self.OneParam()
        elif 5 == op_code or 6 == op_code:
            fields = tuple(int(d) for d in op_params)
            return self.TwoParam(*fields) if 0 < len(op_params) else self.TwoParam()
        else:
            print("this shouldn't happen")

if __name__ == '__main__':
    pass
