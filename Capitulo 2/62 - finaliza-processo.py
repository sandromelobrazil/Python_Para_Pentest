import os

PID = input("Digite o PID a ser finalizado: ")
os.kill(PID, 9)