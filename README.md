Release Instructions for gpst_uicontainer-202.zip
	1.	Update Build Configuration:
	•	Add the config folder to the dist directory.
	•	Make necessary changes only in the buildinfo.json file.
	2.	Download and Unzip Artifact:
	•	Download gpst_uicontainer-202.zip from the Nexus repository:
Download Link
	•	Unzip the .zip file to extract the contents.
	3.	Copy to Production Server:
	•	Copy the extracted folder to:
/apps/ccar_apps/apache-tomcat-9.0.82/webapps/gpst
	•	On the production server, back up the existing dist folder.
	4.	Handle Config Folder:
	•	In the previous dist folder, locate the config folder.
	•	Copy the config folder and paste it into the newly added dist folder.
	5.	Update buildinfo.json:
	•	Open the buildinfo.json file located inside the config folder.
	•	Update the following fields:
	•	"DeploymentDate": Set it to the current date.
	•	"HostName": Set it to "Production".
	6.	Start the Service:
	•	Navigate to the deployment directory and run the following command:
./bin/RunScript.sh start
