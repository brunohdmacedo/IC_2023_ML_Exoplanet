# IDENTIFICAÇÃO DE EXOPLANETAS UTILIZANDO TÉCNICAS DE APRENDIZADO DE MÁQUINA

**Bruno Henrique Dourado Macedo(1)**, Joylan Nunes Maciel(2), Willian Zalewski(3)

(1) Bolsista ITI - FA, Engenharia Física, Instituto Latino-Americano De Ciências Da Vida E Da Natureza (ILACVN), UNILA.

(2) Coorientador(a), Instituto Latino-Americano de Tecnologia, Infraestrutura e Território (ILATIT), Universidade Federal da Integração Latino Americana, UNILA.

(3) Orientador(a), Instituto Latino-Americano de Tecnologia, Infraestrutura e Território (ILATIT), Universidade Federal da Integração Latino Americana, UNILA.

*E-mail de contato: bhd.macedo.2017@aluno.unila.edu.br*

## RESUMO

Nas últimas décadas, o progresso tecnológico e a redução de custos em equipamentos astronômicos levaram a uma expansão significativa dos recursos de coleta e armazenamento de dados pelos cientistas. Missões espaciais como CoRoT, NuSTAR, NEOWISE, Gaia, Hubble, Kepler, TESS e o mais recente Telescópio Espacial James Web aprimoraram nossa compreensão do universo...

### Tabela 1 - Resultado dos experimentos.
| Modelo | Transformação | Teste (Acc %) | Teste (Dp %) | Treino (Acc %) | Treino (Dp %) |
| ------ | -------------- | ------------- | ------------ | -------------- | -------------- |
| RF     | CATCH22        | 83,05         | 0,48         | 82,65          | 0,58           |
| RF     | MINIROCKET     | 83,30         | 0,68         | 83,35          | 0,60           |
| NB     | CATCH22        | 60,70         | 0,69         | 60,70          | 0,73           |
| NB     | MINIROCKET     | 69,20         | 0,41         | 69,65          | 0,70           |
| MLP    | CATCH22        | 77,50         | 0,81         | 76,65          | 0,84           |
| MLP    | MINIROCKET     | 80,05         | 0,32         | 79,05          | 0,35           |

**Fonte:** Autoria própria.

## REFERÊNCIAS

1. MONTANGER, P. O.; ZALEWSKI, W. Programa computacional para a identificação automática de exoplanetas. Revista Brasileira de Iniciação Científica, p. 195-208, abr. 2020. ISSN 2359-232X.

2. ZALEWSKI, W. Modelagem Simbólica de Padrões Morfológicos para a Classificação de Séries Temporais. Dissertação (Doutorado) – Universidade Federal do Paraná- UFPR, 2015.

3. SHALLUE, C. J.; VANDERBURG, A. Identifying exoplanets with deep learning: A five planet resonant chain around Kepler-80 and an eighth planet around Kepler-90. The Astronomical Journal, 2017. DOI 10.3847/1538-3881/aa9e09

## AGRADECIMENTOS

Gostaria de agradecer a UNILA por abrir as portas da universidade, à PRPPG/UNILA e à Fundação Araucária/PR pelo seu apoio através da bolsa ITI, ao professor Willian Zalewski pela orientação neste projeto.

