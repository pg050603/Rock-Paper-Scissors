import testing_modules.utime as utime

state = []
out_queue = []

def push_message(message, strength=0, timestamp=utime.ticks_ms()):
    state.append([message, strength, timestamp])

def get_last_out():
    if not out_queue:
        return None
    return out_queue.pop()

def receive_full():
    if not state:
        return None
    return state.pop(0)

def receive_bytes():
    if not state:
        return None
    return state.pop(0)[0]

def send_bytes(message):
    out_queue.append(message)

def receive():
    msg = receive_bytes()
    if not msg:
        return None
    return str(msg, 'UTF-8')

def receive_bytes_into(buffer):
    raise NotImplementedError

def send(message):
    send_bytes(bytes(message, 'UTF-8'))

def on():
    pass

def config(**kwargs):
    pass

def reset():
    pass
