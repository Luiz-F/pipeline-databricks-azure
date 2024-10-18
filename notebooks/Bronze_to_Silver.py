# Databricks notebook source
# CARREGANDO OS ARQUIVOS DELTA EM DATAFRAME
path = "dbfs:/mnt/dados/bronze/dataset_imoveis/"
df = spark.read.format("delta").load(path)

# COMMAND ----------

# SELECIONANDO AS COLUNAS QUE SERÃO SALVAS
dados_detalhados =  df.select("anuncio.*","anuncio.endereco.*")
df_silver = dados_detalhados.drop("caracteristicas","endereco")

# COMMAND ----------

# CARREGANDO OS DADOS 
path = "dbfs:/mnt/dados/silver/dataset_imoveis"
df_silver.write.format("delta").mode("Overwrite").save(path)
