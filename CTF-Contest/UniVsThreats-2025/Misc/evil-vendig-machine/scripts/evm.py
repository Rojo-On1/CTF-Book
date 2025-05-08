to_unsigned_hex = lambda x: int(hex(x % (2**256)),16)
class EthStack:

    def __init__(self):
        self.stack = list()
        self.memory = dict()

    def PUSH(self,x):
        self.stack.append(x)

    def DIV(self):
        self.stack.append(self.stack.pop() // self.stack.pop())

    def ADDMOD(self):
        self.stack.append((self.stack.pop() + self.stack.pop()) % self.stack.pop())

    def ADD(self):
        self.stack.append(self.stack.pop() + self.stack.pop() % 2**256)

    def MUL(self):
        self.stack.append(self.stack.pop() * self.stack.pop() % 2**256)

    def SUB(self):
        self.stack.append(to_unsigned_hex(self.stack.pop() - self.stack.pop()))

    def MSTORE(self):
        i =  hex(self.stack.pop())
        self.memory[i] = self.stack.pop()

    def MLOAD(self):
        self.stack.append(self.memory.get(hex(self.stack.pop()),0))

    def XOR(self):
        self.stack.append(self.stack.pop() ^ self.stack.pop())

    def EQ(self):
        return self.stack.pop() == self.stack.pop()

    def CHECK(self):
        print()
        print("*"*25)
        print(list(map(hex,self.stack)))
        print("Memory: ",self.memory)
        print("*"*25)

    def PUSH_MANY(arr):
        for b in arr:
            c.PUSH(b)

    def CALLVALUE(self):
        self.stack.append(self.get_flag())

    def get_flag(self):
        CALL_VALUE  = (0x274cade36c + 0x3b83) // 0x57
        return CALL_VALUE

c = EthStack()
c.PUSH(0x951d)
c.PUSH(0x6063eb0c)
c.DIV()
c.PUSH(0x3b83)
c.CALLVALUE()
c.PUSH(0x63)
c.PUSH(0x3f72)
c.PUSH(0xb4)
c.ADDMOD() # 0xba
c.MUL() #  CALL_VALUE * 0xba
c.SUB() #  CALL_VALUE - 0x3b83

c.PUSH(0x2c)
c.PUSH(0x1af3)
c.MUL()
c.PUSH(0x07a4)
c.MSTORE()
c.PUSH(0x07d0b9)
c.PUSH(0xab52)
c.ADD()
c.PUSH(0x07c7)
c.MSTORE()
c.PUSH(0x026a85)
c.PUSH(0x952d)
c.XOR()
c.PUSH(0x0881ba)
c.MSTORE()
c.PUSH(0x07c7)
c.MLOAD()
c.PUSH(0x07a4)
c.MLOAD()
c.MUL()

c.CHECK()  
input()

success = c.EQ()
print(f"FLAG GAINED: {state}")
print(f"FLAG: {hex(c.get_flag())}")
