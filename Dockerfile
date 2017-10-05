FROM python:3.6
COPY apiDamificados/requirements.txt /apiDamificados/requirements.txt
RUN pip install -r /apiDamificados/requirements.txt  
WORKDIR /apiDamificados
COPY apiDamificados /apiDamificados
CMD gunicorn --bind 0.0.0.0:8000 apiDamificados.wsgi:application