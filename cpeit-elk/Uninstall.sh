sudo apt remove elasticsearch -y
sudo apt purge elasticsearch -y 
sudo apt remove logstash -y
sudo apt purge logstash -y
sudo apt remove kibana -y
sudo apt purge kibana -y

sudo echo "

Cleaning up configuration directories left over by the package manager...

"


sudo rm -v -R /usr/share/elasticsearch
sudo rm -v -R /var/lib/elasticsearch
sudo rm -v -R /etc/elasticsearch

sudo rm -v -R /usr/share/logstash
sudo rm -v -R /var/lib/logstash
sudo rm -v -R /etc/logstash

sudo rm -v -R /usr/share/kibana
sudo rm -v -R /etc/kibana


sudo echo "

Uninstallation of the CPEit ELK stack complete, thank you for trying our tool!

"
