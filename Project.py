from collections import Counter

subnets = None

ntwrk_bits = None
count = None

brd_addr = list()

diff = list()

cnt = 1

ntwrk_bits = None
subnet_mask = None

hosts = list()
hosts_count = None

addr = None             #ip address decimal
addr_oct = None         #ip address octates

addrs = ''              #ip address binary
addrs_oct=list()        #ip address binary octates

brd_addr = list()

def add_diff():
    global addr_oct, diff, brd_addr
    
    for ind in range(0, len(addr_oct)):
        brd_addr[ind] = addr_oct[ind] + diff[ind]

def calculate_difference():
    global addr_oct, brd_addr, diff
    
    for i in range(0, len(addr_oct)):
        diff.append( brd_addr[i] - addr_oct[i])
    
    print(diff)

def calc_next_addr ():
    global brd_addr, addr_oct
    
    for each in brd_addr:
        if(brd_addr[3] < 255):
            addr_oct = [brd_addr[0], brd_addr[1], brd_addr[2], brd_addr[3]+1]
        elif(brd_addr[2] < 255):
            addr_oct = [brd_addr[0], brd_addr[1], brd_addr[2]+1, 0]
        elif(brd_addr[1] < 255):
            addr_oct = [brd_addr[0], brd_addr[1]+1, 0, 0]
        else:
            print('Error')
            

def calculate_brd ():
    global addrs_oct, brd_addr
    
    if brd_addr is not None:
        brd_addr.clear()
        
    for each in addrs_oct:
        brd_addr.append(int(each, 2))
        
    print(brd_addr)
    return '.'.join([str(elem) for elem in brd_addr])

def calculate_portion():
    global addrs_oct, addrs, ntwrk_bits
    
    #print(ntwrk_bits)
    
    x = list(addrs)
    c=0
    for each in addrs_oct:
        if (int(each,2) != 0):
            c += 8
        else:
            for i in range(0, 8):
                if (c < ntwrk_bits):
                    x[c] = '1'
                    c += 1
                else:
                    break
    
    addrs = ''.join([str(elem) for elem in x])
    
    c=0
    for each in addrs_oct:
        if (int(each,2) != 0):
            c += 8
        else:
            for i in range(0, 8):
                if (x[c] == '1'):
                    x[c] = '0'
                    c += 1
                elif (x[c] == '0'):
                    x[c] = '1'
                    c += 1
                else:
                    break
    
    addrs = ''.join([str(elem) for elem in x])
    #print(addrs)

def make_octates ():
    global addrs_oct, addrs
    
    addrs_oct.clear()
    
    for i in range(0, 32, 8):
        j = i + 8
        addrs_oct.append(addrs[i:j])
        
    #print(addrs_oct)

def convert_addr_to_str():
    global addrs
    
    for each in addr_oct:
        str_ = bin(each).replace('0b', '')
        #print(str_)
        for i in range(0, 8-len(str_)):
            str_ = '0' + str_
        #print(str_)
        addrs =  addrs + str_ 
        
    #print(addrs)

def validate_requirement():
    global subnets, ntwrk_bits, count
    
    b = 1
    count = 0
    while(b < subnets):
        b = b*2
        count += 1
        
    if (ntwrk_bits + count < 32):
        ntwrk_bits += count
        return True
    else:
        return False

def validate_address(address): 
    global ntwrk_bits
     
    if (ntwrk_bits == 8):
        if (address[1] == 0 and address[2] == 0 and address[3] == 0):
            return True
        else:
            return False
    elif (ntwrk_bits == 16):
        if (address[2] == 0 and address[3] == 0):
            return True
        else:
            return False
    elif (ntwrk_bits == 24):
        if (address[3] == 0):
            return True
        else:
            return False

def calc_ntwrk_bits(frst_oct):
    global ntwrk_bits
    
    if (frst_oct >=0)and(frst_oct <=127):
        print('Class A')
        ntwrk_bits = 8
    elif (frst_oct >=128)and(frst_oct <=191):
        print('Class B')
        ntwrk_bits = 16
    elif (frst_oct >=192)and(frst_oct <=223):
        print('Class C')
        ntwrk_bits = 24
    else:
        print('Error')

def calc_rem (reg):
    x = reg - ntwrk_bits
    v = 1
    count = 1
    _sum = 1
    while (count < x):
        v = v*2
        _sum += v 
        count += 1
        
    return (255 - _sum)

