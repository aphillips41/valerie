CONTAINER_ID=$(docker ps -a |  awk '$NF == "valerie_mongo"' | awk '{printf $1}')


#stop mongo container
docker stop $CONTAINER_ID


#delete mongo container
docker rm $CONTAINER_ID


#spin up new mongo container
docker run -dit --name valerie_mongo --network aarxn_net -p 127.0.0.1:27017:27017 mongo:4.2.1



IMAGE_IDS=$(docker images |  awk '$1 == "valerie_pymongo"' | awk '{printf $3}')

#remove old pymongo_image
docker rmi $IMAGE_IDS

#recreate pymongo image
docker build -t valerie_pymongo .