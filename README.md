#### In window
1. docker compose 설치 [docker desktop](https://docs.docker.com/desktop/install/windows-install/)  
1-1. WSL 2 error → [해결방법](https://suzxc2468.tistory.com/211)
2. docker-compose.yml 작성

```bash
sh Django-web/build.sh
docker-compose up -d #컨테이너 백그라운드로 띄우기
docker-compose logs -f web #컨테이너 로그 계속 읽기
docker-compose down
```