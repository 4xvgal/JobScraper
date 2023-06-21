import os

def Initialization(route, final_route, merged):

    #csv 파일을 공백화 시키고 지워버리는 기능.
    
    saramin = route[0]
    worknet = route[1]

    saramin_final= final_route[0]
    worknet_final= final_route[1]

    # with open(saramin, 'w') as file:
    #     pass

    os.remove(saramin)

    # with open(worknet, 'w') as file:
    #     pass

    os.remove(worknet)

    # with open(saramin_final, 'w') as file:
    #     pass

    os.remove(saramin_final)

    # with open(worknet_final, 'w') as file:
    #     pass

    os.remove(worknet_final)

    # with open(merged, 'w') as file:
    #     pass

    os.remove(merged)
