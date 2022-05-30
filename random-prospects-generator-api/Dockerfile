FROM python:3.7.3-alpine3.10
RUN apk --update add git gcc build-base freetype-dev libpng-dev openblas-dev openssh

WORKDIR /app
COPY controllers controllers
COPY dtos dtos
COPY routes routes
COPY services services
COPY app_environment.py app_environment.py
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN python3 -m pip install -U pip wheel setuptools
RUN pip3 install -r requirements.txt
ENV PORT 5000
EXPOSE ${PORT}
CMD ["python3", "app.py"]