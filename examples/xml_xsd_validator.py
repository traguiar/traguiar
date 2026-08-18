"""Validação de XML contra XSD com diagnóstico objetivo."""

from __future__ import annotations
from pathlib import Path
import argparse
from lxml import etree


def validar_xml(caminho_xml: Path, caminho_xsd: Path) -> list[str]:
    try:
        schema = etree.XMLSchema(etree.parse(str(caminho_xsd)))
        documento = etree.parse(str(caminho_xml))
        schema.assertValid(documento)
        return []
    except (etree.XMLSyntaxError, etree.DocumentInvalid, etree.XMLSchemaParseError) as erro:
        log = getattr(erro, "error_log", None)
        return [str(erro)] if not log else [
            f"linha {item.line}, coluna {item.column}: {item.message}" for item in log
        ]


def main() -> None:
    parser = argparse.ArgumentParser(description="Valida um XML contra um schema XSD.")
    parser.add_argument("xml", type=Path)
    parser.add_argument("xsd", type=Path)
    args = parser.parse_args()
    erros = validar_xml(args.xml, args.xsd)
    if erros:
        print("XML inválido:")
        for erro in erros:
            print(f"- {erro}")
        raise SystemExit(1)
    print("XML válido conforme o XSD.")


if __name__ == "__main__":
    main()
