FROM centos
WORKDIR /project
ADD . /project
RUN yum install epel-release -y
RUN yum update -y
RUN yum install python3 -y
RUN yum install python3-pip  -y
RUN yum install mysql  -y
RUN yum install mysql-devel  -y
RUN yum install mysql-common  -y
RUN yum install mysql-libs  -y
RUN yum install gcc  -y
RUN yum install python3-devel  -y
RUN pip3 install -r requirements.txt
RUN export $(grep -v '^#' ./env/development.env | xargs)
CMD ["sh","entrypoint.sh"]
