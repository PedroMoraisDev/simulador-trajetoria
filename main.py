import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk


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

while y >= 0:

    x = x + vx * dt 
    y = y + vy * dt
    vy = vy - g * dt
    t = t + dt

    lista_x.append(x)
    lista_y.append(y)
    print(t, x, y)
    if y == 0:
        break

distancia = max(lista_x) 

fig, ax = plt.subplots()
ax.set_xlim(0, max(lista_x) + 10)
ax.set_ylim(0, max(lista_y) + 10)
ax.set_title("Trajetória do projétil")
ax.set_ylabel("Altura (m)")
ax.set_xlabel(f'(Distância (m)Percorreu {distancia:.2f} metros')
ax.grid(True)

line, = ax.plot([], [], 'b-')  
point, = ax.plot([], [], 'ro', markersize=8)  

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def animate(i):
    line.set_data(lista_x[:i+1], lista_y[:i+1])
    point.set_data([lista_x[i]], [lista_y[i]])
    return line, point

anim = FuncAnimation(fig, animate, init_func=init, frames=len(lista_x), interval=10, blit=True)
plt.show()