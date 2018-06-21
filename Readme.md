Distributed load testing using kubernetes and locust
======================

The repository contains everything needed to run a distributed load testing environment in kubernetes using a locust master and locust slaves. 


## Table of contents
1. [Project structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Running](#running)
4. [Architecture](#architecture)

### Project structure

    .
    ├── .vscode                                 # launch.json and tasks.json needed to debug the tasks.py in vsc
    ├── docker-image                            # The shared docker image for locust masters and slaves
    │   ├── locust-tasks                        # Python source code
    |   |   ├── requirements.txt                # Python dependencies for tasks.py
    |   |   ├── tasks.py                        # Locust tasks
    |   ├── run.sh                              # Shell script to determine if the docker containers should be master or slave
    │   ├── Dockerfile                          # Dockerfile
    ├── loadtest-chart                          # Helm chart
    |   ├── templates                           # Helm templates
    |   |   ├── _helpers.tpl                    # Helm helpers
    |   |   ├── locust-master-deployment.yaml   # Kubernetes deployment configuration for locust master
    |   |   ├── locust-master-service.yaml      # Kubernetes service configuration for locust master
    |   |   ├── locust-slave-deployment.yaml    # Kubernetes deployment configuration for locust slaves
    |   ├── Chart.yaml                          # Chart definition
    |   ├── values.yaml                         # Chart definition
    └── ...
___

### Prerequisites

| Product            |              Version         |                           Link                          | 
| :------------------|:-----------------------------|:--------------------------------------------------------|
| Python             | 2.7.15                       | [Windows][Python-Windows], [MacOS][Python-macOS]        |
| Docker             | 18.03.0-ce (23751)           | [Windows][Docker-Windows], [MacOS][Docker-macOS]        |
| kubectl            | 2.0.0                        | [Windows][kubectl-Windows], [MacOS][kubectl-MacOS]      |
| Minikube           | 0.27.0                       | [Windows][Minikube], [MacOS][Minikube]                  |
| helm               | 2.9.1                        | [Windows][helm-Windows] [MacOS][helm-macOS]             |


### Running

#### tl;dr

Start minikube
```sh
minikube start
```

Set docker environment to minikube
```sh
eval $(minikube docker-env)
```

Initialize helm
```sh
helm init
```

Build docker image
```sh
docker build docker-image -t locust-tasks:latest
```

Install helm charts onto kubernetes cluster
```sh
helm install loadtest-chart --name locust
```

List services to find locust URL
```sh
minikube service list
```

#### Preparing the local kubernetes cluster
Start a local kubernetes cluster with minikube by running the following command `minikube start`

Confirm that everything is OK by running `minikube status` it should return something like:

```
minikube: Running
cluster: Running
kubectl: Correctly Configured: pointing to minikube-vm at 192.168.99.100
```

Now that we have minikube running we are going to want to point our docker environment to the one running on the cluster. Do this with the command `eval $(minikube docker-env)`. You can unset the environment at any time by running `eval $(docker-machine env --unset)`.

Confirm that the docker environment is correct by running `docker images`. You should see a list of related kubernetes images like k8s.gcr.io.

Now we're ready to install tiller onto our local kubernetes cluster. Tiller will make sure that we can use helm to install, update and delete our charts. The easiest way to do this is to simply run `helm init`.

#### Building the docker image
In the root of the repo, run `docker build docker-image -t locust-tasks:latest`

#### Installing the helm charts
Now that we have the docker image built and registered in the minikube docker registry. We can get our deployments and services for locust into our kubernetes cluster. Simply run `helm install loadtest-chart --name locust`.

#### Confirm the installation and access locust dashboard
To confirm that locust is running in our cluster. Run `minikube service list`. You should find locust-loadtest-chart-master with 3 URL's. Go to the first one and you should now see the locust load testing frontpage.

![locust][locust]


### Architecture

[Python-Windows]: https://www.python.org/downloads/windows/
[Python-MacOS]: https://www.python.org/downloads/mac-osx/
[Docker-Windows]: https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows
[Docker-MacOS]: https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows
[kubectl-Windows]: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-chocolatey-on-windows
[kubectl-MacOS]: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-with-homebrew-on-macos
[Minikube]: https://kubernetes.io/docs/tasks/tools/install-minikube/ 
[helm-Windows]: https://docs.helm.sh/using_helm/#from-chocolatey-windows
[helm-macOS]: https://docs.helm.sh/using_helm/#from-homebrew-macos

[locust]: images/locust.png