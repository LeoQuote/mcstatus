import subprocess
import logging
import traceback

def check_server(workdir):
    check_command = ["./minecraft", "status"]
    try:
        status = subprocess.run(check_command, cwd=workdir, stdout=subprocess.PIPE)
    except FileNotFoundError:
        server_status = 'unknown'
        logging.error('File not found: {}'.format(workdir))
        logging.error(traceback.format_exc())
        return server_status
    logging.info(status.stdout)
    # server_status = 'not ok'
    if 'is running' in status.stdout:
        server_status = 'ok'
    else:
        server_status = 'not ok'
    return server_status


def restart_server(workdir):
    return 'ok'