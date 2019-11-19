import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service

# Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
# running on minikube, and if so, create only services of type ClusterIP.
config = pulumi.Config()
is_minikube = config.require_bool("isMinikube")

app_name = "nginx"
app_labels = { "app": "nginx" }

deployment = Deployment(
    "nginx",
    spec={
        "selector": { "match_labels": app_labels },
        "replicas": 1,
        "template": {
            "metadata": { "labels": app_labels },
            "spec": { "containers": [{ "name": app_name, "image": "nginx" }] }
        }
    })

port = { "port": 80, "target_port": 80, "protocol": "TCP" }

if is_minikube:
    port.update(node_port=30000)

frontend = Service(
    app_name,
    metadata={
        "labels": deployment.spec["template"]["metadata"]["labels"],
    },
    spec={
        "type": "NodePort" if is_minikube else "LoadBalancer",
        "ports": [port],
        "selector": app_labels,
    })

# When "done", this will print the public IP.
if is_minikube:
    pulumi.export("ip", frontend.spec.apply(lambda v: v["cluster_ip"] if "cluster_ip" in v else None))
else:
    pulumi.export("ip", frontend.status.apply(lambda v: v["load_balancer"]["ingress"][0]["ip"] if "load_balancer" in v else None))
