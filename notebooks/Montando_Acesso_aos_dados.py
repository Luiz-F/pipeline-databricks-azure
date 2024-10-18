# Databricks notebook source
# CRIANDO DIRETÓRIO PARA MONTAR O DATALAKE
dbutils.fs.mkdirs("/mnt/dados")

# COMMAND ----------

# COFNIGURANDO A INTEGRAÇÃO DO DATABRICKS COM DATALAKE DA AZURE.
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "",
          "fs.azure.account.oauth2.client.secret": "",
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/39d95a3b-2b14-4125-8155-c31fc74e84b3/oauth2/token"}

dbutils.fs.mount(
  source = "abfss://imoveis@datalakeazureestudo.dfs.core.windows.net/",
  mount_point = "/mnt/dados",
  extra_configs = configs)

