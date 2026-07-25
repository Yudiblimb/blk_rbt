import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)

import pyautogui
import keyboard
import time
print(pyautogui.size())
# Desativa a trava de segurança dos cantos do PyAutoGUI
pyautogui.FAILSAFE = False

# Pausa ajustada para evitar erros de cliques múltiplos no sistema
pyautogui.PAUSE = 0.05

# ------------------------------------------------------------------
# MAPEAMENTO DE PONTOS POR ATALHO
# ------------------------------------------------------------------

PONTOS_GRUPO_1 = [
    (58, 58),  # Ponto 1
    (1014, 58),  # Ponto 2
    (58, 572),  # Ponto 3
    (1015, 572),  # Ponto 4
]

PONTOS_GRUPO_2 = [
    (905, 487),  # Ponto 1
    (1865, 487),  # Ponto 2
    (915, 1000),  # Ponto 3
    (1896, 1000),  # Ponto 4
]

PONTOS_GRUPO_3 = [
    (574, 316),  # Ponto 1
    (1532, 316),  # Ponto 2
    (568, 832),  # Ponto 3
    (1532, 832),  # Ponto 4
]


# ------------------------------------------------------------------
# FUNÇÃO REUTILIZÁVEL DE CLIQUE
# ------------------------------------------------------------------
def executar_cliques(lista_pontos, nome_grupo):
    print(f"\n⚡ Executando [{nome_grupo}]...")
    inicio = time.time()

    for x, y in lista_pontos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

    fim = time.time()
    tempo_ms = (fim - inicio) * 1000
    print(f"✅ [{nome_grupo}] Concluído em {tempo_ms:.2f} ms!")


def main():
    print("==================================================")
    print(" PROGRAMA DE AUTOMAÇÃO MULTI-ATALHOS")
    print(" • Ctrl + Shift + 1 -> Grupo 1 (Topo)")
    print(" • Ctrl + Shift + 2 -> Grupo 2 (Base)")
    print(" • Ctrl + Shift + 3 -> Grupo 3 (Meio)")
    print(" • ESC              -> Encerrar o programa")
    print("==================================================")

    # Configuração dos 3 atalhos mapeados para a função de clique
    keyboard.add_hotkey(
        "ctrl+shift+1", lambda: executar_cliques(PONTOS_GRUPO_1, "Grupo 1")
    )
    keyboard.add_hotkey(
        "ctrl+shift+2", lambda: executar_cliques(PONTOS_GRUPO_2, "Grupo 2")
    )
    keyboard.add_hotkey(
        "ctrl+shift+3", lambda: executar_cliques(PONTOS_GRUPO_3, "Grupo 3")
    )

    # Mantém o script em execução em segundo plano
    keyboard.wait("esc")
    print("\nPrograma encerrado.")


if __name__ == "__main__":
    main()
