import os
import sys
from dataclasses import dataclass
from textwrap import wrap
from typing import Dict, Union

from hash_algorithm import HashAlgorithm
from hash_manager import HashManager
from md5_hash import MD5Hash
from sha1_hash import SHA1Hash
from sha256_hash import SHA256Hash
from sha512_hash import SHA512Hash


# ==========================================================
# TERMINAL STYLE
# ==========================================================
class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    WHITE = "\033[97m"
    MAGENTA = "\033[95m"


# ==========================================================
# KONFIGURASI TABEL
# ==========================================================
TABLE_COLOR = Style.CYAN
TEXT_COLOR = Style.WHITE

BOX_TEXT_WIDTH = 76
MENU_WIDTHS = [6, 16, 14, 31]
RESULT_WIDTHS = [14, 59]


@dataclass(frozen=True)
class ResultView:
    original_text: str
    algorithm_name: str
    bit_length: Union[int, str]
    hash_text: str

    @property
    def hash_length(self) -> int:
        return len(self.hash_text)


# ==========================================================
# TERMINAL SETUP
# ==========================================================
def enable_terminal_color() -> None:
    os.system("")

    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def pause() -> None:
    input(f"\n{Style.DIM}Tekan Enter untuk kembali ke menu...{Style.RESET}")


# ==========================================================
# DATA ALGORITMA
# ==========================================================
def create_algorithms() -> Dict[str, HashAlgorithm]:
    return {
        "1": MD5Hash(),
        "2": SHA1Hash(),
        "3": SHA256Hash(),
        "4": SHA512Hash(),
    }


# ==========================================================
# BOX SATU KOLOM
# ==========================================================
def box_border(left: str, fill: str, right: str) -> None:
    print(TABLE_COLOR + left + (fill * (BOX_TEXT_WIDTH + 2)) + right + Style.RESET)


def box_row(text: str = "", color: str = TEXT_COLOR) -> None:
    text = str(text)

    if len(text) > BOX_TEXT_WIDTH:
        text = text[:BOX_TEXT_WIDTH - 1] + "…"

    print(
        TABLE_COLOR + "║ " +
        color + text.ljust(BOX_TEXT_WIDTH) +
        TABLE_COLOR + " ║" +
        Style.RESET
    )


def box_center(text: str = "", color: str = TEXT_COLOR) -> None:
    text = str(text)

    if len(text) > BOX_TEXT_WIDTH:
        text = text[:BOX_TEXT_WIDTH - 1] + "…"

    print(
        TABLE_COLOR + "║ " +
        color + text.center(BOX_TEXT_WIDTH) +
        TABLE_COLOR + " ║" +
        Style.RESET
    )


def print_info_box(title: str, paragraphs: list[str], title_color: str) -> None:
    print(f"\n{title_color}{Style.BOLD}{title}{Style.RESET}")

    box_border("╔", "─", "╗")

    for paragraph in paragraphs:
        for line in wrap(paragraph, width=BOX_TEXT_WIDTH):
            box_row(line)

    box_border("╚", "─", "╝")


# ==========================================================
# TABEL MULTI KOLOM
# ==========================================================
def table_border(
    widths: list[int],
    left: str,
    fill: str,
    separator: str,
    right: str
) -> None:
    line = left + separator.join(fill * (width + 2) for width in widths) + right
    print(TABLE_COLOR + line + Style.RESET)


def table_row(
    cells: list[str],
    widths: list[int],
    color: str = TEXT_COLOR
) -> None:
    row = TABLE_COLOR + "║" + Style.RESET

    for index, (cell, width) in enumerate(zip(cells, widths)):
        text = str(cell)

        if len(text) > width:
            text = text[:width - 1] + "…"

        row += color + f" {text:<{width}} " + Style.RESET
        row += TABLE_COLOR + "║" + Style.RESET

    print(row)


