import os
os.system("tput setaf 3")
print("\t\t###############################")
os.system("tput setaf 1")
print("\t\t\tHey welcome to Linux TUI ")
os.system("tput setaf 3")
print("\t\t###############################")
os.system("tput setaf 7")
while True:
	os.system("tput setaf 2")
	print("[Enter your work ~]# " , end=" ")
	os.system("tput setaf 7")
	work=input()
	
	if (("date" in work) and ( ("what" in work)  or ("find" in work))):
		os.system("date")
	elif(("list" in work)and(("file" in work)or("data" in work))):
		folder=input("Enter folder name:  ")
		os.system("ls " + folder)
	elif(("IP" in work)or("ip address" in work)):
		os.system(" ifconfig ")
	elif(("configure" in work)and(("webserver" in work)or("httpd" in work))and("aws" not in work)):
		os.system("yum install httpd -y")
		os.system("systemctl start httpd")
		os.system("systemctl enable httpd")
		filename=input("Enter code file name:  ")
		os.system(" cp -rf " + filename + " /var/www/html")


	elif (("configure" in work) and ("docker" in work)):
		os.system("yum install docker-ce  -y")
		os.system("systemctl start docker")
		os.system("systemctl enable docker")
	elif(("get" in work)and("information" in work )and("docker" in work)and(("container" in work)or("os" in work))):
		osname=input("OSName:  ")
		os.system("docker inspect " + osname)
	elif(("get" in work)and("information" in work)and("docker" in work)):
		os.system("docker info")
	elif(("rename" in work)or(("change" in work)and("name" in work))and("docker" in work)and(("container" in work)or("os" in work))):
		OSname=input("Current OSname/containerID:  ")
		NewName=input("New_Name:  ")
		os.system("docker rename " + OSname + " " + NewName)
	elif(("log" in work)and("docker" in work)and(("container" in work)or("os" in work))):
		container=input("OSname/containerID:  ")
		os.system("docker logs " + container)
	elif(("process" in work)or("running service" in work)and("docker" in work)and(("os" in work)or("container" in work))):
		container=input("OSname/containerID:  ")
		os.system("docker top " + container)
	elif(("live stream" in work)and("docker" in work)and(("os" in work)or("container" in work))):
		container=input("OSname/containerID:  ")
		os.system("docker stats " + container)

	elif(("create" in work)and("volume" in work)):
		volumename=input("VOlume_Name:  ")
		os.system("docker volume create " + volumename)
	elif(("remove" in work)and("volume" in work)):
		volumename=input("VOlume_Name:  ")
		os.system("docker volume rm  " + volumename)
	elif(("list" in work)and("volume" in work)):
		os.system("docker volume ls ")
	elif((("information" in work)and("volume" in work))or(("path" in work)and("volume" in work))):
		volumename=input("VOlume_Name:  ")
		os.system("docker volume inspect " + volumename)




	elif(("launch" in work) and ("new" in work) and ("without terminal" not in work) and ("backend" not in work) and("volume" in work)and (("container" in work) or ("os" in work) )):
		ImageName=input("choose image....")
		OsName=input("OsName:   ")
		volumename=input("Volume_Name:  ")
		path=input("Mount path of OS:  ")
		os.system("docker run -it --name " + OsName + " -v " + volumename +":" + path + " " + ImageName)
	elif(("launch" in work) and ("new" in work) and (("without terminal"  in work) or ("backend"  in work)) and("volume" in work)and (("container" in work) or ("os" in work) )):
		ImageName=input("choose image....")
		OsName=input("OsName:   ")
		volumename=input("Volume_Name:  ")
		path=input("Mount path of OS:  ")
		os.system("docker run -dit --name " + OsName + " -v " + volumename +":" + path + " " + ImageName)
	elif(("copy" in work)and(("base to docker" in work)or("local to docker" in work)or ("base os to docker" in work)or("local os to docker" in work))and(("os" in work)or("container" in work))):
		filename=input("source filepath:  ")
		OSName=input("OSName with destination path:  ")
		os.system("docker cp " + filename + " " +OSName)
	elif(("copy" in work)and(("docker os to base" in work)or("docker os to local" in work)or ("docker container to base" in work)or("docker container to local" in work))and(("os" in work)or("container" in work))):
		source=input("OSName with source filepath:  ")
		destination=input("destination path:  ")
		os.system("docker cp " + source + " " +destination)

	elif (("status" in work) and ("docker" in work) or ("what" in work)):
		os.system("systemctl status docker")

	elif(("download" in work) or ("pull" in work) and (("docker" in work) or ("image" in work))):
		ImageName=input("Enter image name....")
		os.system("docker pull " + ImageName)
	elif(("launch" in work) and ("new" in work) and ("without terminal" not in work) and ("backend" not in work) and (("container" in work) or ("os" in work) )):
		ImageName=input("choose image....")
		OsName=input("OsName:   ")
		os.system("docker run -it --name " + OsName + " " + ImageName)
	elif(("launch" in work) and ("new" in work)and(("without terminal" in work) or ("backend" in work)) and (("container" in work) or ("os" in work) )):
		ImageName=input("choose image....")
		OsName=input("OsName:   ")
		os.system("docker run -dit --name " + OsName + " " + ImageName)
	elif((("remove" in work) or ("terminate" in work))and("docker" in work) and (("os" in work) or ("container" in work))):
		OsName=input("OsName/ContainerID:  ")
		os.system("docker rm -f " + OsName)
	elif((("remove" in work) or ("terminate" in work)) and (("docker" in work) and  ("image" in work))):
		ImageName=input("ImageName/ImageID:  ")
		os.system("docker rmi -f " + ImageName)
	elif(("list" in work ) and ("docker" in work) and ("image" in work )):
		os.system("docker images")
	elif(("list" in work ) and ("running" not in work) and (("container" in work) or ("os" in work ))):
		os.system("docker ps -a")
	elif((("list" in work ) or ("running" in work)) and (("container" in work) or ("os" in work ))):
		os.system("docker ps ")

	elif(("restart" in work)and(("os" in work)or("container" in work))):
		ID=input("OSName/ContainerID:  ")
		os.system("docker restart " +ID)
	elif(("start" in work)and(("os" in work)or("container" in work))):
		ID=input("OSName/ContainerID:  ")
		os.system("docker start " +ID)
	elif(("stop" in work)and("os" in work)):
		ID=input("OSName/ContainerID:  ")
		os.system("docker stop " +ID)

	elif(("launch" in work)and ("bash terminal" in work) and("os" in work)):
		ID=input("OSName/ContainerID:  ")
		os.system("docker start " + ID)
		os.system("docker exec -it " + ID + " bash")

	elif(("launch" in work)and("os" in work)):
		ID=input("OSName/ContainerID:  ")
		os.system("docker start " + ID)
		os.system("docker attach " + ID)
	elif(("stop" in work) and(("container" in work)or("os" in work))):
		ID=input("OSName/ContainerID:  ")
		os.system("docker stop " + ID)


	elif(("create docker image" in work)and("using os" in work)):
		ID=input("OSName/ContainerID:  ")
		ImageName=input("ImageName:  ")
		os.system("docker commit " + ID + " " + ImageName)
	elif(("check" in work)and("ip" in work)and("os" in work)):
		OSName=input("OSName/ContainerID:  ")
		os.system('docker inspect --format "{{ .NetworkSettings.IPAddress }}" ' + OSName )

	elif(("save" in work)and("docker image" in work)and("file" in work)):
		ID=input("ImageName/ImageID:  ")
		filename=input("filename:  ")
		os.system("docker save " + ID + " -o " + filename)
	elif(("load" in work)and("docker image" in work)and("file" in work)):
		filename=input("filename:  ")
		os.system("docker  load -i " + filename)
	elif(("login" in work)and("docker" in work)):
		os.system("docker login")
	
	elif(("logout" in work)and("docker" in work)):
		os.system("docker logout")
	elif(("upload" in work)and("docker image" in work)and("docker hub" in work)):
		ID=input("ImageName:  ")
		tagname=input("tagname:  ")
		os.system("docker tag " + ID + " " + tagname + "/" + ID)
		os.system("docker push " + tagname + "/" + ID)




	elif((("configure" in work)and("Namenode" in work))or(("configure" in work)and("namenode" in work))):
		ip = os.system("ifconfig ")
		print("IP of namenode : {}".format(ip))
		os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
		dir = input("Enter directory name with path:  ")
		os.system("mkdir {}".format(dir)) 
		datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
		datafile.write(f'''<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
	<!-- Put site-specific property overrides in this file.-->


	<configuration>
	<property>
	<name>dfs.name.dir</name>
	<value>{dir}</value>
	</property> 
	</configuration>''')
		datafile1=open("/etc/hadoop/core-site.xml", 'w')
		datafile1.write(f'''<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
	<!-- Put site-specific property overrides in this file.-->


	<configuration>
	<property>
	<name>fs.default.name</name>
	<value>hdfs://0.0.0.0:9001</value>
	</property> 
	</configuration>''')

		os.system("systemctl stop firewalld")
		os.system("systemctl disable firewalld")
		os.system("hadoop namenode -format")
		os.system("hadoop-daemon.sh start namenode;jps")
		print("\n\n--------Namenode Started---------")


	elif((("configure" in work)and("Datanode" in work))or(("configure" in work)and("datanode" in work))):
		NN_IP = input("Enter Namenode IP:  ")
		os.system("rm /etc/hadoop/hdfs-site.xml;rm /etc/hadoop/core-site.xml")
		datadir = input("Enter directory name with path:  ")
		os.system("mkdir {}".format(datadir)) 
		datafile=open("/etc/hadoop/hdfs-site.xml", 'w')
		datafile.write(f'''<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
	<!-- Put site-specific property overrides in this file.-->


	<configuration>
	<property>
	<name>dfs.data.dir</name>
	<value>{datadir}</value>
	</property>
	</configuration>''')
		datafile1=open("/etc/hadoop/core-site.xml", 'w')
		datafile1.write(f'''<?xml version="1.0"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?> 
	<!-- Put site-specific property overrides in this file.-->


	<configuration>
	<property>
	<name>fs.default.name</name>
	<value>hdfs://{NN_IP}:9001</value>
	</property> 
	</configuration>''')

		os.system("systemctl stop firewalld")
		os.system("systemctl disable firewalld")
		os.system("rm -rf {datadir};mkdir {datadir}")
		os.system("hadoop-daemon.sh start datanode;jps")
		print("\n\n--------Datanode Started---------")
	elif(("copy" in work)and(("file" in work)or("folder" in work))):
		source=input("source file/folder:  ")
		dest=input("destination file/folder:  ")
		os.system(" cp -rf " + source + " " + dest )





	elif(("login" in work)and("aws cli" in work)):
		os.system("aws configure ")
	elif(("create" in work)and("aws" in work)and("key pair" in work)):
		print("Enter keyname :- ", end='')
		keyname=input()
		os.system("aws ec2  create-key-pair --key-name {}" .format(keyname))
	elif(("create" in work)and("aws" in work)and("security group" in work)):
		print("Enter group_name :- ", end='')
		group_name=input()
		print("Enter vpc_id :-", end='')
		vpc_id=input()
		print("Write description :-", end='')
		Description=input()
		os.system("aws ec2 create-security-group  --group-name {} --vpc-id {} --description {}" .format(group_name, vpc_id, Description))
	elif(("launch" in work)and("ec2-instance" in work)and("aws" in work)):
		print("Enter AMI ID to launch instance :- ", end='')
		ami=input()
		print("Enter Instance type :- ", end='')
		instance=input()
		print("Enter no of instance to launch :- ", end='')
		count=input()
		print("Enter Security group id :- ", end='')
		sg_id=input()
		print("Enter key to attach :- ", end='')
		key=input()
		os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id subnet-a613a0c0 --security-group-ids {} --key-name {}" .format(ami , instance , count , sg_id, key))
	elif(("create" in work)and("ebs" in work)and("aws" in work)):
		print("Enter the Availability Zone Name :- ", end='')
		Availability_Zone_id=input()
		print("Enter size of Volume :- ", end='')
		Size_of_Volume=input()
		os.system("aws ec2  create-volume --availability-zone {} --size {}" .format(Availability_Zone_id , Size_of_Volume))
	elif(("attach" in work)and(("ebs" in work)or("volume" in work))and("aws" in work)and("ec2-instance" in work)):
		print("Enter your ebs volume id :- ", end='')
		volume_id=input()
		print("Enter Instance id where you want to attach ebs :- ", end='')
		instance_id=input()
		os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf" .format(volume_id, instance_id))
	elif(("configure" in work)and(("webserver" in work)or("httpd" in work))and("aws" in work)):
		print("Enter the ip of Instance where you want to configure webserver :-" , end='')
		ip=input()
		print("Enter the key to connect instance :-", end='')
		key=input()
		os.system("ssh -l ec2-user {} -i {}.pem sudo yum install httpd -y" .format(ip , key))
		os.system("ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd" .format(ip , key))
		os.system("ssh -l ec2-user {} -i {}.pem sudo systemctl enable httpd" .format(ip , key))
	elif(("create" in work)and(("persistent storage" in work)or("permanent" in work))and("aws" in work)):
		print("Enter the ip to remote login :-", end='')
		ip=input()
		print("Enter the key name  :-", end='')
		key=input()
		os.system("ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/xvdf" .format(ip , key))
		print("Enter the partition name to format and mount  to  folder :-", end='')
		partition_name=input()
		print("Enter folder name where you want to mount  :-", end='')
		folder_name=input()
		os.system("ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{}"  .format(ip , key, partition_name))
		os.system("ssh -l ec2-user {} -i {}.pem sudo sudo mount /dev/{} {}" .format(ip , key, partition_name, folder_name))
	elif(("stop" in work)and("ec2-instance" in work)and("aws" in work)):
		print("Enter the instance id to stop :- ", end='')
		instance_id=input()
		os.system("aws ec2 stop-instances --instance-ids {}" .format(instance_id))
	elif(("start" in work)and("ec2-instance" in work)and("aws" in work)):
		print("Enter the instance id to start :- ", end='')
		instance_id=input()
		os.system("aws ec2 start-instances --instance-ids {}" .format(instance_id))
	elif(("terminate" in work)and("ec2-instance" in work)and("aws" in work)):
		print("Enter the instance id to terminate :- ", end='')
		instance_id=input()
		os.system("aws ec2 terminate-instances --instance-ids {}" .format(instance_id))
	elif(("create" in work)and("s3 bucket" in work)and("aws" in work)):
		print("Enter the unique name of bucket :-", end='')
		bucket_name=input()
		print("Enter the region name where you want to create s3 bucket :-", end='')
		region_name=input()
		os.system("aws s3 mb s3://{} --region {}" .format(bucket_name, region_name))
	elif(("delete" in work)and("s3 bucket" in work)and("aws" in work)):
		print("Enter the bucket name to delete :-", end='')
		bucket_name=input()
		os.system("aws s3 rb s3://{}" .format(bucket_name,))
	elif(("upload" in work)and("data" in work)and ("s3 bucket" in work)and("aws" in work)):
		print("Enter data source laction :- ", end='')
		source_location=input()
		print("Enter Bucket name where you want to copy files :- ", end='')
		bucket_name=input()
		print('''Press 1  : For public read
Press 2  : For public read write
Press 3  : For private''' )
		print("Enter permission for object :- ", end='')
        
		permission=input()
		if int(permission)==1:
			os.system("aws s3 cp {} s3://{} --acl public-read" .format(source_location, bucket_name, ))  
		elif int(permission)==2:
			os.system("aws s3 cp {} s3://{} --acl public-read-write" .format(source_location, bucket_name, ))
		elif int(permission)==3:
			os.system("aws s3 cp {} s3://{} --acl private" .format(source_location, bucket_name, ))
		else:
			print("not selected right option")    

	elif(("create" in work)and(("cloudfront" in work)or("web distribution" in work))and("aws" in work)):
		print("Enter S3 Bucket Name :- ", end='')
		s3_bucket_name=input()
		os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com" .format(s3_bucket_name))	
	elif(("show" in work)and("partition" in work)and("mount" in work)and("aws" in work)):
		print("Enter the ip of Instance  :-" , end='')
		ip=input()
		print("Enter the key to connect instance :-", end='')
		key=input()
		os.system("ssh -l ec2-user {} -i {}.pem sudo df -h".format(ip , key))
	elif(("show" in work)and("created" in work)and("partition" in work)and("aws" in work)):
		print("Enter the ip of Instance  :-" , end='')
		ip=input()
		print("Enter the key to connect instance :-", end='')
		key=input()
		os.system("ssh -l ec2-user {} -i {}.pem sudo lsblk".format(ip , key))




	elif (("exit" in work ) or ("quit" in work)):
		break
	else:
		print("cmd not found")
