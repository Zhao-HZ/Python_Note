<body>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
</body>

# TCP Client
## 实例代码 (见TCP_Client.py)
## 步骤
```mermaid
flowchart
    A[创建TCP socket]--->B[链接服务器]
    B--->C[发送数据或者接收数据]
    C--->D[关闭socket]
```
# TCP Server
## 实例代码 (见TCP_Server.py)
## 步骤
```mermaid
flowchart
    A[创建一个socket]--->B[bind绑定IP和port]
    B--->C[listen使socket变为可以被动链接]
    C--->D[accept等待客户端的链接]
    D--->E[recv/send接受发送数据]
```
## 生活中的电话机
## 如果想让别人能打通我们的电话，需要做以下几个事情
### 1. 买个手机
### 2. 插上电话卡
### 3. 设计手机为正常接听状态
### 4. 静静的等待别人拨打