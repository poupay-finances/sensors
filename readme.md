# passo a passo para executar o simulador de sensores

## Crie um ambiente virtual

```
python -m venv venv
    
// windows
./venv/scrips/activate

//linux
./venv/bin/activate
```

## Instale as dependências do python

```

pip install -r requirements.txt

//ou

pip3 install -r requirements.txt

```

## Criar variáveis de ambiente para conexão no <b>iot hub</b>

```
CONNECTION_STRING="string de conexão" 
DEVICE_ID="id do dispositivo"
```

## Execute a aplicação e valide se os dados estão sendo enviados para o azure
