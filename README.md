## Docker na aplicação FastAPI 

### Executar a aplicação com Docker Compose 

```bash
docker compose up --build
```

### Acessar a aplicação (Swagger)

A aplicação está disponível na porta 8000. Acesse o Swagger para explorar suas funcionalidades:

```
http://localhost:8000/docs 
```

### Parar e remover containers e volumes 

Execute este comando:

```bash
docker compose down -v
```

### Conclusão 

Este README.md te guia pelos passos básicos para utilizar o Docker compose na sua aplicação FastAPI. ️
