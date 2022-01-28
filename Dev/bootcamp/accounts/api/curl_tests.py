
## test if the token works through the terminal
# curl -X POST -d "email=myXbox@bigmir.net&password=Passw0rd20022016_" http://127.0.0.1:8000/api/users/auth/token/

## obtained token
# token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Im15WGJveEBiaWdtaXIubmV0IiwiZXhwIjoxNjQzMzE0MTAwLCJlbWFpbCI6Im15WGJveEBiaWdtaXIubmV0In0.P_BWhZeWhrLo9VNh_9LkhuiXEQJTTGpryGS3_GH5ms8"

## anothe way of get token
# curl -X POST -H "Content-Type: application/json" -d '{"email":"myXbox@bigmir.net","password":"Passw0rd20022016_"}' http://127.0.0.1:8000/api/users/auth/token/

## get the resource with token
# curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Im15WGJveEBiaWdtaXIubmV0IiwiZXhwIjoxNjQzMzE0MTAwLCJlbWFpbCI6Im15WGJveEBiaWdtaXIubmV0In0.P_BWhZeWhrLo9VNh_9LkhuiXEQJTTGpryGS3_GH5ms8" http://127.0.0.1:8000/api/products/list/

## verify token
# $ curl -X POST -H "Content-Type: application/json" -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6Im15WGJveEBiaWdtaXIubmV0IiwiZXhwIjoxNjQzMzE0MTAwLCJlbWFpbCI6Im15WGJveEBiaWdtaXIubmV0In0.P_BWhZeWhrLo9VNh_9LkhuiXEQJTTGpryGS3_GH5ms8"}' http://localhost:8000/api-token-verify/


