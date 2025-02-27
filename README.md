## Features
- Detects weak JWT secrets using a common wordlist.
- Identifies weak signing algorithms (e.g., `none`, `HS256`).
- Tests for JWT injection vulnerabilities on specified API endpoints.

## Installation
```bash
pip install pyjwt requests
```

## Usage
```bash
python jwt.py -t <JWT_TOKEN> [-u <API_URL>]
```

### Example
```bash
python jwt.py -t "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
```

To test against an API:
```bash
python jwt.py -t <JWT_TOKEN> -u https://api.example.com/protected
```

## License
MIT License

##Donate me a Coffee:
PayPal: pardeshijatin1998@gmail.com
