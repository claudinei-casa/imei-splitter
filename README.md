# imei-splitter-v1.0.0

> Software para tratar e separar os IMEIS dos dispositivos produzidos pela fábrica e prontos para enviar para a Google.
> 

### Por onde começar?

Existem algumas dependências fundamentais necessárias para rodar o projeto, são elas:

- Python 3.9 +
- pip 20.0.2 +

### Como iniciar:

Antes de tudo e indicado criar um ambiente virtual Python, você pode usar virtualenv como no exemplo abaixo ou outros:

```bash
virtualenv -p /usr/bin/python3.9 venv
```

Primeiro você precisa instalar as dependências citadas anteriormente e as demais contidas em **dependencies.txt**:

```bash
pip install -r dependencies.txt
```

Já pode iniciar o imei-splitter usando um:

```bash
python main.py
```

Pronto agora você já pode gerar seus arquivos.

Como saída e gerado uma pasta relatórios onde é são armazenados todos os arquivos.csv.

As demais informações estão disponíveis no ‘software’ na página inicial.
