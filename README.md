<img src="https://skillicons.dev/icons?i=python,flask,docker" />

# ❓ What is `Static Delivery Data`

Static Delivery Data is a simple web service for media archiving in file system in a unique filename following the `uuid` standard, allowing also the request of those files.

# 🛠️ How to run

Clone the repository and using the docker CLI run the build process

```
git clone https://github.com/paolo-05/static-delivery-data/
cd static-delivery-data
docker compose up --build -d
```

# 🚧 Potential fixes

since we only check the file extension, harmful code could be sent in the upload requests, so in a production enviroment it's a thing to keep in mind.
