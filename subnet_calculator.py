ip = input("ENTER IP > ").strip().split(".")
input_ip =[]
for oct in ip:
    input_ip.append(int(oct))

mask = input("ENTER MASK > ").strip().split(".")
input_mask =[]
for oct in mask:
    input_mask.append(int(oct))

"""
network id is calculated using a BINARY AND operation on the ip address and the mask.
each output of the output is 1 ONLY IF the corresponding bit in x and y is 1 else its 0
example:
192.168.0.1
255.255.255.0
=
192.168.0.0
"""

def network_id(ip, mask):
    id = []
    iterator = 0
    for oct in ip:
        a = oct & mask[iterator]
        id.append(a)
        iterator += 1
    return id


"""
broadcast is calculated using a BINARY OR on the network id and the wildcard
each bit of the output is 0 ONLY IF the corresponding bit of x and y is 0, else its 1
example:
192.168.0.1
0.0.0.255
=
192.168.0.255
"""

def broadcast(net_id, wildcard):
    broadcast_addr = []
    iterator = 0
    for oct in net_id:
        x = oct | wildcard[iterator]
        broadcast_addr.append(x)
        iterator += 1
    return broadcast_addr

"""
first ip address is network id + 1
"""


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

"""
last ip address is broadcast - 1
"""


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

"""
wildcard is is inverse of the mask, this can be calculated using a BINARY NOT operation
example:
11001110
00110001

bitewise NOT can be achieved like so:
-x -1
this switches the 1s and 0s 
a bitewise shift is necessary here

x = (1 << 8) is another way of writing x = 256
100000000 = 256
see the 1 is shifted 8 bits to the left

x = (1 << 8) - 1 = 255
formula:
where var is our octet in question
x = (1 << 8) - 1 - var = inverse
example:
x = (1 << 8) - 1 - 128 = 127
127 is the 8 bit binary inverse of 128
x = (1 << 8) - 1 - 0 = 255
255 is the 8 bit binary inverse of 0
"""

def wildcard(mask):
    wild = []
    for oct in mask:
        x = (1 << 8) - 1 - oct
        wild.append(x)
    return wild

"""
the number of ips is just the wildcard - 1
/24 example:
0.0.0.255 - 1 = 254
/16 example:
0.0.255.255
=
00000000000000001111111111111111
=
65535
65535 - 1 = 65534
"""
def number_of_ips(wildcard):
    wilc_base_2 = []
    for oct in wildcard:
        x = str(bin(oct))[2:]
        wilc_base_2.append(x)
    j = ''.join(wilc_base_2)
    no_of_hosts = int(j, 2) - 1
    return no_of_hosts




try:
    print("NETWORK ID:      -   {}".format(network_id(input_ip, input_mask)))
    print("BROADCAST:       -   {}".format(broadcast(network_id(input_ip, input_mask), wildcard(input_mask))))
    print("FIRST ADDRESS:   -   {}".format(first_ip(network_id(input_ip, input_mask))))
    print("LAST ADDRESS:    -   {}".format(last_ip(broadcast(network_id(input_ip, input_mask), wildcard(input_mask)))))
    print("WILDCARD:        -   {}".format(wildcard(input_mask)))
    print("NUMBER OF HOSTS: -   {}".format(number_of_ips(wildcard(input_mask))))
except:
    print("Error")