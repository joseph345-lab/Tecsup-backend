import random


class Tragamonedas:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self._creditos = creditos
        self._total_jugado = 0
        self._total_ganado = 0

    def mostrar(self):
        if self._creditos > 0:
            estado = f"S/ {self._creditos}"
        else:
            estado = "💀 SIN CRÉDITOS"
        print(f"🎰 {self.nombre} — {estado}")

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        else:
            print(f"😢 Perdiste S/ {apuesta}")
        return True

    def mostrar_estadisticas(self):
        balance = self._total_ganado - self._total_jugado
        signo = "+" if balance >= 0 else ""
        print(f"   {self.nombre}")
        print(f"   Apostado: S/ {self._total_jugado}  |  Ganado: S/ {self._total_ganado}")
        print(f"   Balance: S/ {signo}{balance}  |  Créditos actuales: S/ {self._creditos}")
        print()


class TragamonedasFrutas(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍓"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado


class TragamonedasClasico(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["7️⃣", "💎", "🔔", "⭐", "💲", "🎰"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado


class TragamonedasMundial(Tragamonedas):
    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷", "🇪🇸", "🇺🇾"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False
        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos: {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()

        tiene_peru = "🇵🇪" in resultado

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 15
            print(f"🏆 ¡TRIPLETE! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"⚽ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif tiene_peru:
            print(f"🇵🇪 ¡Perú apareció! Recuperas tu apuesta de S/ {apuesta}")
            self._creditos += apuesta
            self._total_ganado += apuesta
        else:
            print(f"😢 Perdiste S/ {apuesta}")
        return True


def jugar_en_maquina(maquina):
    print()
    print(f"--- Entraste a {maquina.nombre} ---")

    while maquina._creditos > 0:
        maquina.mostrar()

        try:
            apuesta = int(input("¿Cuánto apuestas? (0 para volver al casino): "))
        except ValueError:
            print("⚠️  Ingresa un número válido.")
            continue

        if apuesta == 0:
            print("↩️  Volviendo al casino...")
            break

        maquina.jugar(apuesta)
        print()
    else:
        print(f"💸 {maquina.nombre} se quedó sin créditos.")


def mostrar_menu(maquinas):
    print()
    print("=" * 40)
    print("           🎰 CASINO ROYALE 🎰")
    print("=" * 40)
    print()

    for i, m in enumerate(maquinas, 1):
        if m._creditos > 0:
            estado = f"S/ {m._creditos}"
        else:
            estado = "💀 SIN CRÉDITOS"
        print(f"  {i}. {m.nombre} ({estado})")

    print(f"  {len(maquinas) + 1}. Mostrar estadísticas de todas")
    print(f"  {len(maquinas) + 2}. Salir")
    print()


def resumen_general(maquinas):
    print()
    print("=" * 40)
    print("        📊 RESUMEN DEL CASINO")
    print("=" * 40)

    total_jugado = 0
    total_ganado = 0
    vacias = 0

    for m in maquinas:
        total_jugado += m._total_jugado
        total_ganado += m._total_ganado
        if m._creditos == 0:
            vacias += 1

    print(f"  Total apostado por el jugador: S/ {total_jugado}")
    print(f"  Total pagado por el casino:    S/ {total_ganado}")

    balance_casino = total_jugado - total_ganado
    if balance_casino > 0:
        print(f"  🏦 El casino ganó S/ {balance_casino}. (La casa siempre gana)")
    elif balance_casino < 0:
        print(f"  🤑 El jugador ganó S/ {total_ganado - total_jugado}. ¡Rompiste la banca!")
    else:
        print("  🤝 Empate técnico. Nadie ganó, nadie perdió.")

    print(f"  Máquinas fundidas: {vacias} de {len(maquinas)}")
    print("=" * 40)


maquinas = [
    TragamonedasFrutas("La Frutal", 200),
    TragamonedasClasico("La Clásica", 300),
    TragamonedasMundial("Mundial 2026", 150),
]

while True:
    mostrar_menu(maquinas)

    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("⚠️  Opción inválida.")
        continue

    if 1 <= opcion <= len(maquinas):
        maquina = maquinas[opcion - 1]
        if maquina._creditos == 0:
            print("💀 Esa máquina está sin créditos. Elige otra.")
        else:
            jugar_en_maquina(maquina)

    elif opcion == len(maquinas) + 1:
        print()
        print("📊 ESTADÍSTICAS DEL CASINO")
        print("-" * 40)
        for m in maquinas:
            m.mostrar_estadisticas()

    elif opcion == len(maquinas) + 2:
        resumen_general(maquinas)
        print("\n💰 Gracias por visitar el Casino Royale. ¡Vuelve pronto!")
        break

    else:
        print("⚠️  Opción inválida.")