# Random Prospects Generator API
API geradora aleatória de prospects.

---

## Variáveis .env

| Variável | Descrição | Exemplo | 
|----------|-----------|---------|
| PORT | Número da porta da API | 5000 |
| ENVIRONMENT | Ambiente no qual a API está executando | development |
| PROSPECTS_ROUTE | Rota para listar os prospects | /prospects |

---

## Operações

### Listar Prospects
Por padrão, serão retornados 50 registros FAKE

**GET /prospects**
**Content-type/application/json**
**Exemplo de retorno:**

```json
[
  {
    "name": "Sra. Maria Fernanda Costela",
    "mail": "costelamaria-fernanda@hotmail.com",
    "phone_number": "61 3949-7553"
  },
  {
    "name": "Danilo Vieira",
    "mail": "cunhaluiz-fernando@hotmail.com",
    "phone_number": "+55 61 4916-6943"
  }
]
```

