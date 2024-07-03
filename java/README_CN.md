## 用于PADDLE SERVING的JAVA客户端

([ENGLISH](./README.md)|简体中文)

## 开发环境

为了方便用户使用JAVA进行开发，我们提供了编译好的SERVING工程放置在JAVA镜像当中，获取镜像并进入开发环境的方式是

```
docker pull registry.baidubce.com/paddlepaddle/serving:0.6.0-java

docker run --rm -dit --name java_serving registry.baidubce.com/paddlepaddle/serving:0.6.0-java

docker exec -it java_serving bash

cd Serving/java
```

SERVING文件夹是镜像生成时的DEVELOP分支工程目录，需要GIT PULL到最新版本，或者GIT CHECKOUT到想要的分支。

## 安装客户端依赖

由于依赖库数量庞大，因此镜像已经在生成时编译过一次，用户执行以下操作即可

```
mvn compile
mvn install
cd examples
mvn compile
mvn install
```

## 请求BRPC-SERVER

### 服务端启动

以FIT_A_LINE模型为例，服务端启动与常规BRPC-SERVER端启动命令一样。

```
cd ../../examples/C++/fit_a_line

sh get_data.sh

python -m paddle_serving_server.serve --model uci_housing_model --thread 10 --port 9393
```

### 客户端预测
客户端目前支持多种请求方式，目前支持HTTP（数据为JSON格式）、HTTP（数据为PROTO格式）、GRPC

推荐您使用HTTP（数据为PROTO格式），此时数据体为PROTO格式，传输的数据量小，速度快，目前已经帮用户实现了HTTP/GRPC的数据体（JSON/PROTO）的封装函数，详见[CLIENT.JAVA](./src/main/java/io/paddle/serving/client/Client.java)
```
cd ../../../java/examples/target
java -cp paddle-serving-sdk-java-examples-0.0.1-jar-with-dependencies.jar PaddleServingClientExample http_proto <configPath>
```
**注意`<CONFIGPATH>`为客户端配置文件，一般是名为SERVING_CLIENT_CONF.PROTOTXT的文件。**

更多示例详见：[PaddleServingClientExample.java](./examples/src/main/java/PaddleServingClientExample.java)


## 请求PIPELINE-SERVER

### 服务端启动

对于INPUT DATA TYPE = STRING类型，以IMDB MODEL ENSEMBLE模型为例，服务端启动

```
cd ../examples/Pipeline/imdb_model_ensemble

sh get_data.sh

python -m paddle_serving_server.serve --model imdb_cnn_model --port 9292 &> cnn.log &
python -m paddle_serving_server.serve --model imdb_bow_model --port 9393 &> bow.log &

python test_pipeline_server.py &>pipeline.log &
```

### 客户端预测(同步)

```
cd ../../../java/examples/target

java -cp paddle-serving-sdk-java-examples-0.0.1-jar-with-dependencies.jar PipelineClientExample string_imdb_predict
```

### 客户端预测(异步)

```
cd ../../../java/examples/target

java -cp paddle-serving-sdk-java-examples-0.0.1-jar-with-dependencies.jar PipelineClientExample asyn_predict
```

对于INPUT DATA TYPE = INDARRAY类型，以SIMPLE PIPELINE WEBSERVICE中的UCI_HOUSING_MODEL模型为例，服务端启动

```
cd ../examples/Pipeline/simple_web_service

sh get_data.sh

python web_service_java.py &>log.txt &
```

### 客户端预测(同步)

```
cd ../../../java/examples/target

java -cp paddle-serving-sdk-java-examples-0.0.1-jar-with-dependencies.jar PipelineClientExample indarray_predict
```

### 注意事项

1. 在示例中，端口号都是9393，IP默认设置为了127.0.0.1表示本机，注意IP和PORT需要与SERVER端对应。

2. 目前SERVING已推出PIPELINE模式（原理详见[PIPELINE SERVING](../doc/Python_Pipeline/Pipeline_Design_CN.md)），面向JAVA的PIPELINE SERVING CLIENT已发布。

3. 注意PipelineClientExample.java中的ip和port（位于java/examples/src/main/java/[PipelineClientExample.java](./examples/src/main/java/PipelineClientExample.java)），需要与对应Pipeline server的config.yaml文件中配置的ip和port相对应。（以IMDB model ensemble模型为例，位于python/examples/pipeline/imdb_model_ensemble/[config.yaml](../examples/Pipeline/imdb_model_ensemble/config.yml)）

### 开发部署指导

由于JAVA的DOCKER镜像中不含有SERVING需要的编译开发环境，SERVING的常规DOCKER镜像中也不包含JAVA所需要的编译开发环境，对GPU SERVING端和JAVA CLIENT端的二次编译开发需要在各自的DOCKER镜像下完成，下面以GPU模式为例，讲解开发部署的两种形式。

第一种是GPU SERVING和JAVA CLIENT在运行在同一个GPU镜像中，需要用户在启动GPU镜像后，把在JAVA镜像中编译完成后的文件(位于/SERVING/JAVA目录下)拷贝到GPU镜像中的/SERVING/JAVA目录下。

第二种是GPU SERVING和JAVA CLIENT分别在各自的DOCKER镜像中(或具备编译开发环境的不同主机上)部署，此时仅需注意JAVA CLIENT端与GPU SERVING端的IP和PORT需要对应，详见上述注意事项中的第3项。
