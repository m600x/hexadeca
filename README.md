# Hexadeca Pi cluster running Kubernetes

Kubernetes cluster using 16 Raspberry Pi 3B+ plus one as master. Trying to make it as seamless as possible while learning Ansible for automation.

End goal is to drive wife nuts with idiot project.

**Specs**

- 64 cores (22.4Ghz combined)
- 1TB of total storage (each node is equipped with a 64GB uSD)

**Pre-requis**
- Money to throw out your window
- Time to waste
- Ansible installed (on Mac it's `brew install ansible`)
  - If you have an error with permission blablabla, run:
    - `sudo mkdir /usr/local/Frameworks`
    - `sudo chown $(whoami):admin /usr/local/Frameworks`
    - Rerun brew
- All node have the latest Rapbian installed
- They have a static IP
- You have injected your own ssh keys

**Basic usage:**
- Clone the repo.
- By default, the repo/playbook assume that:
  - Nodes have a fixed ip as `192.168.0.XXX`
    - Master: `192.168.0.150`
    - Workers: `192.168.0.151 to 166`
- Edit the hosts files at `ansible/hosts` if that's not the case
- You private SSH keys is already in each node
- Go to `hexadeca/ansible`
- Run `ansible-playbook -i hosts 1-cluster-preparation.yml`

It will update/upgrade `Raspbian`, install a bunch of basic stuff, put `Docker` and `Kubeadm`.

**BOM**


|Item|Quantity|
|---|---|
|Raspberry Pi 3 B+|17
|Sandisk microSD Ultra 64GB|17
|Micro USB cable| 17
|Anker Powerport 10 ports 60w|2
|D-Link switch 16 ports GO-SW-16G|1
|Netgear switch 5 ports DGS-105|1
|Ethernet 50cm flat|18
|**Optional parts**|
|OLED 128x32 i2c|16
|Alphacool radiator 14x14mm full copper (pack of 10)|2
|Pimoroni Unicorn HAT|1
|**WAF**|
|Ikea Sammanhang|2
