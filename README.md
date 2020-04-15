# Fairness Machine

## Introduction
A website survey platform for machine learning fairness.

## Build

### Prerequesite

- mac
- docker [(docker installation on mac)](https://hub.docker.com/editions/community/docker-ce-desktop-mac)

- windows (not verified yet)
- docker [(docker installation on windows)](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

- linux (not verified yet)
- docker [(docker installation on linux)](https://runnable.com/docker/install-docker-on-linux)

### More Environment Setups (if needed)

## Usage (now only for localhost)

1. Clone this repository.
2. Direct to the directory where you have cloned this repository.
3. (option1) Run with console:
```bash
docker-compose up --build
```
4. (option2) Run in backstage:
```bash
docker-compose up -d --build
```
5. Create superuser:
```bash
./django/createsuperuser.sh
```
Then you can follow the instruction to create your own superuser account.
6. [http://localhost:2000/](http://localhost:2000/)