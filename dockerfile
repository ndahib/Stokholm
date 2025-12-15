FROM alpine:latest

RUN apk add --no-cache bash python3 py3-pip

WORKDIR /app
COPY makefile .
COPY requirements.txt .

RUN python3 -m venv /opt/venv \
&& /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY src ./src
ENV PATH="/opt/venv/bin:$PATH"


EXPOSE 3000

CMD ["bash"]