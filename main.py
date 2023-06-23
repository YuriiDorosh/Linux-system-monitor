# import os
# import psutil
# import curses
# import pynvml
#
# from multiprocessing import cpu_count
# from pympler import muppy, summary
#
# def get_cpu_load():
#     return psutil.cpu_percent(interval=0.1, percpu=True)
#
# def get_memory_usage():
#     return psutil.virtual_memory().percent
#
# def get_disk_usage():
#     disk_usage = psutil.disk_usage('/')
#     return disk_usage.percent
#
# def get_gpu_usage():
#     pynvml.nvmlInit()
#     device_count = pynvml.nvmlDeviceGetCount()
#
#     for i in range(device_count):
#         handle = pynvml.nvmlDeviceGetHandleByIndex(i)
#         # device_name = pynvml.nvmlDeviceGetName(handle).decode()
#         device_name = pynvml.nvmlDeviceGetName(handle)
#
#         if "NVIDIA" in device_name:
#             utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
#             return utilization.gpu
#
#     return 0
#
# def update_console(stdscr):
#     stdscr.clear()
#     stdscr.addstr(0, 0, "Press 'q' to quit.")
#     cpu_load = get_cpu_load()
#     memory_usage = get_memory_usage()
#     disk_usage = get_disk_usage()
#     gpu_usage = get_gpu_usage()
#
#     progress_bars = [
#         f"CPU{i}: {load}%" for i, load in enumerate(cpu_load)
#     ] + [
#         f"Memory: {memory_usage}%",
#         f"Disk: {disk_usage}%",
#         f"GPU: {gpu_usage}%",
#     ]
#
#     disk_info = f"Disk Free Space: {psutil.disk_usage('/').free / (1024**3):.2f} GB"
#
#     for i, progress_bar in enumerate(progress_bars):
#         stdscr.addstr(i+2, 0, progress_bar)
#
#     stdscr.addstr(len(progress_bars)+2, 0, disk_info)
#
#     stdscr.refresh()
#
# if __name__ == "__main__":
#     stdscr = curses.initscr()
#     curses.cbreak()
#     stdscr.keypad(True)
#     stdscr.nodelay(True)
#
#     num_cores = cpu_count()
#
#     while True:
#         update_console(stdscr)
#
#         key = stdscr.getch()
#         if key == ord('q'):
#             break
#
#     curses.nocbreak()
#     stdscr.keypad(False)
#     curses.echo()
#     curses.endwin()


import os
import psutil
import pynvml
import tkinter as tk
import sys
import curses

from multiprocessing import cpu_count
from pympler import muppy, summary


def get_cpu_load():
    return psutil.cpu_percent(interval=0.1, percpu=True)


def get_memory_usage():
    return psutil.virtual_memory().percent


def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return disk_usage.percent


def get_gpu_usage():
    pynvml.nvmlInit()
    device_count = pynvml.nvmlDeviceGetCount()

    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        device_name = pynvml.nvmlDeviceGetName(handle)

        if "NVIDIA" in device_name:
            utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)
            return utilization.gpu

    return 0


def update_console():
    os.system('cls' if os.name == 'nt' else 'clear')

    cpu_load = get_cpu_load()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    gpu_usage = get_gpu_usage()

    progress_bars = [
                        f"CPU{i}: {load}%" for i, load in enumerate(cpu_load)
                    ] + [
                        f"Memory: {memory_usage}%",
                        f"Disk: {disk_usage}%",
                        f"GPU: {gpu_usage}%",
                    ]

    disk_info = f"Disk Free Space: {psutil.disk_usage('/').free / (1024 ** 3):.2f} GB"

    for progress_bar in progress_bars:
        print(progress_bar)

    print(disk_info)
def clear_console():
    # Clear console command based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

# def update_console():
#     clear_console()
#
#     cpu_load = get_cpu_load()
#     memory_usage = get_memory_usage()
#     disk_usage = get_disk_usage()
#     gpu_usage = get_gpu_usage()
#
#     progress_bars = [
#         f"CPU{i}: {load}%" for i, load in enumerate(cpu_load)
#     ] + [
#         f"Memory: {memory_usage}%",
#         f"Disk: {disk_usage}%",
#         f"GPU: {gpu_usage}%",
#     ]
#
#     disk_info = f"Disk Free Space: {psutil.disk_usage('/').free / (1024**3):.2f} GB"
#
#     for progress_bar in progress_bars:
#         print(progress_bar)
#
#     print(disk_info)
def update_console(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Press 'q' to quit.")
    cpu_load = get_cpu_load()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    gpu_usage = get_gpu_usage()

    progress_bars = [
        f"CPU{i}: {load}%" for i, load in enumerate(cpu_load)
    ] + [
        f"Memory: {memory_usage}%",
        f"Disk: {disk_usage}%",
        f"GPU: {gpu_usage}%",
    ]

    disk_info = f"Disk Free Space: {psutil.disk_usage('/').free / (1024**3):.2f} GB"

    for i, progress_bar in enumerate(progress_bars):
        stdscr.addstr(i+2, 0, progress_bar)

    stdscr.addstr(len(progress_bars)+2, 0, disk_info)

    stdscr.refresh()


def update_gui():
    cpu_load = get_cpu_load()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    gpu_usage = get_gpu_usage()

    progress_bars = [
                        f"CPU{i}: {load}%" for i, load in enumerate(cpu_load)
                    ] + [
                        f"Memory: {memory_usage}%",
                        f"Disk: {disk_usage}%",
                        f"GPU: {gpu_usage}%",
                    ]

    disk_info = f"Disk Free Space: {psutil.disk_usage('/').free / (1024 ** 3):.2f} GB"

    text = "\n".join(progress_bars) + "\n" + disk_info
    label.config(text=text)

    root.after(1000, update_gui)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        root = tk.Tk()
        root.title("System Monitor")

        label = tk.Label(root, font=("Courier", 12), justify=tk.LEFT)
        label.pack(padx=10, pady=10)

        update_gui()

        root.mainloop()
    else:
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(True)
        stdscr.nodelay(True)

        num_cores = cpu_count()

        while True:
            update_console(stdscr)

            key = stdscr.getch()
            if key == ord('q'):
                break

        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
