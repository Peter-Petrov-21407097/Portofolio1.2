import json

INPUT_FILE = "backup_corrigido.json"
OUTPUT_FILE = "backup_final.json"


trocas = {

    # já existentes
    "curriculos": "currículos",
    "atenþÒo": "atenção",
    "ç§es": "ções",

    # novas correções
    "þÒ": "ção",
    "Ûncia": "ência",
}


def corrigir(texto):

    if not isinstance(texto, str):
        return texto

    for errado, certo in trocas.items():
        texto = texto.replace(errado, certo)

    return texto


def percorrer(obj):

    if isinstance(obj, dict):
        return {k: percorrer(v) for k, v in obj.items()}

    elif isinstance(obj, list):
        return [percorrer(i) for i in obj]

    elif isinstance(obj, str):
        return corrigir(obj)

    return obj


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    dados = json.load(f)

dados = percorrer(dados)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("backup_final.json criado com sucesso!")