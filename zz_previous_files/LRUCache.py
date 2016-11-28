class DoublyListNode:
    
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        # (key, Node) pair
        self.table = {}
        self.cap = capacity
        # dummy head and tail
        self.head = DoublyListNode(-1, -1)
        self.tail = DoublyListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # @return an integer
    def get(self, key):
        node = self.table.get(key)
        if not node:
            print 'get val from key %d' % key
            return -1
        node.prev.next = node.next
        node.next.prev = node.prev
        self.move_to_tail(node)
        print
        print 'get val from key %d' % key
        return node.val
        
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.table:
            node = self.table[key]
            node.val = value
            node.prev.next = node.next
            node.next.prev = node.prev
            self.move_to_tail(node)
        else:
            node = DoublyListNode(key, value)
            if len(self.table) == self.cap:
                self.table.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.next.prev = self.head
            self.table[key] = node
            self.move_to_tail(node)

        print '\n', 'debugging'
        print 'after setting %d -> %d' % (key, value)
        print 'hash table'
        for k, v in self.table.items():
            print k, ': ', v.val, ', ',
        # print(' , '.join(str(k) + ': ' + str(v)) for k, v in self.table.items())
        print '\n', 'linked list'
        cur = self.head
        while cur.next:
            print cur.key, ': ', cur.val, ', ',
            cur = cur.next
            
    def move_to_tail(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

cache = LRUCache(105)

cache.set(33,219);
print cache.get(39);
cache.set(96,56); print cache.get(129); print cache.get(115);
print cache.get(112);cache.set(3,280); print cache.get(40);cache.set(85,193);cache.set(10,10);
cache.set(100,136);cache.set(12,66);cache.set(81,261);cache.set(33,58);
print cache.get(3);cache.set(121,308);cache.set(129,263); print cache.get(105);cache.set(104,38);
cache.set(65,85);cache.set(3,141);cache.set(29,30);cache.set(80,191);
cache.set(52,191);cache.set(8,300); print cache.get(136);cache.set(48,261);
cache.set(3,193);cache.set(133,193);cache.set(60,183);cache.set(128,148);
cache.set(52,176); print cache.get(48);cache.set(48,119);cache.set(10,241); print cache.get(124);
cache.set(130,127); print cache.get(61);cache.set(124,27); print cache.get(94);cache.set(29,304);
cache.set(102,314); print cache.get(110);cache.set(23,49);cache.set(134,12);
cache.set(55,90)

print cache.get(14);print cache.get(104);cache.set(77,165);cache.set(60,160);print cache.get(117);
cache.set(58,30);print cache.get(54);print cache.get(136);print cache.get(128);print cache.get(131);
cache.set(48,114);print cache.get(136);cache.set(46,51);cache.set(129,291);cache.set(96,207);
print cache.get(131);cache.set(89,153);cache.set(120,154);print cache.get(111);print cache.get(47);
print cache.get(5);cache.set(114,157);cache.set(57,82);cache.set(113,106);cache.set(74,208);
print cache.get(56);print cache.get(59);print cache.get(100);print cache.get(132);cache.set(127,202);
print cache.get(75);cache.set(102,147);print cache.get(37);cache.set(53,79);cache.set(119,220);
print cache.get(47);print cache.get(101);print cache.get(89);print cache.get(20);print cache.get(93);
print cache.get(7);cache.set(48,109);cache.set(71,146);print cache.get(43);
print cache.get(122);cache.set(3,160);print cache.get(17);cache.set(80,22);cache.set(80,272);
print cache.get(75);print cache.get(117)


#-1,-1,-1,-1,-1,
# 280,-1,-1,261,-1,
# -1,-1,-1,-1,38,
# -1,-1,-1,148,
# -1,-1,-1,-1,-1,-1,-1,-1,
# 136,-1,-1,-1,-1,-1,153,
# -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,
# 160,51,-1,218,-1,261,-1,-1,-1,193,-1,-1,220,
# -1,-1,-1,-1,306,219,-1,-1,266,193,90,-1,-1,147,-1,
# 148,147,131,-1,291,291,-1,178,-1,136,-1,147,-1,287,
# -1,-1,-1,183,174,110,-1,-1,-1,12,-1,89,305,70,
# -1,94,-1,-1,241,176,220,-1,306,-1,183,-1,12,-1,95,
# -1,-1,311,111,190,84,-1,-1,177,157,-1,-1,174,51,183,
# -1,4,-1,-1,21,51,176,89,-1,-1,176,313,86,229,176,294,110,
# 101,128,49,82,193,193,-1,85,101,126,66,-1,-1,-1,67,66,126,
# 101,84,184,23,198,110,101,130,131,130,239,35,-1,287,-1,240,
# 313,67,-1,121,239,299,101,105,118,160,135,255,-1,11,101,258,
# -1,35,88,160,11,276,291,299,90,75,291,276,118,-1,121,252,145,191,
# -1,75,65,23,139,164,177,165,311,184,309,100,151,-1,167,90,-1,299,
# 173,173,-1,-1,313,45,252,167,212,132,94,137,308,-1,167,164,288,82,2,
# -1,164,299,137,295,139,-1,101,65,249,190,-1,-1,-1,151,203,90,88,190,
# 160,40,24,132,30,-1,161,67,119,161,24,132,-1,267,-1,-1,227,-1,183,311,
# 295,-1,167,188,47,311]