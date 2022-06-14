# Service to get products from supplies
This service excecutin one time day

## how it Work

For up service in development:

1. Build image with: `docker build --no-cache -t pluss_worket .`
2. Create container: `docker run --rm -p 5000:5000 -it pluss_worker /bin/bash`
3. Into container run the command: `flask run --host=0.0.0.0`
4. Use url localhost:5000/sync/key  where _key_ is private for service

### Create and Activate virtual enviroment

1. Create enviroment: `viertualenc myenvname`
2. Activate enviroment: `source /bin/activate`
3. Install dependencies in project: `pip install -r requirements.txt`
4. Run server: `flask run --host:0.0.0.0`

**Notes**:
Those variables are necessaries for start server

export FLASK_DEBUG="True"
export FLASK_ENV=development
export FLASK_APP=main.py

### Note:

* Validate ports actives zombies: `lsof -i :5713` where 8713 is a port.
* Por use mode debbug in vscode you need config launch.json in .vscode with follow configuration:
`{
            "name": "Python: Flask attach",
            "type": "python",
            "request": "attach",
            "port": 5713,
            "host": "localhost"
        }`

after you can commnet the line `initialize_flask_server_debugger_if_needed()` in  main.py after run server and discomment the linea and all rigth, now debbuger with VsCode

* Is importan run the cronJob with:
 `flask crontab add`

Some utils commands are:
Remove cron: `flask crontab remove`
List cron: `flask crontab show`
[SRC flask-cron](https://pypi.org/project/flask-crontab/)




