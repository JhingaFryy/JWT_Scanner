import jwt
import requests
import argparse
import time

# Common Weak Secrets for JWT Cracking
COMMON_SECRETS = ["password", "admin", "123456", "secret", "jwtsecret", "changeme"]

# List of weak algorithms
WEAK_ALGORITHMS = ["none", "HS256", "HS384", "HS512"]

def decode_jwt(token):
    """Decode JWT and check for weak secrets."""
    header = jwt.get_unverified_header(token)
    algorithm = header.get("alg")
    
    if algorithm in WEAK_ALGORITHMS:
        print(f"[!] Weak Algorithm Detected: {algorithm}")
    
    for secret in COMMON_SECRETS:
        try:
            decoded = jwt.decode(token, secret, algorithms=[algorithm])
            print(f"[+] JWT Cracked! Secret: {secret}")
            print(decoded)
            return
        except jwt.exceptions.InvalidSignatureError:
            continue
    
    print("[-] No weak secrets found.")

def test_jwt_injection(url, token):
    """Tests for JWT injection vulnerabilities."""
    manipulated_token = token[:-1] + "A"
    headers = {"Authorization": f"Bearer {manipulated_token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("[!] Potential JWT Manipulation Detected!")
    else:
        print("[-] No immediate JWT vulnerability detected.")

def main():
    parser = argparse.ArgumentParser(description="JWT Security Scanner")
    parser.add_argument("-t", "--token", required=True, help="JWT Token to analyze")
    parser.add_argument("-u", "--url", help="API URL to test for JWT injection")
    args = parser.parse_args()
    
    print("[+] Scanning JWT Token...")
    decode_jwt(args.token)
    
    if args.url:
        print("[+] Testing JWT injection...")
        test_jwt_injection(args.url, args.token)
    
    print("[+] Scan Complete!")

if __name__ == "__main__":
    main()
