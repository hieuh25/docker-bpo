import os
import time
import subprocess
import psycopg2


PATHS = {
    "admin": "/srv/tracker/roundup/roundup/scripts/roundup_admin.py",
    "server": "/srv/tracker/roundup/roundup/scripts/roundup_server.py",
    "dev": "/srv/tracker/python-dev",

    "flag_init": "/srv/tracker/.flags/init",
}


def check_pg_connection():
    while True:
        try:
            psycopg2.connect(
                "host='db' dbname='roundup' "
                "user='roundup' password='roundup'"
            )
        except psycopg2.OperationalError:
            print("---> Wait for DB")
            time.sleep(1)
            continue

        return True


if not os.path.exists("{flag_init}".format(**PATHS)):
    check_pg_connection()

    print("========>>>>> Start initialization")
    print("--------> Init admin")
    subprocess.call(
        "python {admin} -i {dev} init admin".format(**PATHS).split()
    )

    print("--------> Seed users data to DB")
    subprocess.call("python /srv/tracker/bin/createusers.py".split())

    # TODO: above doesn't exit in case of exception yet
    print("--------> Create flag")
    subprocess.call("touch {flag_init}".format(**PATHS).split())


check_pg_connection()

print("========>>>>> Start roundup server")
subprocess.call(
    "python {server} -n 0.0.0.0 -p 9999 "
    "python-dev={dev}".format(**PATHS).split()
)
