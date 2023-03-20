# Prints del autor, GitHub y uso del script
decorative_line = "=" * 80
print(decorative_line)
print("Autor: Santiago Aguado")
print("GitHub: https://github.com/nullx100")
print("Uso: Este script genera un archivo de configuración JSON para un conector OracleCDC de Kafka Connect. Debes de proporcionar los valores de los siguientes parámetros: nombre del conector, nombre del topic, nombre de la base de datos, nombre del schema y nombre de la tabla.")
print("⚠⚠⚠ Peligro de solapamiento de topics si no se sabe lo que se hace. Revisar muy bien el resultado antes de importar en entornos productivos. ⚠⚠⚠")
print(decorative_line)

import json

# Solicitar los valores de los parámetros

domain = input("Ingresa el nombre del dominio (DDD):")
subdomain = input("Ingresa el nombre del dominio (DDD):")
server = input("Ingresa del servidor de base de datos: ")
database = input("Ingresa el nombre de la base de datos: ")
password = input("Ingresa la password de la base de datos para el usuario C##CONFLUENT: ")
schema = input("Ingresa el nombre del schema: ")
table = input("Ingresa el nombre de la tabla: ")


# Formatear los valores
domain = domain.lower()
subdomain = subdomain.lower()
server = server.lower() + ".riu.net"
database = database.upper()
schema = schema.upper()
table = table.upper()

connector_name = f"{database}.{domain}.{subdomain}.{table}.sync-0"
topic_name = f"{domain}.{subdomain}.{table}.sync-0"
topic_redo = f"redo-log-topic-{table}-0"
topic_heartbeat = f"Heartbeat-Topic-{table}-0"
table_regex = f"{database}.({schema}.{table})"
topi_corruption = f"redo-log-topic-{table}-0-error-corruption"

# Crear el diccionario de configuración
config = {
    "name": connector_name,
    "config": {
        "topic.creation.default.partitions": "5",
        "topic.creation.redo.partitions": "1",
        "topic.creation.redo.include": topic_redo,
        "topic.creation.default.replication.factor": "3",
        "topic.creation.redo.retention.ms": "1209600000",
        "topic.creation.redo.replication.factor": "3",
        "topic.creation.default.cleanup.policy": "compact",
        "topic.creation.redo.cleanup.policy": "delete",
        "key.converter.schemas.enable": "false",
        "value.converter.schemas.enable": "false",
        "name": connector_name,
        "connector.class": "io.confluent.connect.oracle.cdc.OracleCdcSourceConnector",
        "tasks.max": "1",
        "key.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "config.action.reload": "restart",
        "errors.retry.timeout": "3",
        "errors.retry.delay.max.ms": "60000",
        "errors.log.enable": "true",
        "errors.log.include.messages": "true",
        "topic.creation.groups": "",
        "oracle.server": server,
        "oracle.port": "1521",
        "oracle.sid": "CONTAINER",
        "oracle.pdb.name": database,
        "oracle.service.name": "",
        "oracle.username": "C##CONFLUENT",
        "oracle.password": password,
        "start.from": "current",
        "redo.log.topic.name": f"redo-log-topic-{table.upper()}-0",
        "redo.log.corruption.topic": topic_corruption,
        "redo.log.consumer.bootstrap.servers": "dev-cp-kafka-headless:9092",
        "behavior.on.dictionary.mismatch": "log",
        "heartbeat.interval.ms": "7200000",
        "heartbeat.topic.name": topic_heartbeat,
        "table.inclusion.regex": table_regex,
        "table.topic.name.template": topic_name,
        "connection.pool.max.size": "20"
    }
}

# Guardar el diccionario como archivo JSON
with open(f"{name}.json", "w") as outfile:
    json.dump(config, outfile, indent=4)
