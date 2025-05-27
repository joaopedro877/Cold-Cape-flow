
Análise da dinâmica marinha na região de Cabo Frio, sudeste do Brasil por estudantes da pós-graduação em geofísica da Universidade federal da Bahia. 

# Resumo
Este projeto visa analisar a circulação oceânica costeira e os processos de ressurgência na região de Cabo Frio, sudeste do Brasil. Usando 5 anos de dados de reanálise do ERA5, buscamos quantificar o transporte de Ekman, transporte geostrófico, tensão de cisalhamento do vento e rotacional do vento, caracterizando a interação oceano-atmosfera que regula os eventos de upwelling na região.

# Introdução
A região de Cabo Frio é conhecida por sua intensa atividade de ressurgência costeira, resultado da interação dos ventos predominantes e da circulação oceânica. Este processo influencia diretamente a produtividade biológica, a dinâmica físico-química da água e os processos de troca de massa e energia entre oceano e atmosfera.

## Objetivo
- Quantificar a variabilidade espaço-temporal da tensão de cisalhamento do vento e seu rotacional.
- Calcular o transporte de Ekman e identificar sua relação com eventos de ressurgência.
- Estimar o transporte geostrófico superficial
- Avaliar os impactos desses processos na dinâmica costeira da região de Cabo Frio.

## Metodologia

### 2.1. Área de Estudo
- Região de Cabo Frio, costa sudeste do Brasil.
- Limites espaciais: 15°S–30°S, 35°W–50°W)

### 2.2. Dados Utilizados
Foram utilizados os dados de reanálise do ERA5 para os anos entre 2020 e 2024, de 3 em 3 horas, relativos a:
- velocidades horizontais e verticais a 10 metros da superfície do mar (u10 e v10)
- densidade do ar sobre o oceano.

### 2.3. Processamento e Análises
- **Coeficiente de arrasto:** Utilizando formula de Large and Yeager (2004)
- **Rotacional do vento:** Calculado a partir dos gradientes espaciais das componentes u e v do vento.
- **Tensão de cisalhamento do vento:** Usando fórmula quadrática baseada na densidade do ar e coeficiente de arrasto.
- **Transporte de Ekman:** A partir da tensão de vento e parâmetros físicos (densidade da água, f).
- **Transporte geostrófico:** 
- **Ferramentas:** Python (numpy)

  ## 3. Resultados Esperados
- Mapas sazonais de:
  - Rotacional do vento
  - Tensão de cisalhamento
  - Transporte de Ekman (superficial)
  - Correntes geostróficas superficiais
- Análise da correlação entre transporte de Ekman e indicadores de ressurgência
- Discussão dos padrões sazonais e interanuais associados à dinâmica costeira


##  Estrutura do projeto
- `data/`: Dados brutos e processados
- `notebooks/`: Notebooks interativos de análise
- `src/`: Código-fonte Python
- `figures/`: Figuras geradas para análises e apresentações
- `docs/`: Documentação técnica e metodológica

## Funcionalidades
- Download automático de dados de vento (ERA5, CCMP ou Scatterometer)
- Cálculo do rotacional do vento e mapas
- Cálculo da tensão de cisalhamento do vento
- Estimativas de transporte de Ekman
- Transporte geostrófico superficial via anomalia da altura do mar
- Visualização dos campos e séries temporais

## Referências
- Pond, S., & Pickard, G. L. (1983). Introductory Dynamical Oceanography.
- Large, W.G., Yeager, S.G., 2004. Diurnal to decadal global forcing for
ocean and sea-ice models: the data sets and flux climatologies.
Technical Note NCAR/TN-460+STR. NCAR, Boulder, CO.
- Castelao, R. M., and
J. A. Barth (2006), Upwelling around Cabo Frio, Brazil: The
importance of wind stress curl, Geophys. Res. Lett., 33, L03602,
doi:10.1029/2005GL025182.
