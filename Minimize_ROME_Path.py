from CLASS_ROMA import Grafo
import pulp as p

def solve_Rome():
    g=Grafo()
    g.read_file('Road.txt')

    start=g.get_node_min()
    destination=g.get_node_max()
    print('** Answer with < Time or Cost > ** ')
    goal = input('Which Condition to Minimize? ')

    problem=p.LpProblem('Minimize_Rome',p.LpMinimize)

    x=[]
    for a in g.arcs:
        var=p.LpVariable(name='from '+str(a.n1)+' to '+str(a.n2),lowBound=0,upBound=1)
        x.append(var)

    #objective function
    objective=p.LpAffineExpression()
    for i in range(len(x)):
        if goal=='time' or goal=='Time':
            objective+=x[i]*g.arcs[i].w1
        elif goal=='cost' or goal=='Cost':
            objective += x[i] * g.arcs[i].w2

    problem+=objective
    #print(problem)

    #constraints
    problem+=x[2]+x[4]<=1

    c1=p.LpAffineExpression()
    for i in range(len(g.arcs)):
        a=g.arcs[i]
        if a.n1==start:
            c1+=x[i]
    problem+=c1==1,'Outcoming_arc_from_Home'
    #
    c2= p.LpAffineExpression()
    for i in range(len(g.arcs)):
        a = g.arcs[i]
        if a.n2 == start:
            c2 += x[i]
    problem += c2 == 0, 'Incoming_arc_to_Home'
    #
    c3= p.LpAffineExpression()
    for i in range(len(g.arcs)):
        a = g.arcs[i]
        if a.n2 == destination:
            c3 += x[i]
    problem += c3 == 1, 'Incoming_arc_to_Rome'
    #
    c4= p.LpAffineExpression()
    for i in range(len(g.arcs)):
        a = g.arcs[i]
        if a.n1 == destination:
            c4 += x[i]
    problem += c4 == 0,'Outcoming_arc_from_Rome'

    ##FOR OTHER NODES THE DIFFERENCE BETWEEN INCOMING & OUTCOMING ARC IS ZERO
    for n in range(destination+1):
        if n!=start and n!=destination:
            c5 = p.LpAffineExpression()
            for i in range(len(g.arcs)):
                a = g.arcs[i]
                if a.n1 == n:
                    c5 += x[i] ### sums all the incoming node
                if a.n2 == n:
                    c5 -= x[i] ## sums all the outcoming code
            problem += c5 == 0

    # SOLVE THE MIN PROBLEM and PRINT OUT RESULTS
    #print(problem)
    status=problem.solve()
    obb=p.value(problem.objective)

    if goal=='time'or goal=='Time':
        print('Shortest_Path_Takes:',obb,'Minutes')
    elif goal=='cost'or goal=='Cost':
        print('Cheapest_Path_Costs:',obb, '€')
    else:
        print('Invalid Input')
        #quit()

    #SET A CONCLUSION
    print("ROADS TO TRAVEL: ")
    min_nodes = []

    #print(x)
    cost=0
    time=0
    for i in range(len(g.arcs)):
        a=g.arcs[i]
        if p.value(x[i])>=.5:
            cost+=a.w1
            time+=a.w2
            min_nodes.append(a.n1)
            min_nodes.append(a.n2)
            print(a.n1,a.n2)

    min_nodes=list(set(min_nodes)) # in alternative create a new=[] and iterate through list and add to new if unique
    print(cost)
    print(time)
    print('\n** Answer < Yes or No >')
    str_nodes = input('Convert Nodes Into Cities? ')
    if str_nodes == 'yes':
        for i in min_nodes:
            g.translate_node(i)

#solve_Rome()