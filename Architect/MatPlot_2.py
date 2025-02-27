import numpy as np
import matplotlib.pyplot as plt

# Параметры сигналов
amplitude = 5  # Амплитуда сигнала
duration = 1e-3  # Длительность визуализации (1 мс)
time_step = 1e-6  # Шаг моделирования (1 мкс)
time = np.arange(0, duration, time_step)  # Временная ось

# Функция для формирования меандра
def generate_square_wave(time, frequency, amplitude):
    period = 1 / frequency  # Период сигнала
    square_wave = amplitude * (np.floor(2 * time / period) % 2)
    return square_wave

# Функция для формирования прямоугольного сигнала с заданной скважностью
def generate_rectangular_wave(time, frequency, amplitude, duty_cycle):
    period = 1 / frequency  # Период сигнала
    rectangular_wave = amplitude * (time % period < duty_cycle * period)
    return rectangular_wave

# Генерация меандра для частот 5 кГц и 10 кГц
square_wave_5kHz = generate_square_wave(time, 5000, amplitude)
square_wave_10kHz = generate_square_wave(time, 10000, amplitude)

# Генерация прямоугольного сигнала со скважностью 4 для частот 5 кГц и 10 кГц
rectangular_wave_5kHz = generate_rectangular_wave(time, 5000, amplitude, 0.25)
rectangular_wave_10kHz = generate_rectangular_wave(time, 10000, amplitude, 0.25)

# Построение графиков
plt.figure(figsize=(12, 8))

# Меандр
plt.subplot(2, 2, 1)
plt.plot(time, square_wave_5kHz)
plt.title("Меандр, 5 кГц")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(time, square_wave_10kHz)
plt.title("Меандр, 10 кГц")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.grid(True)

# Прямоугольный сигнал
plt.subplot(2, 2, 3)
plt.plot(time, rectangular_wave_5kHz)
plt.title("Прямоугольный сигнал, 5 кГц, скважность 4")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(time, rectangular_wave_10kHz)
plt.title("Прямоугольный сигнал, 10 кГц, скважность 4")
plt.xlabel("Время (с)")
plt.ylabel("Амплитуда")
plt.grid(True)

plt.tight_layout()
plt.show()