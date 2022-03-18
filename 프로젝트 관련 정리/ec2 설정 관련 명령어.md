## mobaxterm

### nginx



- nginx default 설정

```
sudo vi /etc/nginx/site-available/default/
```



- 현재 jar의 PID 확인

```
ps -ef | grep <jar-name>.jar
```



- Nginx 재시작

```
sudo service nginx restart
```



- PID 종료

```
kill -9 <PID>
```



- 백그라운드 실행 명령어

```
nohup java -jar build/libs/rikey-0.0.1-SNAPSHOT.jar --server.servlet.context-path=/api &
```

