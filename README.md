# OpenFalconZookeeperMonitor
ZookeeprMonitor部署

1 目录解压到/path/to/ZookeeprMonitor

2 配置Zookeeper实例信息,/path/to/ZookeeprMonitor/conf/zookeeper.conf 每行记录一个实例: ip,port

3 配置完成后可以cd bin,使用python *进行测试

4 配置crontab, 修改conf/zookeepermon_cron文件中zkmonitor安装path; cp zookeepermon_cron /etc/cron.d/

5 几分钟后，可从open-falcon的dashboard中查看Zookeeper metric

6 endpoint默认是ip
