"""Conciliação simples entre apuração e fechamento por estabelecimento."""

from __future__ import annotations
from decimal import Decimal
from pathlib import Path
import argparse
import csv


def ler_valores(caminho: Path) -> dict[str, Decimal]:
    valores: dict[str, Decimal] = {}
    with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            estabelecimento = linha["estabelecimento"].strip()
            valor = Decimal(linha["valor"].replace(".", "").replace(",", "."))
            valores[estabelecimento] = valores.get(estabelecimento, Decimal("0")) + valor
    return valores


def conciliar(apuracao: Path, fechamento: Path, tolerancia: Decimal) -> list[dict[str, str]]:
    valores_apuracao = ler_valores(apuracao)
    valores_fechamento = ler_valores(fechamento)
    estabelecimentos = sorted(valores_apuracao.keys() | valores_fechamento.keys())
    resultado = []
    for estabelecimento in estabelecimentos:
        apurado = valores_apuracao.get(estabelecimento, Decimal("0"))
        fechado = valores_fechamento.get(estabelecimento, Decimal("0"))
        diferenca = apurado - fechado
        resultado.append({
            "estabelecimento": estabelecimento,
            "apurado": str(apurado),
            "fechamento": str(fechado),
            "diferenca": str(diferenca),
            "status": "OK" if abs(diferenca) <= tolerancia else "DIVERGENTE",
        })
    return resultado


def main() -> None:
    parser = argparse.ArgumentParser(description="Concilia duas bases tributárias em CSV.")
    parser.add_argument("apuracao", type=Path)
    parser.add_argument("fechamento", type=Path)
    parser.add_argument("--tolerancia", type=Decimal, default=Decimal("1.00"))
    args = parser.parse_args()
    for linha in conciliar(args.apuracao, args.fechamento, args.tolerancia):
        print(" | ".join(linha.values()))


if __name__ == "__main__":
    main()
