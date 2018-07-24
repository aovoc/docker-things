# spark-cluster


## ssh
```
# service ssh start
```

## Spark Configuation ($SPARK_HOME/conf/)
```
# cp slave.template slave
slave01
slave02

# cp spark-env.sh.template spark-env.sh
export SPARK_WORKER_CORES=5  # for each node
```

## Start Cluster
```
On master node,
# ./sbin/start-master.sh

On slave node,
# ./sbin/start-slave.sh spark://spark-master:$SPARK_MASTER_PORT
```

## Run python script
```
# /opt/spark/spark/bin/spark-submit --master spark://spark-master:$SPARK_MASTER_PORT example_script.py
```

## References
* https://data-flair.training/blogs/install-apache-spark-multi-node-cluster/
* https://github.com/big-data-europe/docker-spark
* https://hub.docker.com/r/bde2020/spark-master/~/dockerfile/
* https://www.ibm.com/support/knowledgecenter/en/SSCTFE_1.1.0/com.ibm.azk.v1r1.azka100/topics/azkic_t_confignetwork.htm


