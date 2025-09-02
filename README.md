# Estimador de π usando Métodos Numéricos

Este projeto estima o valor de π usando o método histórico de Arquimedes, dividindo um círculo em triângulos inscritos.

## 📋 Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

## 🚀 Como executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/estimativa_pi.git
cd estimativa_pi
```

### 2. Crie e ative um ambiente virtual
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar o ambiente (Linux/Mac)
source venv/bin/activate

# Ativar o ambiente (Windows)
venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o programa
```bash
python estimativapi.py
```

## 📊 Método Matemático

Um polígono regular de `n` lados inscrito em um círculo de raio `R = 0.5` (diâmetro = 1):
- Cada lado do polígono tem comprimento: `lado = 2 × R × sin(π/n)`
- Perímetro do polígono: `perímetro = n × lado`
- π estimado: `π ≈ perímetro` (já que circunferência = π × diâmetro)

## 🎯 Resultados Esperados

O programa mostrará uma tabela com estimativas de π para:
- 3, 6, 12, 24, 48, 96, 192, 384 triângulos

E gerará automaticamente:
- Gráfico de convergência da estimativa de π
- Gráfico da evolução do erro absoluto
- Visualização do polígono inscrito (12 lados)

## 🔧 Estrutura do Projeto
```
estimador-pi/
├── estimador_pi.py    # Código principal
├── requirements.txt   # Dependências do Python
├── README.md          # Este arquivo
└── .gitignore         # Arquivos ignorados pelo Git
```

## 📦 Dependências

- `matplotlib >= 3.5.0` - Para geração de gráficos
- `numpy >= 1.21.0` - Para cálculos numéricos

## 💡 Comandos Úteis

```bash
# Ativar o ambiente virtual
source venv/bin/activate

# Desativar o ambiente virtual
deactivate

# Verificar dependências instaladas
pip list
```

## 🆘 Solução de Problemas

### Erro: "python3-venv not installed"
```bash
sudo apt update
sudo apt install python3-venv
```

### Erro: "ModuleNotFoundError"
```bash
# Ative o ambiente virtual e instale as dependências
source venv/bin/activate
pip install -r requirements.txt
```

---

## 👨‍💻 Autor

Rogerio - Atividade de métodos numéricos aplicados à geotecnia.

---
