# pyzxz

`pyzxz` is a lightweight Python client library for uploading files and text to [0x0.st](https://0x0.st), a simple and free file hosting service.

## Features

- Upload files from disk
- Upload in-memory bytes
- Upload plain text
- Check 0x0.st availability

## Installation

```bash
pip install pyzxz
```

## Usage

```python
from pyzxz import ZeroXZero

# Upload a local file
url = ZeroXZero.upload("path/to/file.txt")
print("Uploaded file URL:", url)

# Upload bytes from memory
url = ZeroXZero.upload_from_bytes(b"hello world", "hello.txt")
print("Uploaded bytes URL:", url)

# Upload a text string as a file
url = ZeroXZero.upload_text("Hello from pyzxz!")
print("Uploaded text URL:", url)

# Check if 0x0.st is online
is_online = ZeroXZero.is_available()
print("0x0.st online?", is_online)
```

## License

MIT License © 2025