# 2019-11-pulumi

https://www.pulumi.com/docs/get-started/kubernetes/

```bash
$ minikube start
```

https://www.pulumi.com/docs/get-started/kubernetes/modify-program/

```
$ kubectl get pod
NAME                              READY   STATUS    RESTARTS   AGE
nginx-yhw7bmw4-86c57db685-zskz9   1/1     Running   0          30m

$ kubectl get svc
NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP        38m
nginx-n9r7q192   NodePort    10.106.251.248   <none>        80:30000/TCP   19s

$ curl $(minikube ip):30000
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```
