import auction as auc
from nose.tools import assert_true

#Case testing
test1={
    "aemon": 300,
    "john": 270,
    "viserys": 270,
    "obyern": 250,
    "jaime":50
}

result1={
    "aemon": 270,
    "john": 270,
    "viserys": 250,
    "obyern": 50,
    "jaime": "lost"
}
test2={
    "aemon": 200,
    "john": 200,
    "viserys": 100,
    "obyern": 250,
    "jaime":50
}

result2={
    "obyern": 200,
    "aemon": 200,
    "john": 100,
    "viserys": 50,
    "jaime": "lost"
}

test3={
    "aemon": 200,
    "john": 150,
    "viserys": 100,

}

result3={
    "aemon": 150,
    "john": 100,
    "viserys": "lost"

}

output1=auc.handle_data(test1)
output2=auc.handle_data(test2)
output3=auc.handle_data(test3)
 
def test():
    assert(output1==result1)
def test2():  
    assert(output2==result2)  
def test3():
    assert(output3==result3)