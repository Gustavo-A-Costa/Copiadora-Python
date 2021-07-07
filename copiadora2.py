import shutil

# shutil - é o módulo que contém funções que copiam arquivos
print('____CÓPIA ENTRE PASTAS____')
origem = 'Pasta A'
destino = 'Pasta B'

shutil.copytree(origem, destino, dirs_exist_ok=True)
fim = input('Processo concluído. Aperte enter para encerrar')
print(fim)
