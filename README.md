# Reposiório da disciplina de Algorítmos Numéricos
## Ferramentas
Para instalar o octave: 
```bash
sudo apt install octave
```

Para usar o octave na ferramenta gráfica: 
```bash
octave --gui
```

Para visualizar os algoritmos, ir no diretório `vizaulizacao` e executar
```bash
python3 interpolacaoNewton.py 
```

# Conteúdo
## Capítulo 2

## Capítulo 3
## Interpolação
## 
### Estudo do Erro
> 5.4 Reggero e Lopes, 2009 - Teo. 2 e 3

Existe uma fórmula exata para o erro mas, não é possivel conhecer a função usada na fórmula.
Essa parte desconhecida é igual a diferença dividida, que ainda não conhecemos.
Entretanto é possivel fazer uma aproximação da diferença dividida.
Tendo construido a tabela de diferencas divididas para a ordem `n+1`, usa-se o maior valor em módulo dessas difernças divididas para estimatimar o termo do erro.

> [Visualizador](visualizacao/estimaErro.py)