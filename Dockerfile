FROM    centos:6.7
MAINTAINER  ibuler  <ibuler@qq.com>

COPY . /data/
WORKDIR /data

CMD ["/usr/bin/python", "check_domain.py"]
