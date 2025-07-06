# demo-build-with-ai
Este repositório foi criado para registrar as demonstrações do evento Build With AI 2025.

## Instalação do Ollama

### Instalação via cURL

Execute o comando abaixo para instalar o Ollama:

```sh
curl -fsSL https://ollama.com/install.sh | sh
```

Para rodar o modelo desejado (Gemma 3 Gaia PT-BR, por exemplo):

```sh
ollama run cnmoro/gemma3-gaia-ptbr-4b:q4_K_M
```

### Instalação via Docker

Execute o comando abaixo para subir o Ollama com Docker:

```sh
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Para rodar o modelo dentro do container:

```sh
docker exec -it -d ollama ollama run cnmoro/gemma3-gaia-ptbr-4b:q4_k_m
```

> **Observação:** Com o Docker, o serviço do Ollama ficará disponível em http://localhost:11434, permitindo o acesso à API e ao modelo por essa porta.
