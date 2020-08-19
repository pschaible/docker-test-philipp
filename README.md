# docker-test-philipp

this programm demonstrates how to create a command line interface running command in docker.

start with ./anomaly_detector -t /data/input.json /data/output.json
-t : parameter for Trainin
/data/input.json : path to input datei
/data/output.json : path to output datei. Diese wird auch neu kreiert falls nicht existiert.

Die paramteter werden genau so übernommen falls nicht angegeben. (CMD in Dockerfile)
