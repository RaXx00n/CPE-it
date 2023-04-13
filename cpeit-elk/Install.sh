sudo echo "

Installing Elasticsearch, Kibana, and Logstash...

"


wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
sudo apt-get install apt-transport-https
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list



sudo apt update && sudo apt-get install elasticsearch kibana logstash

sudo chmod -R 777 /var/log/logstash /var/lib/logstash /usr/share/logstash/ /usr/share/kibana /usr/share/elasticsearch/ /etc/elasticsearch/ /var/lib/elasticsearch/ /var/log/elasticsearch/
  
sudo mkdir /usr/share/elasticsearch/data/

sudo cp log4j2.properties /usr/share/elasticsearch/
sudo cp elasticsearch.yml /usr/share/elasticsearch/
sudo cp elasticsearch /etc/default/

sudo chmod 777 /etc/default/elasticsearch

sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service

sudo echo "

Installing the Fingerprint filter for Logstash...

"

sudo bash /usr/share/logstash/bin/logstash-plugin install logstash-filter-fingerprint

sudo cp kibana.yml /usr/share/kibana/config/
