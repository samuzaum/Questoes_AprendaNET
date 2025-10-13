import os, re

pasta = r"C:/Users/SAMUEL/Desktop/Questoes/torque"  
original_inicio = 25
novo_inicio     = 2 
desloc = novo_inicio - original_inicio
saida = os.path.join(pasta, "renumeradas")
os.makedirs(saida, exist_ok=True)

padrao = re.compile(r"questao(\d+)\.html$", re.IGNORECASE)

arquivos = []
for f in os.listdir(pasta):
    m = padrao.match(f)
    if m:
        n = int(m.group(1))
        arquivos.append((n, f))
arquivos.sort(key=lambda x: x[0])

def shift_num(match):
    n = int(match.group(1))
    return f"questao{n + desloc}.html"

def shift_problema(match):
    n = int(match.group(1))
    return f"Problema {n + desloc}"

for n_antigo, nome in arquivos:
    n_novo = n_antigo + desloc
    caminho_antigo = os.path.join(pasta, nome)

    with open(caminho_antigo, "r", encoding="utf-8") as f:
        conteudo = f.read()

    conteudo = re.sub(r"questao(\d+)\.html", shift_num, conteudo)

    conteudo = re.sub(r"Problema\s+(\d+)", shift_problema, conteudo)

    novo_nome = f"questao{n_novo}.html"
    with open(os.path.join(saida, novo_nome), "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"{nome}  ->  renumeradas\\{novo_nome}")

print("Concluído.")
