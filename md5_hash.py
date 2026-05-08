import hashlib
from hash_algorithm import HashAlgorithm


class MD5Hash(HashAlgorithm):
    """
    Implementasi algoritma MD5.
    MD5Hash adalah subtype dari HashAlgorithm.
    """

    def __init__(self) -> None:
        super().__init__("MD5", 128)

    def generate_hash(self, text: str) -> str:
        return hashlib.md5(self._to_bytes(text)).hexdigest()