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

Installing some filters for Logstash...

"
sudo cp logstash.conf /usr/share/logstash/logstash.conf
sudo chmod 777 /usr/share/logstash/logstash.conf

sudo bash /usr/share/logstash/bin/logstash-plugin install logstash-filter-fingerprint
sudo bash /usr/share/logstash/bin/logstash-plugin install logstash-filter-xml

mkdir /usr/share/kibana/config/
sudo cp kibana.yml /usr/share/kibana/config/

systemctl start kibana

sudo echo "

Importing Kibana visualizations...

"
sudo apt-get install npm
npm install -g @kbn/cli
kibana import CPEit.ndjson

sudo echo "

CPEit has been installed, please follow the instructions to authenticate Kibana with Elasticsearch...

1. Paste the password from the following command into /usr/share/logstash/logstash.conf
/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic


2. Paste the enrollment token from the following command into http://127.0.0.1:5601
/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana

3. Paste the Kibana verification code from the following command back into the webpage when asked:
sudo /usr/share/kibana/bin/kibana-verification-code

4. Begin logstash with: /usr/share/logstash/bin/logstash -f /usr/share/logstash/logstash.conf --path.settings /etc/logstash

5. Navigate to http://127.0.0.1:5601 to view your ingested data! Enjoy!

"
