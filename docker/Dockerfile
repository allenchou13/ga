FROM python

ADD ./requirements.txt /app/
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /app/requirements.txt

ADD ./json/* /app/json/
ADD ./run_web.py /app/
ADD ./show.html /app/

WORKDIR /app


EXPOSE 8000

CMD python3 run_web.py
