import requests
from pathlib import Path
from typing import Union


class ZeroXZero:
    """
    A static utility class for interacting with the 0x0.st file hosting service.

    Features:
    - Upload files from disk
    - Upload in-memory data
    - Upload plain text
    - Check service availability
    """

    ENDPOINT_URL = "https://0x0.st"
    HEADERS = {
        "User-Agent": "pyzxz-uploader/1.0 (https://github.com/yourrepo)"
    }

    @staticmethod
    def upload(file_path: Union[str, Path]) -> str:
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"No such file: {file_path}")

        with file_path.open("rb") as f:
            response = requests.post(
                ZeroXZero.ENDPOINT_URL,
                files={"file": f},
                headers=ZeroXZero.HEADERS
            )

        if response.ok and response.text.startswith("https://"):
            return response.text.strip()
        raise ValueError(f"Upload failed: {response.text.strip()}")

    @staticmethod
    def upload_from_bytes(data: bytes, filename: str) -> str:
        files = {"file": (filename, data)}
        response = requests.post(
            ZeroXZero.ENDPOINT_URL,
            files=files,
            headers=ZeroXZero.HEADERS
        )

        if response.ok and response.text.startswith("https://"):
            return response.text.strip()
        raise ValueError(f"Upload failed: {response.text.strip()}")

    @staticmethod
    def upload_text(text: str, filename: str = "text.txt") -> str:
        return ZeroXZero.upload_from_bytes(text.encode("utf-8"), filename)

    @staticmethod
    def is_available() -> bool:
        try:
            response = requests.head(
                ZeroXZero.ENDPOINT_URL,
                timeout=3,
                headers=ZeroXZero.HEADERS
            )
            return response.status_code == 200
        except requests.RequestException:
            return False
