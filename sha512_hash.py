import hashlib
from hash_algorithm import HashAlgorithm


class SHA512Hash(HashAlgorithm):
    """
    Implementasi algoritma SHA-512.
    SHA512Hash adalah subtype dari HashAlgorithm.
    """

    def __init__(self) -> None:
        super().__init__("SHA-512", 512)

    def generate_hash(self, text: str) -> str:
        return hashlib.sha512(self._to_bytes(text)).hexdigest()