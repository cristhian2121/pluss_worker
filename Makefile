# start:
# 	docker run --rm -p 5000:5000
# 	watchman-make -p '**/*.py' -s 1 --run 'touch uwsgi-reload'
# stop:
# 	docker-compose down