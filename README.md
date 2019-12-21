# Bank-Q-A
## 基于银行业务的对话系统
### 主要思路：
- 基于布尔搜索找到相关问题
- 基本编辑距离定位用户具体业务需求，返回答案

### 项目展示
- 网址http://39.100.3.165:34000/#/
- 效果：
![image](https://github.com/RyanPeking/Bank-Q-A/blob/master/img/img.png)

### 本地运行步骤

注：项目数据因为敏感问题未开放

- 启动server.py

- 在dist文件夹里用如下命令：

  ```bash
  python -m http.server 8888 # 端口号
  ```

- 访问http://127.0.0.1:8888/#/
