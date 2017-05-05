'''
Created on Jun 9, 2016

@author: smhaus
'''

def a():
    print ("a")
    
def b():
    print ("b")
    
def two(c,d,e):
    c()
    d()
    e()


if __name__ == '__main__':
    pass
    two(b,a,b)

#smhaus1
