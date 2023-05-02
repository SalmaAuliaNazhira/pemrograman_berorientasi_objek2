# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

async def async_zip(*aiterables):
    aiterators = [aiterable.__aiter__() for aiterable in aiterables]
    done = False
    while True:
        items = [None] * len(aiterators)

        async def fill_in(i):
            try:
                items[i] = await aiterators[i].__anext__()
            except StopAsyncIteration:
                nonlocal done
                done = True







