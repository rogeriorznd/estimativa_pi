# Estimador de π usando Métodos Numéricos

Este projeto estima o valor de π usando o método histórico de Arquimedes, dividindo um círculo em triângulos inscritos.

## Método Matemático

Um polígono regular de `n` lados inscrito em um círculo de raio `R = 0.5` (diâmetro = 1):
- Cada lado do polígono tem comprimento: `lado = 2 × R × sin(π/n)`
- Perímetro do polígono: `perímetro = n × lado`
- π estimado: `π ≈ perímetro` (já que circunferência = π × diâmetro)

## Como executar

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar o programa
python estimador_pi.py
