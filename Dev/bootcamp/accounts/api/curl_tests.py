
## test if the token works through the terminal
# curl -X POST -d "email=myXbox@bigmir.net&password=Passw0rd20022016_" http://127.0.0.1:8000/api/users/auth/token/

# obtained token
# token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Im15WGJveEBiaWdtaXIubmV0IiwiZXhwIjoxNjQzMzE0MTAwLCJlbWFpbCI6Im15WGJveEBiaWdtaXIubmV0In0.P_BWhZeWhrLo9VNh_9LkhuiXEQJTTGpryGS3_GH5ms8"

## anothe way of get token
# curl -X POST -H "Content-Type: application/json" -d '{"email":"myXbox@bigmir.net","password":"Passw0rd20022016_"}' http://127.0.0.1:8000/api/users/auth/token/

## get the resource with token
# curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Im15WGJveEBiaWdtaXIubmV0IiwiZXhwIjoxNjQzMzE0MTAwLCJlbWFpbCI6Im15WGJveEBiaWdtaXIubmV0In0.P_BWhZeWhrLo9VNh_9LkhuiXEQJTTGpryGS3_GH5ms8" http://127.0.0.1:8000/api/products/list/

## verify token
# $ curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Im15WGJveEBiaWdtaXIubmV0IiwiZXhwIjoxNjQzMzE0MTAwLCJlbWFpbCI6Im15WGJveEBiaWdtaXIubmV0In0.P_BWhZeWhrLo9VNh_9LkhuiXEQJTTGpryGS3_GH5ms8"}' http://localhost:8000/api-token-verify/


### *** test GET commands *** ###
## curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8000/api/products/product/1
## curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8000/api/products/list/

# without "Content-Type"
## curl -X GET http://127.0.0.1:8000/api/products/list/ --


### *** POST commands *** ###
# authentication
# curl -X POST -d "email=andriyproniyk@gmail.com&password=Passw0rd20022016_" http://127.0.0.1:8000/api/users/user/sighn-in/  --> {"username":null,"email":"andriyproniyk@gmail.com","token":"946a4db38c564e8a851a869fc64bb3a8ba182b7a"}

# create: if serializer doesn't need authentication 
# curl -X POST -H "Content-Type: application/json" -d '{"title":"Test Post product","content":"bla bla bla","price":"999"}' http://127.0.0.1:8000/api/products/product/create/

## authtoken ##
# create product with authorization header through & auth_token
# curl -X POST -H "Authorization: Token "946a4db38c564e8a851a869fc64bb3a8ba182b7a"" -H "Content-Type: application/json" -d '{"title":"Some title","content":"Some content", "price":"Some price"}' http://127.0.0.1:8000/api/products/product/create/

# curl -X POST -d "username=andriyproniyk@gmail.com&password=Passw0rd20022016_" http://127.0.0.1:8000/api/users/authtoken-get/ - get new authtoken
# curl -H "Authorization: Token 946a4db38c564e8a851a869fc64bb3a8ba182b7a" http://127.0.0.1:8000/api/products/list - test authtoken (nothing appears)
# curl -X POST -d "auth_token=946a4db38c564e8a851a869fc64bb3a8ba182b7a" http://127.0.0.1:8000/api/users/authtoken/sighn-in/ - authorize
# curl -X POST -H "Authorization: Token "946a4db38c564e8a851a869fc64bb3a8ba182b7a"" -H "Content-Type: application/json" -d '{"auth_token":"946a4db38c564e8a851a869fc64bb3a8ba182b7a"}' http://127.0.0.1:8000/api/users/authtoken/sighn-in/ - authorize - works fine

## DELETE METHODS ##
## curl -X DELETE -H "Authorization: Token "946a4db38c564e8a851a869fc64bb3a8ba182b7a"" -H "Content-Type: application/json" -d '{"auth_token":"946a4db38c564e8a851a869fc64bb3a8ba182b7a"}' http://127.0.0.1:8000/api/products/25 --> works fine
## http://127.0.0.1:8000/api/products/product/25 - wont work as ProductViewSet is responsible for operating data but method DELETE is not allowed

