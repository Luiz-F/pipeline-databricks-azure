# Databricks notebook source
# MAGIC %scala
# MAGIC dbutils.fs.ls("/mnt/dados/inbound")

# COMMAND ----------

path = "dbfs:/mnt/dados/inbound/dados_brutos_imoveis.json"
dados = spark.read.json(path)

# COMMAND ----------

display(dados)

# COMMAND ----------

dados_anuncio = dados.drop("imagens","usuario")
display(dados_anuncio)

# COMMAND ----------

from pyspark.sql.functions import col

# COMMAND ----------

df_bronze = dados_anuncio.withColumn("id",col=dados_anuncio.anuncio.id)
display(df_bronze)

# COMMAND ----------


df_bronze.write.format("delta").save("dbfs:/mnt/dados/bronze/dataset_imoveis",mode='OVERWRITE')

# COMMAND ----------

dbutils.fs.ls("/mnt/dados/bronze")
