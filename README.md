# E2E_CV_Class_ChickenDisease
Build a "Chicken Disease Classifier"  using  CNNs, TensorFlow, Flask, Docker, GitHub Actions, AWS ECR EC2



---------------------------
## Main Workflow sequence
--------------------------
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py


-----------------------------
### Project Building steps:
----------------------------

Clone the repository

```bash
https://github.com/MohamedEmam82/E2E_CV_Class_ChickenDisease
```
### STEP 01
------------
- Create & activate a conda environment after opening the repository
```bash
conda create -n mlops python=3.8 -y
conda activate mlops
```


### STEP 02
------------
- install the requirements
```bash
pip install -r requirements.txt
```

```bash
python app.py
```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.
==========================================================================================================================
## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### 3. Create ECR repo to store/save docker image and get it's URI
    - Save the URI: 971422717366.dkr.ecr.us-east-1.amazonaws.com/winequality_repo

==========================================================================================================================	
### 4. Create EC2 machine (Ubuntu) 
## Open EC2 and Install docker in EC2 Machine:

#-- Run the following bash scripts on the EC2 terminal:
# Optional scripts	
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
```
# ---------------------------------------- #

# Required scripts
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```
	✅ curl
	A command-line tool for transferring data to or from a server, using protocols like HTTP, HTTPS, FTP, etc.

	✅ -f (fail silently)
	If the HTTP request fails (e.g. 404 Not Found or 500 Server Error), curl will not output the error HTML—it will instead exit with a nonzero status code. This helps scripts fail early if the download doesn’t succeed.

	✅ -s (silent)
	Suppresses progress bars and other non-error output, making the command quieter.

	✅ -S (show errors)
	When used with -s, this ensures that if there is an error, it still prints the error message instead of being completely silent. So errors are visible, but normal progress output is hidden.

	✅ -L (follow redirects)
	If the server responds with a redirect (HTTP 3xx), curl will automatically follow it to the new location.

	✅ https://get.docker.com
	The URL from which you’re downloading the script. In this case, it’s Docker’s official convenience script for installing Docker on your system.

	✅ -o get-docker.sh
	- o (Output to file instead of stdout.)
	Tells curl to save the downloaded file to a local file called 'get-docker.sh' instead of printing it to the terminal.
	Makes curl behave like a file downloader rather than just a text fetcher.
# ---------------------------------------- #

```bash
sudo sh get-docker.sh
```
# ---------------------------------------- #

```bash
sudo usermod -aG docker ubuntu
```
	✅ sudo
	Runs the command with superuser (root) privileges. Modifying user groups requires administrative rights.

	✅ usermod
	A Linux command used to modify a user’s account information (like groups, shell, home directory, etc.).

	✅ -aG
	-a = append → Add the user to the new group(s) without removing them from any other groups.
	-G = group list → Specifies the group(s) you’re adding the user to.
	Important: If you use -G without -a, it replaces the user’s group memberships with the specified groups, which can lock them out of other groups. So -a is crucial here.

	✅ docker
	The name of the group to which you’re adding the user. In this case, the docker group.
	Members of the docker group can run Docker commands without needing to type sudo every time.

	✅ ubuntu
	The name of the user account you’re modifying. Here, it’s ubuntu.

	- Putting it all together
		Adds the user "ubuntu" to the "docker" group.
		Lets the ubuntu user run Docker commands without needing sudo.
		Must be run as root (hence the sudo).

	- Important note:
		After running this command, the user should log out and log back in for the group membership changes to take effect in their shell session. Alternatively, you could run the below script to switch the current shell to the new group without logging out:
		```bash
		newgrp docker
		```
# ---------------------------------------- #
```bash
newgrp docker
```
	✅ newgrp
	A command that launches a new shell with a different primary group ID. It effectively changes your current shell session’s group context.

	✅ docker
	The name of the group you want to switch to.

	Why would you use newgrp?
	When you add your user to a new group (like docker), the group membership usually doesn’t take effect until you:
	- log out and log back in
	- or start a new session (e.g. new SSH connection)

	Instead of logging out, you can run the above script, this starts a new shell in which your primary group is now "docker". Any group permissions (like accessing the Docker socket) are immediately available in that shell.
# ---------------------------------------- #

```bash
docker --version
```
	- check if docker is installed
==========================================================================================================================	
# 6. Configure EC2 as self-hosted runner:

	- connecting aws ECR with github
	- whenever commit changes to github repo, will automatically push it to aws cloud/ECR
		1- go to github account
		2- access the concerned project repo
		3- click the tabs as following:
			setting > actions > runner > new self hosted runner > choose os 
		4- now come to Download section, and then run command one by one on aws EC2 terminal

==========================================================================================================================
# 7. Setup github secrets for aws:
