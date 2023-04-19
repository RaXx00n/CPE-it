import subprocess


# Run the scripts to generate keywords, feed them through the API to get the CPE, select best CPE, feed those through the API and then clean up the data
subprocess.run(['python', 'get_keywords.py'])
subprocess.run(['python', 'NVD_API_CPE.py'])
subprocess.run(['python', 'match_cpe.py'])
subprocess.run(['python', 'NVD_API_CVE2.py'])
subprocess.run(['python', 'clean_data.py'])
subprocess.run(['python', 'html_report.py'])