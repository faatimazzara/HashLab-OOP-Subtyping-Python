from dataclasses import dataclass
from hash_algorithm import HashAlgorithm


@dataclass(frozen=True)
class HashResult:
    """
    Class untuk menyimpan hasil hashing secara rapi dan terstruktur.
    """

    original_text: str
    algorithm_name: str
    bit_length: int
    hash_text: str

    @property
    def hash_length(self) -> int:
        return len(self.hash_text)


class HashManager:
    """
    Class pengelola proses hashing.

    Konsep subtyping digunakan pada atribut algorithm.
    Tipe yang diterima adalah HashAlgorithm,
    tetapi object yang masuk bisa berupa subtype-nya:
    MD5Hash, SHA1Hash, SHA256Hash, atau SHA512Hash.
    """

    def __init__(self, algorithm: HashAlgorithm) -> None:
        self.set_algorithm(algorithm)

    def set_algorithm(self, algorithm: HashAlgorithm) -> None:
        if not isinstance(algorithm, HashAlgorithm):
            raise TypeError("Algorithm harus merupakan subtype dari HashAlgorithm.")

        self.__algorithm = algorithm

    @property
    def algorithm(self) -> HashAlgorithm:
        return self.__algorithm

    def generate_hash(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Input yang akan di-hash harus bertipe string.")

        return self.__algorithm.generate_hash(text)

    def generate_report(self, text: str) -> HashResult:
        hash_text = self.generate_hash(text)

        return HashResult(
            original_text=text,
            algorithm_name=self.__algorithm.name,
            bit_length=self.__algorithm.bit_length,
            hash_text=hash_text
        )