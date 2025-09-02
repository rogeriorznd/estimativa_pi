#!/usr/bin/env python3
"""
Estimador de π usando o método de polígonos inscritos
Baseado no método de Arquimedes
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def estimar_pi(num_triangulos):
    """
    Estima π dividindo o círculo em triângulos isósceles
    e calculando o perímetro do polígono inscrito
    """
    if num_triangulos < 3:
        raise ValueError("Número de triângulos deve ser pelo menos 3")
    
    # Ângulo central de cada triângulo (em radianos)
    angulo_central = 2 * math.pi / num_triangulos
    
    # Comprimento do lado do polígono (corda)
    # Usando a fórmula: lado = 2 * R * sin(π/n)
    # Como R = 0.5 (diâmetro = 1), lado = sin(π/n)
    lado = math.sin(angulo_central / 2) * 2  # 2 * sin(θ/2)
    
    # Perímetro do polígono
    perimetro = num_triangulos * lado
    
    # π estimado = perímetro (já que diâmetro = 1)
    pi_estimado = perimetro
    
    return pi_estimado

def gerar_tabela_resultados():
    """Gera uma tabela com os resultados para diferentes números de triângulos"""
    # Sequência: 3, 6, 12, 24, 48, 96 triângulos
    num_triangulos_lista = [3, 6, 12, 24, 48, 96, 192, 384]
    
    print("=" * 50)
    print("ESTIMAÇÃO DE π POR POLÍGONOS INSCRITOS")
    print("=" * 50)
    print(f"{'Triângulos':<12} {'π Estimado':<15} {'Erro':<15} {'Erro Relativo %':<15}")
    print("-" * 50)
    
    resultados = []
    
    for n in num_triangulos_lista:
        pi_estimado = estimar_pi(n)
        erro = abs(pi_estimado - math.pi)
        erro_relativo = (erro / math.pi) * 100
        
        resultados.append({
            'triangulos': n,
            'pi_estimado': pi_estimado,
            'erro': erro,
            'erro_relativo': erro_relativo
        })
        
        print(f"{n:<12} {pi_estimado:<15.10f} {erro:<15.10f} {erro_relativo:<15.8f}")
    
    print("=" * 50)
    print(f"π Real: {math.pi:.10f}")
    print("=" * 50)
    
    return resultados

def plotar_grafico(resultados):
    """Gera gráficos mostrando a convergência para π"""
    triangulos = [r['triangulos'] for r in resultados]
    pi_estimados = [r['pi_estimado'] for r in resultados]
    erros = [r['erro'] for r in resultados]
    
    # Criar figura com subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Gráfico 1: Valores estimados de π
    ax1.plot(triangulos, pi_estimados, 'bo-', linewidth=2, markersize=6, label='π Estimado')
    ax1.axhline(y=math.pi, color='r', linestyle='--', linewidth=2, label='π Real')
    ax1.set_xscale('log')
    ax1.set_xlabel('Número de Triângulos')
    ax1.set_ylabel('Valor de π')
    ax1.set_title('Convergência da Estimativa de π')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Adicionar valores nos pontos
    for i, (n, pi_est) in enumerate(zip(triangulos, pi_estimados)):
        ax1.annotate(f'{pi_est:.6f}', (n, pi_est), xytext=(5, 5), 
                    textcoords='offset points', fontsize=8)
    
    # Gráfico 2: Erro absoluto
    ax2.plot(triangulos, erros, 'ro-', linewidth=2, markersize=6)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel('Número de Triângulos')
    ax2.set_ylabel('Erro Absoluto (escala log)')
    ax2.set_title('Evolução do Erro Absoluto')
    ax2.grid(True, alpha=0.3)
    
    # Ajustar layout
    plt.tight_layout()
    plt.savefig('convergencia_pi.png', dpi=300, bbox_inches='tight')
    plt.show()

def plotar_circulo_poligono(num_triangulos=12):
    """Gera uma visualização do círculo com o polígono inscrito"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Criar círculo
    circle = plt.Circle((0, 0), 0.5, fill=False, color='blue', linewidth=2)
    ax.add_artist(circle)
    
    # Criar polígono inscrito
    angulos = np.linspace(0, 2*np.pi, num_triangulos + 1)
    x = 0.5 * np.cos(angulos)
    y = 0.5 * np.sin(angulos)
    
    ax.plot(x, y, 'ro-', linewidth=2, markersize=4)
    ax.set_aspect('equal')
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.6, 0.6)
    ax.set_title(f'Polígono com {num_triangulos} lados inscrito no círculo')
    ax.grid(True, alpha=0.3)
    
    plt.savefig(f'poligono_{num_triangulos}_lados.png', dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Função principal"""
    print("Estimador de π usando Método de Polígonos Inscritos")
    print("=" * 60)
    
    # Gerar e mostrar resultados
    resultados = gerar_tabela_resultados()
    
    # Plotar gráficos
    try:
        plotar_grafico(resultados)
        print("\nGráfico de convergência salvo como 'convergencia_pi.png'")
        
        # Plotar visualização para 12 triângulos (exemplo)
        plotar_circulo_poligono(12)
        print("Visualização do polígono salva como 'poligono_12_lados.png'")
        
    except ImportError:
        print("\nMatplotlib não instalado. Instale com: pip install matplotlib")
    
    # Mostrar análise final
    ultimo_resultado = resultados[-1]
    print(f"\nAnálise Final:")
    print(f"Melhor estimativa: π ≈ {ultimo_resultado['pi_estimado']:.10f}")
    print(f"Erro absoluto: {ultimo_resultado['erro']:.2e}")
    print(f"Precisão: {100 - ultimo_resultado['erro_relativo']:.8f}%")

if __name__ == "__main__":
    main()
