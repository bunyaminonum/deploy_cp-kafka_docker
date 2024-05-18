# deploy_cp-kafka_docker

Bu proje, Docker kullanarak Confluent Platform (CP) ve Kafka'yı dağıtmayı amaçlamaktadır. Bu, Docker konteynerleri kullanarak bir Kafka kümesi kurmayı içerir.

## Başlarken

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler

- Docker
- Docker Compose

### Kurulum

1. Bu depoyu klonlayın:
    ```sh
    git clone https://github.com/your-username/deploy_cp-kafka_docker.git
    ```

2. Proje dizinine gidin:
    ```sh
    cd deploy_cp-kafka_docker
    ```

3. Docker Compose dosyasını çalıştırın:
    ```sh
    docker-compose up -d
    ```

## Servisler

Bu Docker Compose dosyası aşağıdaki servisleri içerir:

- **Zookeeper**: Kafka broker'larının koordinasyonu için gerekli.
- **Kafka Broker'ları**: Kafka mesajlarını işleyen üç broker (broker1, broker2, broker3).
- **Schema Registry**: Kafka için şema yönetimi sağlar.
- **ksqlDB Server ve CLI**: Kafka üzerinde SQL sorguları çalıştırmak için.
- **Control Center**: Kafka kümelerini yönetmek ve izlemek için.
- **Kafka Connect**: Kafka'ya veri akışı sağlamak için.
- **Kafdrop**: Kafka kümelerini görselleştirmek için.
- **REST Proxy**: Kafka'ya REST API üzerinden erişim sağlar.
- **Prometheus**: İzleme ve uyarı sistemi.
- **Grafana**: İzleme verilerini görselleştirmek için.

## Portlar

Aşağıdaki portlar kullanılmaktadır:

- Zookeeper: 2181
- Kafka Broker'ları: 9092, 9093, 9094
- Schema Registry: 8081
- ksqlDB Server: 8088
- Control Center: 9021
- Kafka Connect: 8083
- Kafdrop: 9000
- REST Proxy: 8082
- Prometheus: 9090
- Grafana: 3000

## Volumes

Aşağıdaki veri hacimleri kullanılmaktadır:

- prometheus_data
- grafana_data
- rest-proxy_data
- kafdrop_data
- connect_data
- control-center_data
- schema-registry_data
- ksql-server_data
- ksqldb-cli_data

## Kullanım

Docker Compose dosyasını çalıştırdıktan sonra, yukarıda belirtilen portlar üzerinden servislerinize erişebilirsiniz. Örneğin, Kafka Control Center'a erişmek için tarayıcınızda `http://localhost:9021` adresini ziyaret edebilirsiniz.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.