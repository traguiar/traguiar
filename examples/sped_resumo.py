"""Resumo genérico de registros de um arquivo TXT/SPED."""

from __future__ import annotations
from collections import Counter
from pathlib import Path
import argparse


def resumir_sped(caminho: Path) -> Counter[str]:
    contagem: Counter[str] = Counter()
    with caminho.open("r", encoding="latin-1", errors="replace") as arquivo:
        for linha in arquivo:
            campos = linha.rstrip("\r\n").split("|")
            registro = campos[1].strip() if len(campos) > 1 and campos[1].strip() else "LINHA_INVALIDA"
            contagem[registro] += 1
    return contagem


def main() -> None:
    parser = argparse.ArgumentParser(description="Resume registros de um TXT/SPED.")
    parser.add_argument("arquivo", type=Path)
    args = parser.parse_args()
    if not args.arquivo.is_file():
        raise SystemExit(f"Arquivo não encontrado: {args.arquivo}")
    resumo = resumir_sped(args.arquivo)
    print(f"Registros encontrados: {sum(resumo.values())}")
    for registro, quantidade in resumo.most_common():
        print(f"{registro:>15}  {quantidade:>8}")


if __name__ == "__main__":
    main()