# ==========================================================
# BANNER / OPENING
# ==========================================================
def show_banner() -> None:
    clear_screen()

    ascii_title = [
        "██╗  ██╗ █████╗ ███████╗██╗  ██╗    ██╗      █████╗ ██████╗",
        "██║  ██║██╔══██╗██╔════╝██║  ██║    ██║     ██╔══██╗██╔══██╗",
        "███████║███████║███████╗███████║    ██║     ███████║██████╔╝",
        "██╔══██║██╔══██║╚════██║██╔══██║    ██║     ██╔══██║██╔══██╗",
        "██║  ██║██║  ██║███████║██║  ██║    ███████╗██║  ██║██████╔╝",
        "╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚═════╝",
    ]

    print()
    box_border("╔", "═", "╗")
    box_row("")

    for line in ascii_title:
        box_center(line, Style.CYAN)

    box_row("")
    box_center("String Hashing App with OOP and Subtyping", Style.YELLOW)
    box_row("")
    box_border("╚", "═", "╝")


def show_opening_info() -> None:
    print_info_box(
        "📌 Tentang Program",
        [
            "Program ini digunakan untuk mengubah string biasa menjadi hash text.",
            "Algoritma yang tersedia adalah MD5, SHA-1, SHA-256, dan SHA-512.",
            "Program dibuat dengan konsep OOP agar kode lebih rapi dan mudah dikembangkan.",
        ],
        Style.YELLOW
    )

    print_info_box(
        "📘 Konsep Subtyping",
        [
            "HashManager menerima tipe umum yaitu HashAlgorithm.",
            "Object yang digunakan bisa berupa MD5Hash, SHA1Hash, SHA256Hash, atau SHA512Hash.",
            "Karena semua algoritma adalah turunan dari HashAlgorithm, maka semuanya bisa dipakai oleh HashManager.",
        ],
        Style.MAGENTA
    )


# ==========================================================
# MENU
# ==========================================================
def show_menu(algorithms: Dict[str, HashAlgorithm]) -> None:
    print(f"\n{Style.CYAN}{Style.BOLD}📋 Menu Algoritma Hashing{Style.RESET}")

    table_border(MENU_WIDTHS, "╔", "═", "╦", "╗")
    table_row(["Kode", "Algoritma", "Kekuatan", "Keterangan"], MENU_WIDTHS, Style.BOLD + Style.WHITE)
    table_border(MENU_WIDTHS, "╠", "═", "╬", "╣")

    for key, algorithm in algorithms.items():
        table_row(
            [
                key,
                algorithm.name,
                f"{algorithm.bit_length} bit",
                f"Hashing menggunakan {algorithm.name}",
            ],
            MENU_WIDTHS
        )

    table_row(["5", "Semua", "-", "Tampilkan semua hasil hash"], MENU_WIDTHS)
    table_row(["0", "Keluar", "-", "Tutup aplikasi dengan aman"], MENU_WIDTHS)

    table_border(MENU_WIDTHS, "╚", "═", "╩", "╝")


# ==========================================================
# INPUT
# ==========================================================
def input_choice() -> str:
    return input(f"\n{Style.YELLOW}👉 Masukkan kode pilihan: {Style.RESET}").strip().lower()


def input_text() -> str:
    while True:
        text = input(f"{Style.YELLOW}✍️  Masukkan string yang ingin di-hash: {Style.RESET}").strip()

        if text:
            return text

        print(f"{Style.RED}⚠️  Text tidak boleh kosong. Silakan input ulang.{Style.RESET}")


# ==========================================================
# HASH PROCESS
# ==========================================================
def generate_hash_safely(
    manager: HashManager,
    algorithm: HashAlgorithm,
    text: str
) -> str:
    """
    Fungsi ini dibuat agar main.py tetap aman,
    baik HashManager kamu memakai generate_hash(), hash_text(),
    atau algoritmanya langsung memakai generate_hash().
    """

    manager.set_algorithm(algorithm)

    if hasattr(manager, "generate_hash"):
        return manager.generate_hash(text)

    if hasattr(manager, "hash_text"):
        return manager.hash_text(text)

    if hasattr(algorithm, "generate_hash"):
        return algorithm.generate_hash(text)

    if hasattr(algorithm, "hash"):
        return algorithm.hash(text)

    raise AttributeError("Tidak ditemukan method untuk melakukan hashing.")


def make_result(
    manager: HashManager,
    algorithm: HashAlgorithm,
    text: str
) -> ResultView:
    hash_text = generate_hash_safely(manager, algorithm, text)

    return ResultView(
        original_text=text,
        algorithm_name=getattr(algorithm, "name", algorithm.__class__.__name__),
        bit_length=getattr(algorithm, "bit_length", "-"),
        hash_text=hash_text
    )


