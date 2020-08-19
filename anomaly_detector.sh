#!/bin/sh
docker build -t my-adapp . 
docker run -v $(pwd)/data:/data my-adapp python ./anomaly_detector.py $1 $2 $3
echo $1 $2 $3
