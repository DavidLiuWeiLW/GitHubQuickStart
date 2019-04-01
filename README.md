# GitHubQuickStart
GitHub入门教程

1. 检查SSH Service是否有启动
2. 在默认目录（C:\Users\David）下检查是否有生成SSH Key
3. 如果没有，则生成新的SSH Key：ssh-keygen -t rsa -C "你自己注册GitHub的邮箱" 
4. 将.ssh目录下的id_rsa.pub文件里面的内容复制到GitHub中的SSH中
5. 把SSH Key添加到SSH中：ssh-add ~/.ssh/id_rsa
6. 测试SSH连接到GitHub：ssh -T git@github.com，显示Hi UserName! You've successfully authenticated, but GitHub does not provide shell access.则为成功连接
7. git config --global user.name "username"
8. git config --global user.email "github email"
9. git add .
10. git commit -m ""
11. git push