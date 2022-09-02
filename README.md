# Docker_P_New

to add files== git add . 
or
git add file1 file2

for status=== git status

for commit== git commit -m "messgae"

for push== git push origin main

Docker
Image build==  docker build -t imagemame:tag .

docker run -p 5000:5000 -e PORT=5000 <image_id>

to check ruuning container == docker ps

to stop docker===  docker stop container_id

For deployment==

1)create a folder .github
2) inside .github create another folder workflows
3) Inside workflow create a main.yaml file
4) copy paste yaml code
5) push changes to github

Inside github:
1) check actions-- there we can find build not completed
2) need to pass heroku info to githb for making container
3) Go to settings> Secrets>Actions> Provide heroku email,api key and app name
4) Go to actions> click on failed job> Rerun all jobs
5) Check Heroku Log
6)Succesfull Deployment





