# Excel Translator & Unprotector

Projeto Python para **remover proteção de planilhas Excel** e **traduzir seu conteúdo automaticamente** utilizando a **API Google Cloud Translate**.

---

## Requisitos

- Python 3.8+
- Conta no [Google Cloud](https://cloud.google.com/)
- Chave de API do serviço **Cloud Translation API v2**
- Excel instalado (necessário para uso do `xlwings`)

---

## Instalação

Instale as dependências:

```bash
pip install xlwings google-cloud-translate
```

---

## Configuração da API (key.json)

1. Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2. Ative o serviço **Cloud Translation API**.
3. Crie uma **Service Account**.
4. Gere e baixe a chave no formato JSON.
5. Renomeie para `key.json` e coloque na raiz do projeto.

O código já aponta para esse arquivo:

```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
```

---

## Uso

### 1. Remover proteção da planilha

Executa a cópia da planilha original para uma nova versão desprotegida.

```bash
python desblock.py
```

- Entrada: `input.xlsx`
- Saída: `copy.xlsx`

### 2. Traduzir o conteúdo da planilha

Traduz todas as células com texto da planilha desprotegida.

```bash
python app.py
```

- Entrada: `copy.xlsx`
- Saída: `output.xlsx`
- Padrão de idioma: de **Inglês** para **Português** (`en` → `pt`)

Para mudar os idiomas, edite o `app.py`:

```python
translate_sheet(input_file, output_file, src='pt', dest='en')
```

---

## Observações

- Apenas células com **texto não vazio** são traduzidas.
- A tradução é feita célula por célula.
- Um `sleep(0.1)` foi adicionado para evitar sobrecarga na API do Google.
- Planilhas muito grandes podem demorar — adapte para uso com batch se necessário.

---

## Estrutura do Projeto

```sh
📦 Excel-Translator/
├── 📁 scripts/
│   ├── desblock.py        # Remove proteção da planilha original
│   └── translator.py      # Traduz a planilha
├── 📁 sheets/
│   ├── input.xlsx         # Planilha original (Template)
│   ├── copy.xlsx          # Planilha desprotegida
│   └── output.xlsx        # Planilha traduzida
├── main.py                # Inicia os scripts
├── key.json               # Chave da API do Google (não versionar)
└── README.md
```
