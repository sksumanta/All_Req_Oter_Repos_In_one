#Simple Python Helloworld app using docker

Build the image using the following command

	docker build -t pythonapp:v1 .

Run the Docker container using the command shown below.

	docker run -it -p 80:5000 --name myapp pythonapp:v1

The application will be accessible at

http://<host_ip>:80

