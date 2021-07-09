# Webhook Elf

## Requirements

* Python >= 3.7

## Getting Started

### Setup venv (Optional)

```bash
python3 -m venv venv
source venv/Scripts/activate
```

### Install & Run

```bash
pip3 install -r requirements.txt
cp .env.example .env && vi .env\
python3 -m webhook_src
```

### For developers

```bash
pip3 install -r requirements-dev.txt
pre-commit install
pytest -svv
```

Check <http://127.0.0.1:8000/docs> for api documentation.
