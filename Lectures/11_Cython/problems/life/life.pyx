cimport cython

@cython.boundscheck(False)
def life_update(int[:, ::1] old_state,
                int[:, ::1] new_state):

    cdef int x, y, dx, dy, num_neighbors

    with nogil:
        for x in range(1, old_state.shape[0] - 1):
            for y in range(1, old_state.shape[1] - 1):
                num_neighbors = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if old_state[x + dx, y + dy]:
                            num_neighbors += 1
                if num_neighbors < 2 or num_neighbors > 3:
                    new_state[x, y] = 0
                elif num_neighbors == 3:
                    new_state[x, y] = 1
                else:
                    new_state[x, y] = old_state[x, y]
