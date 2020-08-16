import matplotlib.pyplot as plt
import sort_test
plt.style.use('ggplot')
def read_param(msg, default):
    read = input(msg+f"(ENTER for {default}): ")
    return int(read) if read != "" else default
# Reading parameters
start = read_param("Inital size of the list", 5000)
inc = read_param("Increment of the tests", 5000)
limit = read_param("Stop when all test take more then", 30)
N = read_param("Numbers runs to avg", 1)
# Warining
if N > 1: print("N > 1 increases the time of execution drasticaly, please be patient")
# info = 0 nº de procuras
# info = 1 tempo de ordenação
# info = 2 desvio padrão
# info >=3 lista com tudo
tables = sort_test.comparison_table(info=3, N=N, start=start, increment=inc, limit=limit)
print(*tables, sep="\n\n")
# Nomes e links das imagens
imgs = ["search-chart", "time-chart", "stdev-chart"]
github = "https://raw.githubusercontent.com/gfborges/studies/master/sortcomp/"
link = [github + img + ".png" for img in imgs]
# função para fazer o gráfico e salvar
def chart(df, title, xlabel, ylabel,saveas):
    font ={
        "size":14,
        "weight":"bold"
    }
    df.plot(kind="line", figsize=(12,8))
    plt.title(title, fontdict=font)
    plt.xlabel(xlabel, fontdict=font)
    plt.ylabel(ylabel, fontdict= font)
    plt.savefig(saveas, dpi = 250)
# Fazendo os gráficos
chart(
    df=tables[0],
    title="Comparação da curva de número de busca",
    xlabel="Tamanho das listas",
    ylabel="Número de buscas (min-max)",
    saveas=imgs[0]+".png")
chart(
    df=tables[1],
    title="Comparação dos tempos de procura",
    xlabel="Tamanho da lista",
    ylabel="Tempo de ordenação (min-max)",
    saveas=imgs[1]+".png")
chart(
    df=tables[2],
    title="Comparação dos desvios padrão dos tempo de ordenação",
    xlabel="Tamanho da lista",
    ylabel="Desvio padrão",
    saveas=imgs[2]+".png")
# Ler o arquivo modelo
with open("header.md", "r") as header:
    f = header.readlines()
# Iterar nas tabelas e colocar elas no arquivo modelo
for table in tables:
    # Procura onde será inserido a tabela
    h = f.index("<insert-code-here>\n")
    # Faz o cabeçalho da tabela
    f[h] = 'N | '+ ' | '.join(table.columns)+ '\n'
    f[h+1] = ' | '. join(['---']*(len(table.columns)+1)) + '\n'
    h += 2
    # Faz as linhas na tabela
    for i, row in table.iterrows():
        r =f'{i} | ' + ' | '.join(list(map(str, row.values)))
        f.insert(h,r+"\n")
        h += 1
    img = "![{}]({})\n"
    # Insere o gráfico da tabela
    f.insert(h,img.format(imgs.pop(0),link.pop(0)))
# Escreva o novo arquivo output.md
with open("output.md", "x") as out:
    out.writelines(f)
