#!/usr/bin/env python3
import os
import logging
import subprocess

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

def check_docker_installation():
    logging.info("Check docker and docker-compose versions")
    docker_version_result = os.system("docker -v")
    docker_compose_version_result = os.system("docker-compose -v")

    if docker_version_result and docker_compose_version_result:
        exit("Docker or Docker-compose was not found. Try to install it with https://www.docker.com")

def run_docker_compose():
    logging.info("Run docker-compose")
    run_script(cmd=["docker-compose", "up", "-d"], wait=True)

def run_script(cmd: list, wait: bool) -> None:
    logging.info("Run %s", ' '.join(cmd))
    script_process = subprocess.Popen(' '.join(cmd), stdout=subprocess.PIPE, shell=True)

    if wait:
        script_process.wait()

        if script_process.returncode != 0:
            exit(script_process.returncode)

def stop_docker_compose():
    os.system("docker compose down")


def main():
    setup_logger()
    check_docker_installation()
    run_docker_compose()


if __name__ == "__main__":

    main()