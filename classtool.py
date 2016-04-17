#!/usr/bin/python
class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s = %s ' % (key, getattr(self, key)))
        return ', '.join(attrs)
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())
if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attrs1 = TopTest.count
            self.attrs2 = TopTest.count + 1
            TopTest.count += 2
    class SubTest(TopTest):
        def __init__(self):
            self.attrs2 = SubTest.count + 3
            SubTest.count += 1
            
            #重新定义的方法会覆盖原来已经定义过的方法
    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)