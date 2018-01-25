
input_ip = [10, 1, 1, 1]
input_mask = [255, 255, 255, 0]

def network_id(ip, mask):
    id = []
    iterator = 0
    for oct in ip:
        a = oct & mask[iterator]
        id.append(a)
        iterator += 1
    return id

def broadcast(net_id, wildcard):
    broadcast_addr = []
    iterator = 0
    for oct in net_id:
        x = oct | wildcard[iterator]
        broadcast_addr.append(x)
        iterator += 1
    return broadcast_addr

def first_ip(ip):
    first = []
    binary_list = []
    for oct in ip:
        binary = bin(oct + 256)[3:]
        binary_list.append(binary)
    g = ''.join(binary_list)
    t = int(g, base=2) + 1
    u = str(bin(t))[2:]
    x = 32 - len(str(u))
    r = "{}{}".format("0" * x, u)
    binary_split = [r[start:start+8] for start in range(0, 32, 8)]
    for bin_oct in binary_split:
        first.append(int(bin_oct, base=2))
    return first

def last_ip(ip):
    last = []
    binary_list = []
    for oct in ip:
        binary = bin(oct + 256)[3:]
        binary_list.append(binary)
    g = ''.join(binary_list)
    t = int(g, base=2) - 1
    u = str(bin(t))[2:]
    x = 32 - len(str(u))
    r = "{}{}".format("0" * x, u)
    binary_split = [r[start:start+8] for start in range(0, 32, 8)]
    for bin_oct in binary_split:
        last.append(int(bin_oct, base=2))
    return last


def wildcard(mask):
    wild = []
    for oct in mask:
        x = (1 << 8) - 1 - oct
        wild.append(x)
    return wild

def number_of_ips(wildcard):
    wilc_base_2 = []
    for oct in wildcard:
        x = str(bin(oct))[2:]
        wilc_base_2.append(x)
    j = ''.join(wilc_base_2)
    no_of_hosts = int(j, 2) - 1
    return no_of_hosts





print(number_of_ips(wildcard(input_mask)))
print(last_ip(broadcast(network_id(input_ip, input_mask), wildcard(input_mask))))
print(broadcast(network_id(input_ip, input_mask), wildcard(input_mask)))
print(wildcard(input_mask))
print(network_id(input_ip, input_mask))
print(first_ip(network_id(input_ip, input_mask)))
