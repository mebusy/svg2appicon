FROM python:3-alpine

MAINTAINER golden_slime@hotmail.com

#  to solv 'include/python3.9/Python.h:11:10: fatal error: limits.h: No such file or directory'
RUN apk add musl-dev gcc libffi-dev zlib-dev jpeg-dev cairo
RUN pip3 install cairosvg

COPY entry.sh /usr/bin/

COPY template_Contents.json /opt/res/
COPY svg2appicon.py         /opt/res/

# change work directory
WORKDIR /opt/svg2appicon

ENTRYPOINT ["entry.sh"]


