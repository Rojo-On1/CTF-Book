class CodeVinciVM:
    def __init__(self):
        self.stack = []
        self.file_pointers = {}

    def run(self, code):
        output = ""

        for instruction in code:
            cmd = instruction[0]
            args = instruction[1:]

            if cmd == 'PUSH':
                self.push(*args)
            elif cmd == 'ADD':
                self.add()
            elif cmd == 'SUB':
                self.sub()
            elif cmd == 'PRINT':
                output += str(self.stack.pop()) + "\n"
            elif cmd == 'READ_NEXT_LINE':
                self.read_next_line()
            else:
                output += f"Unknown instruction: {cmd}\n"

        return output

    def push(self, value):
        self.stack.append(value)

    def add(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def sub(self):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def read_next_line(self):
        if not self.stack:
            print("Error: no file specified in the stack.")
            return

        filename = self.stack[-1]

        if filename not in self.file_pointers:
            try:
                self.file_pointers[filename] = open(filename, 'r')
            except FileNotFoundError:
                print(f"Error: the file {filename} does not exist.")
                return

        file_pointer = self.file_pointers[filename]
        line = file_pointer.readline()

        if line:
            self.stack.append(line.strip())
        else:
            print(f"End of file {filename} reached.")
            file_pointer.close()
            del self.file_pointers[filename]

    def load_program(self, filename):
        code = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split()
                        cmd = parts[0]
                        args = [int(arg) if arg.isdigit() else arg for arg in parts[1:]]
                        code.append([cmd] + args)

        except FileNotFoundError:
            print(f"Error: the file {filename} does not exist.")

        return code