def calculate_broadcast_1 ():
    global addr_oct, brd_addr
    
    if (addr_oct[3] > 0):
        brd_addr = [addr_oct[0], addr_oct[1], addr_oct[2], addr_oct[3]-1]
    elif (addr_oct[2] > 0):
        brd_addr = [addr_oct[0], addr_oct[1], addr_oct[2]-1, 255]
    elif (addr_oct[1] > 0):
        brd_addr = [addr_oct[0], addr_oct[1]-1, 255, 255]
    else:
        print('Error')
        
    #print(brd_addr)

def translate_octates_1():
    global addrs_oct, addrs_oct
    
    for i in range(0, len(addrs_oct)):
        addr_oct[i] = int(addrs_oct[i], 2)
        
    #print(addr_oct)

def make_octates_1 ():
    global addrs_oct, addrs
    
    addrs_oct.clear()
    
    for i in range(0, 32, 8):
        j = i + 8
        addrs_oct.append(addrs[i:j])
        
    #print(addrs_oct)

def calc_bit_1(target):
    b = 1
    count = 1
    while(b < target):
        b = b*2
        count += 1
        
    return count

def convert_addr_to_str_1():
    global addrs
    
    for each in addr_oct:
        str_ = bin(each).replace('0b', '')
        #print(str_)
        for i in range(0, 8-len(str_)):
            str_ = '0' + str_
        #print(str_)
        addrs =  addrs + str_ 
        
    #print(addrs)

def calculate_subnets_1():
    global hosts, hosts_count, addrs, ntwrk_bits, addr, brd_addr, addr_oct, subnet_mask
    
    convert_addr_to_str_1()
    
    for each in sorted(hosts, reverse=True):
        print('\n----------------FOR', each, 'HOSTS---------------')
        ind = calc_bit_1(each)
        ind = ind + hosts_count.get(each)
        if (hosts_count.get(each) > 0):
            hosts_count[each] = hosts_count.get(each) - 1
        
        #print('index', ind)
        if (addrs[len(addrs) - ind] == '0'):
            x = list(addrs)
            x[len(addrs) - ind] = '1'
            addrs = ''.join([str(elem) for elem in x])
            #print(addrs)
            
            ntwrk_bits = len(addrs[:(len(addrs) - ind)+1])
            print('NETWORK ADDRESS: ', '.'.join([str(elem) for elem in addr_oct]), '/', ntwrk_bits)
           
            make_octates_1()
            translate_octates_1()
            calculate_broadcast_1()
            
            print('BROADCAST ADDRESS: ', '.'.join([str(elem) for elem in brd_addr]) , '/', ntwrk_bits)
            calc_subnet_mask_1()
            print('SUBNET MASK: ', '.'.join([str(elem) for elem in subnet_mask]))
        else:
            print('This Requirement cannot be satisfied')

def check_if_possible_1():
    global hosts, ntwrk_bits, hosts_count
    
    b = 1
    count = 1
    while(b < max(hosts)):
        b = b*2
        count += 1
    
    print(ntwrk_bits)
    print(count)
    if (ntwrk_bits + count + hosts_count.get(max(hosts)) <= 32):
        return True
    else:
        return False


def calc_if_multiple_1():
    global hosts, hosts_count
    
    hosts_count = Counter(hosts)
    for each in hosts_count:
        hosts_count[each] = hosts_count.get(each) - 1
        
    #print (hosts_count)

def calc_subnet_mask_1():
    global ntwrk_bits, subnet_mask
    
    if (ntwrk_bits == 8):
        subnet_mask = [255, 0, 0, 0]
    elif (ntwrk_bits == 16):
        subnet_mask = [255, 255, 0, 0]
    elif (ntwrk_bits == 24):
        subnet_mask = [255, 255, 255, 0]
    elif (ntwrk_bits > 8) and (ntwrk_bits < 16):
        v = calc_rem(16)
        subnet_mask = [255, v, 0, 0]
    elif (ntwrk_bits > 16) and (ntwrk_bits < 24):
        v = calc_rem(24)
        subnet_mask = [255, 255, v, 0]
    elif (ntwrk_bits > 24) and (ntwrk_bits < 32):
        v = calc_rem(32)
        subnet_mask = [255, 255, 255, v]
    else:
        return      

