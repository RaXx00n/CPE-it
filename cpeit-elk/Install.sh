sudo echo "

Installing Elasticsearch, Kibana, and Logstash...

"

sudo apt-get install elasticsearch kibana logstash

sudo chmod -R 777 /var/log/logstash /var/lib/logstash /usr/share/logstash/Gemfile /usr/share/logstash/Gemfile.lock /usr/share/kibana /usr/share/elasticsearch/ /etc/elasticsearch/ /var/lib/elasticsearch/ /var/log/elasticsearch/
  
sudo mkdir /usr/share/elasticsearch/data/

sudo cp log4j2.properties /usr/share/elasticsearch/
sudo cp elasticsearch.yml /usr/share/elasticsearch/
sudo cp elasticsearch /etc/default/

sudo chmod 777 /etc/default/elasticsearch

sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service
