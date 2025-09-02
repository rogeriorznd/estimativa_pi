"""
Estimador de π usando o método de polígonos inscritos e circunscritos
Baseado no método de Arquimedes
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

def estimar_pi_inscrito(num_lados):
    """
    Estima π usando polígonos inscritos (dentro do círculo)
    """
    if num_lados < 3:
        raise ValueError("Número de lados deve ser pelo menos 3")
    
    # Comprimento do lado do polígono inscrito
    # lado = sin(π/n)
    lado = math.sin(math.pi / num_lados)
    
    # Perímetro do polígono
    perimetro = num_lados * lado
    
    # π estimado = perímetro (já que diâmetro = 1)
    pi_estimado = perimetro
    
    return pi_estimado

def estimar_pi_circunscrito(num_lados):
    """
    Estima π usando polígonos circunscritos (fora do círculo)
    """
    if num_lados < 3:
        raise ValueError("Número de lados deve ser pelo menos 3")
    
    # Comprimento do lado do polígono circunscrito
    # lado = tan(π/n)
    lado = math.tan(math.pi / num_lados)
    
    # Perímetro do polígono
    perimetro = num_lados * lado
    
    # π estimado = perímetro (já que diâmetro = 1)
    pi_estimado = perimetro
    
    return pi_estimado

def gerar_tabela_resultados():
    """Gera uma tabela com os resultados para diferentes números de lados"""
    # Sequência com valores principais (para a tabela)
    num_lados_tabela = [3, 6, 12, 24, 48, 96, 192, 384]
    
    # Sequência completa com muitos pontos para curva suave
    num_lados_completo = [3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 
                          24, 28, 32, 36, 40, 48, 56, 64, 72, 80, 96, 
                          112, 128, 144, 160, 192, 224, 256, 288, 320, 384]
    
    print("=" * 85)
    print("ESTIMAÇÃO DE π POR POLÍGONOS INSCRITOS E CIRCUNSCRITOS")
    print("=" * 85)
    print(f"{'Lados':<6} {'π Inscrito':<14} {'π Circunscrito':<16} {'π Real':<12} {'Intervalo':<20}")
    print("-" * 85)
    
    resultados_inscrito_tabela = []
    resultados_circunscrito_tabela = []
    
    # Calcular apenas para os valores da tabela
    for n in num_lados_tabela:
        pi_inscrito = estimar_pi_inscrito(n)
        pi_circunscrito = estimar_pi_circunscrito(n)
        
        resultados_inscrito_tabela.append({
            'lados': n,
            'pi_estimado': pi_inscrito
        })
        
        resultados_circunscrito_tabela.append({
            'lados': n,
            'pi_estimado': pi_circunscrito
        })
        
        intervalo = f"[{pi_inscrito:.6f}, {pi_circunscrito:.6f}]"
        print(f"{n:<6} {pi_inscrito:<14.10f} {pi_circunscrito:<16.10f} {math.pi:<12.10f} {intervalo:<20}")
    
    print("=" * 85)
    
    # Calcular para todos os pontos (curva suave)
    resultados_inscrito_completo = []
    resultados_circunscrito_completo = []
    
    for n in num_lados_completo:
        resultados_inscrito_completo.append({
            'lados': n,
            'pi_estimado': estimar_pi_inscrito(n)
        })
        
        resultados_circunscrito_completo.append({
            'lados': n,
            'pi_estimado': estimar_pi_circunscrito(n)
        })
    
    return (resultados_inscrito_tabela, resultados_circunscrito_tabela,
            resultados_inscrito_completo, resultados_circunscrito_completo)

def plotar_grafico_comparacao(resultados_inscrito_tabela, resultados_circunscrito_tabela,
                             resultados_inscrito_completo, resultados_circunscrito_completo):
    """Gera gráfico comparando inscritos e circunscritos"""
    # Dados para curva suave
    lados_suave = [r['lados'] for r in resultados_inscrito_completo]
    pi_inscritos_suave = [r['pi_estimado'] for r in resultados_inscrito_completo]
    pi_circunscritos_suave = [r['pi_estimado'] for r in resultados_circunscrito_completo]
    
    # Dados para pontos da tabela
    lados_tabela = [r['lados'] for r in resultados_inscrito_tabela]
    pi_inscritos_tabela = [r['pi_estimado'] for r in resultados_inscrito_tabela]
    pi_circunscritos_tabela = [r['pi_estimado'] for r in resultados_circunscrito_tabela]
    
    # Criar figura
    plt.figure(figsize=(14, 8))
    
    # Curvas suaves
    plt.plot(lados_suave, pi_inscritos_suave, 'b-', linewidth=2.5, alpha=0.7, label='Polígonos Inscritos (π ≤ π_real)')
    plt.plot(lados_suave, pi_circunscritos_suave, 'r-', linewidth=2.5, alpha=0.7, label='Polígonos Circunscritos (π ≥ π_real)')
    
    # Pontos destacados (da tabela)
    plt.plot(lados_tabela, pi_inscritos_tabela, 'bo', markersize=6, alpha=0.8)
    plt.plot(lados_tabela, pi_circunscritos_tabela, 'ro', markersize=6, alpha=0.8)
    
    # Linha do π real
    plt.axhline(y=math.pi, color='g', linestyle='--', linewidth=3, label='π Real')
    
    # Configurar eixo x com valores reais
    plt.xscale('log')
    
    # Definir ticks manualmente para mostrar valores específicos
    ticks_principais = [3, 6, 12, 24, 48, 96, 192, 384]
    plt.xticks(ticks_principais, labels=[str(x) for x in ticks_principais])
    
    plt.xlabel('Número de Lados do Polígono', fontsize=12)
    plt.ylabel('Valor de π Estimado', fontsize=12)
    plt.title('Convergência da Estimativa de π', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)
    
    # Adicionar área sombreada entre as curvas
    plt.fill_between(lados_suave, pi_inscritos_suave, pi_circunscritos_suave, color='gray', alpha=0.2, label='Intervalo de confiança')
    
    # Adicionar valores apenas para os pontos principais
    for i, n in enumerate(lados_tabela):
        plt.annotate(f'{pi_inscritos_tabela[i]:.4f}', (n, pi_inscritos_tabela[i]), 
                    xytext=(0, -20), textcoords='offset points',
                    fontsize=8, ha='center', color='blue', weight='bold')
        plt.annotate(f'{pi_circunscritos_tabela[i]:.4f}', (n, pi_circunscritos_tabela[i]), 
                    xytext=(0, 15), textcoords='offset points',
                    fontsize=8, ha='center', color='red', weight='bold')
    
    # Ajustar limites do eixo y para melhor visualização
    plt.ylim(2.5, 4.0)
    
    # Ajustar layout
    plt.tight_layout()
    plt.savefig('comparacao_inscrito_circunscrito.png', dpi=300, bbox_inches='tight')
    plt.show()

def plotar_poligonos_comparacao():
    """Gera visualizações comparativas dos polígonos"""
    poligonos = [6, 12, 24]  # Polígonos para visualizar
    
    for n in poligonos:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
        
        # Polígono inscrito
        circle1 = plt.Circle((0, 0), 0.5, fill=False, color='blue', linewidth=2)
        ax1.add_artist(circle1)
        
        angulos_inscrito = np.linspace(0, 2*np.pi, n + 1)
        x_inscrito = 0.5 * np.cos(angulos_inscrito)
        y_inscrito = 0.5 * np.sin(angulos_inscrito)
        
        ax1.plot(x_inscrito, y_inscrito, 'bo-', linewidth=2, markersize=6)
        ax1.set_aspect('equal')
        ax1.set_xlim(-0.7, 0.7)
        ax1.set_ylim(-0.7, 0.7)
        
        pi_inscrito = estimar_pi_inscrito(n)
        ax1.set_title(f'Polígono Inscrito ({n} lados)\nπ ≈ {pi_inscrito:.6f} ≤ π_real', fontsize=12)
        ax1.grid(True, alpha=0.3)
        
        # Polígono circunscrito
        circle2 = plt.Circle((0, 0), 0.5, fill=False, color='red', linewidth=2)
        ax2.add_artist(circle2)
        
        raio_circunscrito = 0.5 / math.cos(math.pi / n)
        angulos_circunscrito = np.linspace(0, 2*np.pi, n + 1)
        x_circunscrito = raio_circunscrito * np.cos(angulos_circunscrito)
        y_circunscrito = raio_circunscrito * np.sin(angulos_circunscrito)
        
        ax2.plot(x_circunscrito, y_circunscrito, 'ro-', linewidth=2, markersize=6)
        ax2.set_aspect('equal')
        ax2.set_xlim(-0.7, 0.7)
        ax2.set_ylim(-0.7, 0.7)
        
        pi_circunscrito = estimar_pi_circunscrito(n)
        ax2.set_title(f'Polígono Circunscrito ({n} lados)\nπ ≈ {pi_circunscrito:.6f} ≥ π_real', fontsize=12)
        ax2.grid(True, alpha=0.3)
        
        plt.suptitle(f'Comparação: Polígonos com {n} lados', fontsize=14)
        plt.tight_layout()
        plt.savefig(f'comparacao_{n}_lados.png', dpi=300, bbox_inches='tight')
        plt.show()

def main():
    """Função principal"""
    print("Estimador de π usando Método de Polígonos Inscritos e Circunscritos")
    print("=" * 85)
    
    # Gerar e mostrar resultados
    (resultados_inscrito_tabela, resultados_circunscrito_tabela,
     resultados_inscrito_completo, resultados_circunscrito_completo) = gerar_tabela_resultados()
    
    # Plotar gráficos
    try:
        plotar_grafico_comparacao(resultados_inscrito_tabela, resultados_circunscrito_tabela,
                                 resultados_inscrito_completo, resultados_circunscrito_completo)
        print("\nGráfico de comparação salvo como 'comparacao_inscrito_circunscrito.png'")
        
        # Plotar visualizações comparativas
        plotar_poligonos_comparacao()
        print("Visualizações comparativas salvas como 'comparacao_N_lados.png'")
        
    except ImportError:
        print("\nMatplotlib não instalado. Instale com: pip install matplotlib")
    
    # Mostrar análise final
    ultimo_inscrito = resultados_inscrito_tabela[-1]
    ultimo_circunscrito = resultados_circunscrito_tabela[-1]
    
    print(f"\nAnálise Final:")
    print(f"Melhor estimativa inscrita: π ≈ {ultimo_inscrito['pi_estimado']:.10f}")
    print(f"Melhor estimativa circunscrita: π ≈ {ultimo_circunscrito['pi_estimado']:.10f}")
    print(f"π Real: {math.pi:.10f}")
    print(f"Intervalo: [{ultimo_inscrito['pi_estimado']:.10f}, {ultimo_circunscrito['pi_estimado']:.10f}]")
    print(f"Erro máximo: {abs(ultimo_circunscrito['pi_estimado'] - ultimo_inscrito['pi_estimado']):.2e}")

if __name__ == "__main__":
    main()