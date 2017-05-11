# 如何生成有效的证书

## 获取官方试用的正版证书

注册申请试用即可，获取 base64 格式的证书字符串。

这里有若干已经获取证书：


## 分析证书生成明文

关键使用 atla-anaylysis.py 和 atlassian_pub.pem

将上面的证书拷贝到文件中，替换 `license_key` 的字符串，然后执行程序将会打印明文信息。
d
目录中已经有一些常用的明文信息，如fisheye，drawio等。

## 根据明文信息构造 keygen-xxx

拷贝一份任意的 keygen-xxx.py, 然后把对应的 license 明文信息替换，然后执行命令将会生成密文。

注意需要修改 server_id = 'B48T-DILQ-1L2P-P84A'  为你已经安装 server id

可以参考 license.md 已经创建好的若干证书


# Atlassian 破解

## Last update: 2016-11-17

- Bamboo 5.12.3.1
- Bitbucket 4.8.3
- Confluence 5.10.3
- Crowd 2.9.1
- FishEye / Crucible 4.2.1
- JIRA Software 7.1.9

## How to use?

1. build the image in every sub folder

```
  docker build -t confluence-dp .
```

2. run the image, port is define in dockerfile and

```
  docker run --detach --publish 8090:8090 confluence-dp
  docker run --detach --publish 8080:8080 jira-dp
  docker run --detach --publish 8080:8080 --name jira-dp -d to
  docker run --detach --publish 3306:3306 --name jira-mysql -e MYSQL_ROOT_PASSWORD=d33pn3t -d mysql:5.6
  docker exec -it jira-mysql bash
```

### POSTGRES

```
docker run --detach --publish 5432:5432 --name jira-postgres -e POSTGRES_PASSWORD=d33pn3t -d postgres:9.4

psql -U postgres -W

CREATE DATABASE jiradb WITH ENCODING 'UNICODE' LC_COLLATE 'C' LC_CTYPE 'C' TEMPLATE template0;
```
### command for cloudhero

```
curl -SLO "https://github.com/xinmeng1/ShareFiles/blob/master/mysql-connector-java-5.1.39-bin.jar"
docker run --detach --publish 8080:8080 --name jira-dp -d tommylau/jira
docker run --detach --publish 80:8080 --name jira -d xinmeng/atlassian-jira
docker exec -it jira-dp /bin/bash
```

### MySQL

... where
some-mysql is the name you want to assign to your container,
my-secret-pw is the password to be set for the MySQL root user and tag is the tag specifying the MySQL version you want. See the list above for relevant tags.

```
  docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag

  docker run --name jira-mysql -e MYSQL_ROOT_PASSWORD=deep&net1 -d mysql:5.6

  docker run --name some-app --link some-mysql:mysql -d application-that-uses-mysql
```
