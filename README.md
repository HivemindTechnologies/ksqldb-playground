# ksqlDB Playground

This git repository contains all the necessary resources for getting started with ksqlDB. You can explore it by yourself or read our [blog article on ksqlDB](https://hivemindtechnologies.com/en/blog/introduction-to-ksqlbd), which provides a comprehensive overview of the technology and its capabilities, including step-by-step guides for setting up and using ksqlDB in various scenarios. In addition, the repository includes sample data and code examples to help you start with ksqlDB. 

![Architecture](./architecture.png)

## Setup

### Docker

```shell
docker compose up -d
```

### create venv

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### start fake sensor generator

```shell
source .venv/bin/activate
python sensor.py
```

## Usage

### UIs

- [Kafka UI](http://localhost:8080)
- [MinIO UI](http://localhost:9001) (username: `admin`, password: `password`)
- [InfluxDB UI](http://localhost:8086) (username: `myusername`, password: `passwordpasswordpassword`)

### CLI

start ksqlDB CLI

```shell
docker run --net host -it confluentinc/ksqldb-cli ksql
```

### Endpoints

- Kafka: `localhost:29092`
- S3: `http://localhost:9000` (ACCESS_KEY: `admin`, SECRET_KEY: `password`, bucket: `sink-bucket`)
- InfluxDB: `http://localhost:8086` (token: `mytoken`, org: `myorg`, bucket: `mybucket`)
