

# def sock_pairs (inp) :
#     res = []
#     sock_store = dict()
#     for idx, sock in enumerate(inp):
#         pair = sock.split(',')
#         color = pair[0]
#         leg = pair[1]
#         if leg == 'left':
#             opp_leg = 'right'
#         else:
#             opp_leg = 'left'

#         if (color, opp_leg) in sock_store:
#             opp_sock = sock_store[(color, opp_leg)]
#             opp_idx = opp_sock[-1]
#             res.append((opp_idx, idx + 1))
#         if (color, leg) not in sock_store:
#             sock_store[(color, leg)] = [idx + 1]

#         else:
#             sock_store[(color, leg)].append(idx+1)

#     return res

# if __name__ =='__main__':
#     inp = ['black,left', 'pink,right', 'pink,left', 'black,right', 'black,right', 'black,left']
#     result = sock_pairs(inp)
#     print(result)


def sock_pairs (inp) :
    res = []
    sock_store = dict()
    for idx, sock in enumerate(inp):
        pair = sock.split(',')
        color = pair[1]
        leg = pair[0]
        if leg == 'left':
            opp_leg = 'right'
        else:
            opp_leg = 'left'

        if (color, opp_leg) in sock_store:
            opp_sock = sock_store[(color, opp_leg)]
            opp_idx = opp_sock[-1]
            res.append((opp_idx, idx + 1))
        if (color, leg) not in sock_store:
            sock_store[(color, leg)] = [idx + 1]

        else:
            sock_store[(color, leg)].append(idx+1)

    return res

if __name__ =='__main__':
    inp = ['left,black', 'right,pink', 'left,pink', 'right,black', 'right,black', 'left,black']
    result = sock_pairs(inp)
    print(result)

    # def sockPairings(inp, pairings):
    # ret_arr = []    
    # sockMap = dict()
    
    # for i, pairing in enumerate(inp):
    #     orientation, color = pairing
    #     opp_orientation = 'left'
        
    #     if orientation == 'left':
    #         opp_orientation = 'right'
        
    #     oppKey = opp_orientation + color    
    #     key = orientation + color
        
    #     if (oppKey in sockMap.keys()) and (len(sockMap[oppKey]) != 0):
    #         counterpart = sockMap[oppKey]
    #         cp_index = counterpart.pop()
    #         ret_arr.append([i+1, cp_index])                     
    
    #     if key not in sockMap.keys():
    #         sockMap[key] = [i+1]
    #     else:
    #         sockMap[key].append(i+1)
    
    # return ret_arr
    