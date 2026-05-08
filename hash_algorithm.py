from abc import ABC, abstractmethod


class HashAlgorithm(ABC):
    """
    Abstract Base Class sebagai kontrak untuk semua algoritma hash.

    Semua class turunan wajib mengimplementasikan method generate_hash().
    Class seperti MD5Hash, SHA1Hash, SHA256Hash, dan SHA512Hash
    adalah subtype dari HashAlgorithm.
    """

    def __init__(self, name: str, bit_length: int) -> None:
        if not isinstance(name, str) or name.strip() == "":
            raise ValueError("Nama algoritma harus berupa string dan tidak boleh kosong.")

        if not isinstance(bit_length, int) or bit_length <= 0:
            raise ValueError("Bit length harus berupa bilangan bulat positif.")

        self.__name = name
        self.__bit_length = bit_length

    @property
    def name(self) -> str:
        return self.__name

    @property
    def bit_length(self) -> int:
        return self.__bit_length

    @staticmethod
    def _to_bytes(text: str) -> bytes:
        return text.encode("utf-8")

    @abstractmethod
    def generate_hash(self, text: str) -> str:
        pass