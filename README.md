
## <b> CPEit - Common Platform Enumeration Inventory Tools - 2023 CSI Project</b>


CPEit consists of two components:

An Agent that gathers information on the software installed on a machine from multiple system sources, queries the NVD API using nvdlib to get all protential CPEs, selects both version specific and non-version specific CPEs depending on availability for each installed product using a distance vector, and then queries again to produce CVEs for each version-specific CPE found.
  
  *An ELK stack (UNDER DEVELOPMENT) configured for taking the JSON data generated by the Agent and fuzzy string-matching NIST's Official CPE Dictionary for it, allowing an administrator to quickly build an inventory of CPEs for all installed software on their environment, and keep it up to date automatically by setting the Agent to run on intervals and Elastic to generate alerts.

### <b>How To Use The Agent (For End-Users, Students, Educators, Individual Machines)</b>

1. [Obtain an API Key from NVD](https://nvd.nist.gov/developers/request-an-api-key) (Note: You don't need an API Key for using only the inventory builder functionality of this tool which will just gather information about your installed software, however for building an NVD inventory with all CPE and CPE of that software the key is required.) 

2. Paste the API key into line 14 of NVD_API_CPE.py 

3. Paste the API key into line 19 of NVD_API_CVE2.py

4. Run Launcher.bat to launch the graphical user interface. 

5. Click "Build Inventory" to gather the software information and display it in the GUI.

6. Click "Build NVD Report" to gather CPE strings and known vulnerabilities for the software.

7. Click on a link in the CPE or CVE rows to be taken to the NVD webpage for that product or vulnerability!

8. Click "Display NVD Report" at any time to go back to the report.

If you wish to export the data, Got-Combined.JSON has all of the data up to step 6, and Cleaned.JSON has all of the data up to step 8 (with CPE and CVE). There is a script called senddata.py that is configured to send the data to a running pipeline pre-configured in the ELK stack on port 5000, you will need to add your own address.

You could also deploy this agent over a network and run it using the BUILD_INVENTORY.py and BUILD_NVD_INVENTORY.py scripts. A headless solution for this feature will be added shortly!

  
### <b>How To Install the ELK Stack (For Admins, Engineers, Enterprise)</b>

1. Run the self-installer that will install Elasticsearch, Logstash, and Kibana with the CPEit configurations.

<code>sudo bash cpeit-elk/Install.sh </code>

2. Start logstash with:

<code>/usr/share/logstash/bin/logstash -f /usr/share/logstash/logstash.conf --path.settings /etc/logstash</code>

3. Note the password generated from running:

 <code>/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic</code>
 
4. Copy and paste the password into the password fields in /usr/share/logstash/logstash.conf (lines 40, 85, and 115)
 
5. Note the enrollment token generated from the command below:
 
 <code>/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana</code>
 
 6. Navigate to http://127.0.0.1:5601 and paste this token in.
 
 7. Run the command below for the Kibana verification code and paste it back into the browser:
 
<code>sudo /usr/share/kibana/bin/kibana-verification-code</code>

8. Now all three components of the stack should be working and connected to each other and ingesting the default path set in logstash.conf. By default it is:
/home/kali/Desktop/testdata.ndjson

[testdata.ndjson](https://github.com/RaXx00n/cpeit/blob/main/cpeit-elk/testdata.ndjson) has been included for testing!

9. To install the CPEit data view (under development), [follow these instructions](https://www.elastic.co/guide/en/kibana/current/managing-saved-objects.html) to import SavedObjectsExport.ndjson

10. In order to ingest your own data, you will need to configure senddata.py in the agent's files to one of the Logstash pipelines.

By default the pipeline inputs are: 

path => "/home/kali/Desktop/official_cpe_dictionary_v2.3.xml"

  ^ Download the CPE Dictionary from the NVD website and place it here to ingest the CPE dictionary for faster, offline searching using Elasticsearch. This can take some time to build as there will be over one million records.

path => "/home/kali/Desktop/testdata.ndjson"

  ^ This is the data including for testing.

port => 5000

  ^ This is where to point your senddata.py or other scripts to for ingesting Got-Combined.json
