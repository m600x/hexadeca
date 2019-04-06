# Kubernetes using Ansible

## Ansible

```
# Prepare all nodes including master with basic stuff
ansible-playbook -i hosts 1-cluster-preparation.yml

# Deploy Kubernetes on the master
ansible-playbook -i hosts 2-master-deployment.yml
```

## Manual procedure

Kubernetes installation

```
# Master ignition
sudo kubeadm init --token-ttl=0

# Copy join url format as:
kubeadm join 192.168.0.150:6443 --token (TOKEN) --discovery-token-ca-cert-hash sha256:(TOKEN)

# Run theses commands
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

#Install Weave-net
kubectl apply -f "https://cloud.weave.works/k8s/net?k8s-version=$(kubectl version | base64 | tr -d '\n')"

#Install MetalLB
kubectl apply -f https://raw.githubusercontent.com/google/metallb/v0.7.3/manifests/metallb.yaml

#Install Dashboard
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v1.10.1/src/deploy/alternative/kubernetes-dashboard-arm.yaml
```

## Infos

Deployments cheat sheet
```
#Create manual deployment
  kubectl create deployment (NAME) --image=(HUB_USER)/(HUB_IMAGE)
#Expose ports
  kubectl expose deployment (NAME) --port=(PORT) --type=LoadBalancer
#Retrieve deployments
  kubectl get deployments
#See deployment infos
  kubectl describe deployment (NAME)
#Edit the yaml
  kubectl edit deployment/(NAME)
#Scale the deployment
  kubectl scale deployment --replicas (NUMBER) (NAME)
#Remove deployment
  kubectl delete deployments/(NAME)
```

Services cheat sheet
```
kubectl create service nodeport (NAME) --tcp=80:80
kubectl get svc
kubectl delete services/(NAME)
```
