import math
import matplotlib.pyplot as plt
import tkinter
angulo = float(input("Digite o ângulo: "))
velocidade = float(input("Digite a velocidade inicial (m/s): "))

angulo_rad = math.radians(angulo)
vx = velocidade * math.cos(angulo_rad)
vy = velocidade * math.sin(angulo_rad)

x = 0
y = 0
t = 0

g = 9.8
dt = 0.01

lista_x = []
lista_y = []

while y>= 0:

    x = x + vx * dt
    y = y + vy * dt
    vy = vy - g * dt
    t = t + dt

    lista_x.append(x)
    lista_y.append(y)
    print(t, x, y)
    if y == 0:
      break

plt.plot(lista_x, lista_y)
plt.title("Trajetória do projétil")
plt.xlabel("Distância (m)")
plt.ylabel("Altura (m)")
plt.grid(True)
plt.show()