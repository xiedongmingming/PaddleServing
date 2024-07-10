# PADDLE SERVING CLIENT JAVA SDK

(简体中文|[ENGLISH](Java_SDK_EN.md))

PADDLESERVING提供了JAVA SDK，支持CLIENT端用JAVA语言进行预测，本文档说明了如何使用JAVA SDK。

## 快速开始

### 环境要求

```
- Java 8 or higher
- Apache Maven
```

下表显示了PADDLE SERVING SERVER和JAVA SDK之间的兼容性

| Paddle Serving Server version | Java SDK version |
| :---------------------------: | :--------------: |
|             0.9.0             |      0.0.1       |

1.    直接使用提供的JAVA SDK作为CLIENT进行预测
### 安装

您可以直接下载JAR，安装到本地MAVEN库：

```shell
wget https://paddle-serving.bj.bcebos.com/jar/paddle-serving-sdk-java-0.0.1.jar
mvn install:install-file -Dfile=$PWD/paddle-serving-sdk-java-0.0.1.jar -DgroupId=io.paddle.serving.client -DartifactId=paddle-serving-sdk-java -Dversion=0.0.1 -Dpackaging=jar
```

### MAVEN配置

```text
 <dependency>
     <groupId>io.paddle.serving.client</groupId>
     <artifactId>paddle-serving-sdk-java</artifactId>
     <version>0.0.1</version>
 </dependency>
```

2.    从源码进行编译后使用，详细步骤见[文档](../java/README.md).

3.    相关使用示例见[文档](../java/README.md).

