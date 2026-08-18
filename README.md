<div align="center">
  <img src="assets/banner-thiago-aguiar-v2.png" alt="Thiago Aguiar — Tax Technology, Automação e Dados" width="100%" />

  <h3>Transformo complexidade tributária em soluções digitais auditáveis.</h3>

  [![Python](https://img.shields.io/badge/Python-111111?style=flat-square&logo=python&logoColor=FF7A00)](examples/sped_resumo.py)
  [![XML/XSD](https://img.shields.io/badge/XML%20%2F%20XSD-111111?style=flat-square&logo=xml&logoColor=FF7A00)](examples/xml_xsd_validator.py)
  [![Dados](https://img.shields.io/badge/Análise%20de%20dados-111111?style=flat-square&logo=databricks&logoColor=FF7A00)](examples/conciliacao_tributaria.py)
</div>

## Sobre mim

Sou profissional da área tributária com atuação em **Tax Technology, automação e inteligência fiscal**. Desenvolvo soluções para interpretar arquivos fiscais, validar obrigações, cruzar bases contábeis e transformar regras complexas em controles claros.

```python
thiago = {
    "atuação": "Tax Technology e Inteligência Tributária",
    "especialidades": ["Automação fiscal", "Dados", "Compliance"],
    "tecnologias": ["Python", "APIs", "SQL", "XML/XSD", "HTML/JS"],
    "objetivo": "Reduzir esforço manual sem perder rastreabilidade"
}
```

## Demonstrações técnicas

Todos os exemplos abaixo usam dados fictícios e podem ser executados localmente.

### 01 · Leitor de TXT/SPED

Identifica registros, contabiliza ocorrências e apresenta um resumo do arquivo sem depender de layout fixo.

```python
for linha in arquivo:
    campos = linha.rstrip("\n").split("|")
    registro = campos[1] if len(campos) > 1 else "LINHA_INVALIDA"
    contagem[registro] += 1
```

[Ver código completo →](examples/sped_resumo.py)

### 02 · Validação XML/XSD

Valida estrutura e regras de schema, devolvendo mensagens com linha, coluna e causa do erro.

```python
schema = etree.XMLSchema(etree.parse(caminho_xsd))
documento = etree.parse(caminho_xml)
schema.assertValid(documento)
```

[Ver código completo →](examples/xml_xsd_validator.py)

### 03 · Conciliação tributária

Compara apuração e fechamento por estabelecimento, aplica tolerância e classifica divergências.

```python
diferenca = valor_apurado - valor_fechamento
status = "OK" if abs(diferenca) <= tolerancia else "DIVERGENTE"
```

[Ver código completo →](examples/conciliacao_tributaria.py)

## Soluções que desenvolvo

| Frente | Aplicação prática | Resultado |
|---|---|---|
| Obrigações fiscais | Importação, estruturação e validação | Menos digitação e retrabalho |
| SPED, ECD e ECF | Leitura e cruzamento de registros | Rastreabilidade da origem ao total |
| XML e XSD | Geração e validação de eventos | Diagnóstico técnico antes do envio |
| Conciliações | Comparação por período e estabelecimento | Divergências localizadas rapidamente |
| Reforma Tributária | Mapeamento de operações, NCM/NBS e classificações | Parametrização mais consistente |
| Dados gerenciais | Dashboards e laudos executivos | Informação pronta para decisão |

## Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-111111?style=for-the-badge&logo=python&logoColor=FF7A00)
![JavaScript](https://img.shields.io/badge/JavaScript-111111?style=for-the-badge&logo=javascript&logoColor=FF7A00)
![HTML5](https://img.shields.io/badge/HTML5-111111?style=for-the-badge&logo=html5&logoColor=FF7A00)
![Flask](https://img.shields.io/badge/Flask-111111?style=for-the-badge&logo=flask&logoColor=FF7A00)
![Pandas](https://img.shields.io/badge/Pandas-111111?style=for-the-badge&logo=pandas&logoColor=FF7A00)
![SQLite](https://img.shields.io/badge/SQLite-111111?style=for-the-badge&logo=sqlite&logoColor=FF7A00)
![Git](https://img.shields.io/badge/Git-111111?style=for-the-badge&logo=git&logoColor=FF7A00)
![SAP](https://img.shields.io/badge/SAP%20S%2F4HANA-111111?style=for-the-badge&logo=sap&logoColor=FF7A00)

</div>

## Atividade no GitHub

<div align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=traguiar&show_icons=true&hide_border=true&bg_color=0D0D0D&title_color=FF7A00&icon_color=FF7A00&text_color=FFFFFF&locale=pt-br" alt="Estatísticas do GitHub" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=traguiar&layout=compact&hide_border=true&bg_color=0D0D0D&title_color=FF7A00&text_color=FFFFFF&locale=pt-br" alt="Linguagens mais utilizadas" />
</div>

> Os conteúdos públicos deste perfil utilizam dados fictícios ou anonimizados. Informações, códigos e ativos corporativos permanecem protegidos.

<div align="center">
  <strong>Tributação • Tecnologia • Automação • Dados</strong>
</div>
