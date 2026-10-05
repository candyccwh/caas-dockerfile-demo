# caas-dockerfile-demo

用嚟測 Backstage「Create Container App」嘅 **Build from Dockerfile** 模式嘅最細示範 repo。
一個純 Python stdlib HTTP server（零依賴、build 秒完），**綁 `0.0.0.0:8080`**（平台硬要求）。

## 點測

1. Push 呢個 folder 上 GitHub（例如 `hk-ust/caas-dockerfile-demo` 或你自己帳戶下）
2. Backstage → Create → **Create Container App**，填：
   | 欄位 | 值 |
   |---|---|
   | Target cluster | akslocal5 |
   | Container name | `df-demo`（例如） |
   | Public hostname | 可留空（internal-only），或者一個已註冊嘅名 |
   | How is the image provided? | **Build from Dockerfile** |
   | Source repo | `hk-ust/caas-dockerfile-demo`（owner/name 格式） |
   | Dockerfile path | `Dockerfile` |
   | Container port | `8080` |
   | Database | no（純示範） |
3. Submit → workflow 會 clone 呢個 repo、`docker build`、推去 `ACR/apps/<ns>-<app>:<run_number>`、照常部署

## 驗證

```bash
kubectl --context akslocal5-549357d4-admin@akslocal5-549357d4 -n df-demo get pods
kubectl --context akslocal5-549357d4-admin@akslocal5-549357d4 -n df-demo port-forward svc/df-demo 18080:80
curl http://localhost:18080/anything
```

有 hostname 嘅話直接 `curl https://<hostname>/`。

## 注意

- 私家 repo 嘅話，`container-as-service` repo 要有 secret **`REPO_TOKEN`**（classic PAT，對該 repo 有 read）— workflow 用佢嚟 clone
- 改完記得 push 先會 build 到新嘢（workflow clone 嘅係 main branch 最新 commit）
