import math
import utils/probality

let int a = 4

qubit q1 = (2,3)

if (q1 < 0){
    probe.str(Nice)
}
else-if (q1 > 0){
    probe.int(0)
}
else{
    probe a
}

function non_probalistic_func():
    probe.str(This is not probabilistic)

struct{
    int b = 3
    qubit q2 = (1,0)

    if (q2 < 0){
    probe.str(Nice)
    }
    else-if (q2 > 0){
        probe.int(0)
    }
    else{
        probe b
    }
}

struct{
    register[3]
    H(q1)
    CNOT(q2)
}