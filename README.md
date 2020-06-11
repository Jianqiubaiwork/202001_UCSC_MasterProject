# Fairness Machine

Last updated on 06/11/2020.

A web platform serving surveys for investigating machine learning fairness.


# Prerequisite

- Python >= 3.7
- Django2
- Linux 

# Build

## On AWS Lightsail

- Go through AWS lightsail tutorial

I used AWS lightsail to serve this website ([see the tutorial here](https://aws.amazon.com/getting-started/hands-on/deploy-python-application/)).

- Clone this repo
```bash
export PROJECT_ROOT=~/apps/django/django_projects/Project
git remote add ml https://github.com/Jianqiubaiwork/202001_UCSC_MasterProject.git
git fetch
git checkout aws-dev
```

- Install virtual environment
```bash
cd $PROJECT_ROOT
python3 -m venv ml-env
source ml-env/bin/activate
pip install -U pip
pip install -r requirements.txt
```

- Make migrations
```bash
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

- Restart apache
```bash
sudo /opt/bitnami/ctlscript.sh restart apache
```

# Usage

Please go through my report [here](Fairness_Machine.pdf).
