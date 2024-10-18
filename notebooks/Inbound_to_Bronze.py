# Databricks notebook source
# IMPORTANDO BIBLIOTECA 
from pyspark.sql.functions import col

# COMMAND ----------

# CARREGANDO ARQUIVO RAW
path = "dbfs:/mnt/dados/inbound/dados_brutos_imoveis.json"
dados = spark.read.json(path)

# COMMAND ----------

# TRANSFORMANDO E GRAVANDO NA CAMADA BRONZE.
dados_anuncio = dados.drop("imagens","usuario")
df_bronze = dados_anuncio.withColumn("id",col=dados_anuncio.anuncio.id)
df_bronze.write.format("delta").save("dbfs:/mnt/dados/bronze/dataset_imoveis",mode='OVERWRITE')
