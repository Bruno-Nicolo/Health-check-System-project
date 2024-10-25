from Controls import cpu, ram, disks
import time
import curses


def draw_interface(stdscr):
    curses.curs_set(0)  # Nasconde il cursore
    stdscr.nodelay(1)   # Evita di bloccare l'input

    while True:
        stdscr.clear()  # Pulisce lo schermo

        stdscr.addstr(0, 0, f"CPU usage percentage: {cpu.percentage()}%")
        stdscr.addstr(1, 0, f"CPU usage frequency: {cpu.frequency()}Hz")

        stdscr.addstr(3, 0, f"Memory available space: {ram.available} unità di misura")
        stdscr.addstr(4, 0, f"Memory available space percentage: {ram.percentage}%")
        stdscr.addstr(5, 0, f"Memory in use: {ram.active}")
        stdscr.addstr(6, 0, f"Memory not in use: {ram.inactive}")

        stdscr.addstr(8, 0, f"Disk total space: {disks.total}Gb")
        stdscr.addstr(9, 0, f"Disk used space: {disks.used}Gb")
        stdscr.addstr(10, 0, f"Disk used space in percentage: {disks.percent}%")
        # Upload speed: {network.upload_speed()}Mb/s
        # Download speed: {network.download_speed()}Mb/s

        stdscr.refresh() # Aggiorna lo schermo con le nuove informazioni

        time.sleep(1)

        # Esci dal ciclo se viene premuto un tasto
        if stdscr.getch() != -1:
            break


curses.wrapper(draw_interface)