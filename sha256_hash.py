import hashlib
from hash_algorithm import HashAlgorithm


class SHA256Hash(HashAlgorithm):
    """
    Implementasi algoritma SHA-256.
    SHA256Hash adalah subtype dari HashAlgorithm.
    """

    def __init__(self) -> None:
        super().__init__("SHA-256", 256)

    def generate_hash(self, text: str) -> str:
        return hashlib.sha256(self._to_bytes(text)).hexdigest()