配置新网站
================

## 需要的包：

* nginx
* Python 3.6
* virtualenv + pip
* Git

## Nginx虚拟主机

* 参考nginx.template.conf
* 修改SITENAME

## Systemd服务

* 参考gunicorn-systemd.template.service
* 修改SITENAME

## 文件夹结构

/home/username

----sites

--------SITENAME

-----------database

-----------source

-----------static

-----------virtualenv