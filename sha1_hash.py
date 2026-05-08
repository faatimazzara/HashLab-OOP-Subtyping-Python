import hashlib
from hash_algorithm import HashAlgorithm


class SHA1Hash(HashAlgorithm):
    """
    Implementasi algoritma SHA-1.
    SHA1Hash adalah subtype dari HashAlgorithm.
    """

    def __init__(self) -> None:
        super().__init__("SHA-1", 160)

    def generate_hash(self, text: str) -> str:
        return hashlib.sha1(self._to_bytes(text)).hexdigest()