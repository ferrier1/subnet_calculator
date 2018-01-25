ip = input("ENTER IP > ").strip().split(".")
input_ip =[]
for oct in ip:
    input_ip.append(int(oct))

mask = input("ENTER MASK > ").strip().split(".")
input_mask =[]
for oct in mask:
    input_mask.append(int(oct))



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





print("NETWORK ID:      -   {}".format(network_id(input_ip, input_mask)))
print("BROADCAST:       -   {}".format(broadcast(network_id(input_ip, input_mask), wildcard(input_mask))))
print("FIRST ADDRESS:   -   {}".format(first_ip(network_id(input_ip, input_mask))))
print("LAST ADDRESS:    -   {}".format(last_ip(broadcast(network_id(input_ip, input_mask), wildcard(input_mask)))))
print("WILDCARD:        -   {}".format(wildcard(input_mask)))
print("NUMBER OF HOSTS: -   {}".format(number_of_ips(wildcard(input_mask))))

input()