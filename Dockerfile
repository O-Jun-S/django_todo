FROM python
RUN pip install django
RUN mkdir /work
WORKDIR /work
EXPOSE 8000