def calc_ntwrk_bits_1(frst_oct):
    global ntwrk_bits
    
    if (frst_oct >=0)and(frst_oct <=127):
        print('Class A')
        ntwrk_bits = 8
    elif (frst_oct >=128)and(frst_oct <=191):
        print('Class B')
        ntwrk_bits = 16
    elif (frst_oct >=192)and(frst_oct <=223):
        print('Class C')
        ntwrk_bits = 24
    else:
        print('Error')
        
def validate_address_1(address):      
    if (ntwrk_bits == 8):
        if (address[1] == 0 and address[2] == 0 and address[3] == 0):
            return True
        else:
            return False
    elif (ntwrk_bits == 16):
        if (address[2] == 0 and address[3] == 0):
            return True
        else:
            return False
    elif (ntwrk_bits == 24):
        if (address[3] == 0):
            return True
        else:
            return False

def sbnt_by_hsts():
    global addr, addr_oct, hosts
    
    addr = input('Enter IP Address: ')
    addr_oct = addr.split('.')
    
    #print(addr_oct)
    
    for each in range(0, len(addr_oct)):
        addr_oct[each] = int(addr_oct[each])
    
    '''
    ntwrk_bits = input('Enter the number of network bits: ')
    
    subnet_mask = input('Enter the subnet mask of the address: ')
    '''
    
    calc_ntwrk_bits_1(addr_oct[0])
    if (validate_address_1(addr_oct) ):
        calc_subnet_mask_1()
        
        n_hosts = int(input('Enter the number of Subnets: '))
        for each in range(0, n_hosts):
            print('Enter Subnet', (each+1), 'hosts:', end=' ')
            x = int(input())
            hosts.append(x)
            
        #print(hosts)
        calc_if_multiple_1()
        if (check_if_possible_1()):
            calculate_subnets_1()
        else:
            print('SUBNETTING IS NOT POSSIBLE')
        
    else:
        print('No possible')
        
def sbnt_by_sbnts():
    global addr, addr_oct, subnets, cnt, brd_addr
    
    addr = input('Enter IP Address: ')
    addr_oct = addr.split('.')
    
    subnets = int(input('Enter the number of subnets you want:'))
    
    for each in range(0, len(addr_oct)):
        addr_oct[each] = int(addr_oct[each])
    
    calc_ntwrk_bits(addr_oct[0])
    if (validate_address(addr_oct)):
        if (validate_requirement()):
            print('NETWORK ADDRESS: ', addr)
            convert_addr_to_str()
            make_octates()
            calculate_portion()
            make_octates()
            print('BROADCAST ADDRESS: ', calculate_brd())
            calculate_difference()
            while(cnt <= subnets):
                calc_next_addr()
                print('NETWORK ADDRESS: ', '.'.join([str(elem) for elem in addr_oct]))
                add_diff()
                print('BRAODCAST ADDRESS: ', '.'.join([str(elem) for elem in brd_addr]))
                cnt += 1
        else:
            print('REQUIREMENT NOT VALID')
    else:
        print('INVALID ADDRESS')


def init():
    print(' _____           _____            ____  ______              ____   ____   ')
    print('|       |     |  |    |  |\   |  |        |     |\      /|  |   |  |      | /')
    print('|____   |     |  |____|  | \  |  |____    |     | \    / |  |___|  |___   |/ ')
    print('     |  |     |  |    |  |  \ |  |        |     |  \  /  |  |   |      |  |\ ')
    print('_____|  |_____|  |____|  |   \|  |____    |     |   \/   |  |   |   ___|  | \ ')
    
    print('    ____   ____           ____                  ____   _____   ____   ____')
    print('   |      |    |  |      |      |    |  |      |    |    |    |    |  |   |')
    print('   |      |____|  |      |      |    |  |      |____|    |    |    |  |___|')
    print('   |      |    |  |      |      |    |  |      |    |    |    |    |  | \ ' )
    print('   |____  |    |  |____  |____  |____|  |____  |    |    |    |____|  |  \ ' )
 
def option():
    print('PLEASE SELECT AN APPROPRIATE OPTION:')
    print('1) SUBNETTING BY NUMBER OF HOSTS')
    print('2) SUBNETTING BY NUMBER OF SUBNETS')
    opt = int(input('YOUR OPTION:'))
    
    return opt

def main():
    init()
    c = option()
    if (c == 1):
        sbnt_by_hsts()
    elif (c == 2):
        sbnt_by_sbnts()
    else:
        print('please select an appropriate option')
        
if __name__ == '__main__':
    main()
    

