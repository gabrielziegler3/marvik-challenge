# Simple Flask API

## Usage

Build docker image from project dir
```
docker build . -t marvik
```

Run container with Flask app 
```
docker run -p 3000:3000 marvik
```

Test it running
```
curl -X POST "0.0.0.0:3000/predict?change_format=True"
```
and
```
curl -X POST "0.0.0.0:3000/predict?change_format=False"
```

