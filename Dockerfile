FROM nickgryg/alpine-pandas:3.9

FROM sconecuratedimages/public-apps:python-3.7.3-alpine3.10-scone3.0

### install python3 dependencies you need
#RUN SCONE_MODE=sim pip3 install pyfiglet

#ADD requirements.txt /
#RUN pip3 install -r /requirements.txt

COPY ./src /app

###  protect file system with Scone
COPY ./protect-fs.sh ./Dockerfile /build/
RUN sh /build/protect-fs.sh /app

ENTRYPOINT ["python", "/app/app.py"]
