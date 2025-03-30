#!/usr/bin/env python3
from picklescan.scanner import scan_pickle_bytes, SafetyLevel
import io, pickle, base64

def serve_soup():
    print("Welcome to Grandma's Pickle Soup!")
    inp = input("Give me your secret pickle soup recipe (base64 encoded): ")
    
    try:
        pkl = base64.b64decode(inp)
        result = scan_pickle_bytes(io.BytesIO(pkl), 1337)
        
        if (
            result.scan_err
            or result.issues_count > 0
            or not all([g.safety == SafetyLevel.Innocuous for g in result.globals])
        ):
            print("Grandma doesn't trust your soup! Try again.")
            exit()
        
        recipe = pickle.loads(pkl)
        print("Mmm... Grandma approves this soup recipe!")
    except Exception as e:
        print("Oh no! Your soup exploded: ", str(e))
        exit()

if __name__ == "__main__":
    serve_soup()