# ==========================================================
# RESULT DISPLAY
# ==========================================================
def result_row(label: str, value: str) -> None:
    label_width, value_width = RESULT_WIDTHS
    wrapped_value = wrap(str(value), width=value_width) or [""]

    table_row([label, wrapped_value[0]], RESULT_WIDTHS)

    for line in wrapped_value[1:]:
        table_row(["", line], RESULT_WIDTHS)


def show_result(result: ResultView) -> None:
    print(f"\n{Style.GREEN}{Style.BOLD}✅ Hasil Hashing{Style.RESET}")

    table_border(RESULT_WIDTHS, "╔", "═", "╦", "╗")
    table_row(["Algoritma", result.algorithm_name], RESULT_WIDTHS, Style.BOLD + Style.WHITE)
    table_border(RESULT_WIDTHS, "╠", "═", "╬", "╣")

    result_row("Text Asli", result.original_text)
    result_row("Kekuatan", f"{result.bit_length} bit")
    result_row("Panjang Hash", f"{result.hash_length} karakter hexadecimal")
    result_row("Hash Text", result.hash_text)

    table_border(RESULT_WIDTHS, "╚", "═", "╩", "╝")


def process_single_algorithm(
    manager: HashManager,
    algorithm: HashAlgorithm,
    text: str
) -> None:
    result = make_result(manager, algorithm, text)
    show_result(result)


def process_all_algorithms(
    manager: HashManager,
    algorithms: Dict[str, HashAlgorithm],
    text: str
) -> None:
    print(f"\n{Style.GREEN}{Style.BOLD}🚀 Menampilkan Semua Algoritma{Style.RESET}")

    for algorithm in algorithms.values():
        process_single_algorithm(manager, algorithm, text)


# ==========================================================
# EXIT FEATURE
# ==========================================================
def show_exit_confirm_box() -> None:
    print(f"\n{Style.YELLOW}{Style.BOLD}🚪 Konfirmasi Keluar{Style.RESET}")

    box_border("╔", "─", "╗")
    box_row("Apakah kamu yakin ingin keluar dari program?")
    box_row("Ketik y untuk keluar, atau n untuk kembali ke menu.")
    box_border("╚", "─", "╝")


def confirm_exit() -> bool:
    show_exit_confirm_box()

    while True:
        answer = input(f"{Style.YELLOW}Pilihan kamu (y/n): {Style.RESET}").strip().lower()

        if answer == "y":
            return True

        if answer == "n":
            print(f"{Style.GREEN}Baik, kembali ke menu utama.{Style.RESET}")
            return False

        print(f"{Style.RED}⚠️  Pilihan hanya boleh y atau n.{Style.RESET}")


def show_goodbye_screen() -> None:
    clear_screen()

    print()
    box_border("╔", "═", "╗")
    box_row("")
    box_center("TERIMA KASIH SUDAH MENGGUNAKAN HASH LAB", Style.GREEN)
    box_center("Program selesai dengan aman.", Style.WHITE)
    box_row("")
    box_center("Keep learning Python, OOP, and Subtyping!", Style.YELLOW)
    box_row("")
    box_border("╚", "═", "╝")


# ==========================================================
# MAIN PROGRAM
# ==========================================================
def main() -> None:
    enable_terminal_color()

    algorithms = create_algorithms()
    manager = HashManager(SHA256Hash())

    while True:
        show_banner()
        show_opening_info()
        show_menu(algorithms)

        choice = input_choice()

        if choice in ["0", "q", "quit", "exit", "keluar"]:
            if confirm_exit():
                show_goodbye_screen()
                break

            pause()
            continue

        if choice not in algorithms and choice != "5":
            print(f"\n{Style.RED}⚠️  Pilihan tidak valid. Silakan pilih kode yang tersedia.{Style.RESET}")
            pause()
            continue

        text = input_text()

        if choice in algorithms:
            selected_algorithm = algorithms[choice]

            # Konsep subtyping:
            # selected_algorithm bisa berupa MD5Hash, SHA1Hash, SHA256Hash, atau SHA512Hash.
            # Semuanya tetap diperlakukan sebagai HashAlgorithm.
            process_single_algorithm(manager, selected_algorithm, text)

        elif choice == "5":
            process_all_algorithms(manager, algorithms, text)

        pause()


if __name__ == "__main__":
    main()