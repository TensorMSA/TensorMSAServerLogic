echo "======================="
echo "set path, env variables"
echo "======================="

source ~/.bashrc
export PATH="/root/anaconda2/bin:$PATH"
source ~/anaconda2/bin/activate ~/anaconda2/
export PATH="/home/dev/java/bin:$PATH"
export SPARK_HOME=/home/dev/spark
export HADOOP_CONF_DIR=/home/dev/hadoop/conf
export M2_HOME=/usr/local/maven
export PATH=${M2_HOME}/bin:${PATH}

echo $SPARK_HOME
echo $HADOOP_CONF_DIR
echo $M2_HOME


echo "======================="
echo "step1 : stop spark apps"
echo "======================="

sudo /home/dev/spark/sbin/stop-master.sh
sudo /home/dev/spark/bin/stop-slave.sh

echo "======================="
echo "step2 : stop Livy"
echo "======================="

pkill -f "livy"

echo "======================="
echo "step3 : stop Django"
echo "======================="

cd /home/dev/TensorMSA/
pkill -f "python manage.py runserver"
