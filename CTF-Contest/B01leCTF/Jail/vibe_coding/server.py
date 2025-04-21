#!/usr/bin/env python3

import os

FILE_TEMPLATE = """
import java.io.*;

public class Main {
    // %s
    public static void main(String[] args) {
        // TODO: implement me
    }

    public static String getFlag() throws IOException {
        // FIXME: we probably don't want the user accessing this; just throw for now
        throw new RuntimeException("Not implemented yet");

        // var br = new BufferedReader(new FileReader("/flag.txt"));
        // return br.readLine();
    }
}
"""

blacklist = ['\r', '\n']
if __name__ == "__main__":
    print(r"""+
|        ______  _____  _____  ____    ______  _____   ______   ______  _____  _____   _____
|       |      >/     ||_    ||    |  |   ___||     | |   ___| |   ___|/     \|     | |     |
|       |     < |  /  | |    ||    |_ |   ___||     \  `-.`-.  |   |__ |     ||     \ |    _|_
|       |______>|_____/ |____||______||______||__|\__\|______| |______|\_____/|__|\__\|___| |_|
+
Welcome to b01lersCorp Semantic LOad-balanced Program GENerator (SLOPGEN) v3.20.25.
    """, flush=True)
    comment = input('Enter your prompt below:\n> ')
    # No tricks, please :)
    for banned in blacklist:
        if banned in comment:
            print('Illegal characters: terminating...')
            exit()

    with open('/tmp/Main.java', 'w') as f:
        # Write the prompt into the source file

        f.write(FILE_TEMPLATE % comment)

        # TODO: run the actual model !!!

    print('\nYour program output:\n', flush=True)
    os.system('cd /tmp && javac Main.java && java Main')
    print('===', flush=True)
