def hanoi_solver(n):
    source = list(range(n, 0, -1))
    auxiliary = []
    target = []

    states = []

    def record_state():
        states.append(f"{source} {auxiliary} {target}")

    def move(num, from_rod, to_rod, aux_rod):
        if num == 1:
            disk = from_rod.pop()
            to_rod.append(disk)
            record_state()
        else:
            move(num - 1, from_rod, aux_rod, to_rod)
            disk = from_rod.pop()
            to_rod.append(disk)
            record_state()
            move(num - 1, aux_rod, to_rod, from_rod)

    record_state()
    move(n, source, target, auxiliary)

    return "\n".join(states)