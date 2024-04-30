import time
import multiprocessing

def calcular_pi(n, inicio, fin):
    """
    Función para calcular una parte de la serie de Leibniz para estimar el número PI.

    Parámetros:
    - n: número total de iteraciones para el cálculo.
    - inicio: índice inicial para iterar sobre la serie de Leibniz.
    - fin: índice final para iterar sobre la serie de Leibniz.

    Retorna:
    - pi_parte: resultado parcial del cálculo de PI.
    - iteraciones: número de iteraciones realizadas.
    """
    pi_parte = 0  # Iniciamos la variable que guardara el resultado.
    iteraciones = fin - inicio  # Calculamos el número de iteraciones.
    for k in range(inicio, fin):  # Iteramos sobre el rango especificado.
        pi_parte += ((-1) ** k) / (2 * k + 1)  # Calculamos cada término de la serie de Leibniz y lo sumamos.
    return pi_parte, iteraciones  # Retornamos el resultado parcial del cálculo y el número de iteraciones.

def main(num_procesadores):
    """
    Función principal que calcula el número PI utilizando el método de Leibniz con diferentes números de procesadores.

    Parámetros:
    - num_procesadores: número de procesadores a utilizar para el cálculo.

    No retorna ningún valor, simplemente imprime el número PI calculado, el tiempo de ejecución y el número de iteraciones realizadas en cada procesador.
    """
    n = 9 * 10**7  # Número total de iteraciones para el cálculo.
    inicio = 0  # Índice inicial para la iteración.
    fin = n // num_procesadores  # Dividimos el trabajo en partes iguales para cada procesador.
    pool = multiprocessing.Pool(processes=num_procesadores)  # Creamos un conjunto de procesos.

    tiempo_inicio = time.time()  # Guardamos el tiempo de inicio del cálculo.

    # Utilizamos una lista de comprensión para calcular cada parte del número PI en paralelo.
    resultados = [pool.apply_async(calcular_pi, args=(n, inicio + i * fin, inicio + (i + 1) * fin)) for i in range(num_procesadores)]

    # Sumamos los resultados parciales de cada proceso y multiplicamos por 4 para obtener el valor de PI.
    pi = sum(resultado.get()[0] for resultado in resultados) * 4

    # Obtenemos el número total de iteraciones realizadas en todos los procesadores.
    iteraciones_totales = sum(resultado.get()[1] for resultado in resultados)

    tiempo_fin = time.time()  # Guardamos el tiempo de fin del cálculo.
    
    # Calculamos el tiempo total de ejecución.
    tiempo_total = tiempo_fin - tiempo_inicio

    # Imprimimos el resultado del cálculo, el tiempo de ejecución y el número de iteraciones realizadas en cada procesador.
    print(f"Número PI calculado con {num_procesadores} procesadores: {pi}")
    print(f"Tiempo de ejecución: {tiempo_total} segundos")
    print(f"Iteraciones realizadas en cada procesador: {iteraciones_totales // num_procesadores}")

if __name__ == "__main__":
    # Ejecutamos la función principal con diferentes números de procesadores para observar el comportamiento.
    main(1)  # Probar con 1 procesador
    main(2)  # Probar con 2 procesadores
    main(3)  # Probar con 3 procesadores
