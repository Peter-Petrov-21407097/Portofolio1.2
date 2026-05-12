import json


ficheiros = [
    "db_auth_user_corrigido_v1.json",
    "db_auth_group_corrigido_v1.json",
    "db_licenciatura_corrigido_v1.json",
    "db_unidades_curriculares_corrigido_v3.json",
    "db_docente_corrigido_v1.json",
    "db_tecnologia_corrigido_v1.json",
    "db_competencia_corrigido_v1.json",
    "db_areainteresse_corrigido_v1.json",
    "db_admin_logentry_corrigido_v1.json"
]


resultado = []

for ficheiro in ficheiros:
    with open("db_sem_projetos.json", "w", encoding="utf-8"):
        dados = json.load(f)

        if isinstance(dados, list):
            resultado.extend(dados)
        else:
            print(f"ERRO: {ficheiro} não contém uma lista JSON")

with open("db_corrigido.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)

print("db_corrigido.json criado com sucesso!")
print(f"Total de objetos: {len(resultado)}")