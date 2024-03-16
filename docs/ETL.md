## Extract

O projeto possui uma pasta data/input, nessa primeira etapa fizemos a leitura desses dados em excel e o transformamos em uma lista de dataframes do pandas.

### Função de Extração

### ::: app.pipeline.extract.extract_from_excel


## Transform
Após a ingestão dos arquivos, concatenamos todos os dataframes em um único dataframe com todas as informações.

### Função de Transformação

### ::: app.pipeline.transform.contact_data_frames

## Load
Hora de disponibilizar os dados, para isso, exportamos o dataframe em um arquivo excel para que possa ser consumido.

### Função de Load

### ::: app.pipeline.load.load_excel

