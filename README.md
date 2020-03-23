# pluss_worker
sync products

----- Up service with ------
docker build -t pluss_worker .
docker run --rm -p 5000:5000 -it pluss_worker /bin/bash

----- start sync from URL -----
url/cris