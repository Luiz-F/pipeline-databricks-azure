# Databricks notebook source
dbutils.fs.ls("/mnt/dados/bronze")

# COMMAND ----------

path = "dbfs:/mnt/dados/bronze/dataset_imoveis/"
df = spark.read.format("delta").load(path)

# COMMAND ----------

display(df)

# COMMAND ----------

display(df.select("anuncio.*"))


# COMMAND ----------

display(
    df.select("anuncio.*","anuncio.endereco.*")
    
    
    )


# COMMAND ----------

dados_detalhados =  df.select("anuncio.*","anuncio.endereco.*")
display(dados_detalhados)

# COMMAND ----------

df_silver = dados_detalhados.drop("caracteristicas","endereco")
display(df_silver)

# COMMAND ----------

path = "dbfs:/mnt/dados/silver/dataset_imoveis"
df_silver.write.format("delta").mode("Overwrite").save(path)

# COMMAND ----------

dbutils.fs.ls("/mnt/dados/silver/dataset_imoveis")

# COMMAND ----------


