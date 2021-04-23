# Service to get products from supplies
This service excecutin one time day

## how it Work

For up service in development:

1. Build image with: `docker build --no-cache -t pluss_worket .`
2. Create container: `docker run --rm -p 5000:5000 -it pluss_worker /bin/bash`
3. Into container run the command: `flask run --host=0.0.0.0`
4. Use url localhost:5000/sync/key  where _key_ is private for service
