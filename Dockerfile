FROM python:3

RUN mkdir -p ~/data

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./anomaly_detector.py", "-d", "/data/input.json", "/data/output.json"]